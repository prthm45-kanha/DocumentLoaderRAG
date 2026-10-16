from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader

loader=DirectoryLoader(
    path='Books',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

docs=loader.lazy_load() # for bigDataset
##docs=loader.load() for smallDataset
print(len(docs))

print(docs[34].page_content)
print(docs[34].metadata)

for documents in docs:
    print(documents.metadata)