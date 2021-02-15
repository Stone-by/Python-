from fpdf import FPDF
import datetime
import os.path
from tkinter import*
from tkinter import filedialog
from tkinter import messagebox

now = datetime.datetime.now()

filename = "report.pdf"
file1 = ""
files2 = [4]

def clicked1():
    global file1
    file1 = filedialog.askopenfilename()
    lbl6_2 =Label(window, text=file1)
    lbl6_2.grid(column=1, row=5)

def clicked2():
    global files2
    files2 = filedialog.askopenfilenames()
    lbl7_2 =Label(window, text=files2)
    lbl7_2.grid(column=1, row=6)

def clicked3():
    messagebox.showinfo('', 'Отчет готов!')

    Inst = txt1.get()
    Kaf = txt2.get()
    Group = txt3.get()
    FIO = txt4.get()
    Nomer = txt5.get()

    pdf = FPDF(unit="mm", format="A4")
    pdf.add_page()
    effective_page_width = pdf.w - 2 * pdf.l_margin
    pdf.add_font('TNR', '', 'times-new-roman.ttf', uni=True)

    pdf.image('logo.jpg', x=98, y=5, w=25)
    pdf.set_font('TNR', '', 12)
    pdf.cell(200, 50, "МИНОБРНАУКИ РОССИИ", align="C")
    pdf.ln(5)
    pdf.cell(200, 55, "Федеральное государственное бюджетное образовательное учереждение", align="C")
    pdf.ln(5)
    pdf.cell(200, 55, "высшего образования", align="C")
    pdf.ln(8)
    pdf.set_font('TNR', '', 14)
    pdf.cell(200, 55, '"МИРЭА - Российский технический университет"', align="C")
    pdf.ln(5)
    pdf.cell(200, 55, '"РТУ МИРЭА"', align="C")
    pdf.ln(5)
    pdf.line(10, 65, 200, 65)
    pdf.line(10, 66, 200, 66)
    pdf.ln(5)
    pdf.set_font('TNR', '', 12)
    pdf.cell(200, 55, str(Inst), align="C")
    pdf.ln(5)
    pdf.cell(200, 55, 'Кафедра ' + str(Kaf), align="C")
    pdf.ln(65)
    pdf.set_font('TNR', '', 16)
    pdf.cell(200, 55, 'ОТЧЕТ', align="C")
    pdf.ln(10)
    pdf.cell(200, 55, 'ПО ПРАКТИЧЕСКОЙ РАБОТЕ № ' + str(Nomer), align="C")
    pdf.ln(10)
    pdf.cell(200, 55, 'По дисциплине «Программирование на языке Python»', align="C")
    pdf.ln(75)
    pdf.set_font('TNR', '', 14)
    pdf.cell(100, 25, 'Выполнил студент группы: ' + Group, align="L")
    pdf.cell(120, 25, FIO, align="C")
    pdf.ln(25)
    pdf.set_font('TNR', '', 12)
    pdf.cell(85, 25, 'Практическая работа выполнена: ', align="L")
    pdf.cell(85, 25, now.strftime("«%d»  %m  %Yг."), align="L")
    pdf.line(150, 248, 190, 248)
    pdf.ln(10)
    pdf.cell(85, 25, '«Зачтено» ', align="L")
    pdf.cell(85, 25, now.strftime("«    »  %m  %Yг."), align="L")
    pdf.line(150, 258, 190, 258)

    pdf.add_page()
    pdf.set_font('TNR', '', 16)
    pdf.cell(100, 15, '1. Исходный код программы', align="L")
    pdf.ln(15)
    with open(file1, "r") as file:
        text = file.read()
    pdf.set_font('TNR', '', 12)
    pdf.multi_cell(effective_page_width, 5, text)

    pdf.add_page()
    pdf.set_font('TNR', '', 16)
    pdf.cell(100, 15, '2. Результат выполнения программы', align="L")
    for i in range(len(files2)):
        pdf.ln(15)
        pdf.set_font('TNR', '', 14)
        pdf.image(files2[i], x=30, y=25+(115*i), w=150, h=90)
        pdf.ln(85)
        pdf.cell(190, 25, 'Рис. ' + str(i+1), align="C")

    pdf.output(filename)
    return 0

window = Tk()
window.title("Добро пожаловать в генератор отчетов")
window.geometry('600x600')
lbl1 = Label(window, text="Ваш институт")
lbl1.grid(column=0, row=0)
txt1 = Entry(window,width=10)
txt1.grid(column=1, row=0)
txt1.focus()
lbl2 = Label(window, text="Ваша кафедра")
lbl2.grid(column=0, row=1)
txt2 = Entry(window,width=10)
txt2.grid(column=1, row=1)
lbl3 = Label(window, text="Ваша группа")
lbl3.grid(column=0, row=2)
txt3 = Entry(window,width=10)
txt3.grid(column=1, row=2)
lbl4 = Label(window, text="Ваше ФИО")
lbl4.grid(column=0, row=3)
txt4 = Entry(window,width=10)
txt4.grid(column=1, row=3)
lbl5 = Label(window, text="Ваш номер отчета")
lbl5.grid(column=0, row=4)
txt5 = Entry(window,width=10)
txt5.grid(column=1, row=4)
lbl6 = Label(window, text="Исходный код")
lbl6.grid(column=0, row=5)
btn1 = Button(window, text="Выбрать", command=clicked1)
btn1.grid(column=2, row=5)
lbl7 = Label(window, text="Изображения тестов")
lbl7.grid(column=0, row=6)
btn2 = Button(window, text="Выбрать", command=clicked2)
btn2.grid(column=2, row=6)
btn3 = Button(window, text="Потвердить", command=clicked3)
btn3.grid(column=0, row=7)
window.mainloop()

