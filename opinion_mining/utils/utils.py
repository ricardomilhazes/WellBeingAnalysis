def isSubArray(A, B, n, m):

    # Two pointers to traverse the arrays
    i = 0
    j = 0
 
    # Traverse both arrays simultaneously
    while (i < n and j < m):
 
        # If element matches
        # increment both pointers
        if (A[i] == B[j]):
 
            i += 1
            j += 1
 
            # If array B is completely
            # traversed
            if (j == m):
                return True
         
        # If not,
        # increment i and reset j
        else:
            i = i - j + 1
            j = 0
         
    return False