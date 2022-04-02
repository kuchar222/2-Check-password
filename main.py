"""Główny plik skryptu
"""
from database import Database

PATH = r'passwords.txt'
data = Database(PATH)
data.report()
data.save_correct_passwords()
