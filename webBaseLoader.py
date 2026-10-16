

from langchain_community.document_loaders import WebBaseLoader
url='https://www.flipkart.com/apple-macbook-air-m5-2026-m5-16-gb-512-gb-ssd-tahoe-mdh74hn-a/p/itm7780abdd2be7d?pid=COMHZQX4GXGGJHDY&marketplace=FLIPKART&lid=LSTCOMHZQX4GXGGJHDYEWXLB8&pageUID=1792134617235'

loader=WebBaseLoader(url)

docs=loader.load()

print(len(docs))
print(docs[0].page_content)