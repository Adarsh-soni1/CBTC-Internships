#random library is used to generate a number 
import random
computer_guess_number=random.randrange(1000,10000)

#Code for Mastermind Game
print("\n=========================MASTERMIND GAME========================\n")
print("Computer guessed:",computer_guess_number,"\n")

# 5 chances will be given to user for guessing the number 
chances=5
user_guess_number=int(input(f'Guess the number, you have {chances} chances left: '))

#if user will guess the number in 1st chance
if user_guess_number==computer_guess_number:
    print("\nGreat you WON , you are MASTERMIND")
    print("\n=====================MASTERMIND GAME ENDED======================\n")
    
#if user will need more chances
else:
    trials=0
    while user_guess_number != computer_guess_number and chances:
        trials+=1
        chances-=1
        correct_digits=0
        user_guess_number=str(user_guess_number)
        computer_guess_number=str(computer_guess_number)
        correct=['Y'] *4
        for abc in range(0,4):
            if user_guess_number[abc]==computer_guess_number[abc]:
                correct_digits+=1
                correct[abc]=computer_guess_number[abc]
                
        #correct digits will be shown and others will be shown as "Y"
        if correct_digits<4 and correct_digits>0 and chances:
            print('\nNot the completely correct guess, but you guessed',correct_digits,'numbers right')
            print('Current status is:')
            for digits in correct:
                print(digits, end='')
            print('\n\n')
            user_guess_number=int(input(f'Guess a 4 digit number,you have {chances} chances left:'))
            
        elif correct_digits==0 and chances:
            print('\nNone of the digits is right that you have guessed.\n\n')
            user_guess_number=int(input(f'Guess a 4 digit number, you have {chances} chances left: '))
            
    #if user have guessed the number in the given chances
    if user_guess_number==computer_guess_number:
        print("\nGreat, you WON in",trials,"guesses,you are a MASTERMIND")
        print("\n=====================MASTERMIND GAME ENDED======================\n")
        
    #if user have lost the game
    if chances==0 and user_guess_number!=computer_guess_number:
        print("\nSorry , you LOST as you ran out of chances")   
        print("Number is:",computer_guess_number)
        print("\n=====================MASTERMIND GAME ENDED======================\n")