import numpy as np
import pandas as pd
import streamlit as st

st.title('Day 3 of 100 Days of Streamlit')
st.write('This is a simple web app that takes a word as input and returns its meaning from a dictionary.')

data=pd.DataFrame({1:'Apple',2:'Banana',3:'Cat',4:'Dog',5:'Elephant',6:'Fish',7:'Giraffe',8:'Horse',9:'Iguana',10:'Jaguar',11:'Kangaroo',12:'Lion',13:'Monkey',14:'Nightingale',15:'Ostrich',16:'Penguin',17:'Quail',18:'Rabbit',19:'Snake',20:'Tiger',21:'Umbrella',22:'Vulture',23:'Whale',24:'Xylophone',25:'Yak',26:'Zebra'},index=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])
st.write(data)
cdata=pd.DataFrame(np.random.randn(20,3))
st.bar_chart(cdata)