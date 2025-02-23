# 📧 Email Approval System

## 🌟 Introduction
The **Email Approval System** is a FastAPI-based web application that enables clients to send approval request emails. The recipient can either **approve** or **decline** the request by clicking on the email link. The system stores user details in a **MongoDB database**, encrypts sensitive data, and provides an email verification mechanism.

---

## ⚡ Features
- 📩 Send email approval requests.
- 🔗 Generate encrypted approval/decline links.
- 🔑 Secure data encryption.
- 🛠 Uses **FastAPI**, **MongoDB**, and **FastAPI-Mail**.
- 📁 Organized folder structure for scalability.

---

## 🛠 Prerequisites
Before setting up the project, ensure you have the following installed:

- **Python 3.8+** 👉 [Download Python](https://www.python.org/downloads/)
- **MongoDB** (Local or Cloud) 👉 [MongoDB Atlas](https://www.mongodb.com/)
- **Virtual Environment** (Recommended)
- **Gmail SMTP** for sending emails

---

## 🚀 Project Setup
Follow these steps to set up and run the project.

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/chanu1430/ATE.git
cd ATE
```

### 2️⃣ Create and Activate a Virtual Environment
```sh
For Windows:
-------------
    python -m venv virtualEnv
    virtualEnv\Scripts\activate

For macOS/Linux:
-----------------
    python3 -m venv virtualEnv
    source virtualEnv/bin/activate
```

### 3️⃣ Step 3: Install Project Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Step 4: Set Up Environment Variables
Create a .env file in the project root and add your SMTP email credentials and database connection details:
```sh
touch .env  # For Linux/macOS
echo "" > .env  # For Windows   
#Then, open the .env file and add the following configurations:
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
MAIL_FROM=your-email@gmail.com
MAIL_PORT=587
MAIL_SERVER=smtp.gmail.com
MAIL_STARTTLS=True
MAIL_SSL_TLS=False
MONGO_URI=mongodb+srv://your-db-connection
```

### 5️⃣ Step 5:Run the FastAPI Server
Use Uvicorn to start the FastAPI server:
```sh
uvicorn main:app --reload
```

📂 Project Structure
EmailApproval/
│── crudOperations/         # CRUD operations for MongoDB
│   ├── findOne.py
│   ├── insertOne.py
│   ├── updateOne.py
│
│── dataGeneration/         # Helper functions for data generation
│   ├── generate_unique_id.py
│
│── models/                 # Database models
│   ├── userModel.py
│
│── virtualEnv/             # Virtual environment (ignored in Git)
│
│── .env                    # Environment variables
│── .gitignore              # Ignore sensitive files
│── checkUserApproval.py    # Logic for approval system
│── dataEncryption.py       # Encryption utilities
│── emailTemplate.py        # Email HTML templates
│── main.py                 # Main FastAPI application
│── mongoDB.py              # Database connection setup
│── README.md               # Project documentation
│── requirements.txt        # Python dependencies
