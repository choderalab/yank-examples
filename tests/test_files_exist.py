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

from pathlib import Path
import filecmp
import os
import sys

import pytest
import yaml


def _dirs_equal(comparer):
    """
    Recurse over subdirs testing that there are no:
    - files with same name, but different contents
    - files with different names
    """
    yield all(not bool(x) for x in (comparer.diff_files, comparer.left_only, comparer.right_only))
    for subdir in comparer.subdirs.values():
        yield from _dirs_equal(subdir)


def test_files_exist():
    """
    Compare examples copied to $PREFIX/share/yank
    and those available in the current repo. They should match!
    """
    repo_examples = Path(__file__).parent.parent / 'examples'
    prefix_examples = Path(sys.prefix) / 'share' / 'yank' / 'examples'
    assert repo_examples.is_dir()
    assert prefix_examples.is_dir()
    comparer = filecmp.dircmp(repo_examples, prefix_examples)
    assert all(_dirs_equal(comparer))