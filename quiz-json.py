from tkinter import *
import json
import pandas
from openpyxl.styles.builtins import comma
current_quest_num = 0
prev_question_num = 0
max_quiz_list_size = 0
correct_answer = 0
selected_answer = 0
last_selected_answer = 0
total_score = 0

class main_window:


    def __init__(self, window):
        self.window = window
        self.create_main_window()

    def go_back(self):
        global current_quest_num
        global last_selected_answer
        global selected_answer

        last_selected_answer = 0
        selected_answer = 0

        print("go back button pressed")
        if (current_quest_num <= 0):
            current_quest_num = 0
        else:
            current_quest_num -= 1

        print("current qn: ", current_quest_num)

        '''Clean the last window'''
        self.math_frame.destroy()
        self.math_frame0.destroy()
        self.math_frame1.destroy()
        self.math_frame2.destroy()

        self.play_math_question()


    def go_next(self):
        global current_quest_num
        global max_quiz_list_size
        global last_selected_answer
        global selected_answer

        last_selected_answer = 0
        selected_answer = 0

        print("go next button clicked")
        current_quest_num += 1
        print("current qn: ", current_quest_num)

        '''Clean the last window'''
        self.math_frame.destroy()
        self.math_frame0.destroy()
        self.math_frame1.destroy()
        self.math_frame2.destroy()

        '''point to the last question'''
        if (current_quest_num >= max_quiz_list_size):
            current_quest_num -= 1

        #self.math_frame1.grab_release()

        self.play_math_question()

    def submit_answer(self):
        global current_quest_num
        global correct_answer

        print("submit answer button clicked")
        print("current qn: ", current_quest_num)

    def get_selected_answer(self):
        global current_quest_num
        global max_quiz_list_size
        global selected_answer
        global last_selected_answer
        global correct_answer
        global prev_question_num
        global total_score

        change_of_option = 0

        print("selected answer is:", selected_answer.get(), "correct ans: ", correct_answer)
        print("Selected answer type: ", type(selected_answer))
        print("correct answer type: ", type(correct_answer))

        self.result_lbl = Label(self.math_frame2, text="",
                                font=("times", 16, "bold"))
        self.result_lbl.place(x=100, y=100)


        '''score display'''
        self.score_lbl = Label(self.math_frame2, text="Score: ",font=("times", 16, "bold"), fg="black")
        self.score_lbl.place(x=500, y=150)

        if(last_selected_answer != 0):
            if(last_selected_answer == selected_answer.get()):
                return
            else:
                change_of_option = 1

        if(selected_answer.get() == correct_answer):
            #self.result_lbl = Label(self.math_frame2, text="CORRECT answer !!! Good Job", fg="green",
             #                       font=("times", 16, "bold"))
            self.result_lbl.config(text="CORRECT ANSWER  !! WELL DONE", fg="green")
            #self.result_lbl.place(x=100, y=100)
            if(prev_question_num != current_quest_num):
                total_score += 1
            else:
                if(change_of_option == 1):
                    total_score += 1

            print("score: ", total_score, "/", max_quiz_list_size)
        else:
            #self.result_lbl = Label(self.math_frame2, text="WRONG answer !, Try one more time", fg="red",
             #                       font=("times", 16, "bold"))
            self.result_lbl.config(text="     WRONG ANSWER !!!  TRY AGAIN", fg="red")
            #self.result_lbl.place(x=100, y=100)
            #if (prev_question_num != current_quest_num):
             #   total_score -= 1
            #else:
            if(change_of_option == 1 and total_score != 0):
                total_score -= 1

        self.score_val = Label(self.math_frame2, text=f"{total_score}/{max_quiz_list_size}", font=("times", 16, "bold"), fg="black")
        self.score_val.place(x=650, y=150)

        print("score: ", total_score, "/", max_quiz_list_size)

        print("last qn num: ", prev_question_num, "current qn num: ", current_quest_num)
        print("last sel answer:", last_selected_answer, "selected answer:", selected_answer.get())

        prev_question_num = current_quest_num
        last_selected_answer = selected_answer.get()

        '''Disable the option radio buttons'''
        self.opt1.configure(state="disabled")
        self.opt2.configure(state="disabled")
        self.opt3.configure(state="disabled")
        self.opt4.configure(state="disabled")




    def play_math_question(self):
        global current_quest_num
        global max_quiz_list_size
        global correct_answer
        global selected_answer


        print("play math question")


        self.Tool_Bar.destroy()
        self.math_quiz_button.destroy()
        self.eng_quiz_button.destroy()
        self.sci_quiz_button.destroy()



        with open('quiz.json') as f:
            quiz_list = json.load(f)

        #for item in quiz_list['quiz']:
        item = quiz_list["quiz"]

        max_quiz_list_size = len(quiz_list["quiz"])

        print(item)
        print("current qn num: ", current_quest_num)
        print(item[current_quest_num]['Question'])
        print("list len of json:", len(quiz_list["quiz"]), "max quiz list size",  max_quiz_list_size)


        #type = item['Type']
        option1 = item[current_quest_num]['Option1']
        option2 = item[current_quest_num]['Option2']
        option3 = item[current_quest_num]['Option3']
        option4 = item[current_quest_num]['Option4']
        correct_answer = item[current_quest_num]['Answer']
        print("correct answer: ", correct_answer)

        self.math_frame = Frame(self.window, height=100, width=1000, bd=2, relief=GROOVE)
        self.math_frame.pack()
        self.math_frame.propagate(0)

        math_title = Label(self.math_frame, text="Mathematics questions", bg="green", fg="white",
                           font=("times", 25, "bold"))
        math_title.place(x=250, y=5)

        self.math_frame0 = Frame(self.window, height=100, width=1000, bd=2, relief=GROOVE)
        self.math_frame0.pack() #question
        self.question = Label(self.math_frame0, text=f"{item[current_quest_num]['Question']}", fg="black",
                              font=("times", 16, "bold"))
        self.question.place(x=10, y=10)


        self.math_frame1 = Frame(self.window, height=200, width=1000, bd=2, relief=GROOVE)
        self.math_frame1.pack() #options with radio button

        selected_answer = IntVar()
        self.opt1 = Radiobutton(self.math_frame1, text=f"{item[current_quest_num]['Option1']}",
                           font=("times", 20, "bold"), value=1, variable=selected_answer,
                           command=self.get_selected_answer)
        self.opt1.place(x=20, y=5)
        #opt1.deselect()

        self.opt2 = Radiobutton(self.math_frame1, text=f"{item[current_quest_num]['Option2']}",
                           font=("times", 20, "bold"), value=2, variable=selected_answer,
                           command=self.get_selected_answer)
        self.opt2.place(x=20, y=100)
        #opt2.deselect()

        self.opt3 = Radiobutton(self.math_frame1, text=f"{item[current_quest_num]['Option3']}",
                           font=("times", 20, "bold"), value=3, variable=selected_answer,
                           command=self.get_selected_answer)
        self.opt3.place(x=600, y=5)
        #opt3.deselect()

        self.opt4 = Radiobutton(self.math_frame1, text=f"{item[current_quest_num]['Option4']}",
                           font=("times", 20, "bold"), value=4, variable=selected_answer,
                           command=self.get_selected_answer)
        self.opt4.place(x=600, y=100)
        #opt4.deselect()


        #Buttons
        self.math_frame2 = Frame(self.window, height=200, width=1000, bd=2, relief=GROOVE)
        self.math_frame2.pack() #submit, next, prev button

        '''
        submit_btn = Button(self.math_frame2, text="Submit", bg="green", fg="white", height=1, width=10,
                            font=("times", 20, "bold"), command=self.submit_answer)
        submit_btn.place(x=400, y=10)
        '''

        back_btn = Button(self.math_frame2, text="Back", bg="green", fg="white", height=1, width=10,
                            font=("times", 20, "bold"), command=self.go_back)
        back_btn.place(x=10, y=10)

        next_btn = Button(self.math_frame2, text="Next", bg="green", fg="white", height=1, width=10,
                            font=("times", 20, "bold"), command=self.go_next)
        next_btn.place(x=800, y=10)


        '''Label that shows the result and the score
        self.result_lbl = Label(self.math_frame2, text="correct/Incorrect", fg="black",
                                font=("times", 16, "bold"))
        self.result_lbl.place(x=100, y=100)
        '''



    def create_main_window(self):
        self.Tool_Bar = Frame(self.window, height=70, width=800, bd=2, bg="lightgreen", relief=GROOVE)
        self.Tool_Bar.pack()
        self.Title = Label(self.Tool_Bar, text="Quiz Application", font=("arial", 22), bg="lightgreen")
        self.Title.place(x=20, y=13)

        self.math_quiz_button = Button(self.window, text="Mathematics", font=("arial", 15), bg="lightpink", command=self.play_math_question)
        self.math_quiz_button.place(x=20, y=113)

        self.sci_quiz_button = Button(self.window, text="science", font=("arial", 15))
        self.sci_quiz_button.place(x=220, y=113)

        self.eng_quiz_button = Button(self.window, text="English", font=("arial", 15))
        self.eng_quiz_button.place(x=350, y=113)

        #self.recent_quiz = Frame(self.window, height=500, width=800, bd=2, bg="lightgreen")
        #self.recent_quiz.pack()
        #self.rerecent_quiz()



window = Tk()
window.geometry('1000x700')
window.resizable(False, False)

window.title("LP Quiz")

main_window(window)


#current_quest_num = 0

'''
#convert excel file to json
excel_data_df = pandas.read_excel('quiz.xlsx')
json_str = excel_data_df.to_json(orient='records')
print("Excel to JSON:", json_str)

with open("quiz123.json", "w", encoding="utf-8") as f:
    json.dump(json_str, f)
'''
'''
with open('quiz.json') as f:
    quiz_list = json.load(f)
    #print(quiz_list)
    #print(type(quiz_list['quiz']))


for item in quiz_list['quiz']:
    current_quest_num += 1
    print("Current quest num ", current_quest_num)
    print(item)
    question = item['Question']
    type = item['Type']
    option1 = item['Option1']
    option2 = item['Option2']
    option3 = item['Option3']
    option4 = item['Option4']
    #answer = item['Answer']

    print(question)
    print(type)
    print(option1)
    print(option2)
    print(option3)
    print(option4)
    #print(answer)
'''




window.mainloop()
