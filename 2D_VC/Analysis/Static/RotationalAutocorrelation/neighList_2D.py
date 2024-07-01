import numpy as np

def BoxAtoms (x, y, box1D, dimL):

    boxL = dimL / box1D

    boxes = {}
    for atom in range(len(x)):

        xBox = int(x[atom] / boxL)
        yBox = int(y[atom] / boxL)
        box = str([xBox, yBox])
        
        if box in boxes:
            boxes[box].append(atom)

        else:
            boxes[box] = [atom]

    return boxes

def GetNeighbors(boxes, box1D):

    nKeys = [np.array([i, j]) for i in [-1, 0, 1] for j in [-1, 0, 1]]
    for key in boxes:

        box = np.fromstring(key[1:-1], dtype = int, sep = ',')
        nBoxes = [np.mod((box + nKey), box1D) for nKey in nKeys]

        neighs = []
        for nBox in nBoxes:

            nBox = str(list(nBox))
            if str(nBox) in boxes:
                neighs.extend(boxes[nBox])

        yield neighs
