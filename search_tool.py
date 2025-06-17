import os
from tavily import TavilyClient
from cachetools import TTLCache
import functools
from typing import TypedDict, List, Dict, Any

TavilyResponse = TypedDict('TavilyResponse', {
    'results': List[Dict[str, Any]]
})

cache = TTLCache(maxsize=100, ttl=3600)

tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@functools.lru_cache(maxsize=100)
def cached_search(query: str) -> TavilyResponse:
   return tavily.search(query=query, max_results=2)