import pandas as pd
from typs.index import ID, User, DB_CSV_Paths, UserAuth
from util.passwords import hash_password

def get_user_by_id(user_id: ID):
  df = pd.read_csv(DB_CSV_Paths.users.value)
  result = df[df['id']] == user_id
  return result

def get_user_by_username(username: str):
  try:
    df = pd.read_csv(DB_CSV_Paths.users.value)

    result = df[df['username'] == username]

    if not result.empty:
      return result.iloc[0].to_dict()
    else:
      return None
  # csv was empty
  except pd.errors.EmptyDataError:
    print('empty')
    return None
  # not found in csv
  except KeyError as key_error:
    print(key_error)
    return None

def upsert_user(user_id: ID, user_data: User):
  user = get_user_by_id(user_id)

  if (user):
    update_user(user_id, user_data)
  else:
    update_user(user_id, user_data)

def insert_user(user_id: ID, user_data: User):
  df = pd.DataFrame([user_data.model_dump()])
  to_csv(df, DB_CSV_Paths.users.value)
  return user_data

def update_user(user_id: ID, user_data: User):
  return user_data

def make_user(user_id: ID, user_auth: UserAuth):
  hashed_password = hash_password(user_auth.password)
  user = User(id=user_id, username=user_auth.username, password=hashed_password)
  return user

def to_csv(df, csv_path: DB_CSV_Paths):
  df.to_csv(csv_path, mode='a', header=True, index=True)