from langchain.tools import tool
import requests
from bs4 import BeautifulSoup
from tavily import TavilyClient
import os
import urllib.parse
from dotenv import load_dotenv

load_dotenv()

def get_tavily_client(api_key: str = None) -> TavilyClient | None:
    key = api_key or os.getenv("TAVILY_API_KEY")
    if key and key.strip():
        try:
            return TavilyClient(api_key=key.strip())
        except Exception as e:
            print(f"Warning initializing Tavily client: {e}")
            return None
    return None

def fallback_web_search(query: str, max_results: int = 5) -> str:
    """Fallback search using DuckDuckGo HTML endpoint when Tavily key is not configured."""
    try:
        encoded = urllib.parse.quote_plus(query)
        url = f"https://html.duckduckgo.com/html/?q={encoded}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        resp = requests.get(url, headers=headers, timeout=8)
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.text, "html.parser")
            results = []
            for r in soup.select(".result"):
                title_elem = r.select_one(".result__title")
                snippet_elem = r.select_one(".result__snippet")
                url_elem = r.select_one(".result__url")
                if title_elem and snippet_elem:
                    title = title_elem.get_text(strip=True)
                    snippet = snippet_elem.get_text(strip=True)
                    href = url_elem.get_text(strip=True) if url_elem else "https://duckduckgo.com"
                    results.append(f"Title: {title}\nURL: {href}\nSnippet: {snippet[:300]}\n")
                    if len(results) >= max_results:
                        break
            if results:
                return "\n----\n".join(results)
    except Exception as e:
        print(f"Fallback search warning: {e}")

    return f"No live search results available for query: '{query}'. Please check network or provide TAVILY_API_KEY."

@tool
def web_search(query: str) -> str:
    """Search the web for recent and reliable information on a topic. Returns Titles, URLs and snippets."""
    client = get_tavily_client()
    if client:
        try:
            results = client.search(query=query, max_results=5)
            out = []
            for r in results.get('results', []):
                out.append(
                    f"Title: {r.get('title', 'Untitled')}\nURL: {r.get('url', '')}\nSnippet: {r.get('content', '')[:300]}\n"
                )
            if out:
                return "\n----\n".join(out)
        except Exception as e:
            print(f"Tavily search exception, falling back: {e}")

    return fallback_web_search(query, max_results=5)

@tool
def scrape_url(url: str) -> str:
    """Scrape and return clean text content from a given URL for deeper reading."""
    try:
        resp = requests.get(url, timeout=8, headers={"User-Agent": "Mozilla/5.0"})
        if resp.status_code != 200:
            return f"Failed to fetch {url} (HTTP {resp.status_code})"
        soup = BeautifulSoup(resp.text, "html.parser")
        for tag in soup(["script", "style", "nav", "footer", "header", "noscript"]):
            tag.decompose()
        text = soup.get_text(separator=" ", strip=True)
        return text[:4000] if text else "No text extracted from page."
    except Exception as e:
        return f"Could not scrape URL: {str(e)}"
