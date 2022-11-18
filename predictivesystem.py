# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pickle
loaded_model=pickle.load(open('D:/machine/trained_model.sav','rb'))
input_data=(56,1,1,2,1,1,1,1,1,2,1,2,2,2.9,90,153,4,61,2)
input_data_as_numpy_array=np.asarray(input_data)
input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
prediction=loaded_model.predict(input_data_reshaped)
print(prediction)
if prediction==1:
    print('patient is non hepatitic')
else:
    print('patient is hepatitic')