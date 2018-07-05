import unittest


def toString(List):
    return ''.join(List)

def get_permutations(string):

    # Generate all permutations of the input string
    lt = []
    n = len(string)
    if n == 0:
        return {''}
    a = list(string)


    permute(a, 0, n - 1,lt)

    return set(lt)


def permute(a, start, end , lis):
    if start == end:
        lis.append(toString(a))
    else:
        for i in range(start, end + 1):
            a[start], a[i] = a[i], a[start]
            permute(a, start + 1, end, lis)
            a[start], a[i] = a[i], a[start]

















# Tests

class Test(unittest.TestCase):

    def test_empty_string(self):
        actual = get_permutations('')
        expected = set([''])
        self.assertEqual(actual, expected)

    def test_one_character_string(self):
        actual = get_permutations('a')
        expected = set(['a'])
        self.assertEqual(actual, expected)

    def test_two_character_string(self):
        actual = get_permutations('ab')
        expected = set(['ab', 'ba'])
        self.assertEqual(actual, expected)

    def test_three_character_string(self):
        actual = get_permutations('abc')
        expected = set(['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)