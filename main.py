import csv
import random
from os import system, name
from time import  sleep

class Score:
    final_score = 0
    status = None
    wrong = 0
    correct = 0
    remain = 5

    def calculate_score(self, check):
        if check == 1:
            Score.final_score += 10
            Score.correct += 1
            Score.remain -= 1
        elif check == 3:
            Score.final_score -= 3
            Score.wrong += 1
            Score.remain -= 1
        elif csv == 2:
            Score.wrong += 1
            Score.remain -= 1
        return Score.final_score

    def check_win(self):
        if self.calculate_score(Score.final_score) >= 40:
            Score.status = "Win :)))))"
            print(Score.status)
        else:
            Score.status = "game Over :////"
            print(Score.status)

    def __add__(self, other):
        Score.final_score += other
        return Score.final_score

    def __sub__(self, other):
        Score.final_score += other
        return Score.final_score

    def show_status(self):
        print(
            f" Correct\t Wrong \t Score \t Remaining \n {Score.correct} \t\t\t {Score.wrong} \t\t\t {Score.final_score}\t\t\t{Score.remain}")


class Quiz(Score):
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer



    def check_answer(self, answer_user):

        if answer_user == self.answer:
            print("Correct Answer")
            return 1

        elif answer_user == '':
            print(" Wrong Answer")
            return 2
        else:
            print(" Wrong Answer")
            return 3

    def __str__(self):
        return f"{self.question}"

    @staticmethod
    def save_in_file(d):
        with open("test.csv", "a") as save_file:
            writer = csv.DictWriter(save_file, d.__dict__.values())
            writer.writeheader()


class TrueFalse(Quiz):

    def __str__(self):
        return f"Question No.1\t{self.question}"

    def check_answer(self, answer_user):
        if answer_user == self.answer:
            print("Correct Answer")
            return 1

        elif answer_user == '':
            print(" Wrong Answer")
            return 2
        elif answer_user != "1" or answer_user != "2":
            print(" type  1 or 2")
            return 3


class ShortAnswer(Quiz):
    def __str__(self):
        return f"Question No.2\t{self.question}"


class MultipleChoice(Quiz):
    def __str__(self):
        return f"Question No.3\t{self.question}"

    def check_answer(self, answer_user):
        if answer_user == self.answer:
            print("Correct Answer")
            return 1

        elif answer_user == '':
            print(" Wrong Answer")
            return 2
        elif answer_user != "1" or answer_user != "2" or answer_user != "3" or answer_user != "4":
            print(" type  1 or 2 or 3 or 4")
            return 3


q1 = {"The Atlantic Ocean is the largest ocean on the planet \n 1.True \n 2.False": "2",
      "The study of stars is called astronomy \n 1.True \n 2.False": "1",
      "Protons have a positive charge, whereas electrons have a negative.\n 1.True \n 2.False": "1",
      "You cannot cry in space\n 1.True \n 2.False": "1"}

q2 = {"In which direction does the sun rise? ": "east",
      "Who was the first man to walk on the moon? ": "neil",
      "Which is the longest river on the earth? ": "nile",
      "What do you call the person who brings a letter to your home from post office?": "postman",
      "How many days do we have in a week?": "seven"}

q3 = {"What orange vegetable do rabbits like to eat? \n 1.Carrots 2.Broccoli 3.Oranges 4.apple": "1",
      "What sea creature has 8 legs?\n 1.An octopus 2. A dolphin 3. A crocodile 4.fish": "1",
      "What color is a banana? \n 1. Red 2. Yellow 3. White 4.orange": "2",
      }


def clear():
   clean= system('cls')

def all_func(d):
    d.save_in_file(d)
    print(d)
    n = input("enter answer").lower().replace(" ", "")
    result = d.check_answer(n)
    d.calculate_score(result)
    d.show_status()
    sleep(3)
    clear()



for i in range(0, 2):
    a = random.choice(list(q1.keys()))
    b = TrueFalse(a, q1[a])
    all_func(b)



for i in range(0, 2):
    a = random.choice(list(q2.keys()))
    b = ShortAnswer(a, q2[a])
    all_func(b)


a = random.choice(list(q3.keys()))
b = MultipleChoice(a, q3[a])
all_func(b)
b.check_win()





