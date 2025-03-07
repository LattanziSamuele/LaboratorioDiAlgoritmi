from algoritmi_lcs.forza_bruta import lcs_brute_force
from algoritmi_lcs.ricorsivo import lcs_recursive
from algoritmi_lcs.memoizzazione import lcs_memoized
from algoritmi_lcs.bottom_up import lcs_bottom_up
from test import *
import random
import string
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

if __name__ == '__main__':
    lcs_algorithms = {
      "brute_force": lcs_brute_force,
      "memoization": lcs_memoized,
      "bottom_up": lcs_bottom_up
    }
    string_lengths = list(range(1, 26, 1))

    num_test = 5

    test_same_dimension(lcs_algorithms, string_lengths, num_test)

    lcs_algorithms = {
        "memoization": lcs_memoized,
        "bottom_up": lcs_bottom_up
    }
    string_lengths = list(range(1, 501, 10))

    num_test = 5

    test_same_dimension(lcs_algorithms, string_lengths, num_test)

    lcs_algorithms = {
        "brute_force": lcs_brute_force,
        "recursive": lcs_recursive,
        "memoization": lcs_memoized,
        "bottom_up": lcs_bottom_up
    }

    iterations = 200

    num_tests = 5

    test_time_diff_lengths(lcs_algorithms, iterations, num_tests)

    test_time_repeated_strings(lcs_algorithms, iterations, num_tests)

    test_memory_diff_lengths(lcs_algorithms, iterations, num_tests)


"""lcs_algorithms = {
"brute_force": lcs_brute_force,
"recursive": lcs_recursive,
"memoization": lcs_memoized,
"bottom_up": lcs_bottom_up
}

string_lengths = list(range(1, 17, 1))

num_test = 1

test_same_dimension(lcs_algorithms, string_lengths, num_test)"""