"""klasa zbioru haseł
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
        self.correct_database = self.create_correct_database()
        self.number_passwords = len(self.passwords)
        self.number_correct_passwords = len(self.correct_database)

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

    def create_correct_database(self):
        """tworzy bazę właściwych haseł

        Returns:
            list: lista obiektów klasy Password tylko właściwych haseł
        """
        correct_database =[]
        for password in self.database:
            if password.correct is True:
                correct_database.append(password)
        return correct_database

    def report(self):
        """wyświetla w terminalu informację o liczbie sprawdzonych haseł
        """
        print()
        print('-'*22)
        print(f'Sprawdzone hasła: {self.number_passwords}')
        print(f'Bezpieczne hasła: {self.number_correct_passwords}')
        print('-'*22)

    def save_correct_passwords(self):
        """zapisuje do nowego pliku tylko właściwe hasła
        """
        correct_file = 'correct_passwords.txt'
        print()
        if self.number_correct_passwords:
            try:
                with open(correct_file, 'w', encoding='utf-8') as file:
                    for password in self.correct_database:
                        file.write(str(password)+'\n')
                print(f'Bezpieczne hasła zapisano do pliku: {correct_file}')
            except:
                print('!!! Nie udało się zapisać haseł do pliku !!!')
        else:
            print('Brak haseł do zapisania')
        print()
