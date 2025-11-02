import bcrypt

def hash_password(password: str):
  password_as_bytes = password_string_to_bytes(password)
  salt = bcrypt.gensalt()
  hashed = bcrypt.hashpw(password_as_bytes, salt)
  return hashed

def verify_password(password: str, hashed_password: str):
  password_as_bytes = password_string_to_bytes(password)
  hash_as_bytes = password_string_to_bytes(hashed_password)
  return bcrypt.checkpw(password_as_bytes, hash_as_bytes)

def password_string_to_bytes(password: str):
  return password.encode('utf-8')