import sorting 
import random
import time

random.seed(260)

# Please read all of the following before starting your implementation:
#
# Details about Gradescope submission:
#
# - You should not include anything outside of standard Python libraries.
# - Functions should be tested using Python 3.6+ on a Linux environment.
# - You must submit requirements.py, sorting.py, and a pdf file with the writeup, along with any additional source files that you might create
# - The submission should either be the files themselves, or a zip file not containing any directories.
# - We have provided a project1_tests.py file that contains some simple test cases to give an idea of how we will be running your
#   code. Please use that file when testing your implementation.
#
# (1) Complete the implementations of the following sorting algorithms:
# 
# - MergeSort
# - QuickSort
# - InsertionSort
# - ShellSort
# - BucketSort
# - RadixSort
#
# - Each algorithm is implemented as a class. 
# - project1_tests.py will test the correctness of the sorted outputs for each of the algorithms. 
#
# (2) Experimental time analysis
#
# - The project1_tests.py file also has code to measure the execution time of each algorithm. This is after verifying functional correctness.
#
# - For each implementation, you need to perform runtime experiments on random permutations, with 5 runs for each problem size, for increasing problem sizes.
# - The project1_tests.py file sets the random seed to 260 and runs all algorithms for sizes from 1000 to 16000. Use this default setting for the 1st run.
# - For the remaining 4 runs, choose 4 different seeds. 
# - 
# - Perform the set of experiments for each of the following distributions:
#   - (A) Uniformly distributed permutations, where all permutations are equally likely. This is done for you with the rand.randint() function.
#   - (B) Almost-sorted permutations. These are generated by starting with a sorted array/vector of n numbers, say, the numbers 1,2,3,...,n, in this order. 
#       - Then, independently choose 2log n pairs, (i,j), where i and j are uniformly-chosen random integers in the range from 0 to n-1, 
#       - and swap the numbers at positions i and j in the array/vector.
#       - You will need to implement the code for this in the project1_tests.py file.
#
# - Plot the results of execution time vs the data size for all algorithms (with uniformly distrubted permuations on one plot and almost-sorted permutations on another).
# - Empirically determine the upperbound of the algorithm's running time for each type of distribution.
# - Which common big-O function best describes the observed run-time for each algorithm? O(1), O(log n), O(n), O(nlogn), O(n^2), O(n^3)
# - 
# - Rank all of the sorting algorithms from slowest to fastest based on your experimental results for each distribution.
# - Create 2 tables (1 for each distribution). Each row of the table will have 3 columns: the algorithm name, observed asymptotic run time, theoretical big-O run time.
# - 
# - Do you observe differences between the observed run-time vs the theoretical big-O run time?
# - Include your plots, tables, and observations in pdf doc. 
#
# (3) Invent your own sorting algorithm. You can optimize one of the algorithms you implemented for this project or create a new algorithm.
# - The optimization should provide meaningful run time improvement.
# - Implement a class for this new algorithm (using the provided code as reference).
# - Verify functionaliy as in (1) and repeate the same experiments as in (2) to measure performance. 
# - Describe the algorithm, provide pseudocode, and provide evidence of the run time improvement.  
#
#
# Details about Gradescope submission:
#
# - You should not include anything outside of standard Python libraries.
# - Functions should be tested using Python 3.6+ on a Linux environment.
# - You must submit the requirements.py and the sorting.py files, along with any additional source files that you might create
# - The submission should either be the files themselves, or a zip file not containing any directories.
# - We have provided a project1_tests.py file that contains some simple test cases to give an idea of how we will be running your
#   code. Please use that file when testing your implementation.
#