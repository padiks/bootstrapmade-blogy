# **Flask Tutorial Library – Modular Version**

### **Project structure**

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
│       ├─ about.html       # About page template
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

   * Entry point running Waitress on port 4050

---

This structure makes it **easy to scale**:

* Add new tutorials → just create a new route module + template
* No need to touch `common/__init__.py` or `app.py`

---

### **Setting up and running on Windows**

1. Install Python 3 if not already installed.
2. Create a virtual environment in the project folder:

```cmd
cd C:\path\to\flaskweb
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies:

```cmd
pip install --upgrade pip
pip install flask waitress
```

4. Run the app:

```cmd
python app.py
```

5. Access in browser:

* Home: `http://127.0.0.1:4050/`
* About: `http://127.0.0.1:4050/about`
* Operators tutorial: `http://127.0.0.1:4050/tutorial/operators`

---

### **Running Flask Tutorial Library on Debian**

---

#### **1️⃣ Install system dependencies**

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv -y
```

---

#### **2️⃣ Create a virtual environment**

```bash
cd /home/user/Public/web/flaskweb
python3 -m venv venv
source venv/bin/activate
```

> Your shell prompt should now show `(venv)`.

---

#### **3️⃣ Install Python dependencies**

```bash
pip install --upgrade pip
pip install flask waitress
```

> `waitress` is your production WSGI server.

---

#### **4️⃣ Configure your port**

Port 4050 is used to avoid conflicts:

```python
from waitress import serve
from common import app

if __name__ == "__main__":
    print("Serving on http://localhost:4050")
    serve(app, host="0.0.0.0", port=4050)
```

---

#### **5️⃣ Run the Flask app**

```bash
source venv/bin/activate
python app.py
```

Expected output:

```
Serving on http://localhost:4050
```

---

#### **6️⃣ Access the app in your browser**

* Home page: `http://127.0.0.1:4050/`
* About: `http://127.0.0.1:4050/about`
* Operators tutorial: `http://127.0.0.1:4050/tutorial/operators`

---

#### **7️⃣ Optional: Clean up before deployment**

* Remove `__pycache__` folders:

```bash
find . -type d -name "__pycache__" -exec rm -r {} +
```

* Add `.gitignore` if using Git:

```
__pycache__/
*.pyc
venv/
*.sqlite3
```

---

#### **8️⃣ Notes**

* Always activate your virtual environment when running the project.
* Use `CTRL+C` to stop the server.
* For production, you can run **Waitress in the background**:

```bash
nohup python app.py &
```

---

✅ This README now covers **both Windows and Debian setups**, making it easy for anyone to clone and run the project.

---

### License

This project is intended for learning purposes.
