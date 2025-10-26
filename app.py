from nicegui import ui, app
from nicegui.elements.input import Input
from pydantic import BaseModel
import json
import time

version = int(time.time())  # or manually set a version number

class UserAuth(BaseModel):
  username: str
  password: str

app.add_static_files('/static', 'static')

@app.post('/auth')
def handle_server_auth(userAuth: UserAuth):
  print('Handle server')
  return "cheese"


def handle_client_auth(username_input: Input, password_input: Input):
  print("handle client")
  path = "auth"
  data = {
    'username': username_input.value,
    'password': password_input.value
  }
  js_path = json.dumps(path)
  js_data = json.dumps(data)
  ui.run_javascript(f"post_json({js_path}, {js_data})")

def center_container():
  return ui.column().classes('flex flex-row justify-center w-full')

def page_template():
  ui.add_head_html(f'<script src="/static/functions.js?v={version}"></script>')

@ui.page('/')
def home():
  page_template()
  with center_container():
    with ui.column().classes('flex flex-column'):
      ui.label("Login or Create Account").classes('text-lg')
      username_input = ui.input(label="Username")
      password_input = ui.input(label="Password")
      ui.button(text="Login", on_click=lambda: handle_client_auth(username_input, password_input))

ui.run()