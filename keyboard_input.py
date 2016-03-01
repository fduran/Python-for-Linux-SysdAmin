# Guessing age game

import sys

maxage = 120
guess = 50
message = "Are you younger(y), older(o) or exactly {myguess} years old? "
while True:
    answer = raw_input(message.format(myguess=guess))
    if answer.lower() == 'x':
        print "You look good"
        sys.exit(0)
    if guess == maxage - 1:
        print "Nah, dont' believe you!"
        sys.exit(0)
    if answer.lower() == 'o':
        guess = (maxage+guess)//2
    elif answer.lower() == 'y':
        guess = guess//2
    else:
        print "Please answser y,o or x"
