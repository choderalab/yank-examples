#!/usr/bin/python

# =============================================================================================
# MODULE DOCSTRING
# =============================================================================================

"""
Test examples.

"""

# =============================================================================================
# GLOBAL IMPORTS
# =============================================================================================

import os
import shutil
import subprocess
import tempfile

import openmoltools as omt

from nose.plugins.attrib import attr
from unittest import skipIf
from distutils.util import strtobool

import yank

from .base_checks import HAVE_OE, openeye_exception_message


# =============================================================================================
# UTILITY FUNCTIONS
# =============================================================================================

def add_overrides():
    """
    This function spits out the override flags based on environment variables, mainly for nose tests.

    If the parameter is not set, then there is no overwrite and the default of the script is used

    The environment variables it searches for are the following:
    YANK_MINIMIZE : bool-like
        Choose to minimize the examples
        Tries to parse the variable as a boolean, but if it cannot, this override is not set
    YANK_NUMBER_OF_ITERATIONS : int-like
        Choose how many iterations to run
        Tries to parse the variable as an int, but if it cannot, this override is not set
    YANK_PLATFORM : str
        Choose the platform to run on, see the YANK docs for valid choices (case-sensitive)
        Tries to parse variable as str, but if it cannot, no override is set.
    """
    additional_commands = []

    # Setup minimizes
    minimize = os.environ.get('YANK_MINIMIZE', None)
    try:
        minimize = strtobool(minimize)
    except (AttributeError, ValueError):
        minimize = None
    if minimize is None:  # Check if none (could not parse)
        pass
    elif minimize:  # Check the boolean setting
        additional_commands.append("-o options:minimize:yes")
    else:
        additional_commands.append("-o options:minimize:no")

    # Production number of iterations
    number_of_iterations = os.environ.get('YANK_NUMBER_OF_ITERATIONS', None)
    try:
        number_of_iterations = int(number_of_iterations)
    except (TypeError, ValueError):
        number_of_iterations = None
    if number_of_iterations is None:  # Check if none (could not parse)
        pass
    else:
        additional_commands.append("-o options:number_of_iterations:{}".format(number_of_iterations))

    # Setup Platform
    platform = os.environ.get('YANK_PLATFORM', None)
    try:
        assert platform in ['fastest', 'Reference', 'OpenCL', 'CUDA']
    except AssertionError:
        platform = None
    if platform is None:  # Check if none (could not parse)
        pass
    else:
        additional_commands.append("-o options:platform:{}".format(platform))

    # Finalize and output the string
    return " ".join(additional_commands)


def run_examples(example_directory, yaml_name):
    """
    Generalized function to run an example in a given source directory.
    Provide it with a target directory (to copy all files) and name of a yaml script to run

    This script reads the environment variable to determine if the

    Parameters
    ----------
    example_directory: str
        Directory name/path in the $PYTHONSOURCE/share/yank/examples to copy over to temp folder
    yaml_name: str
        Name of the YAML script inside example_directory to and run with the .yaml extension
    """
    # Get Example Paths
    prefix = yank.__file__
    # Yank path is $PREFIX/lib/pythonX.Y/site-packages/yank/__init__.py, we want $PREFIX
    for i in range(5):  # 5 levels of nesting
        prefix = os.path.dirname(prefix)
    examples_path = os.path.join(prefix, 'share', 'yank', 'examples')
    full_example_directory_path = os.path.join(examples_path, example_directory)
    example_final_directory = os.path.basename(example_directory)
    # Create the temporary files
    temporary_directory = tempfile.mkdtemp()
    with omt.utils.temporary_cd(temporary_directory):
        # Copy over all files
        shutil.copytree(full_example_directory_path, example_final_directory)
        with omt.utils.temporary_cd(example_final_directory):
            # Initialize script
            command = "yank script "
            # Add overrides based on environment
            command += add_overrides()
            # Finalize command
            command += " --yaml={}".format(yaml_name)
            # Run the script!
            return_code = subprocess.call(command, shell=True)
            if return_code:
                raise Exception('Example {} returned exit code {}'.format(example_directory, return_code))
    # Cleanup
    shutil.rmtree(temporary_directory)
    return


@attr('slow')
def test_t4_p_xylene_explicit():
    """
    Test p-xylene binding to t4 lysozyme example in explicit solvent
    """
    example_dir = os.path.join('binding', 't4-lysozyme')
    yaml_name = 'p-xylene-explicit.yaml'
    run_examples(example_dir, yaml_name)


#@attr('slow')
def test_t4_p_xylene_implicit():
    """
    Test p-xylene binding to t4 lysozyme example in implicit solvent
    """
    example_dir = os.path.join('binding', 't4-lysozyme')
    yaml_name = 'p-xylene-implicit.yaml'
    run_examples(example_dir, yaml_name)


@attr('slow')
@skipIf(not HAVE_OE, "Cannot test openeye module without OpenEye tools.\n" + openeye_exception_message)
def test_t4_all_ligands_explicit():
    """
    Test that the all-binders to t4 lysozyme example works in explicit solvent
    This is a slow test
    """
    example_dir = os.path.join('binding', 't4-lysozyme')
    yaml_name = 'all-ligands-explicit.yaml'
    run_examples(example_dir, yaml_name)


#@attr('slow')
@skipIf(not HAVE_OE, "Cannot test openeye module without OpenEye tools.\n" + openeye_exception_message)
def test_t4_all_ligands_implicit():
    """
    Test that the all-binders to t4 lysozyme example works in implicit solvent
    This is a slow test
    """
    example_dir = os.path.join('binding', 't4-lysozyme')
    yaml_name = 'all-ligands-implicit.yaml'
    run_examples(example_dir, yaml_name)


@attr('slow')
def test_hydration_phenol_implicit():
    """
    Test that the phenol hydration implicit example
    """
    example_dir = os.path.join('hydration', 'phenol')
    yaml_name = 'implicit.yaml'
    run_examples(example_dir, yaml_name)


@attr('slow')
def test_hydration_phenol_explicit():
    """
    Test that the phenol hydration explicit example
    """
    example_dir = os.path.join('hydration', 'phenol')
    yaml_name = 'explicit.yaml'
    run_examples(example_dir, yaml_name)


#@attr('slow')
@skipIf(not HAVE_OE, "Cannot test openeye module without OpenEye tools.\n" + openeye_exception_message)
def test_binding_host_guest():
    """
    Test the host guest binding example
    """
    example_dir = os.path.join('binding', 'host-guest')
    yaml_name = 'yank.yaml'
    run_examples(example_dir, yaml_name)


#@attr('slow')
@skipIf(not HAVE_OE, "Cannot test openeye module without OpenEye tools.\n" + openeye_exception_message)
def test_hydration_freesolv():
    """
    Test that the hydration freesolv database example works
    """
    example_dir = os.path.join('hydration', 'freesolv')
    yaml_name = 'yank.yaml'
    run_examples(example_dir, yaml_name)
