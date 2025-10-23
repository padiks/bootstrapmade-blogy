# **Flask Tutorial Library – Modular Version**

```
flaskweb/
│
├─ common/              
│   ├─ __init__.py          # Creates the Flask app instance, sets template/static paths, imports routes
│   └─ routes/              # Folder for all route modules
│       ├─ __init__.py      # Imports all topic routes
│       ├─ home.py          # Home + About routes
│       └─ operators.py     # Operators tutorial (percentage difference calculator)
│
├─ apps/                  
│   └─ templates/           # App-specific templates
│       ├─ home.html        # Root page template
│       └─ tutorial/
│           └─ operators.html  # Tutorial #1 template
│
├─ templates/           
│   └─ base.html            # Shared layout template (Bootstrap, navbar, etc.)
│
├─ static/              
│   └─ css/
│       └─ style.css        # All custom CSS
│
└─ app.py                   # Main run script using Waitress
```

---

### **How it works**

1. `common/__init__.py`

   * Creates the Flask app
   * Sets up multiple template folders (`apps/templates` + `templates/`)
   * Imports all routes from `common/routes/__init__.py`

2. `common/routes/`

   * Each topic has its **own module** (e.g., `operators.py`)
   * `__init__.py` imports them all so Flask registers the routes automatically

3. Templates

   * `base.html` → shared layout (Bootstrap navbar, footer, etc.)
   * `home.html` → Table of Contents
   * `tutorial/operators.html` → Example tutorial page

4. `static/`

   * Custom CSS and assets

5. `app.py`

   * Entry point running Waitress on port 4040

---

This structure makes it **easy to scale**:

* Add new tutorials → just create a new route module + template
* No need to touch `common/__init__.py` or `app.py`

---

If you want, I can also **draw a “template route module” skeleton** you can copy for every new tutorial — it will include:

* GET/POST handling
* Optional Python calculation
* Result display in the template

This will make adding dozens of topics **trivial**.