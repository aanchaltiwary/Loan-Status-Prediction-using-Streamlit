# -*- coding: utf-8 -*-
"""Loan Status Prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13_1kC3XHcvsgNHmQ6mWJJZEJujLH6wJn
"""

import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier

# loading the dataset to pandas DataFrame
loan_dataset = pd.read_csv('dataset.csv')

type(loan_dataset)

# printing the first 5 rows of the dataframe
loan_dataset.head()

# number of rows and columns
loan_dataset.shape

# statistical measures
loan_dataset.describe()

# number of missing values in each column
loan_dataset.isnull().sum()

# dropping the missing values
loan_dataset = loan_dataset.dropna()

# number of missing values in each column
loan_dataset.isnull().sum()

# label encoding
loan_dataset.replace({"Loan_Status":{'N':0,'Y':1}},inplace=True)

# printing the first 5 rows of the dataframe
loan_dataset.head()

# Dependent column values
loan_dataset['Dependents'].value_counts()

# replacing the value of 3+ to 4
loan_dataset = loan_dataset.replace(to_replace='3+', value=4)

# dependent values
loan_dataset['Dependents'].value_counts()

# education & Loan Status
sns.countplot(x='Education',hue='Loan_Status',data=loan_dataset)

# marital status & Loan Status
sns.countplot(x='Married',hue='Loan_Status',data=loan_dataset)

# convert categorical columns to numerical values
loan_dataset.replace({'Married':{'No':0,'Yes':1},'Gender':{'Male':1,'Female':0},'Self_Employed':{'No':0,'Yes':1},
                      'Property_Area':{'Rural':0,'Semiurban':1,'Urban':2},'Education':{'Graduate':1,'Not Graduate':0}},inplace=True)

# separating the data and label
X = loan_dataset.drop(columns=['Loan_ID','Loan_Status','Property_Area','Dependents','Loan_Amount_Term','CoapplicantIncome'],axis=1)
Y = loan_dataset['Loan_Status']

print(X)
print(Y)

x_train, x_test, y_train, y_test = train_test_split(X,Y, test_size = 0.2, random_state = 10)

print(X.shape, x_train.shape, x_test.shape)

model = RandomForestClassifier(max_depth=4, random_state = 10) 
model.fit(x_train, y_train)

pred_test = model.predict(x_test)
accuracy_score(y_test,pred_test)

# accuracy score on training data
pred_train = model.predict(x_train)
accuracy_score(y_train,pred_train)

# saving the model 
import pickle 
pickle_out = open("classifier.pkl", mode = "wb") 
pickle.dump(model, pickle_out) 
pickle_out.close()

!pip install -q pyngrok
!pip install -q streamlit
!pip install -q streamlit_ace

# Commented out IPython magic to ensure Python compatibility.
# %%writefile app.py
#  
# import pickle
# import streamlit as st
#  
# # loading the trained model
# pickle_in = open('classifier.pkl', 'rb') 
# classifier = pickle.load(pickle_in)
#  
# @st.cache()
#   
# # defining the function which will make the prediction using the data which the user inputs 
# def prediction(Gender, Married, Credit_History, Self_Employed, Education, ApplicantIncome, LoanAmount):   
#  
#     # Pre-processing user input    
#     if Gender == "Male":
#         Gender = 1
#     else:
#         Gender = 0
#  
#     if Married == "Unmarried":
#         Married = 0
#     else:
#         Married = 1
#  
#     if Credit_History == "Unclear Debts":
#         Credit_History = 0
#     else:
#         Credit_History = 1 
# 
#     if Self_Employed == "Self-Employed":
#         Self_Employed = 1
#     else:
#        Self_Employed = 0 
# 
#     if Education == "Graduate":
#         Education = 1
#     else:
#        Education = 0 
#   
#  
#     LoanAmount = LoanAmount / 1000
#  
#     # Making predictions 
#     prediction = classifier.predict( 
#         [[Gender, Married, Credit_History, Self_Employed, Education, ApplicantIncome, LoanAmount]])
#      
#     if prediction == 0:
#         pred = 'Rejected'
#     else:
#         pred = 'Approved'
#     return pred
#       
#   
# # this is the main function in which we define our webpage  
# def main():       
#     # front end elements of the web page 
#     html_temp = """ 
#     <div style ="background-color:Beige;padding:13px"> 
#     <h1 style ="color:black;text-align:center;">Loan Status Prediction App</h1> 
#     </div> 
#     """
#       
#     # display the front end aspect
#     st.markdown(html_temp, unsafe_allow_html = True) 
#       
#     # following lines create boxes in which user can enter data required to make prediction 
#     Gender = st.selectbox('Gender',("Male","Female"))
#     Married = st.selectbox('Marital Status',("Unmarried","Married")) 
#     ApplicantIncome = st.number_input("Applicants monthly income") 
#     LoanAmount = st.number_input("Total loan amount")
#     Credit_History = st.selectbox('Credit_History',("Unclear Debts","No Unclear Debts"))
#     Self_Employed =st.selectbox('Employment',("Self-Employed","Employed"))
#     Education =st.selectbox('Education',("Graduate","Not graduate"))
#     result =""
#       
#     # when 'Predict' is clicked, make the prediction and store it 
#     if st.button("Predict"): 
#         result = prediction(Gender, Married, Credit_History, Self_Employed, Education, ApplicantIncome, LoanAmount) 
#         st.success('Your loan is {}'.format(result))
#         print(LoanAmount)
#      
# if __name__=='__main__': 
#     main()

!ngrok authtoken 20MlEx5W7cPxIreIsdihNhwQgXf_2VAp1NBJnvVYG1php5Jvq

!ngrok

from pyngrok import ngrok

!streamlit run app.py &>/dev/null&

!pgrep streamlit

publ_url = ngrok.connect('8501')
publ_url