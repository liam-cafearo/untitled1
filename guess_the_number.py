import random

# uppercase denote constants

NUMBER_OF_USER_GUESSES = 10
RANGE_TOP = 10
RANGE_BOTTOM = 0

while True:
    # While True creates and infinite loop
    # generate the random number
    random_number = random.randint(RANGE_BOTTOM, RANGE_TOP)

    # give the user a certain amount of guesses
    for i in range(NUMBER_OF_USER_GUESSES):
        guess = int(raw_input('guess the number: '))
        if guess == random_number:
            print 'well done'
            break
            # break ends the loop prematurely
        elif guess > random_number:
            print "too high"
            print "Remaining guesses: "
            print NUMBER_OF_USER_GUESSES - 1 - i
            # here we are saying 10 - 1 from i in the for loop
        else:
            print "too low"
            print "Remaining guesses: "
            print NUMBER_OF_USER_GUESSES - 1 - i
            # here we are saying 10 - 1 from i in the for loop

    print "let's try a new number!"
    print "RANGE TOP: "
    print RANGE_TOP
    print "RANGE BOTTOM: "
    print RANGE_BOTTOM