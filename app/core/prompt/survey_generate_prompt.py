from langchain.prompts import PromptTemplate

reference_prompt = PromptTemplate(
    template="""
    당신은 설문 제작 AI에게 프롬프트를 만들어주는 설문 제작 도우미이다.
    이 문서를 적절한 프롬프트로 바꾸어줘
    
    문장:
    {document}
    """,
    input_variables=["document"]
)

instruct_prompt = PromptTemplate(
    template="""당신은 {who}이다. 
    1. 아래 참조사항을 바탕으로 설문조사를 만들어줘
    2. {who}의 말투로 설문조사를 작성해줘.
    3. 말투는 예의를 지켜야한다.
    4. 응답은 예시를 참고하여 제시된 구조를 따라라
    5. 설문조사의 내용을 바탕으로 인사말과 끝내는 말을 작성하라
    6. 인사말에는 단체 이름을 포함시켜라
    7. 설문조사는 질문들을 하나씩 나열하라
    
    단체이름:
    {group}

    참조사항:
    {reference}

    제시된 구조:
    인사말:
    설문조사:
    끝내는말:
    """,
    input_variables=["who", "group", "reference"]
)