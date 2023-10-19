# Hey Everyone....Welcome to my first ever Quiz Game...

print("Hey Friends!!! Let's check your knowledge")

questions=("Which one is not a legal variable name?",
           "Which is the correct file extension for Python files?",
           "Which operator is used to multiply numbers?",
           "Which type of programming does python support?",
           "What will be the value of this Python expression?  4+3%5 ")

options=(("A. _myvar","B. my_var","C. my-var","D. Myyvar"),
         ("A. pyth","B. .py","C. .pt","D. .pyt"),
         ("A. %","B. *","C. x","D. #"),
         ("A. Object-oriented programming","B. Structured programming","C. Functional programming","D. all of the mentioned"),
         ("A. 7","B. 2","C. 4","D. 1"))

answers=("D","B","B","D","A")
guesses=[]
score=0
question_num=0

for question in questions:
    print("---------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess=input("Enter(A,B,C,D):").upper()
    guesses.append(guess)
    if guess==answers[question_num]:
        score+=1
        print("That's Correct!!!")
    else:
        print("Oops..That's Incorrect!!!")
        print(f"{answers[question_num]} is the correct answer")
    question_num+=1
print("-----------------------")
print("--------Results--------")

print("answers: ",end="")
for answer in answers:
    print(answer,end="")
print()

print("guesses: ",end="")
for guess in guesses:
    print(guess,end="")
print()

score=score/len(questions*100)
print(f"Your score is:{score}%")

print("Thanks for Playing!!")