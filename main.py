import tkinter as tk

def get_values():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    return num1, num2

def insert_values(value):
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, value)


def add():
    num1, num2 = get_values()
    res = num1 + num2
    insert_values(res)

def sub():
    num1, num2 = get_values()
    res = num1 - num2
    insert_values(res)

def div():
    num1, num2 = get_values()
    res = num1 / num2
    insert_values(res)

def mul():
    num1, num2 = get_values()
    res = num1 * num2
    insert_values(res)


window = tk.Tk()
window.title('Калькулятор')  # Поменяли название
window.geometry('350x350')    # Задали размер нашего калькулятора
window.resizable(False, False)  # Сделали так, чтобы нельзя было менять размер
button_add = tk.Button(window, text='+', width=2, height=2, command=add)  # Дали название кнопке "+", задали размеры кнопки
button_add.place(x=90, y= 200)     # Расположение кнопки "+"
button_sub = tk.Button(window, text='-', width= 2, height=2, command=sub) # Кнопка '-' и ее размер
button_sub.place(x= 140, y= 200)   # Расположение на окне
button_mull = tk.Button(window,text='/', width=2, height=2, command=div)  # кнопка умножить и ее размеры
button_mull.place(x=190, y=200)            # расположение
button_div = tk.Button(window, text='*', width=2, height=2, command=mul)   # кнопка разделить и ее размер
button_div.place(x=240, y=200)       # расположение
number1_entry = tk.Entry(window, width=22)     # строка для ввода и ее размер
number1_entry.place(x=90, y=75)       #   ее расположение
number2_entry = tk.Entry(window, width=22)    #  вторая строка для ввода и ее размер
number2_entry.place(x=90, y=150)             # расположение второй строки
answer_entry = tk.Entry(window, width=22)   #  строка с ответом и ее размер
answer_entry.place(x=90, y=280)           # расположение строки с ответом
number1 = tk.Label(window, text='Введите первое число: ')   # название для первой строки
number1.place(x= 100, y=50)  #  ее расположение
number2 = tk.Label(window, text='Введите второе число: ')  # название для второй строки
number2.place(x= 100, y=125)    # ее расположение
answer = tk.Label(window, text='Ответ: ')  # название для строки с ответом
answer.place(x= 100, y=250)   # ее расположение: x - по горизонтали, y - по вертикали (для всего окна).

window.mainloop()   # Метод, который обеспечивает все изменения, происходящие в калькуляторе