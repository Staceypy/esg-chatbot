# esg chatbot using RAG architecture with Langchain

This project implements a **chatbot** designed to answer customer questions regarding **ESG (Environmental, Social, and Governance) regulations and reporting**. It utilizes a **Retrieval-Augmented Generation (RAG)** architecture powered by **LangChain** and integrates vector databases for document retrieval and large language model (LLM) responses.

Once providing API keys for OPENAI and LLAMA_CLOUD, and the embeddings stored in Chroma (to be replaced by Pinecone), you can interact with the chatbot using a query-based question-answering (QA) model. You can input any query, and the system will retrieve the most relevant chunks to generate an answer using OpenAI's LLM.
