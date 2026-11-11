"""Reference evidence integrity is not an attestation or host status protocol."""
from __future__ import annotations

import copy
import json
from pathlib import Path

import jsonschema
import pytest

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = json.loads((ROOT / "schemas/review-evidence.reference.schema.json").read_text())
EXAMPLE = json.loads((ROOT / "examples/review-evidence.reference.json").read_text())


def validate_reference_evidence(envelope: dict) -> None:
    jsonschema.Draft202012Validator(SCHEMA).validate(envelope)
    kinds = [r["kind"] for r in envelope["reviewers"]]
    if set(kinds) != {"acceptance", "safety", "continuity"}:
        raise ValueError("exactly three distinct reviewer kinds required")
    if len(set(r["bead_ref"] for r in envelope["reviewers"])) != 3:
        raise ValueError("reviewer bead references must be distinct")
    if len(set(r["reviewer_identity"] for r in envelope["reviewers"])) != 3:
        raise ValueError("reviewers must not share one self-reported identity")


def test_well_formed_reference_does_not_claim_independent_evidence() -> None:
    jsonschema.Draft202012Validator.check_schema(SCHEMA)
    validate_reference_evidence(EXAMPLE)
    assert EXAMPLE["outcome"] == "NOT_RUN"
    assert EXAMPLE["authority"] == "REFERENCE_ONLY"
    assert all(r["session_provenance"] == "NOT_VERIFIED" for r in EXAMPLE["reviewers"])


@pytest.mark.parametrize("mutation", ["publisher","pass","host_proven","missing","duplicate_kind","shared_bead","shared_writer"])
def test_evidence_authority_mutations_fail(mutation: str) -> None:
    doc = copy.deepcopy(EXAMPLE)
    if mutation == "publisher":
        doc["authority"] = "TRUSTED_PUBLISHER"
    elif mutation == "pass":
        doc["outcome"] = "PASS"
    elif mutation == "host_proven":
        doc["reviewers"][0]["session_provenance"] = "VERIFIED"
    elif mutation == "missing":
        doc["reviewers"].pop()
    elif mutation == "duplicate_kind":
        doc["reviewers"][1]["kind"] = "acceptance"
    elif mutation == "shared_bead":
        doc["reviewers"][1]["bead_ref"] = doc["reviewers"][0]["bead_ref"]
    elif mutation == "shared_writer":
        doc["reviewers"][1]["reviewer_identity"] = doc["reviewers"][0]["reviewer_identity"]
    with pytest.raises((jsonschema.ValidationError, ValueError)):
        validate_reference_evidence(doc)
