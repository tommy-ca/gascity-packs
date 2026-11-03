"""Vendoring must never delete outside the canonical vendor/runtime directories."""
from __future__ import annotations

import importlib.util
import pathlib
import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "vendor_canonical_pstack.py"


def load_script():
    spec = importlib.util.spec_from_file_location("pstack_vendor_boundary", SCRIPT)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_default_refresh_targets_are_allowed():
    module = load_script()
    module.assert_safe_paths(ROOT / "vendor" / "pstack", ROOT / "skills")


@pytest.mark.parametrize("dest,runtime", [
    ("formulas", "skills"),
    ("vendor/pstack", "formulas"),
    ("vendor", "skills"),
    ("vendor/pstack", "agents"),
])
def test_pack_owned_paths_are_rejected(dest, runtime):
    module = load_script()
    with pytest.raises(SystemExit, match="vendor refresh"):
        module.assert_safe_paths(ROOT / dest, ROOT / runtime)


def test_arbitrary_external_paths_are_rejected(tmp_path):
    module = load_script()
    sentinel = tmp_path / "keep.md"
    sentinel.write_text("must survive", encoding="utf-8")
    with pytest.raises(SystemExit, match="vendor refresh"):
        module.assert_safe_paths(tmp_path, tmp_path / "runtime")
    assert sentinel.read_text(encoding="utf-8") == "must survive"


def test_symlink_vendor_dest_is_rejected(tmp_path):
    module = load_script()
    link = tmp_path / "linked"
    link.symlink_to(ROOT / "vendor" / "pstack", target_is_directory=True)
    with pytest.raises(SystemExit, match="symlink"):
        module.assert_safe_paths(link, ROOT / "skills")
