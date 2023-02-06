# Game to test accuracy and speed in identifying characters from a list
# Status: works
# to add: make .exe, pictures, sort out hotkey thing, refactor button funtions

from tkinter import *
from random import randint
from time import perf_counter
from playsound import playsound
from PIL import ImageTk, Image

start_time = None

root = Tk()
root.title("数字游戏")
root.iconbitmap("shu3.ico")
current_q = "Ready?"
Questions_asked = -1
Correct_answers = 0

#dragon = Image.open("DALL·E 2022-10-04 00.01.54 - chinese dragon of jade coiled up flying out of the screen, digital art.png")
#dragon = dragon.resize((300, 300))
#dragon = ImageTk.PhotoImage(dragon)
#
#Background_image = Label(root, image=dragon)
#Background_image.place(x=0, y=100)

Question = Label(root, text=current_q, font=("Arial", 40), pady = 20)
Question.grid(row=0, column=0, columnspan=3)
questions = ["一", "二", "三", "四", "五", "六", "七", "八", "九"]
#questions = ["uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
answers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
Test_length = 20


def end_test():
    Button_1.config(state = DISABLED)
    Button_2.config(state = DISABLED)
    Button_3.config(state = DISABLED)
    Button_4.config(state = DISABLED)
    Button_5.config(state = DISABLED)
    Button_6.config(state = DISABLED)
    Button_7.config(state = DISABLED)
    Button_8.config(state = DISABLED)
    Button_9.config(state = DISABLED)
    Score_label.config(text=str(Correct_answers)+ " of "+ str(Questions_asked))
    percentage = 100*Correct_answers/Questions_asked
    Question.config(text = str(round(percentage, 1))+"%")
    Time_label.config(text="time: "+str(round(perf_counter()-start_time, 2))+"s")
    playsound("success-fanfare-trumpets-6185.mp3")


def reset_all():
    Button_1.config(state = NORMAL)
    Button_2.config(state = NORMAL)
    Button_3.config(state = NORMAL)
    Button_4.config(state = NORMAL)
    Button_5.config(state = NORMAL)
    Button_6.config(state = NORMAL)
    Button_7.config(state = NORMAL)
    Button_8.config(state = NORMAL)
    Button_9.config(state = NORMAL)
    global current_q
    global Questions_asked
    global Correct_answers
    global start_time
    current_q = "Ready?"
    Questions_asked = -1
    Correct_answers = 0
    start_time = None
    Question.config(text = current_q)
    Time_label.config(text="Press any button to begin")
    Score_label.config(text=str(Correct_answers)+ " of "+ str(Questions_asked))

def reset_q():
    global start_time
    global Questions_asked
    global Correct_answers
    global current_q
    new_q = randint(0, len(questions)-1)
    if current_q != questions[new_q]:
        current_q = questions[new_q]
    else:
        current_q = questions[(new_q + 1)%9]
    Question.config(text = current_q)
    Score_label.config(text=str(Correct_answers)+ " of "+ str(Questions_asked))
    if start_time is None:
        start_time = perf_counter()
    Time_label.config(text="time: "+str(round(perf_counter()-start_time, 2))+"s")

def Press_1():
    global Questions_asked
    global Correct_answers
    global current_q
    Questions_asked += 1
    if current_q != "Ready?":
        if current_q == questions[0]:
            Correct_answers += 1
            playsound("snd_fragment_retrievewav-14728 (mp3cut.net).mp3")
        else:
            playsound("trumpet-e4-14829 - Copy (mp3cut.net).mp3")
    if Questions_asked < Test_length:
        reset_q()
    else:
        end_test()


def Press_2():
    global Questions_asked
    global Correct_answers
    global current_q
    Questions_asked += 1
    if current_q != "Ready?":
        if current_q == questions[1]:
            Correct_answers += 1
            playsound("snd_fragment_retrievewav-14728 (mp3cut.net).mp3")
        else:
            playsound("trumpet-e4-14829 - Copy (mp3cut.net).mp3")
    if Questions_asked < Test_length:
        reset_q()
    else:
        end_test()

def Press_3():
    global Questions_asked
    global Correct_answers
    global current_q
    Questions_asked += 1
    if current_q != "Ready?":
        if current_q == questions[2]:
            Correct_answers += 1
            playsound("snd_fragment_retrievewav-14728 (mp3cut.net).mp3")
        else:
            playsound("trumpet-e4-14829 - Copy (mp3cut.net).mp3")
    if Questions_asked < Test_length:
        reset_q()
    else:
        end_test()

def Press_4():
    global Questions_asked
    global Correct_answers
    global current_q
    Questions_asked += 1
    if current_q != "Ready?":
        if current_q == questions[3]:
            Correct_answers += 1
            playsound("snd_fragment_retrievewav-14728 (mp3cut.net).mp3")
        else:
            playsound("trumpet-e4-14829 - Copy (mp3cut.net).mp3")
    if Questions_asked < Test_length:
        reset_q()
    else:
        end_test()

