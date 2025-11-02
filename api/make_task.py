from nicegui import app
from db.tasks import create_new_task, get_task_by_id, update_task

def make_task(task):
  user = app.storage.user
  user_id = user['id']
  task_id = task.id
  existing_task = get_task_by_id(task_id)
  if existing_task.empty:
    new_task = create_new_task(task, user_id)
    return new_task
  else:
    updated_task = update_task(task)
    return updated_task
