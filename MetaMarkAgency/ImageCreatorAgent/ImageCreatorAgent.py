from agency_swarm.agents import Agent


class ImageCreatorAgent(Agent):
    def __init__(self):
        super().__init__(
            name="ImageCreatorAgent",
            description="Utilize DALL-E 3 para gerar imagens sincronizadas com o texto do anúncio. Com a tarefa de criar gráficos visualmente ocultos que chamam a atenção e transmitem a mensagem de forma eficaz.",
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools=[],
            tools_folder="./tools"
        )
