import random
def mainmenu():
    print("welcome to number guessing game.choose one of the option to start playing")
    print("1.Easy")
    print("2.medium")
    print("3.difficult")
    print("4.quit")
    selection=int(input("Enter your choice" ))
    if selection == 1:
       easy()
    elif selection==2:
          medium()
    elif selection==3:
         difficult()
    elif selection==4:
         exit
    else:
        print("invalid choice.choose between 1-4")
        mainmenu()

def easy():
    number = random.randint(1, 10)
    print("guess a number between 1 and 10")
    print(" For every failed attempt, one point is lost")
    print("hint=8")
    print("points=10")
    number_of_guesses=0
    points= 10
    while number_of_guesses < 8:
        guess = int(input())
        number_of_guesses += 1
        points= 10-(number_of_guesses)
        if guess < number:
            print('Your guess is too low')
        if guess > number:
            print('Your guess is too high')
        if guess == number:
            print('You guessed the number in '+ str(number_of_guesses) + ' tries!')
            print('the total number of points is:'+ str(points)  )
    else:
        print('You have used up your hints , The number was ' + str(number))


def medium():
    number = random.randint(1, 50)
    print("guess a number between 1 and 50")
    print(" For every failed attempt, one point is lost")
    print("hint= 6")
    print("points=10")
    number_of_guesses=0
    points= 10
    while number_of_guesses < 6:
        guess = int(input())
        number_of_guesses += 1
        points= 10-(number_of_guesses)
        if guess < number:
            print('Your guess is too low')
        if guess > number:
            print('Your guess is too high')
        if guess == number:
            print('You guessed the number in '+ str(number_of_guesses) + ' tries!')
            print('the total number of points is:'+ str(points)  )
    else:
        print('You have used up your hints , The number was ' + str(number))
def difficult():
    number = random.randint(1, 100)
    print("guess a number between 1 and 10")
    print(" For every failed attempt, one point is lost")
    print("hint=3")
    print("points=10")
    number_of_guesses=0
    points= 10
    while number_of_guesses < 3:
        guess = int(input())
        number_of_guesses += 1
        points= 10-(number_of_guesses)
        if guess < number:
            print('Your guess is too low')
        if guess > number:
            print('Your guess is too high')
        if guess == number:
            print('You guessed the number in '+ str(number_of_guesses) + ' tries!')
            print('the total number of points is:'+ str(points)  )
    else:
        print('You have used up your hints , The number was ' + str(number))
mainmenu()