"""klasa hasła, która sprawdza jego poprawność
"""

from hashlib import sha1
import re
import requests


class Password:
    """klasa zawiera hasło i jego hash oraz sprawdza poprawność i czy wyciekło
    """
    def __init__(self, password=str) -> None:
        self.password = password
        self.hash = self.create_hash()
        self.correct = self.validate_password()

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
        return bool(len(self.password) > 7)

    def check_password_strongness(self):
        """sprawdza siłę hasła, czyli czy zawiera wielkie i małe litery
        cyfry i znaki specjalne

        Returns:
            bool: True jeżeli hasło jest silne
        """
        try:
            re.compile(r'[0-9]').search(self.password).group()
            re.compile(r'[A-Z]').search(self.password).group()
            re.compile(r'[a-z]').search(self.password).group()
            re.compile(r'[^0-9a-zA-Z]').search(self.password).group()
            return True
        except AttributeError:
            return False

    def check_pawn(self):
        """sprawdza czy hasło wyciekło

        Returns:
            bool: True jeżeli hasło nie wyciekło
        """
        url = 'https://api.pwnedpasswords.com/range/' + f'{self.hash[:5]}'
        response = requests.get(url).text.split()
        return bool(self.hash[5:] not in [hash.partition(':')[0] for hash in response])

    def validate_password(self):
        """sprawdza czy hasło jest Bezpieczne
        (czy ma odpowiednią ilość znaków, liter i cyfr oraz czy nie wycziekło)

        Returns:
            bool: True jeżeli hasło jest Bezpieczne
        """
        if self.check_password_lenght():
            if self.check_password_strongness():
                return self.check_pawn()
        return False
