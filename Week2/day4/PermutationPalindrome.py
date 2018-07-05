import unittest


def has_palindrome_permutation(the_string):

    # Check if any permutation of the input is a palindrome
    dict1 = {}
    lt=[]

    for char in the_string:
        if char in dict1:
            dict1[char] += 1
        else:
            lt.append(char)
            dict1[char] = 1


    for c in lt:
        if dict1[c] % 2 == 0:
            del dict1[c]

    if len(dict1)>1:
        return False

    return True

















# Tests

class Test(unittest.TestCase):

    def test_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcbcd')
        self.assertTrue(result)

    def test_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabccbdd')
        self.assertTrue(result)

    def test_no_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcd')
        self.assertFalse(result)

    def test_no_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabbcd')
        self.assertFalse(result)

    def test_empty_string(self):
        result = has_palindrome_permutation('')
        self.assertTrue(result)

    def test_one_character_string(self):
        result = has_palindrome_permutation('a')
        self.assertTrue(result)


unittest.main(verbosity=2)
