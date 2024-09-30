class Product:

    def __init__(self, name, weigth, category):
        self.name = name
        self.weigth = weigth
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weigth}, {self.category}'


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        from pprint import pprint
        file = open(self.__file_name, 'r')
        text_read = file.read()
        file.close()
        return text_read

    def add(self, *products):
        from pprint import pprint
        file = open(self.__file_name, 'a+')
        file.seek(0)
        file_read = file.read().splitlines()
        added_products = []
        for product in products:
            if str(product) in file_read:
                print(f'Продукт {product} уже есть в магазине')
            else:
                file.write(f'{product}\n')
        file.close()
        return self.__file_name


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

#print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())