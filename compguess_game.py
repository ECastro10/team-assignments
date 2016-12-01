The user will pick a number between 1 and 100. The computer will start at 1
and keep guessing in increments of 1 until it picks the user number. We will
keep track of the number of guesses it takes for the computer to guess.
We may or may not incorporate a new function.

We'll start by creating a numbers list between 1 and 100
We'll then pick the number 55
Since the computer will begin guessing at numlist[0], everytime the
computer is wrong we'll remove numlist[0]. This loop will break when
computer_guess = user_pick
the count will be user_pick -1.
