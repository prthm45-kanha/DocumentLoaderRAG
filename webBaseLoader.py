from langchain_community.document_loaders import WebBaseLoader
from langchain.chat_models import init_chat_model
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY", "")
model = init_chat_model("qwen/qwen3.8-27b", model_provider="groq")
prompt = PromptTemplate(
    template='Write a summary for the following poem - \n {poem}',
    input_variables=['poem']
)
parser=StrOutputParser()


url='https://www.flipkart.com/apple-macbook-air-m5-2026-m5-16-gb-512-gb-ssd-tahoe-mdh74hn-a/p/itm7780abdd2be7d?pid=COMHZQX4GXGGJHDY&marketplace=FLIPKART&lid=LSTCOMHZQX4GXGGJHDYEWXLB8&pageUID=1792134617235'

loader=WebBaseLoader(url)

docs=loader.load()

print(len(docs))
print(docs[0].page_content)