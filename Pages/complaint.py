import streamlit as st
from sentence_transformers import SentenceTransformer
from qdrant_connection import QdrantConnection


def create_page():
    # initialize session_state
    # encoder choice for vectors
    encoder = SentenceTransformer('all-MiniLM-L6-v2')
    conn = st.experimental_connection(
        'qdrant_db', type=QdrantConnection, database=':memory')
    st.markdown("""
    # Search Similar Complaints
    """)
    sentence = st.text_input(
        "Complaints", "Write your complaint here")
    if sentence != "":
        input_query = encoder.encode(sentence).tolist()
        st.dataframe(conn.query(
            collection_name='comcat-complaints', query=input_query, limit=5))
    st.markdown("""
    ### See the collection you are using by *get_collections*
""")
    st.write(conn.get_collections())

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
    st.markdown("""
    ### An example similarity check with the sentence 'comcat is bad'
""")
    myquery = encoder.encode("comcat is bad").tolist()
    st.dataframe(conn.query(
        collection_name='comcat-complaints', query=myquery, limit=5))
    return True
