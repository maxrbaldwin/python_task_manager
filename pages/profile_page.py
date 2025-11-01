from nicegui import ui, app
from page_components.center_container import center_container
from fastapi.responses import RedirectResponse
from db.tasks import get_task_by_user_id

def profile_page():
  user = app.storage.user

  if user is None:
    return RedirectResponse('/')

  with ui.column().classes('flex flex-column'):
    with ui.column().classes('flex flex-column'):
      ui.link(text="Create Task", target="/create_task")
    
    with ui.column().classes('flex flex-column'):
      user_id = user['id']
      user_tasks = get_task_by_user_id(user_id)
      ui.label('your tasks')

      for task in user_tasks:
        title = task['task_title']
        id = task['id']
        ui.link(text=title, target=f"/task/{id}")
    