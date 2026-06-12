import unittest
from suma_digitos import digitsSum
from palindromos import isPalindrome
from ordenamiento import integerSort


class TestDesafioClever(unittest.TestCase):

    def test_digits_sum(self):
        self.assertEqual(digitsSum(999), 27)
        self.assertEqual(digitsSum(9184501), 28)
        self.assertEqual(digitsSum(12345), 15)

        self.assertEqual(digitsSum(0), 0)
        self.assertEqual(digitsSum(-123), 6)

    def test_is_palindrome(self):
        self.assertTrue(isPalindrome("aabaa"))
        self.assertFalse(isPalindrome("abac"))
        self.assertTrue(isPalindrome("salas"))

        self.assertTrue(isPalindrome("Reconocer"))
        self.assertTrue(isPalindrome("abba"))

    def test_integer_sort(self):
        input_array = [5, -2, 10, 0, 3, -7]
        expected = [-7, -2, 0, 3, 5, 10]
        self.assertEqual(integerSort(input_array), expected)

        self.assertEqual(input_array, [5, -2, 10, 0, 3, -7])

        self.assertEqual(integerSort([]), [])
        self.assertEqual(integerSort([42]), [42])
        self.assertEqual(integerSort([5, 1, 5, 3, 1]), [1, 1, 3, 5, 5])


if __name__ == '__main__':
    unittest.main()