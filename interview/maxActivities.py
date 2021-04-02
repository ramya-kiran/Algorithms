def printMaxActivities(n, arrival, duration):
    finish_index = 0
    # print(finish_index)

    # first item is always selected
    selected_activities = 1

    # calculating finish time and sort it
    finish = [a+d for a,d in zip(arrival, duration)]
    finish.sort()
    print(finish)

    # looping over each activities and selecting them in greedy fashion
    for start_index in range(0, n):

        if arrival[start_index] >= finish[finish_index]:
            selected_activities += 1
            print(finish_index)
            finish_index = start_index

    print(selected_activities)


printMaxActivities(7, [250, 74, 659, 931, 273, 545, 879], [924, 710, 441, 166, 493, 43, 988])
# print(len([250, 74, 659, 931, 273, 545, 879]))