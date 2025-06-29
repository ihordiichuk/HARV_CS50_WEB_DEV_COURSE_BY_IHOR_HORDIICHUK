# CS50 Web Programming Project 3: Mail

This project is a single-page web application that emulates a basic email client. It is built using Django (Python) on the backend and JavaScript on the frontend. The application supports user authentication, composing emails, viewing inbox/sent/archived mailboxes, reading emails, archiving/unarchiving messages, and replying to emails.

---

## Features

- User registration and login with secure session management
- Compose new email with recipient(s), subject, and body
- View mailboxes: Inbox, Sent, Archived
- View individual email detail
- Archive and unarchive messages (toggle)
- Reply to received messages with pre-filled metadata
- Mark emails as read upon opening

---

## Technology Stack

- **Backend:** Python 3, Django
- **Frontend:** HTML5, CSS (Bootstrap), Vanilla JavaScript
- **Database:** SQLite (default Django ORM)
- **API:** RESTful endpoints provided by CS50 starter code

---

## Setup Instructions

Follow these steps in terminal or command line:

```bash
# 1. Clone the repository
git clone <your-repository-url>
cd mail

# 2. (Optional) Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate    # macOS/Linux
venv\Scripts\activate.bat   # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run migrations
python manage.py migrate

# 5. Start development server
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser.

---

## Testing

To test functionality, you can create multiple user accounts and exchange emails between them:

- Register two users (e.g. `user1@local.com`, `user2@local.com`)
- Log in as each user and test:
  - Sending and receiving emails
  - Archiving and unarchiving
  - Reply functionality
  - Automatic redirection to the appropriate mailbox
  - Read/unread visual indicators

---

## Files and Structure

mail/
├── static/mail/            # JavaScript and CSS
│   └── inbox.js            # Main frontend logic
├── templates/mail/         # Django templates
│   ├── layout.html
│   ├── inbox.html
│   ├── login.html
│   ├── register.html
├── views.py                # Django views (API routing logic)
├── models.py               # User, Email models
├── urls.py                 # URL configuration
project3/
├── settings.py             # Django settings
├── urls.py                 # Project-level routes
├── db.sqlite3              # SQLite database
└── manage.py               # Django CLI entry point

---

## CS50 Requirements Coverage

| Requirement                     | Status        |
|----------------------------------|---------------|
| Send Mail                       | ✔ Implemented |
| Mailboxes (Inbox, Sent, Archive)| ✔ Implemented |
| View Email                      | ✔ Implemented |
| Archive and Unarchive           | ✔ Implemented |
| Reply to Email                  | ✔ Implemented |
| JavaScript-Only Transitions     | ✔ Implemented |
| Local State Update (No Reloads) | ✔ Implemented |

---

## License

This project was completed as part of CS50’s Web Programming with Python and JavaScript. The base code and assignment description are provided by Harvard University.
This repository is for educational purposes only.
