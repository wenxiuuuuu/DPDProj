import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd 
import plotly.express as px
from utils import scse_fac_profile, string_to_list
from views import research 
import time

def import_data(index): 
    df = pd.read_csv('nturesearch.csv')
    prof_df = pd.read_csv('newdf.csv')
    selected = df.iloc[index]
    research_area = selected['Research Areas']
    profs = selected['Professors']
    profs = string_to_list(profs)
    prof_list = []
    for i in range(len(profs)): 
        prof_list.append(prof_df['Full Name'][int(profs[i])])
    return research_area, prof_list

def format_func(x): 
    if x == 'NTU': 
        data = pd.read_csv('nturesearch.csv')

        fig = px.pie(data, values='Number', names='Research Areas', title='NTU Faculty Research')
        st.plotly_chart(fig, use_container_width=True)
        
    else: 
        data = pd.read_csv('nusresearch.csv')
        fig2 = px.pie(data, values='Number', names='Research Areas', title='NUS Faculty Research')
        st.plotly_chart(fig2, use_container_width=True)

def display_research_areas(): 
    df = pd.read_csv('nturesearch.csv')
    return df['Research Areas']

def selectoption(option): 
    st.session_state.option=option

def load_view():
    st.title('SCSE Faculty')

    st.markdown(scse_fac_profile())
    researchareas_view = f'<div class="miniheader">Research Areas</div>'
    st.markdown(researchareas_view, unsafe_allow_html=True)
    st.write('')

    col1, col2 = st.columns(2)

    with col1: 
        with st.expander("Hardware and Embedded Systems"):
            research.load_view(0)
        with st.expander("Cyber Security and Forensics"):
            research.load_view(1)
        with st.expander("Artificial and Augmented Intelligence"):
            research.load_view(2)
        with st.expander("Computational Intelligence"):
            research.load_view(3)
        with st.expander("Computer Vision and Sensing"):
            research.load_view(4)

    with col2: 
        with st.expander("Graphics and Interactive Computing"):
            research.load_view(5)
        with st.expander("Computer Networks and Communications"):
            research.load_view(6)
        with st.expander("Parallel and Distributed Computing"):
            research.load_view(7)
        with st.expander("Biomedical Sciences  Life Sciences"):
            research.load_view(8)

    st.markdown(f'<hr style=margin-top:3px;margin-bottom:3px>', unsafe_allow_html=True)
    compare_view = f'<div class="miniheader">Comparison with NUS School of Computing Research Profile</div>'
    st.markdown(compare_view, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1: 
        format_func('NTU')
    with col2: 
        format_func('NUS')
    st.write('While NTU SCSE has a smaller researcher faculty compared to NUS SOC, the division of resources is more even as can be seen from the pie charts above. It can be seen that both faculties have placed a large emphasis on Artificial Intelligence, while less focus is placed on research for Biological Sciences. One aspect that SCSE\'s research faculty could be lacking is the media aspect.')

