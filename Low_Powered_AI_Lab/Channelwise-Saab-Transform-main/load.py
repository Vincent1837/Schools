import numpy as np
from skimage.util import view_as_windows
from pixelhop import Pixelhop

X = np.arange(0, 16).reshape(1, 4, 4, 1)
print(X)

# 要定義下面兩個涵式，才能傳進Agrs裡面
def Shrink(X, shrinkArg):
    win = shrinkArg['win']
    X = view_as_windows(X, (1, win, win, 1), (1, win, win, 1))
    return X.reshape(X.shape[0], X.shape[1], X.shape[2], -1)

def Concat(X, concatArg):
    return X

# Args
SaabArgs = [{'num_AC_kernels':-1, 'needBias':False, 'cw': False},
            {'num_AC_kernels':-1, 'needBias':True, 'cw':True}] 
shrinkArgs = [{'func':Shrink, 'win':2, 'stride': 2}, 
            {'func': Shrink, 'win':2, 'stride': 2}]
concatArg = {'func':Concat}

# pixelhop 模型
p2_new = Pixelhop(load=True).load('./dummy')
output1_new = p2_new.transform(X)
output2_new = p2_new.transform_singleHop(X)

print("printing output")
print(output1_new)
