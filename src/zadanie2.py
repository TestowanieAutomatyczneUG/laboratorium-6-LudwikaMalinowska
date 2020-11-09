class Validate:

    # password = "P455w0rD"

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
        """

        if len(passw) < 8:
            return False

        return True

