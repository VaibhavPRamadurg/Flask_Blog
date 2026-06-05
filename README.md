# Flask Blog

A modern, full-featured blogging platform built with Flask, featuring user authentication, blog post management, and a responsive web interface.

## 🌐 Live Website

**Visit the live website:** [https://flask-blog-17rn.onrender.com](https://flask-blog-17rn.onrender.com)

## ✨ Features

- **User Authentication**
  - User registration and login with secure password hashing (Bcrypt)
  - Password reset via email
  - User account management and profiles
  - Session management with Flask-Login

- **Blog Functionality**
  - Create, read, and delete blog posts
  - View user-specific posts
  - Responsive post display and layout

- **User Profiles**
  - User profile pages with account information
  - Profile picture upload support
  - Personal blog post history

- **Security Features**
  - CSRF protection with Flask-WTF
  - Secure password storage with Bcrypt
  - Email verification for password resets

- **Error Handling**
  - Custom error pages (403, 404, 500)
  - User-friendly error messages

- **Responsive Design**
  - Mobile-friendly interface
  - Clean and intuitive UI

## 🛠️ Technology Stack

- **Backend:** Flask 3.1.3
- **Database:** SQLAlchemy 2.0.49 with PostgreSQL
- **Authentication:** Flask-Login, Flask-Bcrypt
- **Forms:** Flask-WTF, WTForms
- **Email:** Flask-Mail with Resend
- **Frontend:** HTML, CSS, JavaScript
- **Image Processing:** Pillow
- **Server:** Gunicorn
- **Deployment:** Render

## 📋 Requirements

- Python 3.8+
- PostgreSQL

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd Flask_NewBlog
```

### 2. Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the root directory and configure:

```
DATABASE_URL=postgresql://username:password@localhost/flask_blog
SECRET_KEY=your-secret-key-here
MAIL_SERVER=smtp.example.com
MAIL_PORT=587
MAIL_USERNAME=your-email@example.com
MAIL_PASSWORD=your-email-password
```

### 5. Initialize the Database

```bash
python
>>> from flaskblog import create_app, db
>>> app = create_app()
>>> with app.app_context():
...     db.create_all()
>>> exit()
```

### 6. Run the Application

```bash
python run.py
```

The application will be available at `http://localhost:5003`

## 📁 Project Structure

```
Flask_NewBlog/
├── flaskblog/
│   ├── __init__.py              # App factory
│   ├── config.py                # Configuration settings
│   ├── models.py                # Database models
│   ├── errors/
│   │   ├── __init__.py
│   │   └── handlers.py          # Error handlers
│   ├── main/
│   │   ├── __init__.py
│   │   └── routes.py            # Main routes (home, about)
│   ├── posts/
│   │   ├── __init__.py
│   │   ├── forms.py             # Post forms
│   │   └── routes.py            # Post routes
│   ├── users/
│   │   ├── __init__.py
│   │   ├── forms.py             # User forms (register, login, etc.)
│   │   ├── routes.py            # User routes
│   │   └── utils.py             # Utility functions
│   ├── static/
│   │   ├── main.css             # Main stylesheet
│   │   ├── main.js              # JavaScript functionality
│   │   └── profile/             # Profile images directory
│   └── templates/
│       ├── layout.html          # Base template
│       ├── home.html            # Home page
│       ├── about.html           # About page
│       ├── login.html           # Login page
│       ├── register.html        # Registration page
│       ├── account.html         # User account page
│       ├── create_post.html     # Create post page
│       ├── post.html            # Single post view
│       ├── user_posts.html      # User posts list
│       ├── reset_request.html   # Password reset request
│       ├── reset_token.html     # Password reset token
│       └── errors/              # Error pages (403, 404, 500)
├── run.py                       # Application entry point
├── Procfile                     # Heroku/Render configuration
├── requirements.txt             # Python dependencies
└── README.md                    # This file
```

## 🔧 Usage

### Create a Blog Post

1. Log in to your account
2. Navigate to the "Create Post" section
3. Fill in the post title and content
4. Click "Post" to publish

### Reset Password

1. Click "Forgot Password" on the login page
2. Enter your email address
3. Check your email for the reset link
4. Follow the link and create a new password

## 🌍 Deployment

This project is deployed on [Render](https://render.com). To deploy your own version:

1. Push your code to a GitHub repository
2. Connect your repository to Render
3. Set up environment variables in Render dashboard
4. Deploy!

## 📞 Contact & Support

For issues, questions, or suggestions, please feel free to open an issue in the repository.

## 📄 License

This project is open source and available under the MIT License.

---

**Happy Blogging! 📝**
