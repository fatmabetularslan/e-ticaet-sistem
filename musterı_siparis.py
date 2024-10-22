import pyodbc

def connect_to_database():
    db = (
        'Driver={SQL Server};'
        'Server=BETULLL\SQLEXPRESS;'
        'Database=store_db;'
        'Trusted_Connection=True;'
    )
    conn = pyodbc.connect(db)
    return conn

def get_customer_orders(conn, customer_id):
    cursor = conn.cursor()
    sql = """
        SELECT 
            p.product_name,
            o.purchase_date,
            o.purchase_quantity
        FROM purchase o
        JOIN product p ON o.product_id = p.product_id 
        WHERE o.customer_id = ?
    """
    cursor.execute(sql, (customer_id,))
    orders = cursor.fetchall()
    return orders

if __name__ == "__main__":
    conn = connect_to_database()
    customer_id = 2
    orders = get_customer_orders(conn, customer_id)

    if orders:
        print(f"\n--- Müşteri ID: {customer_id} Siparişleri ---")
        for order in orders:
            print(f"Ürün: {order[0]}, Tarih: {order[1]}, Miktar: {order[2]}")
    else:
        print(f"Müşteri ID: {customer_id} için sipariş bulunamadı.")

    conn.close()