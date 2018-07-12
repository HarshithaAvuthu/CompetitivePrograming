import unittest

def merge_lists(my_list, alices_list):
    """merge these two sorted lists"""

    lst = []
    i = 0
    j = 0
    l1 = len(my_list)
    l2 = len(alices_list)
    while i < l1 or j < l2:
        p1 = my_list[i] if i < l1 else float('inf')
        p2 = alices_list[j] if j < l2 else float('inf')
        if p1 < p2:
            i += 1
            lst.append(p1)
        else:
            j += 1
            lst.append(p2)
    return lst
















# Tests

class Test(unittest.TestCase):

    def test_both_lists_are_empty(self):
        actual = merge_lists([], [])
        expected = []
        self.assertEqual(actual, expected)

    def test_first_list_is_empty(self):
        actual = merge_lists([], [1, 2, 3])
        expected = [1, 2, 3]
        self.assertEqual(actual, expected)

    def test_second_list_is_empty(self):
        actual = merge_lists([5, 6, 7], [])
        expected = [5, 6, 7]
        self.assertEqual(actual, expected)

    def test_both_lists_have_some_numbers(self):
        actual = merge_lists([2, 4, 6], [1, 3, 7])
        expected = [1, 2, 3, 4, 6, 7]
        self.assertEqual(actual, expected)

    def test_lists_are_different_lengths(self):
        actual = merge_lists([2, 4, 6, 8], [1, 7])
        expected = [1, 2, 4, 6, 7, 8]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)