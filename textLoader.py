from langchain_community.document_loaders import TextLoader
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

loader=TextLoader('cricket.txt',encoding='utf-8')
docs=loader.load()

print(len(docs))
print(type(docs[0]))
print(docs[0].page_content) 
print(docs[0].metadata)

chain=prompt | model | parser
print(chain.invoke({'poem':docs[0].page_content}))