from llama_index import VectorStoreIndex, SimpleDirectoryReader
import os
os.environ['OPENAI_API_KEY'] = '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'
def getAnswer(question,directoryName):
    document = SimpleDirectoryReader("C:/Users/hp/Desktop/cltrH2/transciptModel/files/"+directoryName).load_data()
    index = VectorStoreIndex.from_documents(document)
    index.storage_context.persist()
    query_engine = index.as_query_engine()
    response = query_engine.query(question)
    return response


