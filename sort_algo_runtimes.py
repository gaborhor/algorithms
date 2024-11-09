import random
from time import time

def merge(A, B):
    out = []
    i, j = 0, 0
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            out.append(A[i])
            i += 1
        else:
            out.append(B[j])
            j += 1
    while i < len(A):
        out.append(A[i])
        i += 1
    while j < len(B):
        out.append(B[j])
        j += 1
    return out
def mergeSort(L):
    if len(L) < 2:
        return L[:]
    else:
        mid = len(L)//2
        left = mergeSort(L[:mid])
        right = mergeSort(L[mid:])
        return merge(left,right)

def insertionSort(L):
    n = len(L)

    # print(f"Pre-sort: {L}")
    for i in range(1,n):
        key = L[i]
        j = i-1
        while j>=0 and L[j]>key:
            L[j+1] = L[j]
            j = j-1
        L[j+1] = key

    # print(f"Post-sort: {L}")

def bubbleSort(L):
    n = len(L)
    counter = 0

    # print(f"Pre-sort: {L}")
    while counter < n :
        for i in range(n-1):
            if L[i] > L[i+1]:
                old_left = L[i]
                old_right = L[i+1]
                L[i] = old_right
                L[i+1] = old_left
                # print(L)
        # print(L)
        counter += 1

    # print(f"Post-sort: {L}")

#################
#### Testing ####
#################

## Individual / Prelim tests

# A = [i for i in range(10)]
# random.shuffle(A)
#
# t1 = time()
# # print(mergeSort(A))
# # insertionSort(A)
# # bubbleSort(A)
# t2 = time()
# mtime = (t2-t1)*1000
# print(mtime)

## Incremented 'n' values testing

# Something to handle multiple sorts for later
def shuffle_and_time(length: int, sort: int):
    L = [i for i in range(length)]
    random.shuffle(L)
    t1 = time()

    if sort == 0:
        mergeSort(L)
    elif sort == 1:
        insertionSort(L)
    elif sort == 2:
        bubbleSort(L)

    t2 = time()
    runtime = (t2-t1)*1000

    return runtime

# Putting table together as list of lists for line separation
def create_table():
    out_table = [["N", "Merge", "Insert", "Bubble"]]

    for i in range(100, 5000+1, 100):
        line_to_table = [i,]

        for j in range(3):
            rounded_time = round(shuffle_and_time(i,j), 1)
            line_to_table.append(rounded_time)

        out_table.append(line_to_table)

    return out_table

# Printing the table
def print_table(table):
    table_len = len(table)

    for i in range(table_len):
        line_len = len(table[i])
        str_to_print = ""
        for j in range(line_len):
            str_to_print += f"{table[i][j]} \t"

        print(str_to_print)

print_table(create_table())