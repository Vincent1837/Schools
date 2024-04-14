import pickle 
import numpy as np
from skimage.util import view_as_windows
from pixelhop import Pixelhop

X = np.arange(0, 16).reshape(1, 4, 4, 1)
print(X)



def Shrink(X, shrinkArg):
    win = shrinkArg['win']
    X = view_as_windows(X, (1, win, win, 1), (1, win, win, 1))
    return X.reshape(X.shape[0], X.shape[1], X.shape[2], -1)


def Concat(X):
    return X

SaabArgs = [{'num_AC_kernels':-1, 'needBias':False, 'cw': False},
            {'num_AC_kernels':-1, 'needBias':True, 'cw':True}] 
shrinkArgs = [{'func':Shrink, 'win':2, 'stride': 2}, 
            {'func': Shrink, 'win':2, 'stride': 2}]
concatArg = {'func':Concat}


p2_new = Pixelhop(load=True).load('./dummy')
output1_new = p2_new.transform(X)
output2_new = p2_new.transform_singleHop(X)

print(output1_new)

""" model = pickle.load(open('./dummy.pkl', 'rb'))
print(model['par'])
 """