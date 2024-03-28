from agency_swarm.tools import BaseTool
from agency_swarm.util import get_openai_client
from pydantic import Field
from dotenv import load_dotenv

load_dotenv()

class AdCopyGenerator(BaseTool):
    """
    Gera textos de anúncios criativos e envolventes, adaptados aos dados demográficos do público-alvo, recursos do produto e tom de anúncio desejado.
    """

    target_audience: str = Field(
        ..., description="Descrição dos dados demográficos do público-alvo."
    )
    product_features: str = Field(
        ..., description="Características do produto ou serviço."
    )
    ad_tone: str = Field(
        ..., description="Tom desejado do texto do anúncio."
    )

    def run(self):
        client = get_openai_client()
        prompt = f"""Gere uma segmentação criativa do texto do anúncio {self.target_audience}, 
       destacando os seguintes recursos: {self.product_features}. 
        O anúncio deverá ter um {self.ad_tone} tom. Não produza mais de 100 caracteres.
        Inclua um título em seu anúncio no seguinte formato:
        Título: [Seu título aqui]
        Ad Copy: [Your ad copy here]"""
        response = client.completions.create(
            model="gpt-4-turbo-preview",
            prompt=prompt,
            temperature=0.7,
            max_tokens=250,
        )
        text = response.choices[0].text.strip()
        headline = text.split("Ad Copy:")[0].split("Título:")[1].strip()
        self.shared_state.set("ad_headline", headline)
        ad_copy = response.choices[0].text.strip().split("Ad Copy:")[1].strip()
        self.shared_state.set("ad_copy", ad_copy)
        return text

if __name__ == "__main__":
    tool = AdCopyGenerator(
        target_audience="público jovem",
        product_features="sustentável, acessível, elegante",
        ad_tone="divertido, enérgico"
    )
    print(tool.run())
