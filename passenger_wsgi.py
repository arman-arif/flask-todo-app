import os
import sys

# 1. Add your project directory to the sys.path
# This ensures Python can find the 'app' module
sys.path.insert(0, os.path.dirname(__file__))

# 2. Import the actual Flask instance
# Since your snippet says 'from app.app import app', we do this:
from main import app as application

# Passenger expects the variable name 'application'
