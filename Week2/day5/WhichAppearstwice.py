import unittest


def find_repeat(numbers_list):

    # Find the number that appears twice
    size=len(numbers_list)
    for i in range (0, size):
        for j in range (i + 1, size):
            if numbers_list[i] == numbers_list[j]:
                return(numbers_list[i])
















# Tests

class Test(unittest.TestCase):

    def test_short_list(self):
        actual = find_repeat([1, 2, 1])
        expected = 1
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_repeat([4, 1, 3, 4, 2])
        expected = 4
        self.assertEqual(actual, expected)

    def test_long_list(self):
        actual = find_repeat([1, 5, 9, 7, 2, 6, 3, 8, 2, 4])
        expected = 2
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)