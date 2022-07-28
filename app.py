import pickle
import streamlit as st 
import xgboost as xgb
import numpy as np
import pandas as pd
from DataPreprocessing_2.data_preprocessing_phase2 import Data_Preprocessing_Phase


st.set_page_config(layout="wide")

def model_prediction_pickel(df):
    model=  pickle.load(open('model.pkl', 'rb'))
    arr = np.array(df)
    value = model.predict(list(arr))
    return value
def side_display():
    with st.sidebar:
        st.title("Dashboard😊")
        st.subheader("\t\t Project Details : ")
        st.subheader("Dataset..")
        st.write("[dataset](https://archive.ics.uci.edu/ml/datasets/thyroid+disease)")
        st.subheader("High Level Document : ")
        st.write("[HLD](https://github.com/SuShAnTBiShT407/Thyroid-Disease-Detection.github.io/tree/main/Docs/HLD)")
        st.subheader("Low Level Document")
        st.write("[LLD](https://github.com/SuShAnTBiShT407/Thyroid-Disease-Detection.github.io/tree/main/Docs/LLD)")
        st.subheader("Architecture")
        st.write("[architecture](https://github.com/SuShAnTBiShT407/Thyroid-Disease-Detection.github.io/tree/main/Docs/WireFrame)")
        st.subheader("Project Code")
        st.write("[code](https://github.com/SuShAnTBiShT407/Thyroid-Disease-Detection.github.io/blob/main/app.py)")
        st.subheader("Report")
        st.write("[report](https://github.com/SuShAnTBiShT407/Thyroid-Disease-Detection.github.io/blob/main/Docs/DPR/TDD_DPR.docx)")
        st.subheader("Demo video")
        st.write("demo video")

st.title("Thyroid Disease Detection")
st.subheader("- using XGboost🏥🏥ᵇʸ ˢᵘˢʰᵃⁿᵗ ᴮⁱˢʰᵗ ")
side_display()

answers = []
age = st.text_input('Age', '18')
st.write('The current Age is', age)
answers.append(int(age))

sex = st.selectbox(
     'Select Gender Female-0, Male-1, Other-2',
     ('0', '1', '2'))

st.write('You selected:', sex)
answers.append(int(sex))

radio_list = ['thyroxine', 'query_thyroxine', 'antithyroid', 'sick',
       'pregnant', 'thyroid_surgery', 'I131 treatment', 'query_hypothyroid',
       'query_hyperthyroid', 'lithium', 'goitre', 'tumor', 'hypopituitary',
       'psych']
count=0
for i in radio_list:
    st.write(i)
    i = st.selectbox(
     "True-1 or False-0",
     ('0', '1'), key = count ) 
    answers.append(int(i))
    count+=1

TSH = st.text_input("TSH value range between 0.0-15.0 ? " ,'5.5')
TSH = pd.to_numeric(TSH)
answers.append(TSH)
T4U = st.text_input("T4U value range between 0.0-2.0 ? " ,'1.5')
T4U = pd.to_numeric(T4U)
answers.append(T4U)
FTI = st.text_input("FTI value range between 0-400 ? " ,'263')
FTI = pd.to_numeric(FTI)
answers.append(FTI)


if st.button('Predict'):
    value = model_prediction_pickel(answers)
    if value[0] == 1:
        st.success("You have Thyroid Disease 😱") 
    else:
        st.success("You are safe 👍😮‍💨")