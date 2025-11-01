from nicegui import ui
from db.tasks import get_task_by_id

def task_page(id: str):
  task = get_task_by_id(id)[0]
  ui.label(task['id'])
  ui.label(task['task_title'])
  ui.label(task['task_description'])