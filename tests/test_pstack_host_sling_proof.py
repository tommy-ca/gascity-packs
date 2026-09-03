from __future__ import annotations

from pathlib import Path

import pytest

from scripts import pstack_host_sling_proof
from scripts.gascity_pack_inference_gate import GateError


def write_roles_city(city_dir: Path, *, name: str = "pstack-pack-inference-gate") -> None:
    city_dir.mkdir(parents=True)
    (city_dir / ".gc").mkdir()
    (city_dir / "city.toml").write_text(
        "\n".join(
            [
                "[daemon]",
                "formula_v2 = true",
                "",
                "[rigs.imports.gc]",
                'source = "/tmp/gascity/roles"',
                "",
            ]
        ),
        encoding="utf-8",
    )
    (city_dir / ".gc" / "site.toml").write_text(f'workspace_name = "{name}"\n', encoding="utf-8")


def test_city_looks_canonical_under_home_gc_cities() -> None:
    path = Path.home() / ".gc" / "cities" / "demo"
    assert pstack_host_sling_proof.city_looks_canonical(path, "demo")


def test_city_looks_canonical_name_gastown(tmp_path: Path) -> None:
    assert pstack_host_sling_proof.city_looks_canonical(tmp_path, "gastown")
    assert pstack_host_sling_proof.city_looks_canonical(tmp_path, "Gastown")
    assert not pstack_host_sling_proof.city_looks_canonical(tmp_path, "pstack-pack-inference-gate")


def test_require_disposable_roles_city_accepts_formula_v2_and_roles(tmp_path: Path) -> None:
    city_dir = tmp_path / "city"
    write_roles_city(city_dir)
    assert pstack_host_sling_proof.require_disposable_roles_city(city_dir) == "pstack-pack-inference-gate"


def test_require_disposable_roles_city_refuses_missing_formula_v2(tmp_path: Path) -> None:
    city_dir = tmp_path / "city"
    write_roles_city(city_dir)
    (city_dir / "city.toml").write_text('[rigs.imports.gc]\nsource = "/tmp/gascity/roles"\n', encoding="utf-8")
    with pytest.raises(GateError, match="formula_v2"):
        pstack_host_sling_proof.require_disposable_roles_city(city_dir)


def test_require_disposable_roles_city_refuses_missing_roles(tmp_path: Path) -> None:
    city_dir = tmp_path / "city"
    write_roles_city(city_dir)
    (city_dir / "city.toml").write_text("[daemon]\nformula_v2 = true\n", encoding="utf-8")
    with pytest.raises(GateError, match="gascity/roles"):
        pstack_host_sling_proof.require_disposable_roles_city(city_dir)


def test_require_disposable_roles_city_refuses_canonical_name(tmp_path: Path) -> None:
    city_dir = tmp_path / "city"
    write_roles_city(city_dir, name="gastown")
    with pytest.raises(GateError, match="canonical"):
        pstack_host_sling_proof.require_disposable_roles_city(city_dir)


def test_proof_payload_orders_poteto_then_build() -> None:
    proof = pstack_host_sling_proof.HostSlingProof(
        city_disposable=True,
        city="/tmp/city",
        poteto=pstack_host_sling_proof.CookRouteReceipt(
            formula="pstack-poteto-mode",
            root_id="de-fr9",
            routed_to="fixture/pstack.coordinator",
        ),
        build=pstack_host_sling_proof.CookRouteReceipt(
            formula="pstack-build",
            root_id="bd-1",
            routed_to="fixture/pstack.architect",
        ),
    )
    payload = pstack_host_sling_proof.proof_payload(proof)
    assert list(payload) == ["city_disposable", "city", "poteto", "build"]
    assert list(payload["poteto"]) == ["formula", "root_id", "routed_to"]
    assert "review" not in payload
    partial = pstack_host_sling_proof.proof_payload(
        pstack_host_sling_proof.HostSlingProof(
            city_disposable=True,
            city="/tmp/city",
            poteto=proof.poteto,
        )
    )
    assert "build" not in partial
    assert list(partial) == ["city_disposable", "city", "poteto"]


def test_script_does_not_launch_review_or_build_helpers() -> None:
    text = Path(pstack_host_sling_proof.__file__).read_text(encoding="utf-8")
    assert "launch_review_formula" not in text
    assert "launch_build_formula" not in text
    assert "parse_host_sling_root" in text
    assert "parse_host_sling_routed_to" in text
