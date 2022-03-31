"""moduł sprawdzania haseł
"""

class ValidatePasswords:
    """klasa sprawdzająca poprawność haseł i czy wyciekło
    """
    def __init__(self, password) -> None:
        self.password = password.password
        self.hash = str(password)

    def check_password_lenght(self):
        """sprawdza długość hasła

        Returns:
            bool: True jeżeli hasło dłuższe równe 8 znaków
        """
        if len(self.password) > 7:
            return True
        else:
            return False

    def check_password_strongness(self):
        # TODO sprawdzić za pomocą Regex siłe hasła
        # czy zawiera wielkie i małe litery, cyfry i znaki specjalne
        # użyć check_password_lenght do sprawdzenia długości
        pass


    def check_pawn(self):
        pass
