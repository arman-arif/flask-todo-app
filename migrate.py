import sys
import os

# 1. Tell Python where your 'app' folder is
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# 2. Import your app, db, and migrate objects
# Based on your previous snippet, they are in app/app.py and app/db.py
from app.app import app
from app.db import db
from flask_migrate import upgrade

def run_migrations():
    with app.app_context():
        print("Starting migration...")
        try:
            # This is the programmatic equivalent of 'flask db upgrade'
            upgrade()
            print("Migration successful!")
        except Exception as e:
            print(f"Migration failed: {e}")

if __name__ == "__main__":
    run_migrations()
