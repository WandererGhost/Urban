import sqlite3


def initiate_db():
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL,
    image TEXT
    )
    ''')
    connection.commit()
    connection.close()


def add_product(id, title, price, description=None, image=None):
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()

    check_product = cursor.execute('SELECT * FROM Products WHERE id=?', (id,))

    if check_product.fetchone() is None:
        cursor.execute('INSERT INTO Products VALUES (?, ?, ?, ?, ?)',
                       (f'{id}', f'{title}', f'{description}', f'{price}', f'{image}'))

    connection.commit()
    connection.close()


def get_all_products():
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()

    cursor.execute('SELECT title, description, price, image FROM Products')
    products = cursor.fetchall()

    connection.close()
    return products
