# Diagramas

Neste diretório, você encontra os diagramas do fluxo de diálogo do _Assistente de Concessionária_. Porque o diagrama completo é muito extenso, optei por dividí-lo em **cinco** partes, representando as três macrotarefas e as duas microtarefas do _bot_.

## Macrotarefas:

As macrotarefas são os serviços atendidos pelo _bot_:

- **Recomendação de modelos:** arquivo `fluxo-recomendar-modelo.png`;
- **Agendamento de test-drive:** arquivo `fluxo-agendar-testdrive.png`;
- e **Aquisição de veículo:** arquivo `fluxo-comprar-carro.png`.

## Microtarefas

As microtarefas são as rotinas compartilhadas pelas macrotarefas:

- **Capturar o modelo informado:** realiza a captura do modelo indicado pelo cliente e redireciona para o próximo da macrotarefa. Arquivo `fluxo-capturar-modelo.png`;
- **Requisitar escolha de modelo:** inquire o cliente sobre o modelo que interessa-lhe na macrotarefa em execução. Se solicitado, esta rotina também direciona o fluxo para a recomendação de modelos. Arquivo `fluxo-requisitar-escolha-modelo.png`.