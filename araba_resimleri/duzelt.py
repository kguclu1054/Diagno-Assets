import os

# Türkçe karakter haritası
tr_map = str.maketrans("çğıöşüÇĞİÖŞÜ", "cgiosuCGIOSU")

# Klasördeki dosyaları gez
for filename in os.listdir("."):
    # Sadece resim dosyalarına bak (py dosyasını değiştirme)
    if filename.endswith(".py"):
        continue
        
    # 1. Türkçe karakterleri İngilizceye çevir
    new_name = filename.translate(tr_map)
    
    # 2. Hepsini küçük harf yap
    new_name = new_name.lower()
    
    # 3. Alt çizgileri (_) ve boşlukları ( ) tireye (-) çevir
    new_name = new_name.replace("_", "-").replace(" ", "-")
    
    # Dosya ismini değiştir
    if filename != new_name:
        try:
            os.rename(filename, new_name)
            print(f"Düzeltildi: {filename} -> {new_name}")
        except Exception as e:
            print(f"Hata: {filename} değiştirilemedi. {e}")

print("\n--- İŞLEM TAMAMLANDI! ---")