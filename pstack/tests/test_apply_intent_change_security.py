"""Regression checks for OpenSpec change-name filesystem isolation."""

from __future__ import annotations

import importlib.util
import pathlib
import subprocess
import sys

import pytest


SCRIPT = pathlib.Path(__file__).resolve().parents[1] / "scripts" / "apply_intent_change.py"


def load_script():
    spec = importlib.util.spec_from_file_location("pstack_apply_intent_change_security", SCRIPT)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.mark.parametrize(
    "name",
    ["", ".", "..", "../outside", "../../openspec", "name/child", r"name\\child", "/tmp/escape", "bad name", "a" * 129],
)
def test_invalid_explicit_change_names_are_rejected(name: str) -> None:
    with pytest.raises(SystemExit, match="invalid OpenSpec change name"):
        load_script().change_name(pathlib.Path("2026-09-02-mapping-gaps"), name)


def test_valid_name_and_archived_date_prefix() -> None:
    module = load_script()
    assert module.change_name(pathlib.Path("2026-09-02-mapping-gaps"), None) == "mapping-gaps"
    assert module.change_name(pathlib.Path("another-name"), "review.v2") == "review.v2"


def test_traversal_cannot_delete_neighbor_directory(tmp_path: pathlib.Path) -> None:
    source = tmp_path / "source"
    source.mkdir()
    (source / "proposal.md").write_text("a source change", encoding="utf-8")
    dest = tmp_path / "dest"
    protected = dest / "openspec" / "protected"
    protected.mkdir(parents=True)
    sentinel = protected / "keep.txt"
    sentinel.write_text("must survive", encoding="utf-8")

    result = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--source", str(source),
            "--dest", str(dest),
            "--change", "../protected",
        ],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode != 0
    assert "invalid OpenSpec change name" in result.stderr
    assert sentinel.read_text(encoding="utf-8") == "must survive"
