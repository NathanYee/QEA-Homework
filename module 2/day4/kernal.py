import numpy as np

def applyKernal(vec, kern):
    #set up return matrix (list)
    final = []

    #initial conditions
    final.append(vec[0])

    #while loop to iterate through vec
    startPos = 0
    while (startPos + len(kern)) <= len(vec):
        #begin with elementwise multiplication to get the nextValue
        nextValue = np.array(vec[startPos : startPos + len(kern)]) * np.array(kern)
        final.append(nextValue.sum())
        startPos += 1
    final.append(vec[-1])
    return final
