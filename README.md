# Chatbot — Assistente de Concessionária

Este é meu trabalho final da disciplina _Chatbots_ do curso _Especialização em Data Science_, pela Universidade Regional de Blumenau — FURB.

## Informações

### Diagramas

Na pasta `diagrama`, você encontrará os diagramas do fluxo de diálogo do _chatbot_. O diagrama está dividido em **cinco** partes, representando as três macrotarefas e as duas microtarefas do _bot_.

As três macrotarefas são as rotinas atendidas pelo _bot_, que são:

- **Recomendação de modelos:** recomendar uma lista de modelos, além de descrevê-los, de acordo com um critério do usuário. O _bot_ consegue avaliar três critérios de seleção: finalidade, categoria e capacidade de passageiros. Este fluxo de diálogo está representado no arquivo `diagrama/fluxo-recomendar-modelo.png`;
- **Agendamento de test-drive:** agendar uma data e horário para realizar o test-drive dum modelo específico na concessionária fictícia. O _bot_ solicita ao usuário que indique um modelo, uma data e um horário para a realização do test-drive. No lugar de informar um modelo inicialmente, o usuário também pode requisitar uma recomendação. Este fluxo de diálogo está representado no arquivo `diagrama/fluxo-agendar-testdrive.png`;
- e **Aquisição de veículo:** realizar a compra dum veículo. O _bot_ solicita ao usuário que indique o modelo do veículo. Opcionalmente, esse também pode solicitar uma recomendação de modelos. Este fluxo de diálogo está representado no arquivo `diagrama/fluxo-comprar-carro.png`.

Vale observar que, por tratar-se dum trabalho acadêmico, as macrotarefas são versões deveras simplificadas de suas contrapartes reais.

As duas microtarefas são rotinas gerenciais compartilhadas pelas macrotarefas de alguma forma, e são:

- **Capturar o modelo informado:** realiza a captura do modelo indicado pelo usuário e redireciona para o próximo da macrotarefa. Este fluxo está representado no arquivo `diagrama/fluxo-capturar-modelo.png`;
- **Requisitar escolha de modelo:** inquire o usuário sobre o modelo que interessa-lhe na macrotarefa em execução. Se solicitado, esta rotina também direciona o fluxo para a recomendação de modelos. Este fluxo de diálogo está representado no arquivo `diagrama/fluxo-requisitar-escolha-modelo.png`.
