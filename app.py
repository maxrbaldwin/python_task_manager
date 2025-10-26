from nicegui import ui, app
from pages.home_page import home_page
from api.server_auth import server_auth, UserAuth

# static file directory
app.add_static_files('/static', 'static')

# api routes
@app.post('/auth')
def handle_server_auth(userAuth: UserAuth):
  server_auth()

# ui pages
@ui.page('/')
def home():
  home_page()

ui.run()