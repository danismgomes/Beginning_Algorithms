# ask user to enter elements for the list to sort!
num_of_elems = int(input("How many elements? "))
a_list = []

for i in range(num_of_elems):
    elem = int(input("Enter element" + str(i) + ": "))
    a_list.append(elem)


def bubble_sort(a_list):
    # i = (0, 1, 2, ..., len(a_list) - 1)
    for i in range(len(a_list)):  # scans
        # j = (0, 1, 2, ..., len(a_list) - 2)
        print("Scan ", i, ": ", a_list)  # print each scan
        swapped = False
        for j in range(len(a_list) - 1):  # comparisons
            if a_list[j] > a_list[j+1]:
                # swap
                temp = a_list[j]
                a_list[j] = a_list[j+1]
                a_list[j+1] = temp
                swapped = True

        if not swapped:
            break


bubble_sort(a_list)
print(a_list)
