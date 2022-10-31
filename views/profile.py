import streamlit as st
import pandas as pd
import math
import plotly.express as px
from collections import OrderedDict
from PIL import Image
from utils import string_to_list

def select_prof(index):
    df = pd.read_csv('newdf1.csv')
    prof_selected = df.iloc[index]
    name = prof_selected['Full Name']
    title = prof_selected['Title']
    biography = prof_selected['biography']
    image_path = prof_selected['images']
    keys = prof_selected['keywords']
    keywords = string_to_list(keys)
    citations = prof_selected['No. of Citations']
    papers_per_year = eval(prof_selected['papers_per_year'])
    citations_per_year = eval(prof_selected['citations_per_year'])
    ntu_url = prof_selected['DR-NTU URL']
    email = prof_selected['Email']
    website_url = prof_selected['Website URL']
    ntu_count = prof_selected['ntu_count']
    sg_count = prof_selected['sg_count']
    total_count = prof_selected['total_count']
    ntu_coauthors = prof_selected['ntu_co']
    ntu_coauthors = string_to_list(ntu_coauthors)

    return name, title, biography, image_path, keywords, citations, papers_per_year, citations_per_year, ntu_url, email, website_url, ntu_count, sg_count, total_count, ntu_coauthors

def load_view(index):
    name, title, biography, image_path, keywords, citations, papers_per_year, citations_per_year, ntu_url, email, website_url, ntu_count, sg_count, total_count, ntu_coauthors = select_prof(index)

    title_container = f'<div class="title">{title} {name}</div'
    st.markdown(title_container, unsafe_allow_html=True)
    st.write('')

    col1, col2 =  st.columns([4,7])

    with col1:
        header_container = f'<div class="header">Profile</div'
        st.markdown(header_container, unsafe_allow_html=True)
        # photo of prof
        image = Image.open('./' + image_path)

        st.image(image)

        if type(biography)==str: 
            bio_container = f'<div class="biography">{biography}</div>'
            st.markdown(bio_container, unsafe_allow_html=True)

        st.write('')
        if email!= None: 
            st.markdown(f'''
                <a href=mailto:{email}>
                    <button style="background-color:#F0F8FF; border-color:#D3D3D3; border-radius: 8px; padding: 10px;
                            width: 250px; font-size: 16px;">
                        Email
                    </button>
                </a>
                ''',
                unsafe_allow_html=True)

        st.write(' ')
        if ntu_url!= None: 
            st.markdown(f'''
                <a href={ntu_url}>
                    <button style="background-color:#F0F8FF; border-color:#D3D3D3; border-radius: 8px; padding: 10px;
                            width: 250px; font-size: 16px;">
                        DR-NTU URL
                    </button>
                </a>
                ''',
                unsafe_allow_html=True)

        if type(website_url) == str: 
            st.write(' ')
            st.markdown(f'''
                <a href={website_url}>
                    <button style="background-color:#F0F8FF; border-color:#D3D3D3; border-radius: 8px; padding: 10px;
                            width: 250px; font-size: 16px;">
                        Personal Website URL
                    </button>
                </a>
                ''',
                unsafe_allow_html=True)


    with col2:
        header_container = f'<div class="header">Research Profile</div'
        st.markdown(header_container, unsafe_allow_html=True)

        if len(keywords)>1: 
            citations_view = f'<div class="miniheader">Keywords</div>'
            st.markdown(citations_view, unsafe_allow_html=True)
            s=''
            for i in keywords:
                s += "- " + i + "\n"
            st.markdown(s)

        if math.isnan(citations) == False: 
            citations = int(citations)
            citations_view = f'<div class="miniheader">Total Citations: {citations}</div>'
            st.markdown(citations_view, unsafe_allow_html=True)
       

        if len(papers_per_year.keys())>1: 
            chart_data = pd.DataFrame()
            chart_data['Years'] = papers_per_year.keys()
            chart_data['Papers'] = papers_per_year.values()
            chart_data['Citations'] = citations_per_year.values()

            line_chart = px.line(chart_data,
                x = 'Years',
                y = ['Papers', 'Citations'],
                labels = ['Year', 'Count'],
                title='Number of Papers and Citations per Year')

            st.plotly_chart(line_chart, unsafe_allow_html=True, use_container_width=True)

        if total_count>0: 
            coauthors_view = f'<div class="miniheader">Coauthors</div>'
            st.markdown(coauthors_view, unsafe_allow_html=True)

            coauthors = ['Total', 'Singapore', 'NTU'] + ntu_coauthors
            parent = ['', 'Total', 'Singapore'] + ['NTU']*len(ntu_coauthors)
            count = [total_count, sg_count, ntu_count] + [1]*len(ntu_coauthors)
        
            coauthors_data = dict(
                Coauthors = coauthors, 
                Subset = parent, 
                Count = count
            )
            fig = px.sunburst(
                coauthors_data,
                names='Coauthors',
                parents='Subset',
                values='Count',
                color='Coauthors', 
                color_continuous_scale='RdBu'
            )
            st.plotly_chart(fig, unsafe_allow_html=True, use_container_width=True)
        
    return (name)