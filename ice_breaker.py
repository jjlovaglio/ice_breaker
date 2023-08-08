# import os
import requests
from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from third_parties import linkedin


if __name__ == "__main__":
    print("hello LangChain")

    summary_template = """
        given the Linkedin information {information} about a person from I want you to create:
        1. a short summary
        2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    ### Scraping of data using ProxyURL (uses credits!) ###
    # linkedin_data = linkedin.scrape_linkedin_profile(linkedin_profile_url='https://www.linkedin.com/in/aldana-m-09581a59/')

    ### Scraping of data using Github Gist (free) ###
    data = requests.get(
        "https://gist.githubusercontent.com/jjlovaglio/e71125a9429ea77f0c6de68c2c4b4f17/raw/e58d9b196027324cab78598bb964b1dd3ab38639/jose-lovaglio.json"
    )
    linkedin_gist_data = data.json()
    # print(linkedin_gist_data)

    print(chain.run(information=linkedin_gist_data))
