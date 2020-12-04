import sqlite3
import csv
import os
import keyboard
import time
import pandas as pd
import threading
from tkinter import *
import shutil
import bcrypt
import getpass as gp
#goto function to see any problem at any particular time
def goto():
    i = int(input('which question you want to go: '))
    os.system("cls" if os.name == "nt" else "clear")
    with open(r'./quiz_wise_questions/'+num+'.csv', 'r') as file:
        reader = csv.reader(file)
        row = list(reader)
        print("Roll No- ", rollno)
        print("Name- ", Name)
        print("Goto Question: (Press - Ctrl+Alt+g)")
        print("Final Submit: (Press Ctrl+Alt+f)")
        print("Export Database Into CSV: (Press Ctrl+Alt+e)")
        print("Ques No ", row[i][0], sep=':-')
        print(row[i][1], " ?")
        print("Option 1) ", row[i][2])
        print("Option 2) ", row[i][3])
        print("Option 3) ", row[i][4])
        print("Option 4) ", row[i][5])
        print("Credits if correct option: ", row[i][7])
        print("Negative Marking: ", row[i][8])
        print("Is Compulsory: ", row[i][9])
    print("Press esc to continue!!")
    pass
#Login function this function make allows you to login
def Login():
    participant = input("Enter your rollno: ")
    password = gp.getpass("Enter your password: ")
    hashedpassword = bytes(password, encoding="utf-8")
    c.execute("SELECT * FROM project1_registration WHERE roll=?", (participant,))
    lst = c.fetchall()
    if lst == []:
        print("Sorry you are not registered!")
        n = input("What you want to do now Register/Exit: ")
        if n == 'Resgiter':
            return Registration()
        else:
            exit(0)
    else:
        if lst[0][1] == participant and bcrypt.checkpw(hashedpassword, lst[0][2]):
            print("logged in!!")
        else:
            print("Invalid Username or Password")
            return Login()
    return participant

#Registration function this function make allows you to Register
def Registration():
    name = input("Enter your Name: ")
    roll = input("Enter Roll Number: ")
    passwd = gp.getpass("Enter your password: ")
    num = int(input("Enter WhatsApp Number: "))

    c.execute("SELECT * FROM project1_registration WHERE roll=?", (roll,))
    lst = c.fetchall()

    if(lst):
        print("You are already registered! Please Login!!")
        temp = int(input("Press 2 to Login and 1 to exit: "))
        if temp == 2:
            return Login()
        else:
            exit(0)
    hashedpassword = bytes(passwd, encoding="utf-8")
    hashed_pw = bcrypt.hashpw(hashedpassword, bcrypt.gensalt())
    c.execute("INSERT INTO project1_registration VALUES(?, ?, ?, ?)",
              (name, roll, hashed_pw, num))
    conn.commit()
    print("You are Registered!!")
    return roll


conn = sqlite3.connect('project1_quiz_cs384.db')
c = conn.cursor()

try:
    c.execute("""CREATE TABLE project1_registration (
                name text,
                roll text,
                password text,
                whatsappNumber integer
                )
            """)
except:
    pass


try:
    c.execute("""CREATE TABLE project1_marks (
                roll text,
                quiz_num text,
                marks integer
                )
            """)
except:
    pass

conn.commit()
Reg_log = int(input("Enter 1 to Register and 2 to Login: "))
rollno = None
if Reg_log == 1:
    rollno = Registration()
else:
    rollno = Login()


c.execute("SELECT * FROM project1_registration WHERE roll=?", (rollno,))
conn.close()


global terminator
terminator = 1



def extract_database(participant):
    con = sqlite3.connect("project1_quiz_cs384.db")
    c = con.cursor()
    c.execute("SELECT * FROM project1_marks WHERE roll=?", (participant,))
    lst = c.fetchall()
    header = ['Roll', 'quiz_num', 'marks']

    if os.path.isdir(r'./quiz_wise_responses/'):
        shutil.rmtree(r'./quiz_wise_responses/')
    os.mkdir(r'./quiz_wise_responses/')

    for tup in lst:
        if not os.path.isfile(r'./quiz_wise_responses/scores_'+tup[1]+'.csv'):
            with open(r'./quiz_wise_responses/scores_'+tup[1]+'.csv', 'w', newline="") as file:
                writer = csv.writer(file)
                writer.writerow(header)
        with open(r'./quiz_wise_responses/scores_'+tup[1]+'.csv', 'a+', newline="") as file:
            writer = csv.writer(file)
            writer.writerow(tup)


def quiz_submit():
    global terminator
    terminator = -1
    print("Quiz Submitted!!  Press esc to get results!")
    pass


def timer(t):
    global terminator
    root = Tk()
    root.geometry("300x80")
    root.title("Timeer")

    minute = StringVar()
    second = StringVar()

    minute.set("00")
    second.set("00")

    minuteEntry = Entry(root, width=3, font=(
        "Arial", 18, ""), textvariable=minute)
    minuteEntry.place(x=100, y=20)

    secondEntry = Entry(root, width=3, font=(
        "Arial", 18, ""), textvariable=second)
    secondEntry.place(x=150, y=20)

    while t > -1:
        if terminator == 0:
            print("Quiz Finished")
            break
        mins, secs = divmod(t, 60)
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))
        root.update()
        time.sleep(1)
        t -= 1
    terminator = 0


