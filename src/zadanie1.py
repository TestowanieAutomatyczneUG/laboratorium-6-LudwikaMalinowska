
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
        >>> h.distance("G", "")
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


if __name__ == "__main__":
    import doctest
    doctest.testmod()
