from langchain_core.prompts import ChatPromptTemplate, PromptTemplate


def get_prompt(prompt_type="chat_basic", parser=None):
    """
    Central prompt factory for the entire project.
    Clean, extensible, production-grade.
    """

    prompt_type = prompt_type.lower()

    # ---------------------------
    # 1. Simple Chat Prompt
    # ---------------------------
    if prompt_type == "chat_basic":
        return ChatPromptTemplate.from_messages([
            ("system", "You are a helpful AI assistant."),
            ("human", "{input}")
        ])

    # ---------------------------
    # 2. Simple Text PromptTemplate
    # ---------------------------
    if prompt_type == "text_basic":
        return PromptTemplate(
            input_variables=["input"],
            template="Explain {input} in simple terms."
        )

    # ---------------------------
    # 3. Structured Chat Prompt (Pydantic/JSON parser aware)
    # ---------------------------
    if prompt_type == "structured_chat":
        if parser is None:
            raise ValueError("Parser is required for structured prompts")

        format_instructions = parser.get_format_instructions()

        return ChatPromptTemplate.from_messages([
            ("system", "You must follow the output format strictly."),
            ("human", """
            Explain the following topic:
            {input}
            {format_instructions}
            """)
        ]).partial(format_instructions=format_instructions)

    # ---------------------------
    # 4. Structured Text PromptTemplate
    # ---------------------------
    if prompt_type == "structured_text":
        if parser is None:
            raise ValueError("Parser is required for structured prompts")

        format_instructions = parser.get_format_instructions()

        return PromptTemplate(
            input_variables=["input"],
            template="""
            Explain the following topic:

            {input}

            {format_instructions}
        """
        ).partial(format_instructions=format_instructions)

    raise ValueError(f"Unknown prompt type: {prompt_type}")
