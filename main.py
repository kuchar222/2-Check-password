"""Główny plik skryptu
"""
from database import Database

path = 'passwords.txt'
data = Database(path)
data.report()
data.save_correct_passwords()
