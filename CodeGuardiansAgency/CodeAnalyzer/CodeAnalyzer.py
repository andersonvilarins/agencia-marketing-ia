from agency_swarm.agents import Agent
from agency_swarm.tools import CodeInterpreter

class CodeAnalyzer(Agent):
    def __init__(self):
        super().__init__(
            name="CodeAnalyzer",
            description="Especializado em recuperar alterações de solicitações pull usando a API GitHub, analisando-as em relação a padrões de qualidade predefinidos para bases de código TypeScript. Comunica as descobertas ao Agente Gerador de Relatórios para compilação do relatório.",
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools=[CodeInterpreter],
            tools_folder="./tools"
        )
