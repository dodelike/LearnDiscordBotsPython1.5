import random
#imports the random library to use commands below

coin = ["heads", "tails"]
toss = random.choice(coin)
#created coin and toss variables to store various values
#toss uses random.choice function with coin as an argument

userV = input(f'Heads or Tails? ').lower()
#userV variable is used to store the value of what the user inputs when asked heads or tails
#.lower() is added to keep input consistent regardless of capitalization

if userV == toss:
    print(f'You win! The coin landed on {toss}.')
else:
    print(f'LOSER! The coin landed on {toss}.')
#if statement is used here to compare userV (user input) to computed random variable (toss)
#an f string (f') is used to enter variable (toss) into feedback given back to user
