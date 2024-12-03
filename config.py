import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Umasenha2236*'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://vinistm:senha123@mysql.server:3306/api_troca'
SQLALCHEMY_TRACK_MODIFICATIONS = False