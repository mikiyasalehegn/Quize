import pyodbc
from tkinter import *


class Store:
    """This class consists of functions that will keep winners data on the national lottery institute's database"""
    def __init__(self):
        super().__init__()
        self.Score = 0
        self.total_question = 5
        self.question_num = 1
        self.window = Tk()
        self.window.config(padx=25, pady=25, bg="#4D5656")
        self.window.title("Trivia Game")
        self.frame = Frame()
        self.window.geometry("900x300")
        self.score = Label(self.window)
        self.val1 = IntVar()
        self.val2 = IntVar()
        self.val3 = IntVar()
        self.choose = IntVar()
        self.first_screen = Frame()
        self.question = ['animals', 'history', 'geography', 'astronomy', 'maths']
        self.questions = []
        self.answers = []
        self.options = []
        self.category = Entry(self.first_screen, textvariable=self.choose, width=15)
        self.connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL '
                                         'Server};SERVER=MIKE;DATABASE=Lotto;Trusted_Connection=yes;')

        self.cursor = self.connection.cursor()
        self.table = "animals"

    def ask(self):
        self.cursor.execute(f"Select questions from "+self.question[int(self.category.get()) - 1]+"")

        while 1:
            row = self.cursor.fetchone()
            if not row:
                break
            for i in row:
                self.questions.append(i)

    def ops(self):
        self.cursor.execute(f"Select options from "+self.question[int(self.category.get()) - 1]+"")

        while 1:
            row = self.cursor.fetchone()
            if not row:
                break
            for i in row:
                self.options.append(i.split(","))

    def ans(self):
        self.cursor.execute(f"Select answers from "+self.question[int(self.category.get()) - 1]+"")

        while 1:
            row = self.cursor.fetchone()
            if not row:
                break
            for i in row:
                self.answers.append(int(i))

        self.cursor.close()
        self.connection.close()

