A simple web-based note-taking application deployed on AWS EC2 using Flask and MariaDB, with a persistent backup strategy using an attached EBS volume.

📌 Project Overview

The Notes App is a lightweight web application that allows users to write, save, and view notes through a web interface. Each note is stored in a MariaDB database along with its creation timestamp.
The application is deployed on an AWS EC2 instance running Red Hat Enterprise Linux 10 and includes a database backup solution using an attached EBS volume.

✨ Key Features

Web-based interface to add notes

Automatic timestamp for each note

Notes displayed in reverse chronological order

Data persistence using MariaDB

Database backup stored on a mounted EBS volume

Deployed on AWS EC2 (Free Tier eligible)

🧩 Application Features

Input form for submitting notes

Notes are saved securely in a database

Each note shows date and time of creation

Latest notes appear at the top of the page

🏗️ Architecture Design

Client: Web browser (HTTP)

Web Server: Flask application running on EC2

Database: MariaDB installed on EC2

Storage:

Root volume for OS and application

Additional EBS volume mounted at /backup for database backups

🛠️ Technology Stack

Programming Language: Python 3.12

Web Framework: Flask

Database: MariaDB

Cloud Provider: AWS

Compute: EC2 (t2.micro / t3.micro)

Operating System: RHEL 10

Storage: AWS EBS

☁️ AWS Infrastructure Setup

EC2 Instance:

OS: Red Hat Enterprise Linux 10

Instance Type: t2.micro / t3.micro

Security Group:

Port 22 (SSH)

Port 80 (HTTP)

EBS Volume:

Additional volume attached to EC2

Mounted at /backup

Used for MariaDB backups

🗄️ Database Schema
CREATE DATABASE notesdb;

CREATE TABLE notes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone <repository-url>
cd notes-app

2️⃣ Create Virtual Environment
python3 -m venv venv
source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Configure MariaDB
CREATE DATABASE notesdb;
CREATE USER 'notesuser'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON notesdb.* TO 'notesuser'@'localhost';
FLUSH PRIVILEGES;


Update database credentials in app.py.

▶️ Run the Application
python3 app.py


Access the application in the browser:

http://<EC2_PUBLIC_IP>

💾 Backup Strategy

An additional EBS volume is attached to the EC2 instance and mounted at /backup.

Database Backup Command
mysqldump -u notesuser -p notesdb > /backup/notes_backup.sql


The backup file is stored on the mounted EBS volume.

This ensures database persistence independent of the EC2 root volume.

📸 Screenshots (Deliverables)

Running web application on EC2

MariaDB database and table

Mounted EBS volume at /backup

Backup file stored in /backup

Terminal outputs for verification

