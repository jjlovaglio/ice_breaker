# import os
from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from third_parties import linkedin

information = """
Elon Reeve Musk (Pretoria, 28 de junio de 1971), conocido como Elon Musk, es un empresario, inversor y magnate sudafricano que también posee las nacionalidades canadiense y estadounidense. Es el fundador, consejero delegado e ingeniero jefe de SpaceX; inversor ángel, director general y arquitecto de productos de Tesla, Inc.; fundador de The Boring Company; cofundador de Neuralink y OpenAI, aunque ya no tiene más participación en esta última por desacuerdos en el rumbo de la empresa, además de ser el director de tecnología de X Corp..4​ Con un patrimonio neto estimado en unos 207 mil millones de dólares en junio de 2023,5​ Musk es la persona más rica del mundo según el índice de multimillonarios de Bloomberg y la lista de multimillonarios en tiempo real de Forbes.6​7​

Musk nació de madre canadiense y padre sudafricano blanco, y se crio en Pretoria (Sudáfrica). Estudió brevemente en la Universidad de Pretoria antes de trasladarse a Canadá a los 17 años. Se matriculó en la Universidad de Queen y se trasladó a la Universidad de Pensilvania dos años después, donde se graduó en Economía y Física. En 1995 se trasladó a California para asistir a la Universidad Stanford, pero en su lugar decidió seguir una carrera empresarial, cofundando la empresa de software web Zip2 con su hermano Kimbal. La empresa fue adquirida por Compaq por 307 millones de dólares en 1999. Ese mismo año, Musk cofundó el banco online X.com, que se fusionó con Confinity en 2000 para formar PayPal. La empresa fue comprada por eBay en 2002 por 1500 millones de dólares.

En 2002, Musk fundó SpaceX, fabricante aeroespacial y empresa de servicios de transporte espacial, de la que es CEO e ingeniero jefe. En 2003, se unió al fabricante de vehículos eléctricos Tesla Motors, Inc. (ahora Tesla, Inc.) como presidente y arquitecto de productos, convirtiéndose en su consejero delegado en 2008. En 2006, ayudó a crear SolarCity, una empresa de servicios de energía solar que posteriormente fue adquirida por Tesla y se convirtió en Tesla Energy. En 2015, cofundó OpenAI, una empresa de investigación sin ánimo de lucro que promueve la inteligencia artificial amigable. En 2016, cofundó Neuralink, una empresa de neurotecnología centrada en el desarrollo de interfaces cerebro-ordenador, y fundó The Boring Company, una empresa de construcción de túneles. También acordó la compra de la importante red social estadounidense Twitter en 2022 por 44 000 millones de dólares. Musk también ha propuesto el hyperloop. En noviembre de 2021, el director general de Tesla fue la primera persona de la historia en acumular una fortuna de 300 000 millones de dólares.8​

Ha sido criticado por hacer declaraciones poco científicas y controvertidas. En 2018, fue demandado por la Comisión de Bolsa y Valores de Estados Unidos (SEC) por tuitear falsamente que había conseguido financiación para una adquisición privada de Tesla. Llegó a un acuerdo con la SEC pero no admitió su culpabilidad, renunciando temporalmente a su presidencia y aceptando limitaciones en su uso de Twitter. En 2019, ganó un juicio por difamación presentado contra él por un espeleólogo británico que asesoró en el rescate de la cueva de Tham Luang. Musk también ha sido criticado por difundir información errónea sobre la pandemia de COVID-19 y por sus otras opiniones sobre asuntos como la inteligencia artificial, las criptomonedas y el transporte público.
"""

if __name__ == '__main__':
    print('hello LangChain')
    # print(os.environ['OPENAI_API_KEY'])

    # summary_template = """
    #     given the Linkedin information {information} about a person from I want you to create:
    #     1. a short summary
    #     2. two interesting facts about them
    # """

    # summary_prompt_template = PromptTemplate(
    #     input_variables=["information"], template=summary_template
    # )

    # llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    # chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    # print(chain.run(information=information))

    linkedin_data = linkedin.scrape_linkedin_profile(linkedin_profile_url='https://www.linkedin.com/in/jose-lovaglio-balbo/')
    print(linkedin_data.text)

    
