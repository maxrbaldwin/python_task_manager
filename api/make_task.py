from nicegui import app
from db.tasks import create_new_task

def make_task(task):
  user = app.storage.user
  user_id = user['id']
  new_task = create_new_task(task, user_id)
  return new_task
