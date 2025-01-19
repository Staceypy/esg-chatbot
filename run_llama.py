from dotenv import load_dotenv

load_dotenv()
from llama_index.core.agent import ReActAgent
from llama_index.llms.openai import OpenAI
from llama_index.core.tools import FunctionTool

from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, Settings, QueryEngineTool

# using the LlamaParse class to parse pdf
from llama_parse import LlamaParse

Settings.llm = OpenAI(model="gpt-3.5-turbo", temperature=0)

# test 1
documents = SimpleDirectoryReader("./data").load_data()
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()

response = query_engine.query(
    "What was the total amount of the 2023 Canadian federal budget?"
)
print(response)

# test 2
documents2 = LlamaParse(result_type="markdown").load_data(
    "./data/2023_canadian_budget.pdf"
)
index2 = VectorStoreIndex.from_documents(documents2)
query_engine2 = index2.as_query_engine()

response2 = query_engine2.query(
    "How much exactly was allocated to a tax credit to promote investment in green technologies in the 2023 Canadian federal budget?"
)
print(response2)

# RAG
# budget_tool = QueryEngineTool.from_defaults(
#     query_engine,
#     name="canadian_budget_2023",
#     description="A RAG engine with some basic facts about the 2023 Canadian federal budget.",
# )

# agent = ReActAgent(tools=[budget_tool, FunctionTool()])

# response = agent.chat(
#     "What is the total amount of the 2023 Canadian federal budget multiplied by 3? Go step by step, using a tool to do any math."
# )

# print(response)