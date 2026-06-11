from dotenv import load_dotenv
load_dotenv()
from langchain.tools import tool
import requests
from bs4 import BeautifulSoup
from tavily import TavilyClient
import os 
from langchain_mistralai import ChatMistralAI
tavily = TavilyClient(os.getenv("TAVILY_API_KEY"))
@tool
def websearch(query:str)->str:
  "Search the web for recent and reliable information on a topic . Returns Titles , URLs and snippets."
  result=tavily.search(query=query,max_results=5)
  out=[]
  for r in result['results']:
    out.append(
      f"Title: {r['title']}\nURL: {r['url']}\nSnippet: {r['content'][:300]}\n"
    )
  return "\n----\n".join(out)


@tool
def scrape_url(url: str) -> str:
    """Scrape and return clean text content from a given URL for deeper reading."""
    try:
        resp = requests.get(url, timeout=8, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(resp.text, "html.parser")
        for tag in soup(["script", "style", "nav", "footer"]):
            tag.decompose()
        return soup.get_text(separator=" ", strip=True)[:3000]
    except Exception as e:
        return f"Could not scrape URL: {str(e)}"



print(websearch.invoke("recent result of war") )


# mistral ai model
'''model = ChatMistralAI(model="mistral-small-2506", temperature=0.9)
response = model.invoke("can u generate image of rahul gandhi")
print(response.content)
'''

