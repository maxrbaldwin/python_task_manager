import pandas as pd
from typs.index import DB_CSV_Paths

def create_new_task(task, user_id):
  new_task = {
    'id': task.id,
    'task_title': task.task_title,
    'task_description': task.task_description,
    'user_id': user_id,
    'is_finished': task.task_status
  }
  task_data = pd.DataFrame([new_task])
  task_data.to_csv(DB_CSV_Paths.tasks.value, mode='a', header=True, index=False)
  return task

def update_task(task):
  task_data = pd.read_csv(DB_CSV_Paths.tasks.value)
  condition = task_data['id'] == task.id
  
  task_data.loc[condition, 'task_title'] = task.task_title
  task_data.loc[condition, 'task_description'] = task.task_description
  task_data.loc[condition, 'is_finished'] = task.task_status

  task_data.to_csv(DB_CSV_Paths.tasks.value, index=False)

  return task


def get_task_by_user_id(user_id):
  try:
    task_data = pd.read_csv(DB_CSV_Paths.tasks.value)
    condition = task_data['user_id'] == str(user_id)
    user_tasks = task_data[condition]
    if not user_tasks.empty:
      return user_tasks.to_dict(orient="records")
    else:
      return []
  # csv was empty
  except pd.errors.EmptyDataError:
    return []
  # not found in csv
  except KeyError as key_error:
    print(key_error)
    return []

def get_task_by_id(task_id: str):
  try:
    task_data = pd.read_csv(DB_CSV_Paths.tasks.value)

    condition = task_data['id'] == task_id
    user_tasks = task_data[condition]
    if user_tasks.empty:
      return []
    else:
      return user_tasks.to_dict(orient="records")
   # csv was empty
  except pd.errors.EmptyDataError:
    return []
  # not found in csv
  except KeyError as key_error:
    print(key_error)
    return []