import json
from nicegui import ui
from nicegui.elements.input import Input
from page_components.center_container import center_container
from page_components.page_template import page_template

def home_page():
  page_template()
  with center_container():
    with ui.column().classes('flex flex-column'):
      ui.label("Login or Create Account").classes('text-lg')
      username_input = ui.input(label="Username")
      password_input = ui.input(label="Password")
      ui.button(text="Login", on_click=lambda: handle_client_auth(username_input, password_input))

def handle_client_auth(username_input: Input, password_input: Input):
  path = "auth"
  data = {
    'username': username_input.value,
    'password': password_input.value
  }
  js_path = json.dumps(path)
  js_data = json.dumps(data)
  ui.run_javascript(f"auth_user({js_path}, {js_data})")