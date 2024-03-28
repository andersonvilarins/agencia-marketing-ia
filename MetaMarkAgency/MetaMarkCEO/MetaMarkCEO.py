from agency_swarm.agents import Agent


class MetaMarkCEO(Agent):
    def __init__(self):
        super().__init__(
            name="MetaMarkCEO",
            description="Supervisiona toda a operação, mantém o fluxo de trabalho entre os agentes e garante o cumprimento dos objetivos da agência. Atua como supervisor estratégico e iniciador do processo de campanha publicitária.",
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools=[],
            tools_folder="./tools"
        )
