package dispatch

import (
    "context"
    "fmt"
    "os"
    "testing"
    "strings"

    "github.com/gastownhall/gascity/internal/beadmeta"
    "github.com/gastownhall/gascity/internal/beads"
    "github.com/gastownhall/gascity/internal/config"
    "github.com/gastownhall/gascity/internal/formula"
)

// Prove the REAL host route dispatcher consumes per-item run targets from a
// dynamically instantiated expansion, without a fixed PStack panel.
func TestPStackDynamicPerItemRouteDispatch(t *testing.T) {
    dir := os.Getenv("PSTACK_FORMULAS")
    if dir == "" { t.Fatal("PSTACK_FORMULAS unset") }
    previous := formula.IsFormulaV2Enabled()
    formula.SetFormulaV2Enabled(true)
    defer formula.SetFormulaV2Enabled(previous)

    options := testProcessOptionsWithControlDispatcher("app")
    options.routeCfg.cfg.Agents = append(options.routeCfg.cfg.Agents,
        config.Agent{Name:"research-a", Dir:"app"},
        config.Agent{Name:"review-b", Dir:"app"},
    )
    control := beads.Bead{Metadata:map[string]string{
        beadmeta.ExecutionRigContextMetadataKey:"app",
        beadmeta.RootStoreRefMetadataKey:"rig:app",
    }}
    for _, count := range []int{2,3,5,8} {
        t.Run(fmt.Sprintf("N%d",count),func(t *testing.T) {
            routes := map[string]bool{}
            for i:=0;i<count;i++ {
                targetName:="research-a"
                if i%2==1 { targetName="review-b" }
                target:= &formula.Step{ID:fmt.Sprintf("plan.item.%d",i+1),Title:"Dynamic item"}
                vars:=map[string]string{
                    "task_id":fmt.Sprintf("t%d",i), "route_target":targetName,
                    "scope_ref":"src/", "objective":"Inspect bounded source",
                    "artifact_path":fmt.Sprintf("runs/r%d.json",i),
                    "revision":strings.Repeat("a",40),
                    "workflow_id":"bd-run", "method":"interrogate",
                    "provider":"claude", "model":"model-a",
                }
                f,err:=formula.CompileExpansionFragment(context.Background(),"pstack-dynamic-worker",[]string{dir},target,vars)
                if err!=nil { t.Fatalf("host expand N=%d item=%d: %v",count,i,err) }
                if err:=routeFanoutFragmentSteps(f,control,options,beads.NewMemStore());err!=nil {
                    t.Fatalf("host route N=%d item=%d: %v",count,i,err)
                }
                workAttempt, controlNode := false, false
                for _, step := range f.Steps {
                    if step.Metadata[beadmeta.RunTargetMetadataKey] != targetName { continue }
                    routed:=step.Metadata[beadmeta.RoutedToMetadataKey]
                    if step.Metadata[beadmeta.KindMetadataKey]==beadmeta.KindRalph {
                        if routed!="app/"+config.ControlDispatcherAgentName {
                            t.Fatalf("item %d Ralph control incorrectly routed %q",i,routed)
                        }
                        controlNode=true
                        continue
                    }
                    if strings.Contains(step.ID, ".iteration.") {
                        if routed!="app/"+targetName {
                            t.Fatalf("item %d executing attempt routed %q, expected %q",i,routed,"app/"+targetName)
                        }
                        workAttempt=true
                    }
                }
                if !controlNode || !workAttempt {
                    t.Fatalf("item %d missing independently routed worker attempt / controller: ctrl=%t worker=%t fragment=%+v",i,controlNode,workAttempt,f.Steps)
                }
                routes[targetName]=true
            }
            if len(routes)!=2 { t.Fatalf("not heterogeneous routes: %v",routes) }
        })
    }
}
