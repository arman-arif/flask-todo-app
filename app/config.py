import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'Xahph7pha3oofahg@aac#oh3Eichee9u')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
