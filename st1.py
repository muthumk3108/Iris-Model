import streamlit as st
import pickle

st.title('Iris Predictions')

st.write('iris data predictions')

sl=st.number_input('Enter the sepal length value')
sw=st.number_input('Enter the sepal width value')
pl=st.number_input('Enter the petal length value')
pw=st.number_input('Enter the petal width value')

if st.button('Predict'):

    with open('iris_model.pkl','rb') as model:
        main_model = pickle.load(model)

        datas=[[sl,sw,pl,pw]]

        preds=main_model.predict(datas)

        st.write(f'The predicted value is {preds}')