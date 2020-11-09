import unittest


class Hamming:

    def distance(self, a, b):
        """
        liczy odległość Hamminga dla genotypów A i B
        odległość hamminga to różnica genów na takich samych pozycjach
        np AABB oraz ACBA mają odległość Hamminga równą 2
        >>> h = Hamming()
        >>> h.distance("", "")
        0
        >>> h.distance("A", "A")
        0
        >>> h.distance("G", "T")
        1
        >>> h.distance("GGACTGAAATCTG", "GGACTGAAATCTG")
        0
        >>> h.distance("GGACGGATTCTG", "AGGACGGATTCT")
        9
        >>> h.distance("AATG", "AAA")
        Traceback (most recent call last):
            ...
        ValueError: ValueError
        >>> h.distance("ATA", "AGTG")
        Traceback (most recent call last):
            ...
        ValueError: ValueError
        >>> h.distance("", "G")
        Traceback (most recent call last):
            ...
        ValueError: ValueError
        """

        if a == "" and b == "":
            return 0

        if len(a) == 0 or len(b) == 0:
            raise ValueError("ValueError")

        if len(a) != len(b):
            raise ValueError("ValueError")

        if a == b:
            return 0
        else:
            count = 0
            for i in range(len(a)):
                if a[i] != b[i]:
                    count += 1
            return count


# class HammingTest(unittest.TestCase):
#
#     # Utility functions
#     def setUp(self):
#         try:
#             self.temp = Hamming()
#
#         except AttributeError:
#             self.assertRaisesRegex = self.assertRaisesRegexp
#
#     def test_empty_strands(self):
#         self.assertEqual(self.temp.distance("", ""), 0)
#
#     def test_single_letter_identical_strands(self):
#         self.assertEqual(self.temp.distance("A", "A"), 0)
#
#     def test_single_letter_different_strands(self):
#         self.assertEqual(self.temp.distance("G", "T"), 1)
#
#     def test_long_identical_strands(self):
#         self.assertEqual(self.temp.distance("GGACTGAAATCTG", "GGACTGAAATCTG"), 0)
#
#     def test_long_different_strands(self):
#         self.assertEqual(self.temp.distance("GGACGGATTCTG", "AGGACGGATTCT"), 9)
#
#     def test_disallow_first_strand_longer(self):
#         with self.assertRaisesWithMessage(ValueError):
#             self.temp.distance("AATG", "AAA")
#         # self.assertRaises(ValueError, self.temp.distance, "AATG", "AAA")
#
#     def test_disallow_second_strand_longer(self):
#         with self.assertRaisesWithMessage(ValueError):
#             self.temp.distance("ATA", "AGTG")
#         # self.assertRaises(ValueError, self.temp.distance, "ATA", "AGTG")
#
#     def test_disallow_left_empty_strand(self):
#         with self.assertRaisesWithMessage(ValueError):
#             self.temp.distance("", "G")
#         # self.assertRaises(ValueError, self.temp.distance, "", "G")
#
#     def test_disallow_right_empty_strand(self):
#         with self.assertRaisesWithMessage(ValueError):
#             self.temp.distance("G", "")
#         # self.assertRaises(ValueError, self.temp.distance, "G", "")
#
#     def assertRaisesWithMessage(self, exception):
#         return self.assertRaisesRegex(exception, r".+")
#
#     def tearDown(self):
#         self.temp = None


if __name__ == "__main__":
    import doctest
    doctest.testmod()