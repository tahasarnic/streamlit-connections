# ---PACKAGES---
from streamlit.connections import ExperimentalBaseConnection
from streamlit.runtime.caching import cache_data
from qdrant_client import QdrantClient, models
import pandas as pd


class QdrantConnection(ExperimentalBaseConnection[QdrantClient]):
    # Connect to qdrant
    def _connect(self, **kwargs) -> QdrantClient:
        """
        Pass a local path for testing,
        Pass a host and port for server connection,
        Pass url and api key for cloud connection
        you can both use secret.toml or inputs for the variables 
        """
        if 'path' in kwargs:
            path = kwargs.pop('path')
            return QdrantClient(path=path)
        elif 'host' in kwargs & 'port' in kwargs:
            host = kwargs.pop('host')
            port = kwargs.pop('port')
            return QdrantClient(host=host, port=port)
        elif 'url' in kwargs and 'api_key' in kwargs:
            url = kwargs.pop('url')
            api_key = kwargs.pop('api_key')
            return QdrantClient(url=url, api_key=api_key)
        elif 'path' in list(self._secrets.keys()):
            path = self._secrets['path']
            return QdrantClient(path=path)
        elif 'host' in list(self._secrets.keys()) and 'port' in list(self._secrets.keys()):
            host = self._secrets['host']
            port = self._secrets['port']
            return QdrantClient(host=host, port=port)
        elif 'url' in list(self._secrets.keys()) and 'api_key' in list(self._secrets.keys()):
            url = self._secrets['url']
            api_key = self._secrets['api_key']
            return QdrantClient(url=url, api_key=api_key)
        else:
            return QdrantClient(":memory:")

    # Cursor for using qdrant client methods
    def cursor(self) -> QdrantClient:
        return self._instance

    # Viewing created collections
    def get_collections(self):
        return self._instance.get_collections()

    # Creating a collection
    def create_collection(self, collection_name: str, size: int, distance_type=models.Distance.COSINE):
        self._instance.recreate_collection(
            collection_name=collection_name,
            vectors_config=models.VectorParams(
                size=size,  # Vector size is defined by used model
                distance=distance_type
            )
        )

    # Uploading vectors to collection
    def upload_vectors(self, collection_name: str, vector: list = None, documents: list = None):
        self._instance.upload_records(
            collection_name=collection_name,
            records=[
                models.Record(
                    id=idx,
                    vector=vec,
                    payload=doc
                ) for idx, (doc, vec) in enumerate(zip(documents, vector))
            ]
        )

    # Query
    def query(self, collection_name: str, query: list, limit: int = 5, **kwargs) -> pd.DataFrame:
        hits = self._instance.search(
            collection_name=collection_name,
            query_vector=query,
            limit=limit
        )
        results = []
        for i in range(len(hits)):
            results.append(hits[i].payload)

        return pd.DataFrame(results)
