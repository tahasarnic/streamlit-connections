from streamlit.connections import ExperimentalBaseConnection
from streamlit.runtime.caching import cache_data

from qdrant_client import models, QdrantClient


class QdrantConnection(ExperimentalBaseConnection[QdrantClient]):

    def _connect(self, **kwargs) -> QdrantClient:

        if 'database' in kwargs:

            return "return crazy person"

        else:
            server_url = self._secrets['url']
            api_key = self._secrets['api-key']

        return QdrantClient(url=server_url, api_key=api_key)
