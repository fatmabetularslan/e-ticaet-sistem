def islemler(conn, cursor):
    while True:
        print("\n--- Ürün İşlemleri ---")
        print("1. Ürün Ekle")
        print("2. Ürün Güncelle")
        print("3. Ürün Sil")
        print("4. Ürün Listele")
        print("5. Ana Menüye Dön")

        secim = input("Seçiminiz (1-5): ")

        if secim == "1":
            urun_ekle(conn, cursor)
        elif secim == "2":
            urun_guncelle(conn, cursor)
        elif secim == "3":
            urun_sil(conn, cursor)
        elif secim == "4":
            urun_listele(conn, cursor)
        elif secim == "5":
            break
        else:
            print("Geçersiz seçim!")

def urun_ekle(conn, cursor):
    ad = input("Ürün Adı: ")
    kod = input("Ürün Kodu: ")
    stok = int(input("Stok Miktarı: "))
    sql = "INSERT INTO product (product_name, product_code, stock) VALUES (?, ?, ?)"
    cursor.execute(sql, (ad, kod, stok))
    conn.commit()
    print("Ürün başarıyla eklendi.")

def urun_guncelle(conn, cursor):
    id = int(input("Güncellenecek Ürün ID: "))
    sql = "SELECT * FROM product WHERE product_id = ?"
    cursor.execute(sql, (id,))
    urun = cursor.fetchone()
    if urun:
        ad = input(f"Yeni Ad ({urun[1]}): ") or urun[1]
        kod = input(f"Yeni Kod ({urun[2]}): ") or urun[2]
        stok = int(input(f"Yeni Stok ({urun[3]}): ")) or urun[3]
        sql = "UPDATE product SET product_name = ?, product_code = ?, stock = ? WHERE product_id = ?"
        cursor.execute(sql, (ad, kod, stok, id))
        conn.commit()
        print("Ürün başarıyla güncellendi.")
    else:
        print("Geçersiz ürün ID!")

def urun_sil(conn, cursor):
    id = int(input("Silinecek Ürün ID: "))
    sql = "DELETE FROM product WHERE product_id = ?"
    cursor.execute(sql, (id,))
    conn.commit()
    print("Ürün başarıyla silindi.")

def urun_listele(conn, cursor):
    sql = "SELECT * FROM product"
    cursor.execute(sql)
    urunler = cursor.fetchall()
    if urunler:
        print("\n--- Ürün Listesi ---")
        for urun in urunler:
            print(f"ID: {urun[0]}, Ad: {urun[1]}, Kod: {urun[2]}, Stok: {urun[3]}")
    else:
        print("Ürün bulunamadı.")