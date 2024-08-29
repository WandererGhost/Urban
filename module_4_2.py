def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')

    inner_function()


test_function()
inner_function()  # Программа не видит эту функцию, так как она находится внутри другой функции.
# А внутри функций действует уже локальное пространство имён. Хотя в данном случае функция inner_function
# находится в объемлющем пространстве фунции test_function
