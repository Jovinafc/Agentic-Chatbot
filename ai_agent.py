import os

#Setting up API Keys.
GROQ_API_KEY=os.environ.get('GROQ_API_KEY')
TAVILY_API_KEY=os.environ.get('TAVILY_API_KEY')
OPENAI_API_KEY=os.environ.get('OPENAI_API_KEY')
#Tavily Code - CVYFXZLPQWTH3KCNKF5HVV8T


#Setting LLM Tools
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
# from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_tavily import TavilySearch

openai_llm = ChatOpenAI(model="gpt-4o-mini")
groq_llm = ChatGroq(model='meta-llama/llama-4-scout-17b-16e-instruct')

search_tool = TavilySearch(max_results=2)

#Setting up AI Agents

from langgraph.prebuilt import create_react_agent
from langchain_core.messages.ai import AIMessage

system_prompt = 'Act an an AI chatbot who is smart and friendly.'

def get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider):
    if provider == "Groq":
        llm = ChatGroq(model=llm_id)
    elif provider == "OpenAI":
        llm = ChatOpenAI(model=llm_id)
        
    tools = [TavilySearch(max_results=2)] if allow_search else []
        
    agent = create_react_agent(
        model = llm,
        tools=tools,
        prompt=system_prompt
    )

    # query = 'Tell me about the trends in crypto markets'
    # query = 'Top 10 Best Test Cricket Batsmen'
    state={"messages": query}
    response = agent.invoke(state)
    messages = response.get("messages")
    ai_messages = [message.content for message in messages if isinstance(message, AIMessage)]
    print(ai_messages[-1])
    
    return ai_messages[-1]



