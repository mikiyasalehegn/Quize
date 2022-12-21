from utilities import *


class Quiz(Store):
    def index(self):
        self.ask()
        self.ops()
        self.ans()
        self.first_screen.place_forget()
        self.frame.place(relx=.5, rely=.5, anchor=CENTER,)
        self.question = Label(self.frame, width=65, font="Arial, 15",
                              text=self.questions[0])
        self.option1 = Checkbutton(self.frame, variable=self.val1,
                                   text=self.options[0][0], font=1,
                                   command=lambda: self.check(1))
        self.option2 = Checkbutton(self.frame, variable=self.val2,
                                   text=self.options[0][1], font=1,
                                   command=lambda: self.check(2))
        self.option3 = Checkbutton(self.frame, variable=self.val3,
                                   text=self.options[0][2], font=1,
                                   command=lambda: self.check(3))
        self.question.pack()
        self.option1.pack(padx=60)
        self.option2.pack(padx=60)
        self.option3.pack(padx=60)

        next_button = Button(self.frame, text="next", command=self.nextt)
        next_button.pack()

        score = Label(self.window)
        score.place_forget()

    def nextt(self):
        if self.val1.get() == 1:
            selected_option = 1
        elif self.val2.get() == 1:
            selected_option = 2
        elif self.val3.get() == 1:
            selected_option = 3
        else:
            selected_option = -1
        if self.answers[self.question_num - 1] == selected_option:
            self.Score += 1
        self.question_num += 1
        if self.question_num > self.total_question:
            self.frame.place_forget()
            self.score.place(relx=.5, rely=.5, anchor=CENTER)
            self.score.config(text="Score: " + str(self.Score))
        else:
            self.val1.set(0)
            self.val2.set(0)
            self.val3.set(0)
            self.question.config(text=self.questions[self.question_num - 1])
            self.option1.config(text=self.options[self.question_num - 1][0])
            self.option2.config(text=self.options[self.question_num - 1][1])
            self.option3.config(text=self.options[self.question_num - 1][2])

    def check(self, option):
        if option == 1:
            self.val2.set(0)
            self.val3.set(0)
        elif option == 2:
            self.val1.set(0)
            self.val3.set(0)
        elif option == 3:
            self.val1.set(0)
            self.val2.set(0)

    def select(self):
        self.first_screen.place(relx=.5, rely=.5, anchor=CENTER)

        lable_1 = Label(self.first_screen,
                           text="Welcome to Trivia Game!", font="Arial, 15", relief="sunken", bd=1, width=60, justify="left")
        lable_2=Label(self.first_screen,text='\n\t1.Animals\n\t2.History\n\t3.Geography\n\t4.Astronomy\n\t5.Maths',
                      bd=1, relief="sunken", font="Times 20", justify="left", width=20, padx=5)
        lable_1.pack(side="top")
        lable_2.pack()
        self.category.pack()
        self.play_b = Button(self.first_screen, text="Play", command=self.index)
        self.play_b.pack()
        self.window.mainloop()