def Press_5():
    global Questions_asked
    global Correct_answers
    global current_q
    Questions_asked += 1
    if current_q != "Ready?":
        if current_q == questions[4]:
            Correct_answers += 1
            playsound("snd_fragment_retrievewav-14728 (mp3cut.net).mp3")
        else:
            playsound("trumpet-e4-14829 - Copy (mp3cut.net).mp3")
    if Questions_asked < Test_length:
        reset_q()
    else:
        end_test()

def Press_6():
    global Questions_asked
    global Correct_answers
    global current_q
    Questions_asked += 1
    if current_q != "Ready?":
        if current_q == questions[5]:
            Correct_answers += 1
            playsound("snd_fragment_retrievewav-14728 (mp3cut.net).mp3")
        else:
            playsound("trumpet-e4-14829 - Copy (mp3cut.net).mp3")
    if Questions_asked < Test_length:
        reset_q()
    else:
        end_test()

def Press_7():
    global Questions_asked
    global Correct_answers
    global current_q
    Questions_asked += 1
    if current_q != "Ready?":
        if current_q == questions[6]:
            Correct_answers += 1
            playsound("snd_fragment_retrievewav-14728 (mp3cut.net).mp3")
        else:
            playsound("trumpet-e4-14829 - Copy (mp3cut.net).mp3")
    if Questions_asked < Test_length:
        reset_q()
    else:
        end_test()

def Press_8():
    global Questions_asked
    global Correct_answers
    global current_q
    Questions_asked += 1
    if current_q != "Ready?":
        if current_q == questions[7]:
            Correct_answers += 1
            playsound("snd_fragment_retrievewav-14728 (mp3cut.net).mp3")
        else:
            playsound("trumpet-e4-14829 - Copy (mp3cut.net).mp3")
    if Questions_asked < Test_length:
        reset_q()
    else:
        end_test()

def Press_9():
    global Questions_asked
    global Correct_answers
    global current_q
    Questions_asked += 1
    if current_q != "Ready?":
        if current_q == questions[8]:
            Correct_answers += 1
            playsound("snd_fragment_retrievewav-14728 (mp3cut.net).mp3")
        else:
            playsound("trumpet-e4-14829 - Copy (mp3cut.net).mp3")    
    if Questions_asked < Test_length:
        reset_q()
    else:
        end_test()


Button_1= Button(root, text="1", command = Press_1, font=("Arial", 20), padx = 20, pady = 20)
Button_2= Button(root, text="2", command = Press_2, font=("Arial", 20), padx = 20, pady = 20)
Button_3= Button(root, text="3", command = Press_3, font=("Arial", 20), padx = 20, pady = 20)

Button_4= Button(root, text="4", command = Press_4, font=("Arial", 20), padx = 20, pady = 20)
Button_5= Button(root, text="5", command = Press_5, font=("Arial", 20), padx = 20, pady = 20)
Button_6= Button(root, text="6", command = Press_6, font=("Arial", 20), padx = 20, pady = 20)

Button_7= Button(root, text="7", command = Press_7, font=("Arial", 20), padx = 20, pady = 20)
Button_8= Button(root, text="8", command = Press_8, font=("Arial", 20), padx = 20, pady = 20)
Button_9= Button(root, text="9", command = Press_9, font=("Arial", 20), padx = 20, pady = 20)

Button_1.grid(row=3, column=0)
Button_2.grid(row=3, column=1)
Button_3.grid(row=3, column=2)

Button_4.grid(row=2, column=0)
Button_5.grid(row=2, column=1)
Button_6.grid(row=2, column=2)

Button_7.grid(row=1, column=0)
Button_8.grid(row=1, column=1)
Button_9.grid(row=1, column=2)

#root.wm_attributes('-transparentcolor', root['bg'])

Button_reset = Button(root, text= "Reset", command = reset_all)
Button_reset.grid(row=6, column=0)

Score_label = Label(root, text=str(Correct_answers)+ " of "+ str(Questions_asked), justify="center")
Score_label.grid(row=4, column = 0, columnspan = 3)

Time_label = Label(root, text="Press any button to begin", justify = "center")
Time_label.grid(row=5, column = 0, columnspan = 3)


def Press1(whyDoIHaveToDoItLikeThis):    Press_1()
def Press2(whyDoIHaveToDoItLikeThis):    Press_2()
def Press3(whyDoIHaveToDoItLikeThis):    Press_3()
def Press4(whyDoIHaveToDoItLikeThis):    Press_4()
def Press5(whyDoIHaveToDoItLikeThis):    Press_5()
def Press6(whyDoIHaveToDoItLikeThis):    Press_6()
def Press7(whyDoIHaveToDoItLikeThis):    Press_7()
def Press8(whyDoIHaveToDoItLikeThis):    Press_8()
def Press9(whyDoIHaveToDoItLikeThis):    Press_9()

root.bind('1', Press1)
root.bind('2', Press2)
root.bind('3', Press3)
root.bind('4', Press4)
root.bind('5', Press5)
root.bind('6', Press6)
root.bind('7', Press7)
root.bind('8', Press8)
root.bind('9', Press9)

root.mainloop()