def print_square_with_optional_hole(x, y):
    choice = input("Do you want a hole in the square? (y/n): ").strip().lower()

    hole_size = 0
    if choice == "y":
        hole_size = int(input("Enter hole size: "))

        max_hole = min(x, y) - 2
        if max_hole < 1:
            print("Square too small for a hole.")
            hole_size = 0
        else:
            if hole_size > max_hole:
                print(f"Hole too large, reducing to {max_hole}")
                hole_size = max_hole
            if hole_size < 0:
                hole_size = 0

    top = (x - hole_size) // 2
    bottom = top + hole_size
    left = (y - hole_size) // 2
    right = left + hole_size

    for i in range(x):
        row = []
        for j in range(y):
            if choice == "y" and top <= i < bottom and left <= j < right:
                row.append(" ")
            else:
                row.append("d")
        print("".join(row))


def main():
    x = int(input("Enter height (x): "))
    y = int(input("Enter width (y): "))

    print_square_with_optional_hole(x, y)


if __name__ == "__main__":
    main()
