import os
from jinja2 import Environment, FileSystemLoader

def load_template(filename):
    templates_path = os.path.join(os.path.dirname(__file__), '..', 'templates')
    env = Environment(loader=FileSystemLoader(templates_path))

    template = env.get_template(filename)
    return template