import hashlib
import string
import random
import base64


def make_random_salt(salt_len=10):
    salt = ""
    for i in range(salt_len):
        salt = salt + random.choice(string.ascii_letters)
    return salt


def encryp_psw(pw=None, salt=None):
    if salt is None:
        salt = make_random_salt()
    if pw is None:
        pw = make_random_salt(16)
        return hashlib.sha256(pw.encode('utf-8') + salt.encode('utf-8')).hexdigest(), salt, pw
    else:
        return hashlib.sha256(pw.encode('utf-8') + salt.encode('utf-8')).hexdigest(), salt


def base64_decode(input_str):
    return base64.b64decode(input_str)


def base64_encode(input_str):
    return base64.b64encode(input_str)
