def print_the_puzzle(board):
    print("Your current grid\n")
    row_labels = "ABCDEFGHI"
    print("   1 2 3   4 5 6   7 8 9")

    for row_index, row in enumerate(board):
        if row_index % 3 == 0 and row_index != 0:
            print("   " + "-" * 21)

        print(f"{row_labels[row_index]} ", end=" ")

        for col_index, value in enumerate(row):
            if col_index % 3 == 0 and col_index != 0:
                print("|", end=" ")

            display = "_" if value == "." else value
            print(display, end=" ")

        print()