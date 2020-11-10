import re
import unittest

class Validate:

    def ValidPassword(self, passw):
        """
        metoda sprawdza czy podane hasło (passw) jest prawidłowe
        jeśli jest prawidłowe zwraca true, w przeciwnym wypadku false
        Prawidłowe hasło to hasło składające się z:
        -Co najmniej 8 liter
        -Co najmniej 1 wielka litera, cyfra oraz znak specjalny.

        >>> v = Validate()
        >>> v.ValidPassword("1234567")
        False
        >>> v.ValidPassword("password")
        False
        >>> v.ValidPassword("password1")
        False
        >>> v.ValidPassword("Password.1")
        True
        >>> v.ValidPassword("Password11")
        False
        >>> v.ValidPassword(111)
        Traceback (most recent call last):
            ...
        ValueError
        """

        if not isinstance(passw, str):
            raise ValueError


        hasCapitalLetter = False
        hasNumber = False
        hasChar = False

        if len(passw) < 8:
            return False

        for letter in passw:
            if letter.isupper():
                hasCapitalLetter = True
                break

        numbers = [0,1,2,3,4,5,6,7,8,9]

        for num in numbers:
            if passw.find(str(num)) >= 0:
                hasNumber = True
                break

        characters = '!"#$%&' + "'" + '()*+,-./:;<=>?@[' + "\\" + ']^_`{|}~'

        for char in characters:
            # print(char)
            if passw.find(char) >= 0:
                hasChar = True

        return hasCapitalLetter and hasNumber and hasChar


if __name__ == "__main__":
    import doctest
    doctest.testmod()


class ValidateTest(unittest.TestCase):

    def setUp(self):
        self.temp = Validate()

    def test_less_8(self):
        self.assertEqual(self.temp.ValidPassword("12345"), False)

    def test_must_have_Capital_Letter(self):
        self.assertEqual(self.temp.ValidPassword("password"), False)

    def test_must_have_number(self):
        self.assertEqual(self.temp.ValidPassword("Password"), False)

    def test_must_have_special_char(self):
        self.assertEqual(self.temp.ValidPassword("Password.1"), True)

    def test_passwd_without_char_is_false(self):
        self.assertEqual(self.temp.ValidPassword("Password11"), False)

    def disallow_not_string(self):
        self.assertRaises(ValueError, self.temp.ValidPassword, 111)

    def tearDown(self):
        self.temp = None