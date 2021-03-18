#ver 0.0.2

from tkinter import*
from tkinter import filedialog
from tkinter import messagebox
from tkinter import Menu

from docxtpl import DocxTemplate
from docxcompose.composer import Composer
from docx import Document as Document_compose

Kod_YDK = ""
Naz_Stat = ""
FIO = ""
Work = ""
Email = ""
Anot = ""
Kluhc_Sl = ""
Naz_Stat_Ang = ""
FIO_Ang = ""
Work_Ang = ""
Email_Ang = ""
Anot_Ang = ""
Kluhc_Sl_Ang = ""
file1 = ""
file2 = ""
file2_Ang = ""

def PEREMEN():
    doc = DocxTemplate("title_page_template.docx")
    context = {'UDK': Kod_YDK,
               'PROJECTNAME_RU': Naz_Stat,
               'NAME_RU': FIO,
               'ADRESS_RU': Work,
               'email': Email,
               'annotation_RU': Anot,
               'keywords_RU':  Kluhc_Sl,
               'PROJECTNAME_EN': Naz_Stat_Ang,
               'NAME_EN': FIO_Ang,
               'ADRESS_EN': Work_Ang,
               'annotation_EN': Anot_Ang,
               'keywords_EN': Kluhc_Sl_Ang}
    doc.render(context)
    doc.save("title_page.docx")

def combine_all_docx(filename_master,files_list):
    number_of_sections=len(files_list)
    master = Document_compose(filename_master)
    composer = Composer(master)
    for i in range(0, number_of_sections):
        doc_temp = Document_compose(files_list[i])
        composer.append(doc_temp)
    composer.save("combined_file.docx")

