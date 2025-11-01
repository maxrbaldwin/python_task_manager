from uuid import UUID
from pydantic import BaseModel
from typing import NewType
from enum import Enum

ID = NewType('ID', UUID)
Username = NewType('Username', str)
Password = NewType('Password', str)

class UserAuth(BaseModel):
  username: Username
  password: Password

class User(UserAuth):
  id: ID

class DB_CSV_Paths(Enum):
  users = './db/users.csv'
  tasks = './db/tasks.csv'

class CreateTask(BaseModel):
  id: str
  task_title: str
  task_description: str