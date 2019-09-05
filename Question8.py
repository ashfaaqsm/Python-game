while True: #loop to play again
    player1=input("Choose rock, raper, scissors: ")
    player2=input("Choose rock, raper, scissors: ")

    #input of player 1 and player 2

    if player1==player2: #checking if draw
        print("Draw,Choose again")

    # comparing the inputs
    elif player1=='rock':
        if player2=='scissors':
            print("Congratulation player 1 is the winner")

            new = int(input("Do you want to play again(1.yes.2no): ")) #user's decision to play again or not
            if new == 2:
                print("Program ended")
                break
            elif new == 1:
                print("New game")
        else:
            print("Congratulation player 2 is the winner")

            new = int(input("Do you want to play again(1.yes.2no): "))
            if new ==2:
                print("Program ended")
                break
            elif new == 1:
                print("New game")
    # comparing the inputs
    elif player1=='scissors':
        if player2=='paper':
            print("Congratulation player 1 is the winner")
            new = int(input("Do you want to play again(1.yes.2no): "))
            if new == 2:
                print("Program ended")
                break
            elif new == 1:
                print("New game")
        else:
            print("Congratulation player 2 is the winner")
            new = int(input("Do you want to play again(1.yes.2no): "))
            if new == 2:
                print("Program ended")
                break
            elif new == 1:
                print("New game")
    # comparing the inputs
    elif player1=='paper':
        if player2=='rock:':
            print("Congratulation player 1 is the winner")
            new = int(input("Do you want to play again(1.yes.2no): "))
            if new != 1:
                print("Program ended")
                break
            elif new == 1:
                print("New game")
        else:

            print("Congratulation player 1 is the winner")
            new = int(input("Do you want to play again(1.yes.2no): ")) 
            if new == 2:
                print("Program ended")
                break
            elif new == 1:
                print("New game")