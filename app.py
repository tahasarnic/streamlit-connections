import streamlit as st
from sentence_transformers import SentenceTransformer
from qdrant_connection import QdrantConnection
from streamlit_option_menu import option_menu

#from qdrant_client import models
#import pandas as pd
#from json import loads
st.set_page_config(page_title="Complaint Matching",
                   layout="wide", initial_sidebar_state="collapsed")

# Title
col1, col2 = st.columns([1, 5])
with col1:
    st.image("Static/logo.png")
with col2:
    selected = option_menu("Complaint Matching with QdrantDB", ["Home", "Complaint Matching",],
                           icons=["caret-right-fill", "caret-right-fill"], menu_icon="cast", orientation="horizontal", styles={
        "container": {"background-color": "#6cd4f4", "border-radius": "0"},
        "menu-title": {"font-size": "24px", "color": "#333", "font-family": "'Open Sans', sans-serif", "font-weight": "600"},
        "nav-link": {"font-size": "24px", "color": "#FFF", "font-family": "'Open Sans', sans-serif", "font-weight": "500", "--hover-color": "#333"},
        "nav-link-selected": {"background-color": "#fff", "color": "#333"}
    }, default_index=0)

encoder = SentenceTransformer('all-MiniLM-L6-v2')  # encoder choice for vectors


if selected == "Home":
    st.markdown(""" 
## What is the aim of this project?
A demo  to show how to connect to QdrantDB within streamlit.

## What is Complaint Matching?
Complaints/tickets are a huge part of customer service in several industries even outside of tech. 
To find answers quickly people should be able to see similar problems that opened before.
                
In the second page, you can write your complaints to see the similar problems that opened before. 
Have fun playing with it :smile:
                
## How to connect?
You can use the QdrantConnection class inside connections.py file. Check the file for more detailed information.
                
1. Call *st.experimantal_connection* inside your project with type = QdrantConnection & assign it to a variable.
                
    :warning: Do not forget giving a name such as 'qdrant_db'
                
2. Use st.secrets for connection inputs.
    * pass a local path as *path* for testing
    * pass a *host* and *port* for personal server connection
    * pass a *url* & *api_key* for cloud connection
                
3. View the generated collections by *get_collections* function. OR create your own vector database by *create_collections* function.
                
    :mag_right: **Tip**: Use *upload_vectors* to upload your own database.

4. Query most similar results by *query*, change parameters as you fit. 
                
    :mag_right: **Tip**: The results will be returned as DataFrame.

                
### What is in the data?
A csv file with more than 5000 unique public complaints made about Comcast internet and television service in October 2016.
                
The source: [Kaggle Comcast Consumer Complaints](https://www.kaggle.com/datasets/archaeocharlie/comcastcomplaints)
""")

if selected == "Complaint Matching":
    conn = st.experimental_connection(
        'qdrant_db', type=QdrantConnection, database=':memory')

    st.write(conn.get_collections())

    st.write(conn.cursor().get_collections())

    # """
    # You can use the following example to how to upload new documents to vector database such as qdrant

    # conn.create_collection(collection_name='new_collection',
    #                        size=384, distance_type=models.Distance.COSINE)

    # df = pd.read_csv('complaints.csv')
    # df = df.dropna()
    # documents = loads(df.to_json(orient = 'records'))
    # text = [{'text':doc['text']} for doc in documents]

    # @st.cache_data(ttl = 3600)
    # def get_embeddings(text):
    #     embedding = []
    #     for i in range(len(text)):
    #         embedding.append(encoder.encode(text[i]['text']).tolist())
    #     return embedding

    # conn.upload_vectors(collection_name='new_collection', vector = get_embeddings(text), documents = documents)
    # """
    myquery = encoder.encode("comcat is bad").tolist()
    st.dataframe(conn.query(
        collection_name='comcat-complaints', query=myquery, limit=5))
