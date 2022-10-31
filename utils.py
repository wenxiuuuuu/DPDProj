import re
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import streamlit as st

def string_to_list(keywords): 
    keys = re.sub(r'[^\w ,]', '', keywords)
    keys = keys.split(',')
    return keys

def scse_fac_profile(): 
    profile = 'At SCSE, we believe that people are key to the success of our school. SCSE is home to more than 80 inspiring and world-renowned academics committed to excellence in teaching and research. Our faculty, who hail from top universities worldwide, teach and mentor our PhD students and undergraduates in the B.Eng (Computer Engineering) and B.Eng (Computer Science) programmes. With their diverse expertise and experience, they contribute to SCSE’s vibrant research and learning culture. These innovative and passionate talents spearhead research topics in the exciting spectrum of Computer Science and Engineering, and constantly challenge what defines the state-of-the-art in their respective fields of endeavour.'
    return profile