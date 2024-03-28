from agency_swarm.agents import Agent


class AdCopyAgent(Agent):
    def __init__(self):
        super().__init__(
            name="AdCopyAgent",
            description="É especializado na geração de textos de anúncios criativos e envolventes usando ferramentas de IA. Avalia o público-alvo e as características do produto/serviço para criar mensagens atraentes.",
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools=[],
            tools_folder="./tools"
        )
