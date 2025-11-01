import pandas as pd
from typs.index import DB_CSV_Paths

def create_new_task(task, user_id):
  new_task = {
    'id': task.id,
    'task_title': task.task_title,
    'task_description': task.task_description,
    'user_id': user_id,
    'is_finished ': False
  }
  task_data = pd.DataFrame([new_task])
  task_data.to_csv(DB_CSV_Paths.tasks.value, mode='a', header=True, index=True)
  return task

def get_task_by_user_id(user_id):
  task_data = pd.read_csv(DB_CSV_Paths.tasks.value)

  condition = task_data['user_id'] == user_id
  user_tasks = task_data[condition]

  return user_tasks.to_dict(orient="records")

def get_task_by_id(task_id: str):
  task_data = pd.read_csv(DB_CSV_Paths.tasks.value)

  condition = task_data['id'] == task_id
  user_tasks = task_data[condition]

  return user_tasks.to_dict(orient="records")