import time
from nicegui import ui

version = int(time.time())

def page_template():
  ui.add_head_html(f'<script src="/static/functions.js?v={version}"></script>')