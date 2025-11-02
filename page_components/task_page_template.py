import json
from uuid import uuid4
from nicegui import ui
from page_components.page_template import page_template
from page_components.center_container import center_container
from page_components.parent_styled_container import parent_styled_container
from page_components.header import header

def task_page_template(task: dict, label: str):
  page_template()
  
  id = task.get('id', str(uuid4()))
  title_placeholder = task.get('task_title')
  description_placeholder = task.get('task_description')
  status_placeholder = task.get('is_finished') or "Not Finished"
  with center_container():
    with parent_styled_container():
      with ui.column().classes('flex flex-column'):
        header(label)
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
  