def start_quiz(rollno, Name):
    global terminator
    conn = sqlite3.connect('project1_quiz_cs384.db')
    c = conn.cursor()
    header = []
    lst = [1, 2, 3,4,5,6,7,8,9,10]
    Correct_Choices, Wrong_choices, Unattempted, Marks_Obtained, Total_Quiz_Marks = 0, 0, 0, 0, 0
    with open(r'./quiz_wise_questions/'+num+'.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if header == []:
                header = row
                header.pop()
                header.append("marked_choice")
                with open(r'./individual_responses/'+num+'_'+rollno+'.csv', 'w', newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow(header)
            else:
                print("Roll No- ", rollno)
                print("Name- ", Name)
                print('Unattempted questions- ', lst)
                print("Goto Question: (Press - Ctrl+Alt+g)")
                print("Final Submit: (Press Ctrl+Alt+f)")
                print("Export Database Into CSV: (Press Ctrl+Alt+e)")
                if terminator == 1:
                    print("Press esc to continue!")
                    keyboard.wait('esc')
                answer = -1
                if terminator == 1:
                    print("Ques No ", row[0], sep=':-')
                    print(row[1], " ?")
                    print("Option 1) ", row[2])
                    print("Option 2) ", row[3])
                    print("Option 3) ", row[4])
                    print("Option 4) ", row[5])
                    print("Credits if correct option: ", row[7])
                    print("Negative Marking: ", row[8])
                    print("Is Compulsory: ", row[9])
                    if row[9] == 'n':
                        answer = input("Enter choice [1/2/3/4/S]: S to Skip ")
                    else:
                        answer = input("Enter choice [1/2/3/4]: ")
                if terminator != 1:
                    answer = -1
                Total_Quiz_Marks += int(row[7])
                temp = row
                temp.pop()
                if answer == -1:
                    Unattempted += 1
                    temp.append("Not answered")
                elif answer != 'S':
                    temp.append(answer)
                    if int(answer) == int(row[6]):
                        Correct_Choices += 1
                        Marks_Obtained += int(row[7])
                    else:
                        Wrong_choices += 1
                        Marks_Obtained += int(row[8])
                    lst.remove(int(row[0]))
                else:
                    temp.append(answer)
                    Unattempted += 1
                with open(r'./individual_responses/'+num+'_'+rollno+'.csv', 'a+', newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow(temp)
                os.system("cls" if os.name == "nt" else "clear")
    if terminator == 0:
        print("Last response not submitted due to lack of time")
    if terminator != -1:
        print("Roll No- ", rollno)
        print("Name- ", Name)
        print('Unattempted questions- ', lst)
        print("Export Database Into CSV: (Press Ctrl+Alt+e)")
        print("Press esc to get results!")
        keyboard.wait('esc')
    terminator = 0
    additional_col = {
        "Total": [Correct_Choices, Wrong_choices,
                  Unattempted, Marks_Obtained, Total_Quiz_Marks],
        "Legend": ["Correct Choices", "Wrong Choices",
                   "Unattempted", "Marks Obtained", "Total Quiz Marks"]
    }
    new_df = pd.DataFrame(additional_col)
    df = pd.read_csv(r'./individual_responses/'+num+'_'+rollno+'.csv')
    df = pd.concat([df, new_df], axis=1)
    if os.path.isfile(r'./individual_responses/'+num+'_'+rollno+'.csv'):
        os.remove(r'./individual_responses/'+num+'_'+rollno+'.csv')
    df.to_csv(r'./individual_responses/'+num+'_'+rollno+'.csv', index=False)
    print("Total Quiz Questions: ", Correct_Choices+Wrong_choices+Unattempted)
    print("Total Quiz Questions Attempted: ", Correct_Choices+Wrong_choices)
    print("Total Correct Question Attempted: ", Correct_Choices)
    print("Total Wrong Questions Attempted: ", Wrong_choices)
    print(f'Total Marks: {Marks_Obtained}/{Total_Quiz_Marks}')
    try:
        c.execute(
            "DELETE from project1_marks WHERE roll=? AND quiz_num=?", (rollno, num))
        conn.commit()
        c.execute("INSERT INTO project1_marks VALUES(?, ?, ?)",
                  (rollno, num, Marks_Obtained))
        conn.commit()
    except:
        print("There is some Mistake!!")


keyboard.add_hotkey("ctrl+alt+f", quiz_submit)
keyboard.add_hotkey("ctrl+alt+e", extract_database, args=(rollno,))
keyboard.add_hotkey("ctrl+alt+g", goto)
conn = sqlite3.connect('project1_quiz_cs384.db')
c = conn.cursor()
c.execute("SELECT * FROM project1_registration WHERE roll=?", (rollno,))
Name = c.fetchall()[0][0]
num = str(
    input("Which quiz you want to take? q1/q2/q3 or press 0 to exit: "))
if num == '0':
    exit(0)
else:
    t1 = threading.Thread(target=timer, args=(1200,))
    t2 = threading.Thread(target=start_quiz, args=(rollno, Name,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
c.execute(
    "SELECT * FROM project1_marks WHERE roll=? AND quiz_num=?", (rollno, num))
conn.close()


