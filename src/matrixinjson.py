import numpy as np
import json
import codecs


def saveMatrix(matrix):
    matrix_json = matrix
    # print(type(matrixJSON))
    save = matrix_json.tolist()
    # print(type(matrixJSON))
    # print(mat)

    json.dump(save, codecs.open('../Datas/matrix.json', 'w', encoding='utf-8'), separators=(',', ':'), sort_keys=True, indent=4)


def restoreMatrix():
    obj_text = codecs.open('../Datas/matrix.json', 'r', encoding='utf-8').read()
    b_new = json.loads(obj_text)
    a_new = np.array(b_new)
    # print("saved matrix is")
    # print(a_new)
    return a_new
