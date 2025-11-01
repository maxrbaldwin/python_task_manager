import json
from uuid import uuid4
from nicegui import ui
from page_components.page_template import page_template

def task_page_template(task: dict, label: str):
  page_template()
  ui.label(label)

  id = task.get('id', str(uuid4()))
  title_placeholder = task.get('task_title')
  description_placeholder = task.get('task_description')
  status_placeholder = 'Finished' if task.get('is_finished') else "Not Finished"
  with ui.column().classes('flex flex-column'):
    task_title = ui.input(label="Task Title", value=title_placeholder)
    task_description = ui.textarea(label="Task Description", value=description_placeholder)
    task_status = ui.radio(['Finished', 'Not Finished'], value=status_placeholder)
    ui.button(text=label, on_click=lambda: handle_task(id, task_title, task_description, task_status.value))

def handle_task(id, title, description, status):
  data = {
    'id': id,
    'task_title': title.value,
    'task_description': description.value,
    'task_status': status
  }
  js_data = json.dumps(data)
  ui.run_javascript(f"handle_task({js_data})")
  