# Notes App

A simple web-based note-taking application deployed on AWS EC2 with MariaDB and backup strategy.

## Project Overview
The Notes App allows users to write, save, and view notes. Each note is stored in a MariaDB database with a timestamp.

## Key Features
- Add notes with timestamps
- Store notes in MariaDB
- Display notes in reverse chronological order
- Backup database using mounted EBS volume

## Technology Stack
- Python 3.12
- Flask
- MariaDB
- AWS EC2 (RHEL 10)
- AWS EBS

## How to Run
```bash
pip install -r requirements.txt
python app.py
