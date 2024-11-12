# Promtior Chat Bot Challenge

## This is a simple chatbot that can answer some questions about the Promtior company.

### How to run the chatbot:
1. Clone the repository
2. Run the command `python3 app.py`
3. Ask the chatbot some questions about the Promtior company
4. Enjoy!
# Promtior Chatbot Assistant

## Project Overview

This project implements a chatbot assistant based on the RAG (Retrieval Augmented Generation) architecture to answer questions about the company Promtior. The solution uses the **LangChain** library for the response generation chain and **Langserve** for deployment. The chatbot retrieves information from two sources: the Promtior website and a provided PDF file. This information serves as context to answer questions about the company’s services, founding date, and other key features.

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

1. **Interactive Menu**: 
   - A console menu allows the user to select predefined questions about Promtior or ask custom questions. This menu is located in the `main()` function of the program.

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
   ```
2. Install the required packages.
   ```bash
    pip install -r requirements.txt
    ```
3. Create an .env file on the src folder with the following variables:
    ```bash
    OPENAI_API_KEY=your_openai_api_key
    ```
4. Run the application.
   ```bash
   python app.py
   ```
   or
   ```bash
   python3 app.py
   ```

### Usage Instructions

1. Run the application following the steps above.
2. Select a predefined question or ask a custom question.
3. The chatbot will process the question and provide an answer 
based on the context retrieved from the website and PDF.
4. Enjoy interacting with the Promtior chatbot assistant!