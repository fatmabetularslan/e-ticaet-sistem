import pyodbc

class UrunIslemleri:
    def __init__(self, conn, cursor):
        self.conn = conn
        self.cursor = cursor

    def islemler(self):
        while True:
            print("\n--- Ürün İşlemleri ---")
            print("1. Ürün Ekle")
            print("2. Ürün Güncelle")
            print("3. Ürün Sil")
            print("4. Ürün Listele")
            print("5. Ana Menüye Dön")

            secim = input("Seçiminiz (1-5): ")

            if secim == "1":
                self.urun_ekle()
            elif secim == "2":
                self.urun_guncelle()
            elif secim == "3":
                self.urun_sil()
            elif secim == "4":
                self.urun_listele()
            elif secim == "5":
                break
            else:
                print("Geçersiz seçim!")

    def urun_ekle(self):
        ad = input("Ürün Adı: ")
        kod = input("Ürün Kodu: ")
        stok = int(input("Stok Miktarı: "))
        sql = "INSERT INTO product (product_name, product_code, stock) VALUES (?, ?, ?)"
        self.cursor.execute(sql, (ad, kod, stok))
        self.conn.commit()
        print("Ürün başarıyla eklendi.")

    def urun_guncelle(self):
        id = int(input("Güncellenecek Ürün ID: "))
        sql = "SELECT * FROM product WHERE product_id = ?"
        self.cursor.execute(sql, (id,))
        urun = self.cursor.fetchone()
        if urun:
            ad = input(f"Yeni Ad ({urun[1]}): ") or urun[1]
            kod = input(f"Yeni Kod ({urun[2]}): ") or urun[2]
            stok = int(input(f"Yeni Stok ({urun[3]}): ")) or urun[3]
            sql = "UPDATE product SET product_name = ?, product_code = ?, stock = ? WHERE product_id = ?"
            self.cursor.execute(sql, (ad, kod, stok, id))
            self.conn.commit()
            print("Ürün başarıyla güncellendi.")
        else:
            print("Geçersiz ürün ID!")

    def urun_sil(self):
        id = int(input("Silinecek Ürün ID: "))
        sql = "DELETE FROM product WHERE product_id = ?"
        self.cursor.execute(sql, (id,))
        self.conn.commit()
        print("Ürün başarıyla silindi.")

    def urun_listele(self):
        sql = "SELECT * FROM product"
        self.cursor.execute(sql)
        urunler = self.cursor.fetchall()
        if urunler:
            print("\n--- Ürün Listesi ---")
            for urun in urunler:
                print(f"ID: {urun[0]}, Ad: {urun[1]}, Kod: {urun[2]}, Stok: {urun[3]}")
        else:
            print("Ürün bulunamadı.")