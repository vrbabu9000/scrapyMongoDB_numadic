import streamlit as st
import pandas as pd
import pymongo
client = pymongo.MongoClient("mongodb+srv://babu:babu@babu-cluster0.v2wpr.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

def app():
    st.markdown('## Scraped Data')

    st.write("This data was extracted from indiatoday website using scrapy")

    st.write("The following is the DataFrame of the Scraped data loaded from MongoDB.")

    def get_data():
        items = client['babu-cluster0']['news_scrapy_numadic'].find()
        return items

    items = list(get_data())

    df = pd.DataFrame.from_records(items)
    df.drop('_id',axis=1,inplace=True)
    st.write(df)
