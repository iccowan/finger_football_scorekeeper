# Keep score of a finger football game


def main():
    # Get the names of both players
    player1 = input('Name of player 1: ')
    player2 = input('Name of player 2: ')

    # Run a loop and show the score and wait for an input
    game_over = False
    score_p1 = 0
    score_p2 = 0

    while not game_over:
        # Print the current score
        print('Current Score:')
        print('-------------')
        print(player1 + '\t' + player2)
        print(str(score_p1) + '\t' + str(score_p2))
        print()

        # Wait for an input for the next score
        score = input('Who scored? 1 -> ' + player1 + '; 2 -> ' + player2 + ': ').strip()
        if score.upper() == 'FINISH':
            game_over = True
        else:
            pat = input('PAT good? 1 -> YES; 2 -> NO: ').strip()

            # Add the score to whoever scored
            if pat == '1':
                if score == '1':
                    score_p1 += 7
                else:
                    score_p2 += 7
            else:
                if score == '1':
                    score_p1 += 6
                else:
                    score_p2 += 6

        # Clear the screen
        for i in range(50):
            print()

    # When the game is over, print the final score
    print('Final Score:')
    print('-------------')
    print(player1 + '\t' + player2)
    print(str(score_p1) + '\t' + str(score_p2))
    print()

    # Print out the final winner
    print('The final winner is...')
    if score_p1 > score_p2:
        print(player1 + '!')
    elif score_p1 < score_p2:
        print(player2 + '!')
    else:
        print('It was a tie!')


main()
