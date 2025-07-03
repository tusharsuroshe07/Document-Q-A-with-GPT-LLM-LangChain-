import os
from langchain.document_loaders import PyPDFLoader
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

# Set your OpenAI API key
os.environ["OPENAI_API_KEY"] = "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"

# Load PDF
loader = PyPDFLoader("sample.pdf")
pages = loader.load_and_split()

# Create embeddings
embeddings = OpenAIEmbeddings()
db = FAISS.from_documents(pages, embeddings)

# Setup retriever
retriever = db.as_retriever()

# Build QA chain
qa = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(model_name="gpt-3.5-turbo"),
    chain_type="stuff",
    retriever=retriever
)

# Ask your question
query = "What is this document about?"
result = qa.run(query)
print("Answer:", result)
