import tkinter as tk


def add_():
    num_1 = int(number1_entry.get())
    num_2 = int(number2_entry.get())
    res = num_1 + num_2
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, res)


def sub_():
    num_1 = int(number1_entry.get())
    num_2 = int(number2_entry.get())
    res = num_1 - num_2
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, res)

def mult_():
   num_1 = int(number1_entry.get())
   num_2 = int(number2_entry.get())
   res = num_1 * num_2
   answer_entry.delete(0, 'end')
   answer_entry.insert(0, res)

def div_():
   num_1 = int(number1_entry.get())
   num_2 = int(number2_entry.get())
   res = num_1 / num_2
   answer_entry.delete(0, 'end')
   answer_entry.insert(0, res)


window = tk.Tk()  # Метод для создания окна
window.title('Калькулятор')  # Метод изменения названия окна
window.geometry('350x350')  # Метод задаёт исходные размеры окна
window.resizable(False, False)  # Т.к. метод размещения кнопок не очень хорошо
# реагирует на изменения размера окна, то вот данный метод, который не даёт манять размеры
# исходного окна
button_add = tk.Button(window, text='+', width=5, height=5, command=add_)
# Собственно создание кнопки (естественно в отдельной переменной)
button_add.place(x=25, y=100)  # Метод размещения кнопки, после чего она и появляется на экране

button_sub = tk.Button(window, text='-', width=5, height=5, command=sub_)
button_sub.place(x=110, y=100)

button_mult = tk.Button(window, text='x', width=5, height=5, command=mult_)
button_mult.place(x=195, y=100)

button_div = tk.Button(window, text='/', width=5, height=5, command=div_)
button_div.place(x=280, y=100)

number1_entry = tk.Entry(window, width=21)  # Данный метод создаёт поле для ввода
number1_entry.place(x=25, y=50)  # Размещаем как и выше кнопки
number1 = tk.Label(window, text='Введите первое число')  # Команда создающая текстовые "подсказки"
number1.place(x=25, y=25)  # Размещение

number2_entry = tk.Entry(window, width=21)
number2_entry.place(x=195, y=50)
number2 = tk.Label(window, text='Введите второе число')
number2.place(x=195, y=25)

answer_entry = tk.Entry(window, width=49)
answer_entry.place(x=25, y=250)
answer = tk.Label(window, text='Ответ')
answer.place(x=25, y=225)

window.mainloop()  # Это метод обновления окна. Одна из наиболее важных строчек.
# Весь код пишется в основмном между ней и строчкой, в которой мы в принципе создали окно
