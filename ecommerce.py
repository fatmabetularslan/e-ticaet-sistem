import pyodbc
import musteri
import urun
import satın_alma
import musterı_siparis

class ECommerce:
    def __init__(self):
        self.conn = self.connect_to_database()
        self.cursor = self.conn.cursor()

    def connect_to_database(self):
        db = (
            'Driver={SQL Server};'
            'Server=BETULLL\SQLEXPRESS;'
            'Database=store_db;'
            'Trusted_Connection=True;'
        )
        conn = pyodbc.connect(db)
        return conn

    def run(self):
        while True:
            print("\n--- E-Ticaret Sistemi ---")
            print("1. Satın Alma İşlemleri")
            print("2. Müşteri İşlemleri")
            print("3. Ürün İşlemleri")
            print("4. Müşteri Siparişlerini Görüntüle") 
            print("5. Çıkış")

            secim = input("Seçiminiz (1-5): ")

            if secim == "1":
                satın_alma_islemleri = satın_alma.SatınAlmaIslemleri(self.conn, self.cursor)
                satın_alma_islemleri.islemler()
            elif secim == "2":
                musteri_islemleri = musteri.MusteriIslemleri(self.conn, self.cursor)
                musteri_islemleri.islemler()
            elif secim == "3":
                urun_islemleri = urun.UrunIslemleri(self.conn, self.cursor)
                urun_islemleri.islemler()
            elif secim == "4":
                customer_id = int(input("Müşteri ID'sini girin: "))
                orders = musterı_siparis.get_customer_orders(self.conn, customer_id)

                if orders:
                    print(f"\n--- Müşteri ID: {customer_id} Siparişleri ---")
                    for order in orders:
                        print(f"Ürün: {order[0]}, Tarih: {order[1]}, Miktar: {order[2]}")
                else:
                    print(f"Müşteri ID: {customer_id} için sipariş bulunamadı.")

                devam = input("Başka bir işlem yapmak ister misiniz? (e/h): ").lower()  
                if devam != 'e':
                    continue  
                else:
                    continue

            elif secim == "5":
                break
            else:
                print("Geçersiz seçim!")

        self.conn.close()

if __name__ == "__main__":
    ecommerce = ECommerce()
    ecommerce.run()