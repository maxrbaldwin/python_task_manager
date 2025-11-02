import json
from nicegui import ui
from nicegui.elements.input import Input
from page_components.center_container import center_container
from page_components.parent_styled_container import parent_styled_container
from page_components.page_template import page_template
from page_components.header import header

def home_page():
  page_template()
  with center_container():
    with parent_styled_container():
      header("Login or Create Account")
      username_input = ui.input(label="Username")
      password_input = ui.input(label="Password", password=True)
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