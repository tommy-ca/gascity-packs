## 1. OpenSpec

- [ ] 1.1 Validate-only this live change
- [ ] 1.2 Archive only after operator go

## 2. Rename

- [ ] 2.1 Set `pstack/pack.toml` `[pack] name` to `tommy-ca/pstack`
- [ ] 2.2 Update `test_pack_metadata_and_import`
- [ ] 2.3 Keep vendor `upstream.toml` without `tommy-ca/pstack`
- [ ] 2.4 README dest names `tommy-ca/pstack`

## 3. Publish

- [ ] 3.1 Dry-run `gc pack registry publish pstack/`
- [ ] 3.2 Review-gate then submit
- [ ] 3.3 Do not restamp gastownhall `registry.toml`
- [ ] 3.4 Do not merge gastownhall
