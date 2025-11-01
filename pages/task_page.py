from page_components.task_page_template import task_page_template
from db.tasks import get_task_by_id

def task_page(id: str):
  task = get_task_by_id(id)[0]
  label = 'Edit Task'
  task_page_template(task, label)
  