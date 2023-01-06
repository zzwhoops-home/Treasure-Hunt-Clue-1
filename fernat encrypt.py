import os
import base64
from colorama import Fore, Style, init
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

init()

def fernet_gen(password):
  p_word = password
  
  kdf = PBKDF2HMAC(
      algorithm=hashes.SHA256(),
      length=32,
      salt=b"m\xea\x8c\x10T\xd1\xa8\xb7%8\xf3\xe4\x89\xccP;",
      iterations=1000,
  )
  
  or_key = kdf.derive(p_word.encode('utf-8'))
  key = base64.urlsafe_b64encode(or_key)
  return key

keys = open("key.txt", "w")

def encrypt(key):
  f = Fernet(key)
  token = f.encrypt(b"")
  keys.writelines('the key is ' + str(key) + ' \nThe cipher text is ' + str(token))

def decrypt(key):
  f = Fernet(key)  
  token = b'gAAAAABiG5QCElEFJMl9grK_zokpDCZIvcmTddTkwMj3h1AypdwdJWsjAmNIb4e22sWaVaCRAhVjrr6uGapxEpnSGH1yFtuJvQ=='
  print(f.decrypt(token))

#Ih8tEG01d
#Pr0StH3t1c

encrypt(fernet_gen("P3aR1YwH1tEs"))

keys.close()