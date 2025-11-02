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
        ui.link(text="Create Task", target="/create_task")
        
        header('Your Tasks')
      
      with ui.column().classes('flex flex-column min-w-sm'):
        user_id = user['id']
        user_tasks = get_task_by_user_id(user_id)
        user_tasks_copy = user_tasks

        if user_tasks.empty:
          return
        
        for task in user_tasks.to_dict(orient="records"):
          title = task['task_title']
          id = task['id']
          ui.link(text=title, target=f"/task/{id}")
        
        finished_condition = user_tasks_copy['is_finished'] == 'Finished'
        finished_tasks = user_tasks_copy[finished_condition]

        if finished_tasks.empty:
          return
        
        header('Finished tasks')
        for finished_task in finished_tasks.to_dict(orient="records"):
          title = finished_task['task_title']
          id = finished_task['id']
          ui.link(text=title, target=f"/task/{id}")
    