class MAIN:
    def Bloc1():
        def Potverd():
            global Kod_YDK
            Kod_YDK = txt1.get()
            global Naz_Stat
            Naz_Stat = txt2.get()
            global FIO
            FIO = txt3.get()
            global Work
            Work = txt4.get()
            global Email
            Email = txt5.get()
            global Anot
            Anot = txt6.get()
            global Kluhc_Sl
            Kluhc_Sl = txt7.get()
            global Naz_Stat_Ang
            Naz_Stat_Ang = txt8.get()
            global FIO_Ang
            FIO_Ang = txt9.get()
            global Work_Ang
            Work_Ang = txt10.get()
            global Email_Ang
            Email_Ang = txt11.get()
            global Anot_Ang
            Anot_Ang = txt12.get()
            global Kluhc_Sl_Ang
            Kluhc_Sl_Ang = txt13.get()
            window2.destroy()
        window2 = Tk()
        window2.title("Блок 1")
        window2.geometry('350x350')
        lbl1 = Label(window2, text="Код УДК")
        lbl1.grid(column=0, row=0)
        txt1 = Entry(window2, width=10)
        txt1.grid(column=1, row=0)
        lbl2 = Label(window2, text="Название статьи")
        lbl2.grid(column=0, row=1)
        txt2 = Entry(window2, width=10)
        txt2.grid(column=1, row=1)
        lbl3 = Label(window2, text="ФИО автора/авторов")
        lbl3.grid(column=0, row=2)
        txt3 = Entry(window2, width=10)
        txt3.grid(column=1, row=2)
        lbl4 = Label(window2, text="Место выполнения работы")
        lbl4.grid(column=0, row=3)
        txt4 = Entry(window2, width=10)
        txt4.grid(column=1, row=3)
        lbl5 = Label(window2, text="e-mail")
        lbl5.grid(column=0, row=4)
        txt5 = Entry(window2, width=10)
        txt5.grid(column=1, row=4)
        lbl6 = Label(window2, text="Аннотация")
        lbl6.grid(column=0, row=5)
        txt6 = Entry(window2, width=10)
        txt6.grid(column=1, row=5)
        lbl7 = Label(window2, text="Ключевые слова")
        lbl7.grid(column=0, row=6)
        txt7 = Entry(window2, width=10)
        txt7.grid(column=1, row=6)
        lbl8 = Label(window2, text="Название статьи(Англ)")
        lbl8.grid(column=0, row=7)
        txt8 = Entry(window2, width=10)
        txt8.grid(column=1, row=7)
        lbl9 = Label(window2, text="ФИО автора/авторов(Англ)")
        lbl9.grid(column=0, row=8)
        txt9 = Entry(window2, width=10)
        txt9.grid(column=1, row=8)
        lbl10 = Label(window2, text="Место выполнения работы(Англ)")
        lbl10.grid(column=0, row=9)
        txt10 = Entry(window2, width=10)
        txt10.grid(column=1, row=9)
        lbl11 = Label(window2, text="e-mail(Англ)")
        lbl11.grid(column=0, row=10)
        txt11 = Entry(window2, width=10)
        txt11.grid(column=1, row=10)
        lbl12 = Label(window2, text="Аннотация(Англ)")
        lbl12.grid(column=0, row=11)
        txt12 = Entry(window2, width=10)
        txt12.grid(column=1, row=11)
        lbl13 = Label(window2, text="Ключевые слова(Англ)")
        lbl13.grid(column=0, row=12)
        txt13 = Entry(window2, width=10)
        txt13.grid(column=1, row=12)
        btn1 = Button(window2, text="Потвердить", command=Potverd)
        btn1.grid(column=0, row=13)
        txt1.focus()
        window2.mainloop()
    def Bloc2():
        def Text():
            global file1
            file1 = filedialog.askopenfilename()
        def Potverd():
            window3.destroy()
        window3 = Tk()
        window3.title("Блок 2")
        window3.geometry('350x350')
        btn1 = Button(window3, text="Текст статьи", command=Text)
        btn1.grid(column=0, row=0)
        btn2 = Button(window3, text="Потвердить", command=Potverd)
        btn2.grid(column=0, row=1)
        window3.mainloop()
    def Bloc3():
        def Spisok():
            global file2
            file2 = filedialog.askopenfilename()
        def Spisok_Ang():
            global file2_Ang
            file2_Ang = filedialog.askopenfilename()
        def Potverd():
            window4.destroy()
        window4 = Tk()
        window4.title("Блок 3")
        window4.geometry('350x350')
        btn1 = Button(window4, text="Список литературы", command=Spisok)
        btn1.grid(column=0, row=0)
        btn2 = Button(window4, text="Список литературы на английском", command=Spisok_Ang)
        btn2.grid(column=0, row=1)
        btn3 = Button(window4, text="Потвердить", command=Potverd)
        btn3.grid(column=0, row=2)
        window4.mainloop()
    def Dop1():
        messagebox.showinfo('Доп 1','Тут пока ничего нет!')
    def Dop2():
        messagebox.showinfo('Доп 2','Тут пока ничего нет!')
    def Create():
        #Само создание файла
        PEREMEN()
        filename_master = "title_page.docx"
        files_list = [file1]
        combine_all_docx(filename_master, files_list)
        #Само создание файла
        messagebox.showinfo('Конец', 'Статья готова!')
    def clicked_meny_1():
        messagebox.showinfo('Помощь','Вас приветсвует генератор статей! Я помогаю собрать готовую статью в pdf файл, изменяю параметры страницы, шрифта, интервала и предупреждаю, если статья меньше необходимого! Вам нужно лишь заполнить все три Блока для создания и нажать "создать". Спасибо за внимание! Версия: 0.0.1')
    def clicked_meny_2():
        messagebox.showinfo('Авторы', 'Борисов «Moreez317» Александр и Чепелюк «Stoneby» Иван')
    window1 = Tk()
    window1.title("Генератор статей")
    window1.geometry('700x350')
    btn1 = Button(window1, text="Блок 1", command=Bloc1)
    btn1.grid(padx=100, pady=30, column=0, row=0)
    btn2 = Button(window1, text="Блок 2", command=Bloc2)
    btn2.grid(padx=100, pady=30, column=0, row=1)
    btn3 = Button(window1, text="Блок 3", command=Bloc3)
    btn3.grid(padx=100, pady=30, column=0, row=2)
    btn4 = Button(window1, text="Доп 1", command=Dop1)
    btn4.grid(padx=100, pady=30, column=0, row=3)
    btn5 = Button(window1, text="Доп 2", command=Dop2)
    btn5.grid(padx=0, pady=30, column=1, row=3)
    btn6 = Button(window1, text="Создать", command=Create)
    btn6.grid(padx=300, pady=30, column=3, row=3)
    #MENU
    menu = Menu(window1)
    new_item = Menu(menu)
    new_item = Menu(menu, tearoff=0)
    menu.add_cascade(label='Меню', menu=new_item)
    window1.config(menu=menu)
    new_item.add_command(label='Помощь', command=clicked_meny_1)
    new_item.add_command(label='Авторы', command=clicked_meny_2)
    #MENU
    window1.mainloop()

start = MAIN()
