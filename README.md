# Flask Tutorial Library

```
flaskweb/
│
├─ common/              
│   ├─ __init__.py      # Creates the Flask app instance
│   └─ routes.py        # Defines all app routes
│
├─ apps/                 
│   └─ templates/       # App-specific templates
│       ├─ home.html    # Root page template
│       └─ tutorial/
│           └─ operators.html  # Tutorial #1: Percentage difference calculator
│
├─ templates/           
│   └─ base.html        # Shared layout template (Bootstrap, navbar, etc.)
│
├─ static/              
│   └─ css/
│       └─ style.css    # All custom CSS
│
└─ app.py               # Main run script using Waitress
```
