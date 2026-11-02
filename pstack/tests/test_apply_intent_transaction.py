"""Transactional OpenSpec application regressions. No OpenSpec CLI required."""
from __future__ import annotations

import importlib.util
import pathlib
import sys

import pytest

SCRIPT = pathlib.Path(__file__).resolve().parents[1] / "scripts" / "apply_intent_change.py"


def load_script():
    spec = importlib.util.spec_from_file_location("pstack_apply_transaction", SCRIPT)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_invalid_change_does_not_replace_existing_tree(tmp_path, monkeypatch):
    module = load_script()
    source = tmp_path / "source"
    source.mkdir()
    (source / "proposal.md").write_text("new", encoding="utf-8")
    dest = tmp_path / "repo"
    target = dest / "openspec" / "changes" / "change"
    target.mkdir(parents=True)
    sentinel = target / "proposal.md"
    sentinel.write_text("old", encoding="utf-8")
    monkeypatch.setattr(module, "validate", lambda *_: 7)
    monkeypatch.setattr(sys, "argv", ["apply", "--source", str(source), "--dest", str(dest), "--change", "change"])
    assert module.main() == 7
    assert sentinel.read_text(encoding="utf-8") == "old"
    assert set(target.parent.iterdir()) == {target}


def test_successful_copy_promotes_new_tree_and_removes_previous(tmp_path):
    module = load_script()
    source = tmp_path / "source"
    source.mkdir()
    (source / "proposal.md").write_text("new", encoding="utf-8")
    target = tmp_path / "dest" / "changes" / "change"
    target.mkdir(parents=True)
    (target / "stale.md").write_text("old", encoding="utf-8")
    module.copy_change(source, target)
    assert (target / "proposal.md").read_text(encoding="utf-8") == "new"
    assert not (target / "stale.md").exists()
    assert list(target.parent.iterdir()) == [target]


def test_promotion_failure_restores_previous_tree(tmp_path, monkeypatch):
    module = load_script()
    source = tmp_path / "source"
    source.mkdir()
    (source / "proposal.md").write_text("new", encoding="utf-8")
    target = tmp_path / "dest" / "changes" / "change"
    target.mkdir(parents=True)
    (target / "keep.md").write_text("old", encoding="utf-8")
    original_rename = pathlib.Path.rename

    def break_promotion(path, destination):
        if path.name == "candidate":
            raise OSError("injected promotion failure")
        return original_rename(path, destination)

    monkeypatch.setattr(pathlib.Path, "rename", break_promotion)
    with pytest.raises(OSError, match="injected"):
        module.copy_change(source, target)
    assert (target / "keep.md").read_text(encoding="utf-8") == "old"
    assert list(target.parent.iterdir()) == [target]


def test_symlink_target_refused(tmp_path):
    module = load_script()
    source = tmp_path / "source"
    source.mkdir()
    outside = tmp_path / "outside"
    outside.mkdir()
    (outside / "keep.md").write_text("intact", encoding="utf-8")
    dest = tmp_path / "target"
    dest.symlink_to(outside, target_is_directory=True)
    with pytest.raises(SystemExit, match="symlink"):
        module.copy_change(source, dest)
    assert (outside / "keep.md").read_text(encoding="utf-8") == "intact"
