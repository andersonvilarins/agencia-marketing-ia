from agency_swarm.agents import Agent


class CEO(Agent):
    def __init__(self):
        super().__init__(
            name="CEO",
            description="Serve como interface principal para o usuário, orquestrando o processo de análise e geração de relatórios. Inicia tarefas e é responsável pelo desempenho geral da agência.",
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools=[],
            tools_folder="./tools"
        )
