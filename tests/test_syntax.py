#!/usr/bin/python

# =============================================================================================
# MODULE DOCSTRING
# =============================================================================================

"""
Test YAML syntax in examples.

"""

# =============================================================================================
# GLOBAL IMPORTS
# =============================================================================================

import os
import pytest
import openmoltools as omt
from pathlib import Path
from yank.experiment import ExperimentBuilder

EXAMPLES = Path(__file__).parent.parent / 'examples'

@pytest.mark.parametrize("path", [
    'hydration/phenol/explicit.yaml',
    'hydration/phenol/implicit.yaml',
    'hydration/freesolv/sams.yaml',
    'binding/abl-imatinib/explicit.yaml',
    'binding/abl-imatinib/implicit.yaml',
    'binding/abl-imatinib/sams.yaml',
    'binding/host-guest/sams-explicit/experiments/analysis.yaml',
    'binding/host-guest/sams-explicit/experiments/experiments.yaml',
    'binding/host-guest/repex.yaml',
    'binding/host-guest/sams.yaml',
    'binding/t4-lysozyme/all-ligands-implicit.yaml',
    'binding/t4-lysozyme/p-xylene-implicit.yaml',
    'binding/t4-lysozyme/p-xylene-explicit.yaml',
    'binding/t4-lysozyme/all-ligands-explicit.yaml',
])
def test_yaml_syntax(path):
    path = os.path.join(EXAMPLES, path)
    with omt.utils.temporary_cd(os.path.dirname(path)):
        builder = ExperimentBuilder(script=path)
