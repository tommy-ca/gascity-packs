# LLMWiki v2 graph-engineering source intake — rights-HELD

**Status:** planned only, NO producer execution. This Gas City pack has **no** producer package dependency and imports neither QStack nor its LLMWiki runtime.

## Sources
- GasCity host `gastownhall/gascity@6bd609f5bfb41f43f444843b1220d0cde4473446`, path-scoped rights still HELD.
- GasCity pack `gastownhall/gascity-packs@7f86098c04ead8cb78706ddc9524cf4cab83b028`, rights still HELD.
- Earlier GraphCode/longgraph reference audit: QStack draft PR #3297. No source fulltext copied here.

## Planned exact CLI (not executed)
On a trusted local QStack checkout, after confirming `packages/llmwiki-v2` package and `uv.lock`:
```bash
uv run --locked --package llmwiki-v2 llmwiki-v2 ingest \
  --source-id gascity-host-ref \
  --locator https://github.com/gastownhall/gascity \
  --revision 6bd609f5bfb41f43f444843b1220d0cde4473446

uv run --locked --package llmwiki-v2 llmwiki-v2 ingest \
  --source-id gascity-packs-ref \
  --locator https://github.com/gastownhall/gascity-packs \
  --revision 7f86098c04ead8cb78706ddc9524cf4cab83b028
```
These are metadata-only `HELD`/unverified notices and **never** source capture or knowledge compilation.

## Authorized workflow (separate explicit future approval)
1. Independently verify exact revision/bytes, per-path license, rights signer and source fidelity.
2. Capture originals only under separately signed rights grant and trusted source snapshot; attribute original semantic summaries and prepare HELD `Goal/WorkBead/DependencyEdge/ControlEdge/Claim/ReviewGate/Checkpoint` pages.
3. Verify citations against original spans and reconcile competing assertions; never turn agent prose into verified evidence.
4. Independently authenticate reviewer decision bound to same base/article, use existing sole CAS publisher; produce immutable bundle with separate externally trusted issuer pin.
5. Run read-only QUERY/LINT and check link/citation/compilation/absence mode. QStack may read only authorized published bundle, never pack files or staged raw candidates.

**No rights approval, source bytes capture, CAS publication, model-assisted compounding, release verification or real CLI invocation was performed here.** A metadata file in a PR is not itself a LLMWiki ingested record.
