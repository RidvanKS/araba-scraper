# config.py
import os
from dotenv import load_dotenv

load_dotenv()

DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'port': int(os.getenv('DB_PORT', 5432)),
    'dbname': os.getenv('DB_NAME', 'araba_ilan'),
    'user': os.getenv('DB_USER', 'postgres'),
    'password': os.getenv('DB_PASSWORD'),
}

# Kontrol: Şifre varsa devam et
if not DB_CONFIG['password']:
    raise Exception("❌ DB_PASSWORD tanımlanmamış! Render'da environment variables'na ekle")