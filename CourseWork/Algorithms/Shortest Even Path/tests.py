import unittest
from even_weights import num_opt_even_weight_paths


def check(prices, k, expected_profit, solution):
    """Checks if a given solution is correct for the given
    price history and k.

    Args:
        prices: a list of turkey prices, where prices[i] is the price
        of a turkey on day i.
        k: the maximum number of turkeys you can buy
        expected_profit: maximum profit from buying up to k turkeys
        solution: A list of trades

    Returns:
        If the given solution has up to k non-overlapping trades
        and generates the maximum profit
    """

    if len(solution) > k:
        return False

    solution = sorted(solution)
    actual_profit = 0
    prev_sell = None
    for idx_buy, idx_sell in solution:
        actual_profit += prices[idx_sell] - prices[idx_buy]
        if prev_sell is None:
            prev_sell = idx_sell
        elif idx_buy <= prev_sell:
            return False
    return expected_profit == actual_profit


tests = [
    (
        {"a": {"b": 3, "c": 5}, "b": {"c": 3}, "c": {}},
        "a",
        {'a': 1, 'b': 0, 'c': 1}
    ),
    (
        {"a": {"b": 3, "c": 5, "d": 2}, "b": {"c": 3}, "d": {"c": 4}, "c": {}},
        "a",
        {'a': 1, 'b': 0, 'd': 1, 'c': 2}
    ),
    (
        {"a": {"b": 3, "c": 5, "d": 2}, "b": {"c": 3}, "d": {"c": 4, "e": 6}, "c": {"e": 2}, "e": {}},
        "a",
        {'a': 1, 'b': 0, 'd': 1, 'c': 2, 'e': 3}
    ),
    (
        {"a": {"b": 3, "c": 5, "d": 2, "e": 8}, "b": {"c": 3, "e": 5}, "d": {"c": 4, "e": 6}, "c": {"e": 2}, "e": {}},
        "a",
        {'a': 1, 'b': 0, 'd': 1, 'c': 2, 'e': 5}
    ),
    (
        {"a": {"b": 3, "c": 5, "d": 2, "e": 1}, "b": {"c": 3, "e": 5}, "d": {"c": 4, "e": 6}, "c": {"e": 2}, "e": {}},
        "a",
        {'a': 1, 'b': 0, 'd': 1, 'c': 2, 'e': 4}
    ),
    (
        {"a": {"b": 1, "c": 1, "d": 1, "e": 1}, "b": {"c": 1, "d": 1, "e": 1}, "c": {"d": 1, "e": 1}, "d": {"e": 1},
         "e": {}},
        "a",
        {'a': 1, 'b': 0, 'c': 1, 'd': 2, 'e': 3}
    ),
    (
        {"a": {"b": 1, "c": 1, "d": 1}, "b": {"c": 1, "d": 1, "e": 2}, "c": {"d": 1, "e": 2}, "d": {"e": 2}, "e": {}},
        "a",
        {'a': 1, 'b': 0, 'c': 1, 'd': 2, 'e': 3}
    ),
]

# Test 7 - large test, should run in about a second
N = 1000
graph = {u: {} for u in range(N)}
for u in graph:
    for v in range(u + 1, N):
        graph[u][v] = 1
solution = {i: i - 1 for i in range(1, N)}
solution[0] = 1
tests.append((graph, 0, solution))

# Test 8 - large test, should run in about a second
N = 1000
graph = {u: {} for u in range(N)}
for u in graph:
    for v in range(u + 1, N):
        graph[u][v] = v - u
solution = {0: 1}
for i in range(1, N):
    solution[i] = 0
    if i % 2 == 0:
        solution[i] = 2 ** (i - 1)
tests.append((graph, 0, solution))


class TestCases(unittest.TestCase):
    def test_00(self):
        graph, start, solution = tests[0]
        self.assertEqual(num_opt_even_weight_paths(graph, start), solution)

    def test_01(self):
        graph, start, solution = tests[1]
        self.assertEqual(num_opt_even_weight_paths(graph, start), solution)

    def test_02(self):
        graph, start, solution = tests[2]
        self.assertEqual(num_opt_even_weight_paths(graph, start), solution)

    def test_03(self):
        graph, start, solution = tests[3]
        self.assertEqual(num_opt_even_weight_paths(graph, start), solution)

    def test_04(self):
        graph, start, solution = tests[4]
        self.assertEqual(num_opt_even_weight_paths(graph, start), solution)

    def test_05(self):
        graph, start, solution = tests[5]
        self.assertEqual(num_opt_even_weight_paths(graph, start), solution)

    def test_06(self):
        graph, start, solution = tests[6]
        self.assertEqual(num_opt_even_weight_paths(graph, start), solution)

    def test_07(self):
        graph, start, solution = tests[7]
        self.assertEqual(num_opt_even_weight_paths(graph, start), solution)

    def test_08(self):
        graph, start, solution = tests[8]
        self.assertEqual(num_opt_even_weight_paths(graph, start), solution)


if __name__ == "__main__":
    res = unittest.main(verbosity=3, exit=False)