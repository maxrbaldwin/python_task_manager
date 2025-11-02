from nicegui import ui, app
from typs.index import UserAuth, Task

#api routes
from api.server_auth import server_auth
from api.make_task import make_task

#pages
from pages.home_page import home_page
from pages.profile_page import profile_page
from pages.create_task_page import create_task_page
from pages.task_page import task_page

# static file directory
app.add_static_files('/static', 'static')

# api routes
@app.post('/auth')
def handle_server_auth(user_auth: UserAuth):
  return server_auth(user_auth)

@app.post('/handle_task')
def handle_task(task: Task):
  return make_task(task)

# ui pages
@ui.page('/')
def home():
  home_page()

@ui.page('/profile')
def profile():
  profile_page()

@ui.page('/create_task')
def create_task():
  create_task_page()

@ui.page('/task/{id}')
def task(id: str):
  task_page(id)
# bad
ui.run(storage_secret="538bae6e-a02d-4443-b35d-558afb77de23")