## 1. Specs

- [x] 1.1 Record `gc formula show` on the live-city requirement. Copy every
      live scenario. Add the formula-show scenario. Do not MODIFY
      remaining-units.

## 2. Honesty lock

- [x] 2.1 Add `test_pack_formulas_show_through_a_city` next to the list
      test. Same `MAINTAINED_PACKS` table, skip, wiring, and `write_city`.
- [x] 2.2 Lock `gc formula show` in `test_delivery_checks_cover_pstack`.
      Lock that show is not sling. Keep the two sling-unproven sentences.
- [x] 2.3 Name formula show in REQUIREMENTS Evidence Commands. Keep
      `Formula sling of pstack-poteto-mode and pstack-build remains unproven.`
- [x] 2.4 Name formula show on the TRACEABILITY metadata evidence class
      only if the locked import and sling sentences stay.

## 3. Apply

- [x] 3.1 Validate-only against this repository `openspec/`.
- [x] 3.2 Archive into this repository `openspec/`.
- [x] 3.3 Run `uv run --with pytest --with pyyaml pytest -q pstack/tests/test_pstack_pack.py`.
- [x] 3.4 Run the live matrix with `GC_TEST_BIN` set, filtered to
      `formulas_show or pstack`.
