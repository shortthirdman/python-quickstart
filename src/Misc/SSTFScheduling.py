def calculate_difference(queue: list, head: int, diff):
    """
    Calculates difference of each  
    track number with the head position
    """
    for i in range(len(diff)):
        diff[i][0] = abs(queue[i] - head)


def find_minimum(diff):
    """
    Find unaccessed track which is
    at minimum distance from head
    """
    index = -1
    minimum = 999999999

    for i in range(len(diff)):
        if (not diff[i][1] and
                minimum > diff[i][0]):
            minimum = diff[i][0]
            index = i
    return index

def shortest_seek_time_first(request, head):
        if (len(request) == 0):
            return

        l = len(request)
        diff = [0] * l

        # initialize array
        for i in range(l):
            diff[i] = [0, 0]

        # count total number of seek operation
        seek_count = 0

        # stores sequence in which disk
        # access is done
        seek_sequence = [0] * (l + 1)

        for i in range(l):
            seek_sequence[i] = head
            calculate_difference(request, head, diff)
            index = find_minimum(diff)

            diff[index][1] = True

            # increase the total count
            seek_count += diff[index][0]

            # accessed track is now new head
            head = request[index]

        # for last accessed track
        seek_sequence[len(seek_sequence) - 1] = head

        print("Total number of seek operations", seek_count)
        print("Seek Sequence is")
        # print the sequence
        for i in range(l + 1):
            print(seek_sequence[i])

# Driver code
if __name__ =="__main__":

    # request array
    size = int(input("Process size: "))
    processes = []
    for i in range(1, size + 1):
        process = int(input("Process " + str(i) + ": "))
        processes.append(process)
    head = int(input("Initial head count: "))
    shortest_seek_time_first(processes, head)