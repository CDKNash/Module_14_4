import sqlite3

def initiate_db():

    connection = sqlite3.connect("Product_TG.db")
    cursor = connection.cursor()

    cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    ''')

    cursor.execute("CREATE INDEX IF NOT EXISTS idx_id ON Products(id)")

    for i in range(1, 5):
        cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",(f'Продукт {i}', f'Описание {i}', f'{i * 100}'))


    connection.commit()
    connection.close()


def get_all_products():
    connection = sqlite3.connect("Product_TG.db")
    cursor = connection.cursor()

    products = cursor.execute('SELECT * FROM Products').fetchall()

    connection.commit()
    connection.close()

    return products