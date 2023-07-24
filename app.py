import streamlit as st
from qdrant_connection import QdrantConnection

conn = st.experimental_connection('qdrant_db', type=QdrantConnection)