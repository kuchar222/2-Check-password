"""moduł hasła
"""

from hashlib import sha1

class Password:
    """klasa zawiera hasło i jego hash
    """
    def __init__(self, password=str) -> None:
        self.password = password
        self.hash = self.create_hash(self.password)

    @staticmethod
    def create_hash(password):
        """tworzy hash dla hasła według metody SHA-1

        Args:
            password (string): hasło do hashowania

        Returns:
            string: hash hasła
        """
        return sha1(password.encode('utf-8')).hexdigest()

    def __str__(self) -> str:
        return self.hash[:5]
