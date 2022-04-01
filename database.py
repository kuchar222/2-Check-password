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
        self.passwords = self.take_passwords_from_file()
        self.database = self.create_database()

    def take_passwords_from_file(self):
        """pobiera hasła z pliku 

        Args:
            path (str): ścieżka do pliku z hasłami

        Returns:
            list: lista haseł
        """
        passwords = []
        with open(self.path, encoding='utf-8') as file:
            for password in file:
                passwords.append(password.strip())
        return passwords

    def create_database(self):
        """tworzy bazę składającą się z haseł klasy Password

        Args:
            passwords (list): lista z hasłami z pliku

        Returns:
            list: lista objektów klasy Password
        """
        database = []
        for password in self.passwords:
            database.append(Password(password))
        return database

    def save_correct_passwords(self):
        """zapisuje do nowego pliku tylko właściwe hasła
        """
        with open('correct_passwords.txt', 'w') as file:
            for password in self.database:
                if password.correct == True:
                    file.write(str(password)+'\n')
