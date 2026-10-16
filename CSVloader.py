from langchain_community.document_loaders import CSVLoader

loader=CSVLoader(file_path='user_purchase_data_400.csv')
data=loader.load()
print(len(data))

print(data[1])