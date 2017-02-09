import random

play = "y"
while play == "y":
    print "I'm thinking of a number between 1 and 10."
    print "You have 5 guesses left."
    left = 5
    num = random.randint(1,10)
    guess = int(raw_input("What's the number? "))
    while guess != num:
        left -= 1
        if num > guess:
            print "%d is too low." % guess
        else:
            print "%d is too high." % guess
        print "You have %d guesses left" % left
        if left == 0:
            break
        guess = int(raw_input("What's the number? "))
    if num == guess:
        print "Yes! You guessed correctly!"
    else:
        print "Sorry, you ran out of guesses!"
    play = raw_input("Do you want to play again? (y/n) ")
print "Bye!"
