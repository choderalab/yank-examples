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
import re

import openmoltools as omt

from nose.plugins.attrib import attr

import yank

# =============================================================================================
# UTILITY FUNCTIONS
# =============================================================================================


def prepare_number_of_iterations(yaml_string):
    """
    Modify the YAML file string to figure out if we need to modify the YAML string

    3 Cases:
    1) number_of_iterations present: modify the number after to 1
    2) number_of_iterations absent but options present: add the line
    3) options absent: add options, add number_of_iterations.

    :param yaml_string: Raw string from a .yaml file used for YANK. === NO STRING MANIPULATION BEFORE FEEDING IN===
    :return: parsed_yaml_string: Modified string with number_of_iterations = 0 parsed
    """

    iteration_var = "number_of_iterations"
    number_of_iterations = "1"
    if iteration_var in yaml_string:  # Case 1
        search_string = "number_of_iterations:\s*\d+"
        replacement_string = "number_of_iterations: " + number_of_iterations
    elif "options:" in yaml_string:  # Case 2
        # Compute indentation level. May need to exclude \n from \s: [ \t\n\r\f\v]
        number_of_spaces = len(re.search("(?:options:\s*\n+)\s+", yaml_string).group(0))
        search_string = "options:\n"
        replacement_string = search_string + ' ' * number_of_spaces + iteration_var + ': ' + number_of_iterations
    else:  # Case 3
        # Use re.match here since we are looking from the start of the string
        match = re.match("(?:\s*\S+\s*\n+)\s+", yaml_string)
        if not match:  # Check for 0 length string
            raise IOError("yaml_string does not appear to be in any expected format!")
        number_of_spaces = len(match.groups(0))
        search_string = "$"
        replacement_string = "\n\noptions:\n" + ' ' * number_of_spaces + iteration_var + ': ' + number_of_iterations
    parsed_yaml_string = re.sub(search_string, replacement_string, yaml_string)
    return parsed_yaml_string


def run_examples(example_directory, yaml_name):
    """
    Generalized function to run an example in a given source directory.
    Provide it with a target directory (to copy all files) and name of a yaml script to run

    :param example_directory: Directory name/path in the $PYTHONSOURCE/share/yank/examples to copy over to temp folder
    :param yaml_name: Name of the YAML script inside example_directory to tweak and run with the .yaml extension
    :return: None
    """
    # Get Example Paths
    prefix = yank.__file__
    # Yank path is $PREFIX/lib/pythonX.Y/site-packages/yank/__init__.py, we want $PREFIX
    for i in range(5):  # 5 levels of nesting
        prefix = os.path.dirname(prefix)
    examples_path = os.path.join(prefix, 'share', 'yank', 'examples')
    full_example_directory_path = os.path.join(examples_path, example_directory)
    # Create the temporary files
    temporary_directory = tempfile.mkdtemp()
    with omt.utils.temporary_cd(temporary_directory):
        # Copy over all files
        for example_file in os.listdir(full_example_directory_path):
            shutil.copy2(example_file, '.')  # Copy to current folder since we already chdir'd here
        # Get the yaml file going!
        with open(yaml_name) as f:
            raw_yaml = f.read()
        processed_yaml = prepare_number_of_iterations(raw_yaml)
        with open(yaml_name, 'w') as f:
            f.write(processed_yaml)
        # Run the script!
        command = "yank script --yaml={}".format(yaml_name)
        return_code = subprocess.call(command)
        if return_code:
            raise Exception('Example %s returned exit code %d' % (example_directory, return_code))
    return


def test_t4_p_xylene_explicit():
    """
    Test p-xylene binding to t4 lysozyme example in explicit solvent
    """
    example_dir = os.path.join('binding', 't4-lysozyme')
    yaml_name = 'p-xylene-explicit.yaml'
    run_examples(example_dir, yaml_name)


def test_t4_p_xylene_implciit():
    """
    Test p-xylene binding to t4 lysozyme example in implicit solvent
    """
    example_dir = os.path.join('binding', 't4-lysozyme')
    yaml_name = 'p-xylene-impicit.yaml'
    run_examples(example_dir, yaml_name)


@attr('!slow')
def test_t4_all_ligands_explicit():
    """
    Test that the all-binders to t4 lysozyme example works in explicit solvent
    This is a slow test
    """
    example_dir = os.path.join('binding', 't4-lysozyme')
    yaml_name = 'all-ligands-explicit.yaml'
    run_examples(example_dir, yaml_name)


@attr('!slow')
def test_t4_all_ligands_implicit():
    """
    Test that the all-binders to t4 lysozyme example works in implicit solvent
    This is a slow test
    """
    example_dir = os.path.join('binding', 't4-lysozyme')
    yaml_name = 'all-ligands-implicit.yaml'
    run_examples(example_dir, yaml_name)


def test_hydration_phenol_implicit():
    """
    Test that the phenol hydration implicit example
    """
    example_dir = os.path.join('hydration', 'phenol')
    yaml_name = 'implicit.yaml'
    run_examples(example_dir, yaml_name)


def test_hydration_phenol_explicit():
    """
    Test that the phenol hydration explicit example
    """
    example_dir = os.path.join('hydration', 'phenol')
    yaml_name = 'explicit.yaml'
    run_examples(example_dir, yaml_name)

def test_binding_host_guest():
    """
    Test the host guest binding example
    """
    example_dir = os.path.join('binding', 'host-guest')
    yaml_name = 'yank.yaml'
    run_examples(example_dir, yaml_name)


def test_hydration_freesolv():
    """
    Test that the hydration freesolv database example works
    """
    example_dir = os.path.join('hydration', 'freesolv')
    yaml_name = 'yank.yaml'
    run_examples(example_dir, yaml_name)