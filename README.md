# Promtior Chat Bot Challenge

## This is a simple chatbot that can answer some questions about the Promtior company.

## Project Overview

This project implements a chatbot assistant based on the RAG (Retrieval Augmented Generation) architecture to answer questions about the company Promtior. The solution uses the **LangChain** library for the response generation chain and **LangServe** for deployment. The chatbot retrieves information from two sources: the Promtior website and a provided PDF file. This information serves as context to answer questions about the company’s services, founding date, and other key features.

The chatbot development involved several stages:
1. **Information Retrieval** from the web and PDF.
2. **Document Splitting** to optimize processing and tagging of relevant sections.
3. **Response Generation** using `ChatOpenAI` with a custom prompt.

### Main Challenges and Solutions
- **Integrating Multiple Sources**: It was necessary to combine documents from different sources, both the website and a PDF file, to ensure that the context provided to the chatbot was comprehensive.
- **Handling Specific Context**: To accurately answer specific questions (such as the founding date), sections of the PDF were tagged, making it easier for the model to find precise answers.
- **Prompt Optimization**: A custom prompt was created to guide the model to use the provided context, improving response quality.

## Architecture and Components

### Component Diagram

Below is a diagram showing the system components and their interactions, from receiving a question to generating the response.

![Component Diagram](path/to/diagram.png) <!-- Insert the diagram here after creating it in Draw.io or Lucidchart -->

### System Components

1. **API Endpoint**:
   - A `/chatbot` endpoint is exposed through FastAPI to receive questions from users and return answers based on the context. An additional `/chain` route is provided for playground access.

2. **Document Retrieval Functions**:
   - `get_documents_from_web(url)`: Uses `WebBaseLoader` to extract content from the Promtior website and splits it into manageable chunks.
   - `get_document_from_file(file)`: Uses `PyPDFLoader` to load and split a PDF file, tagging relevant sections (e.g., those related to the company's founding) to improve context accuracy.

3. **Language Model**:
   - `ChatOpenAI`: The OpenAI `gpt-3.5-turbo` model is configured with `temperature=0` to generate precise answers based on the provided context.

4. **Generation Pipeline (LangChain)**:
   - `create_stuff_documents_chain`: Utilizes the language model along with the generated context from the documents to answer the user’s questions.

## Usage

### Installation

1. Clone the repository.
   ```bash
   git clone https://github.com/insaurraldef/PromtiorChatBot.git
    cd PromtiorChatBot
    ```
2. Install the required packages.
3. Create an .env file in the project directory with the following variables:
    ```bash
    OPENAI_API_KEY=your_openai_api_key
    ```
4. Run the FastAPI server:
    ```bash
    python server.py
    ```
   or
    ```bash
    python3 server.py
    ```
   The API server will start on http://localhost:8000.
5. Access the `/chatbot` endpoint to interact with the chatbot.

## Usage Instructions
1.	Access the /chatbot endpoint to interact with the Promtior chatbot.
2.	Send a POST request to http://localhost:8000/chatbot with JSON data like:
   ```bash
    "input": "What services does Promtior offer?"
   ```
The chatbot will respond with an answer based on the context retrieved from the website and PDF file.
3.	Enjoy interacting with the Promtior chatbot assistant!
