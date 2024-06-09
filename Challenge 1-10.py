#CHALLENGE 1
'''Write a program that:
• asks the user to input their age
• outputs 'Your age is: ' followed by their 
ag'''                   #You must use: Sequencing & Variables


user = int(input('Enter your age: '))
print("Your age is " + str(user) )


#CHALLENGE 2
'''Write a program that:
• asks the user to input two numbers 
• calculates the average 
• outputs the result'''             #You must use: Sequencing & Variables

first_number = float(input('Enter first number: '))
second_number = float(input('Enter second number: '))
average = first_number/second_number
print('Average = ' + str(average))



#CHALLENGE 3
'''Write a program that:
• asks the user to input the width and 
height of a rectangle
• calculates the area
• outputs the result'''         #You must use: Sequencing & Variables


width = float(input('Enter width: '))
height = float(input('Enter height: '))
area = width * height
print("Area = " + str(area))


#CHALLENGE 4
'''Write a program that:
• asks the user to input two numbers
• divides the first number by the second 
number
• outputs the result'''         #You must use: Sequencing & Variables


first_number = float(input('Enter first number: '))
second_number = float(input('Enter second number: '))
division = first_number/second_number
print('Answer = ' + str(division))



#CHALLENGE 5
'''Write a program that:
• asks the user their name
• asks what their favourite subject is 
(using their name in the question)
• responds to their answer by saying 
that you like that subject as well'''           #You must use: Sequencing & Variables


name = input('Enter your name: ')
subject = input(name +' enter your favourite subject: ')
print(name +' you like '+ subject + ' as well' )


#CHALLENGE 6
'''Write a program that:
• asks the user their name
• if it is the same as your name, outputs 
'You’re cool', otherwise outputs 'Nice 
to meet you'''              #You must use: Sequencing & Variables

name = input('Enter your name: ')
if name == 'Blessing':
    print('You’re cool')
else:
    print('Nice to meet you')


#CHALLENGE 7

'''Write a program that:
• asks the user how long on average 
they spend watching TV each day
• if it is less than 2 hours, outputs ‘That 
shouldn’t rot your brain too much’; if it 
is less than 4 hours per day, outputs 
‘Aren’t you getting square eyes?’; 
otherwise outputs ‘Fresh air beats 
channel flicking’'''            #You must use: Sequencing & Variables


tv_time = (input('Enter time spent on tv: '))
if tv_time < '2 hours':
    print('That shouldn\'t rot your brain much')
elif tv_time < '4 hours' :
    print('Aren\'t you getting square eyes?' )
else :
    print('you getting square eyes')


#CHALLENGE 8
'''Write a program that:
• converts and outputs marks into 
grades, using the following data:
Greater than or equal to 75 A
Greater than or equal to 60 B
Greater than or equal to 35 C
Less than 35 D'''               #You must use: Sequencing & Variables


grade = int(input('Enter grade: '))
if grade >= 75:
    print('Your grade is an A')
elif grade >= 60:
    print('Your grade is an B')
elif grade >= 35:
    print('Your grade is an C')
elif grade <= 35:
    print('Your grade is an D')


#CHALLENGE 9
'''Write a program that:
• asks the user to name one of the 
Olympic Values (Respect, Excellence 
and Friendship)
• if they correctly name one, output 
'That’s correct‘, otherwise output 'Try 
again'
'''             #You must use: Sequencing & Variables


Olympic_values = input('Pick an olympic value: ')
if Olympic_values == 'Respect' or Olympic_values == 'Excellence' or Olympic_values == 'Friendship':
    print('That’s correct')
else: 
    print('Try again')


#CHALLENGE 10

'''Write a game that:
• allows the user to play rock, paper, 
scissors against the computer
• must display the computer’s choice 
and show the result of the game'''          #You must use: Sequencing & Variables


print('------ROCK----PAPER----SCISSORS')

import random
options = ['rock', 'paper', 'scssors']
player = input('Pick an option: ')
computer = random.choice(options)
output = {'Player' : player, 'Computer' : computer}
print(output)
if player == computer:
    print('TIE !!!')
elif player == 'rock' and computer == 'scissors':
    print('You win')
elif player == 'paper' and computer == 'rock':
        print('You win')
elif player == 'scissors' and computer == 'paper':
     print('You win')
else: 
    print('You loose')
