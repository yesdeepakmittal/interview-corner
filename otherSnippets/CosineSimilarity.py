import numpy as np
def Cossim(A,B):
    ##### write the code to find cosine similarity between A ad B
    #### A, B -> lists of input values
    #### both lists contain three values , denoting the values of vectors along i,j and k unit vectors
    #code starts here
    numerator = 0
    a = 0
    b = 0

    for i in range(len(A)):
        numerator += A[i]*B[i]
        a += np.power(A[i],2)
        b += np.power(B[i],2)
    return numerator/(np.sqrt(a) * np.sqrt(b))