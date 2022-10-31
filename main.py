import streamlit as st
from views import profile, scse_fac
import pandas as pd 
import time

st.set_page_config(layout="wide")
with open('assets/styles.css') as f:
    st.write(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def display_prof_list():
    df = pd.read_csv('newdf.csv')
    name = df['Full Name']
    return name 

def load_view():

    # welcome page
    welcome = st.empty()
    with welcome.container():
        welcome_container = f'<div class="welcome">Welcome to SCSE Faculty Page!</div>'
        image_welcome = f'<img class ="image" src="https://www.ntu.edu.sg/images/librariesprovider118/peos-ranking/190918_facultygroupshot57d58653-2a99-4b05-91e1-ddbf059aca80.jpg?sfvrsn=9c46052_5">'
        st.markdown(welcome_container, unsafe_allow_html=True)
        st.write('')
        st.markdown(image_welcome, unsafe_allow_html=True)
    
    # sidebar buttons
    st.sidebar.header('SCSE Professors')

    if st.sidebar.button('SCSE Faculty', key='Faculty'):
        welcome.empty()
        scse_fac.load_view()
    st.sidebar.text('Click to view profiles!')

    for i in range(82):
        if st.sidebar.button(display_prof_list()[i]):
            welcome.empty()
            with st.spinner('Retrieving data....'):
                time.sleep(1)
            profile.load_view(i)   

load_view()
