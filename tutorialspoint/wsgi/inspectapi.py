from falcon import inspect
from app import app

app_info = inspect.inspect_app(app)
print(app_info)