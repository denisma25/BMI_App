from tkinter import *


root = Tk()
root.title('BMI App')
root.geometry('640x480')
root.resizable(width=False, height=False)


# Widgets
label_for_height = Label(
    text='Введите Ваш рост (м.)',
    font=('Consolas', '18')
)
entry_for_height = Entry(
    width=10,
    font=('Consolas', '30'),
    justify=CENTER
)

label_for_weigth = Label(
    text='Введите Ваш вес (кг.)',
    font=('Consolas', '18')
)
entry_for_weigth = Entry(
    width=10,
    font=('Consolas', '30'),
    justify=CENTER
)


def calculate():
    height = float(entry_for_height.get())
    weigth = float(entry_for_weigth.get())

    # bmi = weigth / (height ** 2)

    bmi = round(weigth / (height ** 2), 2)
    

    if bmi < 15.99:
        status = 'выраженный дефицит массы тела'
    elif bmi > 16 and bmi < 18.49:
        status = 'недостаточная масса тела'
    elif bmi > 18.5 and bmi < 24.99:
        status = 'норма'
    elif bmi > 25 and bmi < 29.99:
        status = 'предожирение'
    elif bmi > 30 and bmi < 34.99:
        status = '1 степень ожирения'
    elif bmi > 35 and bmi < 39.99:
        status = '2 степень ожирения'
    else:
        status = '3 степень ожирения'

    result_label = Label(
        text=f'''
    Ваш ИМТ: {bmi} кг/м2\n
    Это {status}
        ''',
        font=('Consolas', '18')
    )
    result_label.pack()
    



submit_button = Button(
    text='Рассчитать',
    font=('Consolas', '16'),
    command=calculate
)


# Placing widgets
label_for_height.pack()
entry_for_height.pack()
label_for_weigth.pack()
entry_for_weigth.pack()
submit_button.pack()


if __name__ == '__main__':
    root.mainloop()