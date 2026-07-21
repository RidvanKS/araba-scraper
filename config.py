import os
from dotenv import load_dotenv
from urllib.parse import urlparse

load_dotenv()

# DATABASE_URL'den parse et
DATABASE_URL = os.getenv('DATABASE_URL')

if DATABASE_URL:
    # PostgreSQL URL'sinden değerleri çıkart
    parsed = urlparse(DATABASE_URL)
    DB_CONFIG = {
        'host': parsed.hostname,
        'port': parsed.port or 5432,
        'dbname': parsed.path.lstrip('/'),
        'user': parsed.username,
        'password': parsed.password,
        'sslmode': 'require'
    }
else:
    # Local development için fallback
    DB_CONFIG = {
        'host': os.getenv('DB_HOST', 'localhost'),
        'port': int(os.getenv('DB_PORT', 5432)),
        'dbname': os.getenv('DB_NAME', 'araba_ilan'),
        'user': os.getenv('DB_USER', 'postgres'),
        'password': os.getenv('DB_PASSWORD'),
    }

# Kontrol: Şifre varsa devam et
if not DB_CONFIG['password']:
    raise Exception("❌ DB_PASSWORD tanımlanmamış!")
