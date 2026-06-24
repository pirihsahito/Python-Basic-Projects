# Created a program capable of displaying questions to the User like KBC

question1 = ["What is capital of Pakistan?", 'Karachi', 'Lahore', 'Islamabad', 'Multan', 'Islamabad']
question2 = ["Who is Prime Minister of Pakistan?", 'Imran Khan', 'Asim Munir', 'Maryam Nawaz', 'Shehbaz Sharif', 'Shehbaz Sharif']
question3 = ["Which is national game of Pakistan?", 'Cricket', 'Hockey', 'Football', 'Tennis', 'Hockey']
question4 = ["Which is oldest language spoken in Pakistan?", 'Sindhi', 'Panjabi', 'Pashto', 'Balochi', 'Sindhi']
question5 = ["What is capital of Sindh?", 'Hyderabad', 'Sukkur', 'Karachi', 'Khairpur Mirs', 'Karachi']

levels = [1000, 2000, 3000, 4000, 5000]

money = 0
questions = [question1, question2, question3, question4, question5]
for i, q in enumerate(questions):
    print(f"Question for Rs. {levels[i]}:", q[0])
    print("(a)", q[1])
    print("(b)", q[2])
    print("(c)", q[3])
    print("(d)", q[4])
    print("Write correct Answer:")
    ans = input()
    if(ans.lower() == q[5].lower()):
        print("Congrats Your Answer is Correct")
        money += levels[i]
        print("You have WON Rs.")
    else:
        print("Ops! Answer is Wrong")
        break
print("GAME OVER! You are taking home Rs.", money)