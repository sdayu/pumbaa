'''
Created on Oct 13, 2013

@author: boatkrap
'''

import hashlib

class SecretManager:
    def __init__(self, secret):
        self.password_secret = secret

    def get_password_secret(self):
        return self.password_secret

        
    def get_hash_password(self, password):
        salt = hashlib.sha512(self.password_secret.encode('utf-8'))
        hash_pass = hashlib.sha512(password.encode('utf-8'))
        
        hash_pass.update((self.password_secret + salt.hexdigest()).encode('utf-8'))
        return hash_pass.hexdigest()
    