import os

class Config:
    MYSQL_HOST = os.environ.get('MYSQL_HOST', '10.160.215.50')
    MYSQL_USER = os.environ.get('MYSQL_USER', 'dba')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', 'Pipoca123')
    MYSQL_DB = os.environ.get('MYSQL_DB', 'concessionarias_auto_prime')
