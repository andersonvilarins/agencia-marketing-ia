from agency_swarm.agents import Agent


class FacebookManagerAgent(Agent):
    def __init__(self):
        super().__init__(
            name="FacebookManagerAgent",
            description="Cuida do agendamento e postagem dos anúncios no Facebook. Garante que cada anúncio seja publicado de acordo com as melhores práticas de tempo e segmentação de público.",
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools=[],
            tools_folder="./tools"
        )
