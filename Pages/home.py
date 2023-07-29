import streamlit as st


@st.cache_resource()
def create_page():

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
    return True
