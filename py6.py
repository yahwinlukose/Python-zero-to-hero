questions=("What is my name? ",
           "What is my age? ",
           "What is my country?",
           "What is my hobby?",
           "What is my favourite food?")
options=(("A.yahwin","B.lukose","C.Ram"),
            ("A.20","B.21","C.22"),
            ("A.india","B.usa","C.uk"),
            ("A.coding","B.reading","C.singing"),
            ("A.pizza","B.biriyani","C.chocolate"))
answers=("A","C","A","A","B")
guess=[]
score=0
question_num=0
for question in questions:
    print("--------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    user_answer=input("Enter your answer (A, B, C): ").upper()
    guess.append(user_answer)
    if user_answer==answers[question_num]:
        score+=1
        print("Correct answer!")
    else:
        print(f"Wrong answer! The correct answer is {answers[question_num]}")
    question_num+=1
print("--------------------")
print("Results")
for answer in answers:
    print(answer,end=" ")

for gue in guess:
    print(gue,end=" ")     
print(f"\nYour score is {score}/{len(questions)}")
percentage=(score/len(questions))*100       
print(f"Your percentage is {percentage}%")