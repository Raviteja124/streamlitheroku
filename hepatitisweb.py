# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 21:30:54 2022

@author: teja1
"""

import numpy as np
import pickle
import streamlit as st


loaded_model=pickle.load(open('D:/machine/trained_model.sav','rb'))

def hepatitis_prediction(input_data):
    input_data_as_numpy_array=np.asarray(input_data)
    input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
    prediction=loaded_model.predict(input_data_reshaped)
    print(prediction)
    if prediction==1:
        return 'patient is non hepatitic'
    else:
        return 'patient is hepatitic'
    
def main():
    
    st.title("Hepatitis prediction web app")
    
   # class,age,sex,steroid,antivirals,fatigue,malaise,anorexia,liver_big,liver_firm,
   #spleen_palable,spiders,ascites,varices,bilirubin,alk_phosphate,sgot,albumin,protime,histology
    age=st.text_input('Number of age')
    sex=st.text_input('sex')
    steroid=st.text_input('steroid value')
    antivirals=st.text_input('antivirals value')
    fatigue=st.text_input('fatigue value')
    malaise=st.text_input('malaise value')
    anorexia=st.text_input('anorexia value')
    liver_big=st.text_input('liver_big value')
    liver_firm=st.text_input('live_rfirm value')
    spleen_palable=st.text_input('spleen_palable value')
    spiders=st.text_input('spiders value')
    ascities=st.text_input('ascities value')
    varices=st.text_input('varices value')
    bilirubin=st.text_input('bilirubin value')
    alk_phosphate=st.text_input('alkphosphate value')
    sgot=st.text_input('sgot value')
    albumin=st.text_input('albumin value')
    protime=st.text_input('protime value')
    histology=st.text_input('histology value')
    
    diagnosis=""
    
    if st.button("Hepatitis Test Result"):
        diagnosis=hepatitis_prediction([age,sex,steroid,antivirals,fatigue,malaise,anorexia,liver_big,liver_firm,spleen_palable,spiders,ascities,varices,bilirubin,alk_phosphate,sgot,albumin,protime,histology])

    st.success(diagnosis)
    
    
if __name__=='__main__':
    main()

    
    
    
    
    
    
    
    
    
    