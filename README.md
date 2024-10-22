# E-Ticaret Sistemi

Bu proje, Python ile yazılmış basit bir e-ticaret sistemidir. Müşteri yönetimi, ürün yönetimi, satın alma işlemleri ve sipariş takibi gibi temel işlevleri içerir.

## Özellikler

* **Müşteri Yönetimi:**
    * Müşteri ekleme, güncelleme ve silme
    * Müşteri bilgileri görüntüleme
* **Ürün Yönetimi:**
    * Ürün ekleme, güncelleme ve silme
    * Ürün bilgileri görüntüleme
    * Stok yönetimi
* **Satın Alma İşlemleri:**
    * Sepete ürün ekleme
    * Sepetteki ürünlerin görüntülenmesi
    * Ödeme işlemi
* **Sipariş Takibi:**
    * Sipariş oluşturma
    * Sipariş durumu takibi
    * Sipariş bilgileri görüntüleme

## Kurulum

1. **Python 3.x** ve **pyodbc** kütüphanesini yükleyin:
   ```bash
   pip install pyodbc
  
store_db adında bir SQL Server veritabanı oluşturun.

connect_to_database() fonksiyonunda veritabanı bağlantı bilgilerini güncelleyin.

main() fonksiyonunu çalıştırın.

* **Kullanım**
Program çalıştırıldığında, ana menüde seçenekler sunulacaktır.

1: Satın Alma İşlemleri

2: Müşteri İşlemleri

3: Ürün İşlemleri

4: Müşteri Siparişlerini Görüntüle

5: Çıkış

Seçeneklerden birini seçerek istediğiniz işlemleri gerçekleştirebilirsiniz.

* **Teknolojiler**
  
Python

pyodbc

SQL Server


**Lisans**
Bu proje MIT Lisansı altında lisanslanmıştır.
