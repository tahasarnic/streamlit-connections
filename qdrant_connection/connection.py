#---PACKAGES---
from streamlit.connections import ExperimentalBaseConnection
from qdrant_client import models, QdrantClient

class QdrantConnection(ExperimentalBaseConnection[QdrantClient]):
    def _connect(self, **kwargs) -> QdrantClient:
        if 'database' in kwargs:
            db = kwargs.pop('database')
        else:
            url = self._secrets['url']
            api_key = self._secrets['api_key']
        return QdrantClient(url=url, api_key=api_key)
