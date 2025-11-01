import json
from uuid import uuid4
from nicegui import ui
from page_components.page_template import page_template

def create_task_page():
  page_template()
  ui.label('Create task')
  with ui.column().classes('flex flex-column'):
    task_title = ui.input(label="Task Title")
    task_description = ui.textarea(label="Task Description")
    ui.button(text="Create Task", on_click=lambda: handle_create_task(task_title, task_description))

def handle_create_task(title, description):
  data = {
    'id': str(uuid4()),
    'task_title': title.value,
    'task_description': description.value,
  }
  js_data = json.dumps(data)
  ui.run_javascript(f"handle_create_task({js_data})")