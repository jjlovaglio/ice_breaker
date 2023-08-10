from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI

from langchain.agents import initialize_agent, Tool, AgentType
from tools.tools import get_profile_url

from langchain.output_parsers import ResponseSchema
from langchain.output_parsers import StructuredOutputParser

def lookup(name: str) -> str:
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    template = """given the full name {name_of_person} I want you to get it me a link to their profile page.
                  Answer with actual url. No preface."""
    tools_for_agent = [
        Tool(
            name="Crawl Google 4 linkedin profile page",
            func=get_profile_url,
            description="useful for when you need to get the Linkedin Page URL",
        )
    ]

    agent = initialize_agent(
        tools=tools_for_agent,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
    )

    url_schema = ResponseSchema(
        name="url",
        description="The URL of a website. For example: https://www.google.com, https://medium.com, https://www.linkedin.com, ...",
    )
 
    output_parser = StructuredOutputParser.from_response_schemas([url_schema])
 
    prompt_template = PromptTemplate(
        template=template,
        input_variables=["name_of_person"],
        output_parser=output_parser,
    )

    linkedin_profile_url = agent.run(prompt_template.format_prompt(name_of_person=name))
    return linkedin_profile_url
