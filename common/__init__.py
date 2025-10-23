import os
from flask import Flask
from jinja2 import ChoiceLoader, FileSystemLoader

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Paths to template folders
APPS_TEMPLATES = os.path.join(BASE_DIR, "apps", "templates")
SHARED_TEMPLATES = os.path.join(BASE_DIR, "templates")
STATIC_DIR = os.path.join(BASE_DIR, "static")

# Create Flask app with multiple template folders
app = Flask(
    __name__,
    template_folder=APPS_TEMPLATES,  # main template folder
    static_folder=STATIC_DIR
)

# Ensure Flask can find templates in both apps/templates and templates/
app.jinja_loader = ChoiceLoader([
    FileSystemLoader(APPS_TEMPLATES),
    FileSystemLoader(SHARED_TEMPLATES)
])

# Enable debug mode
app.debug = True

# Import routes
from common import routes


