import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_community.document_loaders import WebBaseLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langserve import add_routes
from pydantic import BaseModel
from dotenv import load_dotenv
load_dotenv()

# Document loading functions
def get_documents_from_web(url):
    loader = WebBaseLoader(url)
    docs = loader.load()
    splitter = RecursiveCharacterTextSplitter()
    return splitter.split_documents(docs)

def get_document_from_file(file):
    document_loader = PyPDFLoader(file)
    documents = document_loader.load()
    splitter = RecursiveCharacterTextSplitter()
    split_docs = splitter.split_documents(documents)
    for doc in split_docs:
        if "founded" in doc.page_content.lower():
            doc.metadata['relevance'] = 'founding_date'
        else:
            doc.metadata['relevance'] = 'general_info'
    return split_docs

# Load documents once at startup
relevant_info = get_documents_from_web("https://www.promtior.ai/")
relevant_info.extend(get_document_from_file("AI Engineer.pdf"))

# Model and prompt setup
model = ChatOpenAI(
    model='gpt-3.5-turbo',
    temperature=0
)

# Define prompt template with context
system_template = (
    "Acts as an expert assistant to the Promtior company and answers users' questions using the context information provided.\n"
    "Context: {context}\n"
    "Question: {input}"
)

prompt = ChatPromptTemplate.from_template(system_template)

# Create the chain
chain = create_stuff_documents_chain(llm=model, prompt=prompt)

# Create the FastAPI application
app = FastAPI(
    title="Promtior Chatbot Server",
    version="1.0",
    description="An API server for the Promtior chatbot using LangChain",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.getenv("FRONTEND_URL")],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Endpoint to accept only a text question from the user
class Question(BaseModel):
    input: str

@app.post("/chatbot")
def chatbot_endpoint(question: Question):
    # Pass relevant_info as context directly
    response = chain.invoke({"input": question.input, "context": relevant_info})
    return {"response": response}

# Add playground route
add_routes(app, chain, path="/chain")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)