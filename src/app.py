from dotenv import load_dotenv
load_dotenv()

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

def get_documents_from_web(url):
    loader = WebBaseLoader(url)
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter()
    splitDocs = splitter.split_documents(docs)
    return splitDocs

def get_document_from_file(file):
    document_loader = PyPDFLoader(file)
    documents = document_loader.load()

    # Divide y etiqueta contenido de los documentos
    splitter = RecursiveCharacterTextSplitter()
    split_docs = splitter.split_documents(documents)

    # Opcional: etiquetar cada sección si tienes conocimiento de qué partes mencionarían la fundación
    for doc in split_docs:
        if "founded" in doc.page_content.lower():
            doc.metadata['relevance'] = 'founding_date'
        else:
            doc.metadata['relevance'] = 'general_info'

    return split_docs

relevant_info = get_documents_from_web("https://www.promtior.ai/")
relevant_info.extend(get_document_from_file("AI Engineer.pdf"))

model = ChatOpenAI(
    model='gpt-3.5-turbo',
    temperature=0
)

prompt = ChatPromptTemplate.from_template(
"Answer the user's question:"
"Context: {context}"
"Question: {input}"
)

chain = create_stuff_documents_chain(llm=model, prompt=prompt)

def ask_question(question):
    response = chain.invoke({"input": question, "context": relevant_info})
    return response


def main():
    while True:
        print("\n--- Menu ---")
        print("1. What services does Promtior offer?")
        print("2. When was the company founded?")
        print("3. Who founded Promtior?")
        print("4. What companies work with Promtior?")
        print("5. Ask a custom question")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            question = "What services does Promtior offer?"
            response = ask_question(question)
            print("\nResponse: ", response)
        elif choice == "2":
            question = "When was the company founded?"
            response = ask_question(question)
            print("\nResponse: ", response)
        elif choice == "3":
            question = "Who founded Promtior?"
            response = ask_question(question)
            print("\nResponse: ", response)
        elif choice == "4":
            question = "What companies work with Promtior?"
            response = ask_question(question)
            print("\nResponse: ", response)
        elif choice == "5":
            question = input("Write your question: ")
            response = ask_question(question)
            print("\nResponse: ", response)
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Error. Try again")


# Ejecuta el menú
if __name__ == "__main__":
    main()