import streamlit as st
import pymongo
client = pymongo.MongoClient("mongodb+srv://babu:babu@babu-cluster0.v2wpr.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

def app():
    st.title('Top News India')
    st.write('Scrapy-scarped and MongoDB-stored newsfeed')

    def get_data():
        items = client['babu-cluster0']['news_scrapy_numadic'].find()
        return items


    items = get_data()
    data_load_state = st.text('Loading data...')

    # Print results.
    for item in items:
        st.markdown(f"""
        ### {item['title']} 
        {item['content']}""")
        st.text("")
        st.markdown(f"""
        {item['url']}""")
    data_load_state.text('Loading data...done!')