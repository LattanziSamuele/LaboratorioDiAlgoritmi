from algoritmi_lcs.forza_bruta import lcs_brute_force
from algoritmi_lcs.ricorsivo import lcs_recursive
from algoritmi_lcs.memoizzazione import lcs_memoized
from algoritmi_lcs.bottom_up import lcs_bottom_up
import random
import string
import timeit
import matplotlib
import sys
import tracemalloc
from tabulate import tabulate
import numpy as np

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


def generate_random_string(length):
    x = ''.join(random.choices(string.ascii_uppercase, k=length))
    return x


def generate_random_string_from_alphabet(length, alphabet="ABCDEFGH"):
    x = ''.join(random.choices(alphabet, k=length))
    return x


def generate_repeated_string(length, alphabet="ABCD", min_repetition_size=2, max_repetition_size=4):
    s = []
    while len(s) < length:
        char = random.choice(alphabet)
        block_size = random.randint(min_repetition_size, max_repetition_size)
        s.extend([char] * block_size)
    return ''.join(s[:length])


def measure_time(lcs_function, x, y):
    start_time = timeit.default_timer()
    lcs_function(x, y)
    stop_time = timeit.default_timer()
    return stop_time - start_time


def measure_total_memory(lcs_func, x, y):
    tracemalloc.start()
    lcs_func(x, y)
    peak = tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()
    return peak



def test_same_dimension(lcs_algorithms, string_lengths, num_test):
    if len(string_lengths) <= 15:
        results = {"brute_force": [], "recursive": [], "memoization": [], "bottom_up": []}
    elif len(string_lengths) <= 25:
        results = {"brute_force": [], "memoization": [], "bottom_up": []}
    else:
        results = {"memoization": [], "bottom_up": []}

    for length in string_lengths:
        x = generate_random_string(length)
        y = generate_random_string(length)
        print(f"\n Testing con stringhe di lunghezza {length}...")

        for name, function in lcs_algorithms.items():
            times = [measure_time(function, x, y) for _ in range(num_test)]
            avg_time = sum(times) / num_test
            results[name].append(avg_time)
            print(f"  {name}: {avg_time:.6f} sec")

    if len(string_lengths) <= 15:
        result = plot_results("Confronto Algoritmi LCS", "Lunghezza stringhe (m=n)", "Tempo di Esecuzione (s)",
                              string_lengths, results["memoization"], results["bottom_up"], results["brute_force"],
                              results["recursive"])
        result.savefig("Confronto Algoritmi LCS1.png", dpi=300)
    elif len(string_lengths) <= 25:
        result = plot_results("Confronto Algoritmi LCS", "Lunghezza stringhe (m=n)", "Tempo di Esecuzione (s)",
                              string_lengths, results["memoization"], results["bottom_up"], results["brute_force"])
        result.savefig("Confronto Algoritmi LCS2.png", dpi=300)
    else:
        result = plot_results("Confronto Algoritmi LCS", "Lunghezza stringhe (m=n)", "Tempo di Esecuzione (s)",
                              string_lengths, results["memoization"], results["bottom_up"])
        result.savefig("Confronto Algoritmi LCS3.png", dpi=300)


def test_time_diff_lengths(lcs_algorithms, iterations, num_tests, min_len=1, max_len=15):
    results = {name: [] for name in lcs_algorithms}

    for _ in range(iterations):
        m = random.randint(min_len, max_len)
        n = random.randint(min_len, max_len)
        x = generate_random_string(m)
        y = generate_random_string(n)

        for name, function in lcs_algorithms.items():
            times = [measure_time(function, x, y) for _ in range(num_tests)]
            avg_time = sum(times) / num_tests
            results[name].append(avg_time)

    print(f"\n Testing con Stringhe di lunghezza diversa...")
    print_statistics_time(results)


def test_time_repeated_strings(lcs_algorithms, iterations, num_tests, min_len=5, max_len=15):
    results = {name: [] for name in lcs_algorithms}

    for _ in range(iterations):
        m = random.randint(min_len, max_len)
        n = random.randint(min_len, max_len)

        x = generate_repeated_string(m)
        y = generate_repeated_string(n)

        for name, function in lcs_algorithms.items():
            times = [measure_time(function, x, y) for _ in range(num_tests)]
            avg_time = sum(times) / num_tests
            results[name].append(avg_time)

    print(f"\n Testing con Stringhe di lunghezza diversa...")
    print_statistics_time(results)


def test_memory_diff_lengths(lcs_algorithms, iterations, num_tests, min_len=1, max_len=15):
    results = {name: [] for name in lcs_algorithms}
    for _ in range(iterations):
        m = random.randint(min_len, max_len)
        n = random.randint(min_len, max_len)
        x = generate_random_string(m)
        y = generate_random_string(n)

        for name, function in lcs_algorithms.items():
            mem_usage = [measure_total_memory(function, x, y) for _ in range(num_tests)]
            avg_mem = sum(mem_usage) / num_tests
            results[name].append(avg_mem)

    print_statistics_mem("Memoria totale usata", results)


def print_statistics_time(results):
    for algo, times in results.items():
        print(f"\n Statistiche per {algo}:")
        print(f"  - Tempo medio: {np.mean(times):.6f} sec")
        print(f"  - Mediana: {np.median(times):.6f} sec")
        print(f"  - Tempo massimo: {np.max(times):.6f} sec")
        print(f"  - Tempo minimo: {np.min(times):.6f} sec")


def print_statistics_mem(title, results):
    print(f"\n {title}")
    for algo, values in results.items():
            print(f"    {algo}:")
            print(f"    - Memoria media: {np.mean(values):.2f} bytes")
            print(f"    - Mediana: {np.median(values):.2f} bytes")
            print(f"    - Memoria massima: {np.max(values):.2f} bytes")
            print(f"    - Memoria minima: {np.min(values):.2f} bytes")


def plot_results(title, x_lab, y_lab, x, memoized, bottom_up, brute_force=None, recursive=None):
    figure = plt.figure()
    plt.title(title)
    plt.xlabel(x_lab)
    plt.ylabel(y_lab)

    if brute_force:
        plt.plot(x, brute_force, color='red', label='Brute Force')
    if recursive:
        plt.plot(x, recursive, color='blue', label='Recursive')
    plt.plot(x, memoized, color='green', label='Memoized')
    plt.plot(x, bottom_up, color='purple', label='Bottom Up')

    plt.legend()
    plt.grid(True)
    return figure
