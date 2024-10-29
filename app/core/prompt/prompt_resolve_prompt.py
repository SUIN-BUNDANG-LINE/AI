from langchain.prompts import PromptTemplate

prompt_resolve_prompt = PromptTemplate(
    template="""
    사용자 프롬프트에서 ai가 모를 것 같은 정보를 인터넷 검색을 통해 알아내려고한다.
    너는 인터넷 검색을 위해 검색이 잘 될것 같은 키워드를 딱 하나 제공해야한다. 
    키워드는 사용자 프롬프트에 주어진 단어들로만 조합해서 만드시오.
        
    ### 사용자 프롬프트
    {user_prompt}
    
    ### Output
    -
    """,
    input_variables=["user_prompt"],
)
