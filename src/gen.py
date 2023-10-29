from langchain.llms import Ollama
from langchain.chains import RetrievalQA

ollama = Ollama(base_url='http://localhost:11434', model="codellama:13b")
model = "codellama:13b"
# qachain=RetrievalQA.from_chain_type(ollama, retriever=vectorstore.as_retriever())

def explain_diff(diff):
    content = diff["content"]
    systemPrompt = f"""    
    Only use the following information to answer the question. 
    - Do not use anything else
    - Do not use your own knowledge.
    - Do not use your own opinion.
    - Do not use anything that is not in the diff.
    Task: Write a git commit message for the following diff
    ```
    {content}
    ```
    """
    return ollama(systemPrompt)

