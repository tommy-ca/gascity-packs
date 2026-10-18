## 1. Specs

- [x] 1.1 Record tommy fork dest, hosted publish, and `pr-pstack-publish`
      on remaining-units. Copy every live scenario. Add the publish
      scenario.

## 2. Dest lock

- [x] 2.1 Rewrite `docs/pstack-program-plan.md` intro, persist text, spawn
      graph, publish H2, land merge, and appendices. Keep the check-plan
      skeleton.
- [x] 2.2 One Delivery boundary sentence for tommy fork dest and hosted
      registry. Keep the two locked sling sentences.
- [x] 2.3 Replace the restamp-as-publication assert in
      `test_delivery_checks_cover_pstack`. Lock the new spawn sentences
      and `pr-pstack-publish`. Keep boot-recipe source.

## 3. Apply

- [x] 3.1 Validate-only against this repository `openspec/`.
- [x] 3.2 Archive into this repository `openspec/`.
- [x] 3.3 Run `uv run --with pytest --with pyyaml pytest -q pstack/tests/test_pstack_pack.py`.
