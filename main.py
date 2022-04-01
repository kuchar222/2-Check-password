from database import Database

data = Database('passwords.txt')
data.save_correct_passwords()