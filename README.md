# Document-Q-A-with-GPT-LLM-LangChain-
Document Q&amp;A with GPT using LangChain enables users to ask questions about specific documents, leveraging large language models to extract and generate accurate answers. LangChain integrates tools like document loaders and vector databases to retrieve relevant context and enhance response quality.

# Document Q&A with GPT (LangChain)

## Setup
1. Install dependencies:
   pip install -r requirements.txt

# OpenAI API KEY IS PAID : So You Can Use Own openAI API Key ( General Cost IS 5$ Strarting )
2. Add your OpenAI API key in `app.py`:
   os.environ["OPENAI_API_KEY"] = "your-api-key-here"

3. Run the script:
   python app.py

## What it does
- Loads a PDF
- Converts it to embeddings
- Lets you ask GPT questions only based on that document
