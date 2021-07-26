"""Test solution to robot path programming test.

###############################################################################
# test_robot_path.py
#
# Revision:     1.00
# Date:         7/22/2021
# Author:       Alex
#
# Purpose:      Functional testing of the solution to the robot programming
#               exercise.  Solution tested using multiple ASCII maps.
#
###############################################################################
"""

# %% Imports
# Standard system imports
from pathlib import Path
import filecmp
from shutil import copyfile

# Related third party imports
import pytest

# Local application/library specific imports
import interview.robot.robot_path as rp


# %% Functional tests
# Define file paths to be used for functional testing.
test_path = Path('./tests/func/interview/robot/test_robot_path/testpaths/')
test_files = list(x for x in test_path.iterdir() if x.is_file())
soln_path = Path('./tests/func/interview/robot/test_robot_path/solutions/')
soln_files = list(x for x in soln_path.iterdir() if x.is_file())
test_files.sort()       # Ensure test filenames are ordered
soln_files.sort()       # Ensure solution filenames have same order as tests
num_files = len(test_files)
test_ids = [x.stem for x in test_files]
indices = list(range(num_files))


@pytest.mark.parametrize('index', indices, ids=test_ids)
def test_solution(tmp_path, index):
    """Test solution to robot shortest path programming exercise.

    This test is parameterized and will test the solution against multiple
    ASCII maps.  The resulting output file is compared to a solution file to
    verify that the shortest path is correctly computed.

    Uses pytest's tmp_path fixture to create a temporary directory that will be
    torn down and removed after the test completes.
    """
    # Get paths of test file and its solution file
    test_file = test_files[index]
    soln_file = soln_files[index]
    # Copy the files to the pytest tmp_path directory
    test_copy = tmp_path / test_file.name
    soln_copy = tmp_path / soln_file.name
    copyfile(test_file, test_copy)
    copyfile(soln_file, soln_copy)
    # Pass the path of the copied test file to the solver
    output_file = rp.robot_solution(test_copy)
    # Verify that the output file is the same as the solution file
    assert filecmp.cmp(soln_copy, output_file, shallow=False)
