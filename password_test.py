from password import Password

def test_create_hash():
    password1 = 'Walid'
    password2 = 'kdmfcspkd7820/'
    password3 = 'walid'
    password4 = 'Walid'
    test_password1 = Password(password1)
    test_password2 = Password(password2)
    test_password3 = Password(password3)
    test_password4 = Password(password4)
    assert test_password1.hash != test_password2.hash
    assert test_password1.hash != test_password3.hash
    assert test_password1.hash == test_password4.hash
    assert test_password1.hash != test_password1.password

