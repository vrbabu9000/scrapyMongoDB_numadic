import streamlit as st
from multiapp import MultiApp
from apps import scraped_data, search_data, home
import pymongo

app = MultiApp()

st.markdown("""
# Scrapy-News Project
#### by Vignesh R Babu

This is a small project done as per the rules stated for getting a Data Science internship at Numadic, Goa.
This is a quick-no-revison work. PS Errors might be there.

""")

# Add all your application here
app.add_app("Home", home.app)
app.add_app("Scraped Data", scraped_data.app)
app.add_app("Search Database", search_data.app)

#Define MongoDB client
client = pymongo.MongoClient("mongodb+srv://babu:babu@babu-cluster0.v2wpr.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

@st.cache
def get_data():
    items = client['babu-cluster0']['news_scrapy_numadic'].find()
    return items
# The main app
app.run()
