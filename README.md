# HICONNECT 🚀

A local file-sharing web application built using Flask to enable seamless file transfer between devices on the same network.

---

## 🧠 Motivation

Most file transfer methods either rely on cloud services or require complex setup.  
This project was built to understand how file sharing actually works at a lower level — using HTTP, local networking, and backend logic.

The goal was simple:

> Build a lightweight, local-first file transfer system that works across devices without external dependencies.

---

## ⚙️ Features

- 🔐 Authentication using environment variables
- 📥 Upload files (mobile → laptop)
- 📤 Download files (laptop → mobile)
- 📂 Access system Downloads folder
- 🌐 Works over local network (LAN)
- 🎨 Clean, modern UI

---

## 🧩 Tech Stack

- **Backend:** Python (Flask)
- **Frontend:** HTML, CSS
- **Environment Management:** python-dotenv
- **Security Basics:** Password hashing (Werkzeug)
- **Networking:** Local IP-based access

---

## 🏗️ How It Works

1. Flask runs a local web server
2. Devices on the same network connect via IP
3. File uploads use HTTP POST requests
4. File downloads use HTTP GET requests
5. Sessions handle authentication

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone <your-repo-link>
cd HICONNECT
