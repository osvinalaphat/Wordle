answer = "minis"
tries = 6
guess = None

while guess != answer and tries != 0:

    board = ["_", "_", "_", "_", "_",]
    guess = str(input("Try to guess the word! "))

    if len(guess) == 5:

        tries = tries - 1

        for i in range(len(guess)):

            if guess[i] == answer[i]: # green tile
                board[i] = guess[i]

            elif guess[i] in answer: # yellow tile
                board[i] = "🟡"
                
        print(''.join(board))

    else:
        print("Error: the word needs to be 5 letters")

if guess == answer:
    print("\nYou got the answer!")
else:
    print("\nYou lost.")
print("The word was", answer)
