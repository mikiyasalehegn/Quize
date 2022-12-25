from utilities import *


class Quiz(Store):
    def index(self):
        self.first_screen.place_forget()
        self.ask()
        self.ops()
        self.ans()
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

        next_button = Button(self.frame, text="Next", command=self.nextt)
        next_button.pack(side="bottom")

        # home_button = Button(self.frame, text="Home", command=self.back)
        # home_button.pack(side="bottom")

        score = Label(self.window)
        score.place_forget()

    def nextt(self):
        if self.val1.get() == 1:
            self.selected_option = 1
        elif self.val2.get() == 1:
            self.selected_option = 2
        elif self.val3.get() == 1:
            self.selected_option = 3
        else:
            self.selected_option = -1
        if self.answers[self.question_num - 1] == self.selected_option:
            self.correct_ans.pack(side="top")
            self.correct_ans.config(text="Correct", bg="#008000", width=10)
            self.Score += 1
        elif self.answers[self.question_num - 1] != self.selected_option:
            self.correct_ans.pack(side="top")
            self.correct_ans.config(text="Wrong", bg="#FF0000", width=10)
        self.question_num += 1
        if self.question_num > self.total_question:
            self.show_score()
            self.correct_ans.destroy()
            self.frame.place_forget()
        else:
            self.show_score()
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
        self.frame.pack_forget()
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


