import pyodbc

class MusteriIslemleri:
    def __init__(self, conn, cursor):
        self.conn = conn
        self.cursor = cursor

    def islemler(self):
        while True:
            print("\n--- Müşteri İşlemleri ---")
            print("1. Müşteri Ekle")
            print("2. Müşteri Güncelle")
            print("3. Müşteri Sil")
            print("4. Müşteri Listele")
            print("5. Ana Menüye Dön")

            secim = input("Seçiminiz (1-5): ")

            if secim == "1":
                self.musteri_ekle()
            elif secim == "2":
                self.musteri_guncelle()
            elif secim == "3":
                self.musteri_sil()
            elif secim == "4":
                self.musteri_listele()
            elif secim == "5":
                break
            else:
                print("Geçersiz seçim!")

    def musteri_ekle(self):
        ad = input("Müşteri Adı: ")
        puan = int(input("Müşteri Puanı: "))
        sql = "INSERT INTO customer (customer_name, customer_points) VALUES (?, ?)"
        self.cursor.execute(sql, (ad, puan))
        self.conn.commit()
        print("Müşteri başarıyla eklendi.")

    def musteri_guncelle(self):
        id = int(input("Güncellenecek Müşteri ID: "))
        sql = "SELECT * FROM customer WHERE customer_id = ?"
        self.cursor.execute(sql, (id,))
        musteri = self.cursor.fetchone()
        if musteri:
            ad = input(f"Yeni Ad ({musteri[1]}): ") or musteri[1]
            puan = int(input(f"Yeni Puan ({musteri[2]}): ")) or musteri[2]
            sql = "UPDATE customer SET customer_name = ?, customer_points = ? WHERE customer_id = ?"
            self.cursor.execute(sql, (ad, puan, id))
            self.conn.commit()
            print("Müşteri başarıyla güncellendi.")
        else:
            print("Geçersiz müşteri ID!")

    def musteri_sil(self):
        id = int(input("Silinecek Müşteri ID: "))
        sql = "DELETE FROM customer WHERE customer_id = ?"
        self.cursor.execute(sql, (id,))
        self.conn.commit()
        print("Müşteri başarıyla silindi.")

    def musteri_listele(self):
        sql = "SELECT * FROM customer"
        self.cursor.execute(sql)
        musteriler = self.cursor.fetchall()
        if musteriler:
            print("\n--- Müşteri Listesi ---")
            for musteri in musteriler:
                print(f"ID: {musteri[0]}, Ad: {musteri[1]}, Puan: {musteri[2]}")
        else:
            print("Müşteri bulunamadı.")