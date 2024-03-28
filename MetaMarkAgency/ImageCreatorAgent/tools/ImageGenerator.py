from agency_swarm.tools import BaseTool
from agency_swarm.util import get_openai_client
from pydantic import Field
import openai
import os
import base64

from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

class ImageGenerator(BaseTool):
    """
    Gera imagens com base no texto do anúncio e em temas ou solicitações específicas, utilizando DALL-E 3.
    """

    ad_copy: str = Field(
        ..., description="A cópia do anúncio para basear a imagem."
    )
    theme: str = Field(
        ..., description="O tema específico ou objetivos visuais da imagem."
    )
    specific_requests: str = Field(
        None, description="Quaisquer solicitações específicas relacionadas à criação da imagem."
    )

    def run(self):
        client = get_openai_client()
        client.timeout = 120
        prompt = f"Crie uma imagem que represente visualmente: {self.ad_copy}. Theme: {self.theme}. {('Solicitações específicas: ' + self.specific_requests) if self.specific_requests else ''}"
        response = client.images.generate(
                  model="dall-e-3",
                  prompt=prompt,
                  n=1,
                  size="1024x1024",
                response_format="b64_json",
                )

        self.save_image(response.data[0].b64_json)

        client.timeout = 4

        return "Imagem criada com sucesso. Agora você pode prosseguir com a criação de anúncios"

    def save_image(self, image_data):
        with open("image.png", "wb") as f:
            f.write(base64.b64decode(image_data))
            f.close()

        self.shared_state.set("image_path", os.path.abspath("image.png"))

if __name__ == "__main__":
    tool = ImageGenerator(ad_copy="Um lindo pôr do sol", theme="Natureza",
                          specific_requests="Incluir um rio na imagem.")
    tool.run()

    print(tool.shared_state.get("image_path"))



