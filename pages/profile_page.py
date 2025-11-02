from nicegui import ui, app
from page_components.center_container import center_container
from page_components.parent_styled_container import parent_styled_container
from page_components.header import header
from fastapi.responses import RedirectResponse
from db.tasks import get_task_by_user_id

def profile_page():
  user = app.storage.user

  if user is None:
    return RedirectResponse('/')
  with center_container():
    with parent_styled_container():
      with ui.column().classes('flex flex-column'):
        header('YourTasks')
        ui.link(text="Create Task", target="/create_task")
      
      with ui.column().classes('flex flex-column'):
        user_id = user['id']
        user_tasks = get_task_by_user_id(user_id)
        for task in user_tasks:
          title = task['task_title']
          id = task['id']
          ui.link(text=title, target=f"/task/{id}")
    