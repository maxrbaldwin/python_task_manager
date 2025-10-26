from pydantic import BaseModel

class UserAuth(BaseModel):
  username: str
  password: str

def server_auth():
  print('Handle server')
  return "cheese"