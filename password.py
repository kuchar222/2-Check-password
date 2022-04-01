"""moduł hasła
"""

from hashlib import sha1
import requests

class Password:
    """klasa zawiera hasło i jego hash oraz sprawdza poprawność i czy wyciekło
    """
    def __init__(self, password=str) -> None:
        self.password = password
        self.hash = self.create_hash()
        #  sprawdzanie poprawności hasła
        if self.check_password_lenght(): 
            if self.check_password_strongness():
               self.correct = self.check_pawn()
            else:
                self.correct = False
        else:
            self.correct = False

    def create_hash(self):
        """tworzy hash dla hasła według metody SHA-1

        Args:
            password (string): hasło do hashowania

        Returns:
            string: hash hasła
        """
        return sha1(self.password.encode('utf-8')).hexdigest().upper()

    def __str__(self) -> str:
        return self.password

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
        return True

    def check_pawn(self):
        """sprawdza czy hasło wyciekło

        Returns:
            bool: True jeżeli hasło nie wyciekło
        """
        url = 'https://api.pwnedpasswords.com/range/' + f'{self.hash[:5]}'
        ans = requests.get(url).text.split()
        req = [hash.partition(':')[0] for hash in ans]
        if self.hash[5:] not in req:
            return True
        else:
            return False
