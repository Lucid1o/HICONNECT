from flask import Flask, render_template, request, redirect, session, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
import os

# Load env variables
load_dotenv()

app = Flask(__name__, template_folder='Templates')
app.secret_key = os.getenv("SECRET_KEY")

# Load credentials
USERNAME = os.getenv("USERNAME")
PASSWORD_HASH = generate_password_hash(os.getenv("PASSWORD"))

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Adjust this if using WSL
DOWNLOADS_PATH = os.getenv("DOWNLOADS_PATH", "C:\\Users\\MIHIR\\Downloads")


#  Login page
@app.route('/')
def home():
    return render_template('login.html')


#  Login logic
@app.route('/login', methods=['POST'])
def login():
    user = request.form.get('username')
    pwd = request.form.get('password')

    if user == USERNAME and check_password_hash(PASSWORD_HASH, pwd):
        session['user'] = user
        return redirect('/dashboard')
    return "❌ Invalid credentials"


#  Dashboard
@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect('/')
    return render_template('index.html', user=session['user'])


#  Upload
@app.route('/upload', methods=['POST'])
def upload():
    if 'user' not in session:
        return "Unauthorized"

    file = request.files.get('file')

    if file:
        file.save(os.path.join(UPLOAD_FOLDER, file.filename))
        return redirect('/dashboard')

    return "Upload failed"


#  Uploaded files
@app.route('/files')
def files():
    if 'user' not in session:
        return "Unauthorized"

    files = os.listdir(UPLOAD_FOLDER)
    return "<br>".join([f"<a href='/download/{f}'>{f}</a>" for f in files])


#  Download uploaded file
@app.route('/download/<filename>')
def download(filename):
    if 'user' not in session:
        return "Unauthorized"

    return send_from_directory(UPLOAD_FOLDER, filename)


#  Downloads folder
@app.route('/downloads')
def downloads():
    if 'user' not in session:
        return "Unauthorized"

    files = os.listdir(DOWNLOADS_PATH)
    return "<br>".join([f"<a href='/download_real/{f}'>{f}</a>" for f in files])


@app.route('/download_real/<filename>')
def download_real(filename):
    if 'user' not in session:
        return "Unauthorized"

    return send_from_directory(DOWNLOADS_PATH, filename)


#  Logout
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
