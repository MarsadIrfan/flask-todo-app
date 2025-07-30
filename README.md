# ✅ Flask To-Do App with Login

Welcome to the **Flask To-Do App** — a beautifully simple task manager built with 💖 using Flask, HTML, CSS, and SQLite. With support for user sign-up and login, you'd expect everyone to get their own list... but surprise! 🎉 **Everyone sees the same To-Do list.** Yes, really. More on that below. 😅

---

## ✨ Features

- 🧾 **Add & Delete Tasks** — A sleek and minimal UI with buttons that just work
- 🔐 **User Authentication** — Sign up and log in with securely encrypted passwords using Werkzeug
- 🛠️ **Flask + SQLite** — Fast, lightweight backend with elegant frontend
- 🎨 **Clean & Neat UI** — Simple, effective, and easy on the eyes
- 🤝 **One List to Rule Them All** — All users share the same to-do list. Unintentionally intentional.

---

## 🧩 Tech Stack

| Tech         | Purpose                            |
|--------------|------------------------------------|
| Flask        | Web framework                      |
| SQLite       | Lightweight database               |
| Flask_SQLAlchemy | ORM for working with the DB |
| Werkzeug     | Secure password hashing            |
| HTML + CSS   | For the beautiful frontend         |

---

## 🚧 My Little "Oops" (a.k.a. Shared To-Do List) 😅

> Originally, the app was meant to be multi-user — but I *accidentally* made it so that **everyone logs into a shared list**.  
>   
> It became a weirdly fun feature — login as anyone, and you’ll still see the same to-dos. Great for roommates? A family dashboard? A public TODO leaderboard? Who knows!  
>   
> Feel free to fork and fix it... or embrace the chaos 😄

---

## 🔧 Setup & Installation

### 1. Clone the Repo

```bash
git clone https://github.com/MarsadIrfan/flask-todo-app.git
cd flask-todo-app
```
### 2. Installations

```bash
pip install flask flask-sqlalchemy werkzeug
```

### 3. Initialize_db
- Delete the todo.db in the instance/ folder as it contains some dummy credentials and data
- run:
  ```bash
  python init_db.py
  ```

### 4. Run Server 
enter this in the terminal:
```bash
flask run
```
### 5. Signup, login and use
- Signup using the signup button on the bottom of the login page
- Return back to the login page and login into you account
- Add or delete tasks here

---

### 🧪 Want to Improve It?
Things you could add (and maybe submit a pull request? 😉):
- Separate to-do lists per user 🧍‍♂️🧍‍♀️
- Due dates or priorities ⏰
- Toggle task completion ✅
- Dark mode 🌓

---

### 🛡 License
MIT License. Use it, learn from it, break it, fix it.

---

### 🙌 Final Words
Thanks for stopping by! I hope this project makes you smile, or at least inspires your next project.
Feel free to star ⭐ the repo, fork 🍴 it, or share some feedback!
Made with coffee ☕ and questionable design choices by Marsad Irfan

---



