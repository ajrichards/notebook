"""
sudo apt-get install bcrypt
pip install py-bcrypt

"""

import bcrypt


def get_hashed_password(plain_text_password):
    """
    Hash a password for the first time
    Using bcrypt, the salt is saved into the hash itself)
    """
    
    return bcrypt.hashpw(plain_text_password, bcrypt.gensalt())

def check_password(plain_text_password, hashed_password):
    """
    Check hased password. Useing bcrypt, the salt is saved into the hash itself
    """
    return bcrypt.checkpw(plain_text_password, hashed_password)

## test it
enc_passwd = get_hashed_password('foo-bar')
print(enc_passwd)
print(check_password('foo-bar',enc_passwd))
print(check_password('foo-foo',enc_passwd))
