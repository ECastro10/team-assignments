'''The user will pick a number between 1 and 100. The computer will start at 1
and keep guessing in increments of 1 until it picks the user number. We will
keep track of the number of guesses it takes for the computer to guess.
We may or may not incorporate a new function.

We'll start by creating a numbers list between 1 and 100
We'll then pick the number 55
Since the computer will begin guessing at numlist[0], everytime the
computer is wrong we'll remove numlist[0]. This loop will break when
computer_guess = user_pick
the count will be user_pick -1.

dirty code for chrono'''
import random
numlist = []
usernum = int(input("give us a number "))
guesses = 0


def genlist():
    '''
    input: none
    usage:generate a list within a range
    output: is a list with a range called numlist
    '''

    pass

def chrono():
    '''
    input:none
    usage: how the computer will chronologically attempt to guess the user
    number in the list. we do this by deleting the numlist[0] and have the
    computer keep guessing numlist[0] in a loop.
    output: will show when the loop breaks when compguess == usernum
    we'll show the count as usernum - 1
    '''

    pass

def randi():
    '''
    input:none
    usage: we'll have the computer randomly pick a number in a list (rcomp)
    the list's range changes on whether computers choice is greater or lower
    than the usernumber.
    output: The loop breaks when the random number ==usernumber. we'll track
    count of the number of attempts it takes the comp to guess. printing
    the amount of times
    '''
    numlist = list(range(1,101))
    rcomp = random.choice(numlist)
    while rcomp != usernum:
        print('Computer guess is:',rcomp)
        numlist.remove(rcomp)
        rcomp = random.choice(numlist)
    print(numlist)

randi()

def main():
    '''
    input: use global variables: usernum, numlist, guesses
    usage: based on the global numbers we'll see how the computer does using
    two different strategies.
    output: we'll show the number of times it takes the comp to guess using
    the different functions.
    '''

    pass
