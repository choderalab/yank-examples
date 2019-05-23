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
from pathlib import Path
import yaml

import openmoltools as omt
from yank.experiment import ExperimentBuilder, YankLoader

EXAMPLES = Path(__file__).parent.parent / 'examples'

@pytest.mark.parametrize("path", [
    'hydration/phenol/explicit.yaml',
    'hydration/phenol/implicit.yaml',
    'hydration/freesolv/sams.yaml',
    'binding/abl-imatinib/explicit.yaml',
    'binding/abl-imatinib/sams.yaml',
    'binding/host-guest/repex.yaml',
    'binding/host-guest/sams.yaml',
    'binding/t4-lysozyme/all-ligands-implicit.yaml',
    'binding/t4-lysozyme/p-xylene-implicit.yaml',
    'binding/t4-lysozyme/all-ligands-explicit.yaml',
])
def test_yaml_syntax(path):
    """
    Test syntax only. If successful, `ExperimentBuilder`
    will be able to initialize safely.
    """
    path = os.path.join(EXAMPLES, path)
    with omt.utils.temporary_cd(os.path.dirname(path)):
        builder = ExperimentBuilder(script=path)

@pytest.mark.parametrize("path", [
    'binding/t4-lysozyme/p-xylene-explicit.yaml',
    'binding/abl-imatinib/implicit.yaml',
])
def test_yaml_syntax_cuda(path):
    """
    Same as test_yaml_syntax, but removing `platform: CUDA`
    to avoid errors unrelated to syntax if the test machine
    does not have CUDA enabled
    """
    path = EXAMPLES / path
    with omt.utils.temporary_cd(os.path.dirname(path)):
        with open(path) as f:
            data = yaml.load(f, Loader=YankLoader)
        del data['options']['platform']
        builder = ExperimentBuilder(script=data)
