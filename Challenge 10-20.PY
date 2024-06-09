 # CHALLENGE 11

'''Write a program that: 
• asks the user to input a sentence
• calculates and outputs how many 
characters there are in the sentence'''


user = input('Enter a sentence: ')
print('there are',len(user), 'characters')


#CHALLENGE 12

'''Write a program that: 
• asks the user to input a sentence
• outputs the sentence in upper case'''

user = input('Enter any sentence: ')
print(user.upper())


#CHALLENGE 13

'''Write a program that:
• asks the user to input a sentence
• asks the user to input:
• the word they want to replace 
• the word they want to replace it with
• outputs the new sentence'''


user =input("Enter any sentnce: ")
replaced_word = input("Enter word to be replaced: ")
new_word = input('Enter new word: ')
print(user.replace(replaced_word, new_word))


#CHALLENGE 14
'''Write a program that:
• asks the user to input a sentence 
• outputs the number of times the word 
'the' occurs in it'''


user = input('Enter a sentence: ')
if 'the' in  user:
    count = (user.count('the'))
    print('The number of times "the" appears is ' + str(count))



    #CHALLENGE 15
'''Write a program that:
• asks the user to input a sentence
• outputs the sentence in lower case'''


user = input('Enter a sentence: ')
print(user.lower())


#CHALLENGE 16

'''Write a program that:
• outputs all numbers between 1 and 10'''                       #YOU MUST USE FOR LOOP FOR THIS CODE

for i in range(1,10):
    print(i)



#CHALLENGE 17

'''Write a program that:
• outputs all odd numbers between                                   
1 and 99'''                                                     #YOU MUST USE FOR LOOP FOR THIS CODE


for i in range(1,99):
    if i % 2 == 1:
        print(i)


#CHALLENGE 18
'''Write a program that:
• asks the user to input a number
• outputs the times table for that 
number
'''                                                         #YOU MUST USE FOR LOOP FOR THIS CODE
user = int(input('Enter a number: '))
for i in range(1,13):
    print(user * i)


#CHALLENGE 19
'''Write a program that:
• asks the user to input a number
• outputs the times table for that 
number
• starts again every time it finishes'''            #You must use a For Loop and a While Loop for this challenge.


while True:
    user = int(input('Enter a number: '))
    for i in range(1,13):
            print(user * i)


#CHALLENGE 20

'''Write a program that:
• asks the user to input a number and 
repeats until they guess the number 7 
• congratulate the user with a ‘Well 
Done’ message when they guess 
correctly'''


while True :
    user = int(input('Enter number:'))
    if user == 7:
        print('Well done')
        break



