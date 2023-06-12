# https://python.langchain.com/en/latest/getting_started/getting_started.html

from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
) 

# print("open-ai api key")
 
llm = ChatOpenAI(temperature=0,
                 model_name="gpt-3.5-turbo",
                 openai_api_key="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")

messages = [
    SystemMessage(content="You are a helpful assistant that translates English to French."),
    HumanMessage(content="I love programming.")
]

print( llm(messages) )
# -> AIMessage(content="J'aime programmer.", additional_kwargs={})
