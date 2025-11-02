from uuid import uuid4
from nicegui import app
from db.users import get_user_by_username, insert_user, make_user
from typs.index import UserAuth
from util.passwords import verify_password

def server_auth(user_auth: UserAuth):
  user = get_user_by_username(user_auth.username)
  if user is None:
    id = uuid4()
    user = make_user(id, user_auth)
    user = insert_user(id, user)
    app.storage.user['id'] = user.id
    return user
  else:
    check_password = verify_password(user_auth.password, user['password'])
    if check_password:
      app.storage.user['id'] = user['id']
      return user
    else:
      return False