# Tests for YANK Examples
 
The tests for this repo are contained in the `test_examples` directory. 
Because each test may have different names/files/directories, a couple 
utility functions have been included which let test writers point to the 
directories and files and run the same type of test on them.
 
All the tests are currently 
disabled on travis-ci due to how slow the minimization step is on the CPU 
until a solution can be found.  