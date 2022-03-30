"""zbiór haseł
"""
from password import Password

class Database:
    """klasa zbioru haseł
    """
    def __init__(self, path=str) -> None:
        """tworzy obiekt klasy zbioru haseł na podstawie pliku z hasłami

        Args:
            path (str, optional): ścieżka do pliku z hasłami. Defaults to str.
        """
        self.path = path
        self.passwords = self.take_passwords_from_file(self.path)
        self.database = self.create_database(self.passwords)

    @staticmethod
    def take_passwords_from_file(path):
        """pobiera z pliku hasła

        Args:
            path (str): ścieżka do pliku z hasłami

        Returns:
            list: lista haseł
        """
        passwords = []
        with open(path, encoding='utf-8') as file:
            for password in file:
                passwords.append(password.strip())
        return passwords

    @staticmethod
    def create_database(passwords):
        """tworzy bazę składającą się z haseł klasy Password

        Args:
            passwords (list): lista z hasłami z pliku

        Returns:
            list: objekty klasy Password
        """
        database = []
        for password in passwords:
            database.append(Password(password))
        return database
