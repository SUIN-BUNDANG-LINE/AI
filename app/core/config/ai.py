from langchain_openai import ChatOpenAI, OpenAIEmbeddings

chat = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.5,
)

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-large"
)