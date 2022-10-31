import streamlit as st 
import pandas as pd 
from utils import string_to_list

def import_data(index): 
    df = pd.read_csv('nturesearch.csv')
    prof_df = pd.read_csv('newdf.csv')
    selected = df.iloc[index]
    research_area = selected['Research Areas']
    research_desc = selected['Description']
    profs = selected['Professors']
    profs = string_to_list(profs)
    prof_list = []
    for i in range(len(profs)): 
        prof_list.append(prof_df['Full Name'][int(profs[i])])
    return research_area, prof_list, research_desc

def load_view(index): 
    research_area, prof_list, research_desc = import_data(index)
    
    bio_container = f'<div class="description">{research_desc}</div>'
    st.markdown(bio_container, unsafe_allow_html=True)
    # horizontal line 
    st.markdown(f'<hr style=margin-top:3px;margin-bottom:3px>', unsafe_allow_html=True)

    st.markdown("Our Researchers: ")
    s=''
    for i in prof_list:
        s += "- " + i + "\n"
    st.markdown(s)