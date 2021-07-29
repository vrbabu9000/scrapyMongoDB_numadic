import streamlit as st
import pymongo
from streamlit_tags import st_tags
import re

client = pymongo.MongoClient("mongodb+srv://babu:babu@babu-cluster0.v2wpr.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

def app():
    st.markdown('## Search Database')

    #get keywords from the user
    def key():
        keywords = st_tags(
            label='##### Enter Keywords & press Enter:',
            text='Press enter to add more',
            value=['Covid', 'police', 'India'],
            suggestions=['fire','isro'],
            maxtags=4,
            key='1')
        return keywords
    inputs = key()

    #define query function using regex (it is slow. could be speeded up using inbuilt Search Index query)
    def query(input):
        for x in input:
            result = client['babu-cluster0']['news_scrapy_numadic'].find({"content": {"$regex": f"{x}" }})
            for item in result:
                st.markdown(f"""
                ### {item['title']} 
                {item['content']}""")
                st.text("")
                st.markdown(f"""
                {item['url']}""")

    if st.button('Search'):
        df = query(inputs)
        st.write(df)












