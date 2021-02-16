from fpdf import FPDF
import datetime
import os.path
from tkinter import*
from tkinter import filedialog
from tkinter import messagebox
from tkinter import Menu

Inst = ""
Kaf = ""
Group = ""
FIO = ""
Nomer = ""
Predmet = ""
file1 = ""
files2 = [99]
filename = ""

now = datetime.datetime.now()

class GENERATOR_OTCHET:
    def MENY(self):
        def clicked1():
            def clicked1_1():
                def clicked1_CREAT():
                    global Inst
                    Inst = txt1_CREAT.get()
                    global Kaf
                    Kaf = txt2_CREAT.get()
                    global Group
                    Group = txt3_CREAT.get()
                    global FIO
                    FIO = txt4_CREAT.get()
                    lbl_OBZOR = Label(window2, text="Готово")
                    lbl_OBZOR.grid(column=0, row=3)
                window3 = Tk()
                window3.title("Новый профиль")
                window3.geometry('350x350')
                lbl1_CREAT = Label(window3, text="Институт")
                lbl1_CREAT.grid(column=0, row=0)
                txt1_CREAT = Entry(window3, width=10)
                txt1_CREAT.grid(column=1, row=0)
                txt1_CREAT.focus()
                lbl2_CREAT = Label(window3, text="Кафедра")
                lbl2_CREAT.grid(column=0, row=1)
                txt2_CREAT = Entry(window3, width=10)
                txt2_CREAT.grid(column=1, row=1)
                lbl3_CREAT = Label(window3, text="Группа")
                lbl3_CREAT.grid(column=0, row=2)
                txt3_CREAT = Entry(window3, width=10)
                txt3_CREAT.grid(column=1, row=2)
                lbl4_CREAT = Label(window3, text="ФИО")
                lbl4_CREAT.grid(column=0, row=3)
                txt4_CREAT = Entry(window3, width=10)
                txt4_CREAT.grid(column=1, row=3)
                btn_CREAT = Button(window3, text="Потвердить", command=clicked1_CREAT)
                btn_CREAT.grid(column=0, row=4)
                window3.mainloop()
            def clicked1_2():
                global Inst
                Inst = ""
                global Kaf
                Kaf = ""
                global Group
                Group = ""
                global FIO
                FIO = ""
                lbl_OBZOR = Label(window2, text="Другой")
                lbl_OBZOR.grid(column=0, row=3)
            window2 = Tk()
            window2.title("Профиль")
            window2.geometry('350x350')
            btn1 = Button(window2, text="Создать", command=clicked1_1)
            btn1.grid(column=0, row=0)
            btn2 = Button(window2, text="Другой", command=clicked1_2)
            btn2.grid(column=0, row=1)
            window2.mainloop()
        def clicked2():
            def clicked1_1():
                global Predmet
                Predmet = "Программирование на Python"
                def clicked1_1():
                    global file1
                    file1 = filedialog.askopenfilename()
                    lbl6_2 = Label(window3, text="Готово")
                    lbl6_2.grid(column=1, row=0)
                def clicked1_2():
                    global files2
                    files2 = filedialog.askopenfilenames()
                    lbl7_2 = Label(window3, text="Готово")
                    lbl7_2.grid(column=1, row=1)
                def clicked1_3():
                    global Nomer
                    Nomer = txt5.get()
                    lbl_OBZOR = Label(window3, text="Готово")
                    lbl_OBZOR.grid(column=2, row=2)
                window3 = Tk()
                window3.title("Данные")
                window3.geometry('350x350')
                btn1 = Button(window3, text="Код", command=clicked1_1)
                btn1.grid(column=0, row=0)
                btn2 = Button(window3, text="Тест", command=clicked1_2)
                btn2.grid(column=0, row=1)
                lbl5 = Label(window3, text="Номер отчета")
                lbl5.grid(column=0, row=2)
                txt5 = Entry(window3, width=10)
                txt5.grid(column=1, row=2)
                btn3 = Button(window3, text="Потвердить", command=clicked1_3)
                btn3.grid(column=0, row=3)
                window3.mainloop()
            def clicked1_2():
                global Predmet
                Predmet = "2"
            def clicked1_3():
                global Predmet
                Predmet = "3"
            window2 = Tk()
            window2.title("Предмет")
            window2.geometry('350x350')
            btn1 = Button(window2, text="Программирование на Python", command=clicked1_1)
            btn1.grid(column=0, row=0)
            btn2 = Button(window2, text="2", command=clicked1_2)
            btn2.grid(column=0, row=1)
            btn2 = Button(window2, text="3", command=clicked1_3)
            btn2.grid(column=0, row=2)
            lbl_OBZOR = Label(window2, text="Выбран "+Predmet)
            lbl_OBZOR.grid(column=0, row=3)
            window2.mainloop()
        def clicked3():
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
            pdf.cell(200, 55, 'По дисциплине «'+ Predmet +'»', align="C")
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
                pdf.image(files2[i], x=30, y=25 + (115 * i), w=150, h=90)
                pdf.ln(85 + (i * 30))
                pdf.cell(190, 25, 'Рис. ' + str(i + 1), align="C")
            global filename
            filename = "ОТЧЕТ_ПО_"+Predmet+"_НОМЕР_"+Nomer+"_СТУДЕНТА_"+FIO+"_ГРУППЫ_"+Group+".pdf"
            pdf.output(filename)
            messagebox.showinfo('Конец', 'Отчет готов!')
        def clicked_meny_1():
            messagebox.showinfo('Помощь', 'Вас приветствует генератор отчетов! Я могу создавать отчеты по любому из предоставленных мною предметов! Вам необходимо лишь заполнить пункт Профиль и Предмет полностью и правильно, а то я пока еще недоделан и могу что-то не понять, если вы заполните что-то не так! Заранее извиняюсь!')
        def clicked_meny_2():
            messagebox.showinfo('Авторы', 'Борисов «Moreez317» Александр и Чепелюк «Stoneby» Иван')
        def clicked4():
            open(filename)
        def clicked5():
            messagebox.showinfo('Отправить email', 'Не реализовано!')
        def clicked6():
            exit()
        window = Tk()
        window.title("Добро пожаловать в генератор отчетов")
        window.geometry('350x350')
        lbl1 = Label(window, text="Ваш профиль")
        lbl1.grid(column=0, row=0)
        btn1 = Button(window, text="Выбрать", command=clicked1)
        btn1.grid(column=1, row=0)
        lbl2 = Label(window, text="Ваш предмет")
        lbl2.grid(column=0, row=1)
        btn2 = Button(window, text="Выбрать", command=clicked2)
        btn2.grid(column=1, row=1)
        btn3 = Button(window, text="Создать отчет", command=clicked3)
        btn3.grid(column=0, row=2)
        btn3 = Button(window, text="Предпросмотр", command=clicked4)
        btn3.grid(column=0, row=3)
        btn3 = Button(window, text="Отправить email", command=clicked5)
        btn3.grid(column=0, row=4)
        btn3 = Button(window, text="Выход", command=clicked6)
        btn3.grid(column=0, row=5)
        menu = Menu(window)
        new_item = Menu(menu)
        new_item = Menu(menu, tearoff=0)
        menu.add_cascade(label='Меню', menu=new_item)
        window.config(menu=menu)
        new_item.add_command(label='Помощь', command=clicked_meny_1)
        new_item.add_command(label='Авторы', command=clicked_meny_2)
        window.mainloop()
start = GENERATOR_OTCHET()
start.MENY()
