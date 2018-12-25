import hashlib, uuid


def get_salt():
    salt = uuid.uuid4().hex
    return salt


def hash_string(salt, string):
    salt = salt.encode()
    string = string.encode()
    hashed_string = hashlib.md5(string + salt).hexdigest()
    return hashed_string


if __name__ == '__main__':
    salt = get_salt()
    password = hash_string(salt, 'admin123')
    print("salt: %s \nhash: %s" % (salt, password))