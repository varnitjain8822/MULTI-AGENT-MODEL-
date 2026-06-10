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
  "search the web for recent and reliabele information"
  result=tavily.search(query=query,max_results=5)
  out=[]
  for r in result['results']:
    out.append(
      f"Title: {r['title']}\nURL: {r['url']}\nSnippet: {r['content'][:300]}\n"
    )
  return "\n----\n".join(out)

print(websearch.invoke("recent result of war") )


# mistral ai model
'''model = ChatMistralAI(model="mistral-small-2506", temperature=0.9)
response = model.invoke("can u generate image of rahul gandhi")
print(response.content)
'''

