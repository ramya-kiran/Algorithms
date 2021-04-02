def tower_of_hanoi(number_of_discs, start, end, inter):

    if number_of_discs == 1:
        print("Moving disc " + str(number_of_discs) + " from " + start + " to " + end)
        return
    else:
        tower_of_hanoi(number_of_discs - 1, start, inter, end)
        print("Moving disc " + str(number_of_discs) + " from " + start + " to " + end)
        tower_of_hanoi(number_of_discs - 1, inter, end, start)


if __name__ == '__main__':
    tower_of_hanoi(3, "A", "C", "B")
