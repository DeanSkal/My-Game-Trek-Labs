print("Welcome to my project")
total_questions = 2
Password = "Bean"

answer = input("Is your name Dean? (yes/no): ")
if answer.lower() == 'yes':
    print ('You may continue')
elif answer.lower() == 'no':
    print ('You should not be here')
else:
    print ('You should not be here')
if answer.lower() == 'yes':
    answer = input("What is the password: ")
    if Password == answer:
        print ('Welcome to my project')
    elif answer.lower() =='bean':
        print('Welcome to my project')
    else:
        print ('you liar')