theCell = {
    '1': ' ', '2': ' ', '3': ' ',
    '4': ' ', '5': ' ', '6': ' ',
    '7': ' ', '8': ' ', '9': ' '
}

cell_keys = []

for key in theCell:
    cell_keys.append(key)


def printCell(cell):
    cell1 = "1" if cell['1'] == " " else cell['1']
    cell2 = "2" if cell['2'] == " " else cell['2']
    cell3 = "3" if cell['3'] == " " else cell['3']
    cell4 = "4" if cell['4'] == " " else cell['4']
    cell5 = "5" if cell['5'] == " " else cell['5']
    cell6 = "6" if cell['6'] == " " else cell['6']
    cell7 = "7" if cell['7'] == " " else cell['7']
    cell8 = "8" if cell['8'] == " " else cell['8']
    cell9 = "9" if cell['9'] == " " else cell['9']

    print('\n┌─┬─┬─┐')
    print(f"│{cell1}│{cell2}│{cell3}│")
    print('├─┼─┼─┤')
    print(f"│{cell4}│{cell5}│{cell6}│")
    print('├─┼─┼─┤')
    print(f"│{cell7}│{cell8}│{cell9}│")
    print('└─┴─┴─┘')


def main():

    turn = 'X'
    count = 0

    for _ in range(10):
        printCell(theCell)
        move = input(f"{turn}\'s turn to choose a square (1-9): ")

        if theCell[move] == ' ':
            theCell[move] = turn
            count += 1
        else:
            print(f"\"{move}\" is not available.\nChoose another one")
            continue

        # check win
        if count >= 5:
            if theCell['7'] == theCell['8'] == theCell['9'] != ' ':
                printCell(theCell)
                print("\nGame Over.\n")
                print(f"{turn} win!")
                break
            elif theCell['4'] == theCell['5'] == theCell['6'] != ' ':
                printCell(theCell)
                print("\nGame Over.\n")
                print(f"{turn} win!")
                break
            elif theCell['1'] == theCell['2'] == theCell['3'] != ' ':
                printCell(theCell)
                print("\nGame Over.\n")
                print(f"{turn} win!")
                break
            elif theCell['1'] == theCell['4'] == theCell['7'] != ' ':
                printCell(theCell)
                print("\nGame Over.\n")
                print(f"{turn} win!")
                break
            elif theCell['2'] == theCell['5'] == theCell['8'] != ' ':
                printCell(theCell)
                print("\nGame Over.\n")
                print(f"{turn} win!")
                break
            elif theCell['3'] == theCell['6'] == theCell['9'] != ' ':
                printCell(theCell)
                print("\nGame Over.\n")
                print(f"{turn} win!")
                break
            elif theCell['7'] == theCell['5'] == theCell['3'] != ' ':
                printCell(theCell)
                print("\nGame Over.\n")
                print(f"{turn} win!")
                break
            elif theCell['1'] == theCell['5'] == theCell['9'] != ' ':
                printCell(theCell)
                print("\nGame Over.\n")
                print(f"{turn} win!")
                break

        # tie
        if count == 9:
            print("\nGame Over.\n")
            print("It's a Tie!!")

        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

    restart = input("Another round?(y/n)")
    if restart == "y" or restart == "Y":
        for key in cell_keys:
            theCell[key] = " "

        main()


if __name__ == "__main__":
    main()
