from nicegui import ui

def header(title: str):
  return ui.label(title).classes('text-lg')