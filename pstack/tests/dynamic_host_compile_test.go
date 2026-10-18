package formula

import (
    "context"
    "os"
    "path/filepath"
    "strings"
    "testing"
)

func TestPStackDynamicFanoutHostCompiler(t *testing.T) {
    dir := os.Getenv("PSTACK_FORMULAS")
    if dir == "" { t.Fatal("PSTACK_FORMULAS unset") }
    dir, err := filepath.Abs(dir)
    if err != nil { t.Fatal(err) }
    previous := IsFormulaV2Enabled()
    SetFormulaV2Enabled(true)
    defer SetFormulaV2Enabled(previous)
    for _, method := range []string{"swarm","arena","interrogate"} {
        t.Run(method, func(t *testing.T) {
            recipe, err := Compile(context.Background(), "pstack-"+method+"-multi", []string{dir}, nil)
            if err != nil { t.Fatalf("real host Compile: %v", err) }
            fanout := false
            for _, step := range recipe.Steps {
                if step.Metadata["gc.kind"] == "fanout" && strings.Contains(step.ID, "plan-fanout") {
                    fanout = true
                    if step.Metadata["gc.bond"] != "pstack-dynamic-worker" {
                        t.Fatalf("wrong dynamic expansion: %+v", step.Metadata)
                    }
                }
            }
            if !fanout { t.Fatal("missing host-minted dynamic plan fanout control") }
        })
    }
    target := &Step{ID: "plan.item.1", Title: "Runtime item"}
    vars := map[string]string{
        "task_id":"issue-a", "route_target":"myorg.fast-research",
        "scope_ref":"src/a.go", "objective":"Inspect behavior",
        "artifact_path":"runs/a.json", "revision":strings.Repeat("a",40),
        "workflow_id":"bead-123", "method":"swarm", "provider":"claude",
        "model":"haiku",
    }
    fragment, err := CompileExpansionFragment(context.Background(), "pstack-dynamic-worker", []string{dir}, target, vars)
    if err != nil { t.Fatalf("real host CompileExpansionFragment: %v", err) }
    if len(fragment.Steps) == 0 { t.Fatal("no dynamic worker fragment steps") }
    found := false
    for _, step := range fragment.Steps {
        if strings.Contains(step.ID, "work") && step.Metadata["gc.run_target"] == "myorg.fast-research" {
            if step.Metadata["pstack.dynamic.artifact_path"] != "runs/a.json" {
                t.Fatalf("artifact path not interpolated: %+v", step.Metadata)
            }
            found = true
        }
    }
    if !found { t.Fatalf("per-item dynamic role target was not substituted: %+v", fragment.Steps) }
}
