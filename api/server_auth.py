from uuid import uuid4
from nicegui import app
from db.index import get_user_by_username, insert_user, make_user
from typs.index import UserAuth

def server_auth(user_auth: UserAuth):
  try:
    user = get_user_by_username(user_auth.username)
    if user is None:
      id = uuid4()
      user = make_user(id, user_auth)
      user = insert_user(id, user)
      app.storage.user['id'] = user.id
      return user
    
    app.storage.user['id'] = user['id']

    return user
  except:
    return False