# -*- coding: utf-8 -*-
import sqlite3


def initiate_db():
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products(
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT,
        price INTEGER NOT NULL,
        image TEXT
        )
        ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER NOT NULL,
        balance INTEGER NOT NULL
        )
        ''')

    connection.commit()
    connection.close()


def add_product(title, price, description=None, image=None):
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()

    cursor.execute('''
    INSERT INTO Products (title, description, price, image) VALUES (?, ?, ?, ?)
    ''', (f'{title}', f'{description}', f'{price}', f'{image}'))

    connection.commit()
    connection.close()


def get_all_products():
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()

    cursor.execute('SELECT title, description, price, image FROM Products')
    products = cursor.fetchall()

    connection.close()
    return products


def add_user(username, email, age):
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()

    cursor.execute('''
       INSERT INTO Users (username, email, age, balance)
       VALUES (?, ?, ?, ?)
       ''', (username, email, age, 1000))

    connection.commit()
    connection.close()


def is_included(username):
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()

    # Проверка, существует ли пользователь с данным именем
    cursor.execute('''
    SELECT COUNT(*) FROM Users WHERE username = ?
    ''', (username,))

    count = cursor.fetchone()[0]
    connection.close()

    return count > 0