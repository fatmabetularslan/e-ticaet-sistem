def islemler(conn, cursor):
    while True:
        print("\n--- Müşteri İşlemleri ---")
        print("1. Müşteri Ekle")
        print("2. Müşteri Güncelle")
        print("3. Müşteri Sil")
        print("4. Müşteri Listele")
        print("5. Ana Menüye Dön")

        secim = input("Seçiminiz (1-5): ")

        if secim == "1":
            musteri_ekle(conn, cursor)
        elif secim == "2":
            musteri_guncelle(conn, cursor)
        elif secim == "3":
            musteri_sil(conn, cursor)
        elif secim == "4":
            musteri_listele(conn, cursor)
        elif secim == "5":
            break
        else:
            print("Geçersiz seçim!")

def musteri_ekle(conn, cursor):
    ad = input("Müşteri Adı: ")
    puan = int(input("Müşteri Puanı: "))
    sql = "INSERT INTO customer (customer_name, customer_points) VALUES (?, ?)"
    cursor.execute(sql, (ad, puan))
    conn.commit()
    print("Müşteri başarıyla eklendi.")

def musteri_guncelle(conn, cursor):
    id = int(input("Güncellenecek Müşteri ID: "))
    sql = "SELECT * FROM customer WHERE customer_id = ?"
    cursor.execute(sql, (id,))
    musteri = cursor.fetchone()
    if musteri:
        ad = input(f"Yeni Ad ({musteri[1]}): ") or musteri[1]
        puan = int(input(f"Yeni Puan ({musteri[2]}): ")) or musteri[2]
        sql = "UPDATE customer SET customer_name = ?, customer_points = ? WHERE customer_id = ?"
        cursor.execute(sql, (ad, puan, id))
        conn.commit()
        print("Müşteri başarıyla güncellendi.")
    else:
        print("Geçersiz müşteri ID!")

def musteri_sil(conn, cursor):
    id = int(input("Silinecek Müşteri ID: "))
    sql = "DELETE FROM customer WHERE customer_id = ?"
    cursor.execute(sql, (id,))
    conn.commit()
    print("Müşteri başarıyla silindi.")

def musteri_listele(conn, cursor):
    sql = "SELECT * FROM customer"
    cursor.execute(sql)
    musteriler = cursor.fetchall()
    if musteriler:
        print("\n--- Müşteri Listesi ---")
        for musteri in musteriler:
            print(f"ID: {musteri[0]}, Ad: {musteri[1]}, Puan: {musteri[2]}")
    else:
        print("Müşteri bulunamadı.")