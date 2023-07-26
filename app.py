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
    st.image("static/logo.png")
with col2:
    st.title('Complaint Matching with QdrantDB')
    selected = option_menu("", ["About", "Complaint Matching",],
                           icons=["caret-right-fill", "caret-right-fill", "caret-right-fill", "caret-right-fill", "caret-right-fill"], menu_icon="cast", orientation="horizontal", styles={
        "container": {"background-color": "#6cd4f4", "border-radius": "0"},
        "nav-link": {"font-size": "24px", "color": "#FFF", "font-family": "'Open Sans', sans-serif", "font-weight": "600", "--hover-color": "#999999"},
        "nav-link-selected": {"background-color": "#fff", "color": "#333333"}
    }, default_index=0)


if selected == "Complaint Matching":
    conn = st.experimental_connection('qdrant_db', type=QdrantConnection)

    st.write(conn.get_collections())

    st.write(conn.cursor().get_collections())
    encoder = SentenceTransformer('all-MiniLM-L6-v2')

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
