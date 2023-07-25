import streamlit as st
import pandas as pd
from json import loads
from sentence_transformers import SentenceTransformer
from qdrant_connection import QdrantConnection
from qdrant_client import models

conn = st.experimental_connection('qdrant_db', type=QdrantConnection)

st.write(conn.get_collections())

st.write(conn.cursor().get_collections())

conn.create_collection(collection_name='new_collection', size = 384, distance_type = models.Distance.COSINE)

df = pd.read_csv('complaints.csv')
df = df.dropna()
documents = loads(df.to_json(orient = 'records'))
text = [{'text':doc['text']} for doc in documents]

encoder = SentenceTransformer('all-MiniLM-L6-v2')

@st.cache_data(ttl = 3600)
def get_embeddings(text):
    embedding = []
    for i in range(len(text)):
        embedding.append(encoder.encode(text[i]['text']).tolist())
    return embedding


conn.upload_vectors(collection_name='new_collection', vector = get_embeddings(text), documents = documents)

myquery = encoder.encode("comcat is bad").tolist()
st.dataframe(conn.query(collection_name='new_collection', query=myquery, limit = 5))