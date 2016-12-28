from util import LoadData, Load, Save, DisplayPlot
import numpy as np
def main():
    a = np.array([[[1],[2]], [[2],[3]], [[3],[2]], [[4],[3]]])
    inputs_train, inputs_valid, inputs_test, target_train, target_valid, \
        target_test = LoadData('../toronto_face.npz')
    print(inputs_train.shape)
    print(a.shape)
if __name__ == '__main__':
    main()
