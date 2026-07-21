#!/usr/bin/env python3
"""
Render'de her gün otomatik çalışacak script
PythonAnywhere veya Render'a yüklüyorum
"""
import sys
import os
from datetime import datetime

# Kodun dizini
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)

from main import ArabamStokTakip
from config import DB_CONFIG

def main():
    print(f"\n{'='*60}")
    print(f"🚗 ARABAM STOK TAKİP - OTOMATİK ÇALIŞMA")
    print(f"{'='*60}")
    print(f"⏰ Başlangıç: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*60}\n")
    
    try:
        # Scraper başlat
        scraper = ArabamStokTakip(db_config=DB_CONFIG)
        
        # Günlük tam tarama (Mod 1)
        success = scraper.run()
        
        if success:
            print("\n✅ BAŞARILI - İşlem tamamlandı!")
            return 0
        else:
            print("\n⚠️ UYARI - İşlem tamamlanmadı")
            return 1
            
    except Exception as e:
        print(f"\n❌ KRİTİK HATA: {e}")
        import traceback
        traceback.print_exc()
        return 2

if __name__ == "__main__":
    sys.exit(main())