print("Welcome to my project")
total_questions = 3
Password = "Bean"
Password2 = "Lapa"
Password3 = ""

answer = input("Is your name Dean? (yes/no): ")
if answer.lower() == 'yes':
    print ('You may continue')
elif answer.lower() == 'no':
    print ('You should not be here')
else:
    print ('You should not be here')
print ('')
if answer.lower() == 'yes':
    answer = input("What is the password: ")
    if Password == answer:
        print ('You may continue')
    elif answer.lower() =='bean':
        print('You may continue')
    else:
        print ('you liar')

    if Password == answer:
        print ('')
        answer = input("What is the second password: ")
        if Password2 == answer:
            print('Welcome to my project')
        elif answer.lower() == 'lapa':
            print('Welcome to my project')
        else:
            print('you very smart liar')
    elif answer.lower() == 'bean':
        print('')
        answer = input("What is the second password: ")
        if Password2 == answer:
            print('You may continue')
        elif answer.lower() == 'lapa':
            print('You may continue')
        else:
            print('you very smart liar')




