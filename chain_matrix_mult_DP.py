def parentStr(traceback, low=0, high=None): # DAC process is standard by now, no comment
    if high == None:
        high = len(traceback) - 1
    if low == high:
        return f"A{low}"

    split = traceback[low][high]

    left_best = parentStr(traceback, low, split)
    right_best = parentStr(traceback, split+1, high)

    return "(" + left_best + ")(" + right_best + ")"

def chainMatrix(dims):
    # Create empty "value" table and traceback table
    n = len(dims)-1
    min_table = [[None for i in range(n)] for j in range(n)]
    traceback = [[None for i in range(n)] for j in range(n)]

    for i in range(n):  # Fill in base case values in min_table
        min_table[i][i] = 0     # Base case is only a single matrix available, no dims to check multiplication of

    for chainLength in range(2, n+1):   # Fill in rest of min_table: chainLength = 2 at start
        for i in range(n+1 - chainLength):  # for i in range(len(dims) - 2) : i = 0 at start
            j = i + chainLength - 1         # j = 0 + 2 - 1 = 1
            min_table[i][j] = float('inf')  # initialize placeholders for min_table with which to compare real calculations
            for k in range(i,j):            # for k in range(0,1)

                # q = min_table[0][0] + min_table[0+1][1] + dims[0]*dims[0+1]*dims[1+1]
                q = min_table[i][k] + min_table[k+1][j] + dims[i]*dims[k+1]*dims[j+1]   # q = 0 + 0 + 30*35*15 = 15750

                if q < min_table[i][j]: # if newly-calculated value less than stored value
                    min_table[i][j] = q # replace stored value
                    traceback[i][j] = k # store "where to split" for future traceback usage at the location denoted by
                                        # the "span" of matrices you want to check order for: in this case, [0][5]

    print(parentStr(traceback))

    for row in min_table:   # For visualization of tables to understand eventual traceback
        print(row)
    for row in traceback:
        print(row)

    return min_table[0][len(dims)-2]


dims = [30,35,15,5,10,20,25]
print(chainMatrix(dims))