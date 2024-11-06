from langchain.prompts import PromptTemplate


improve_user_prompt_with_searched_result_prompt = PromptTemplate(
    template="""
    search result를 활용하여 user prompt에 어울리는 예시를 만들어주세요
    예시만 출력하세요
    
    ### User Prompt
    {user_prompt}
    
    ### search result
    {search_result}
    
    ### Output
    - 
    """,
    input_variables=["user_prompt", "search_result"],
)
