def islemler(conn, cursor):
    while True:
        musteri_id = int(input("Müşteri ID: "))
        sql = "SELECT * FROM customer WHERE customer_id = ?"
        cursor.execute(sql, (musteri_id,))
        musteri = cursor.fetchone()
        if musteri:
            print("\n--- Ürün Listesi ---")
            sql = "SELECT * FROM product"
            cursor.execute(sql)
            urunler = cursor.fetchall()
            for urun in urunler:
                print(f"ID: {urun[0]}, Ad: {urun[1]}, Kod: {urun[2]}, Stok: {urun[3]}")

            while True:
                urun_kodu = input("Satın alınacak ürün kodu (Çıkmak için 'q'): ")
                if urun_kodu.lower() == 'q':
                    break

                sql = "SELECT * FROM product WHERE product_id = ?"  # Use product_id
                cursor.execute(sql, (urun_kodu,))
                urun = cursor.fetchone()
                if urun:
                    if urun[3] > 0:
                        miktar = int(input("Miktar: "))
                        if miktar <= urun[3]:
                            sql = "INSERT INTO purchase (customer_id, product_id, purchase_date, purchase_quantity) VALUES (?, ?, GETDATE(), ?)"
                            cursor.execute(sql, (musteri_id, urun[0], miktar))
                            conn.commit()
                            print("Satın alma işlemi başarıyla tamamlandı.")
                            sql = "UPDATE product SET product_stock = product_stock - ? WHERE product_id = ?"
                            cursor.execute(sql, (miktar, urun[0]))
                            conn.commit()
                        else:
                            print("Stokta yeterli ürün yok.")
                    else:
                        print("Ürünün stoğu mevcut değil.")
                else:
                    print("Geçersiz ürün kodu!")

        else:
            print("Kayıtlı müşteri bulunamadı.")

        if input("Başka işlem yapmak ister misiniz? (e/h): ").lower() != "e":
            break