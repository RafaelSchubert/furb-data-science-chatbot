# Chatbot — Assistente de Concessionária

Este é meu trabalho final da disciplina _Chatbots_ do curso _Especialização em Data Science_, pela Universidade Regional de Blumenau — FURB.

O _chatbot_ pode ser visualizado [aqui](https://web-chat.global.assistant.watson.cloud.ibm.com/preview.html?region=us-south&integrationID=3a368ba3-96ec-46f3-b9ac-c4ca0ce59126&serviceInstanceID=a2550b64-1b49-49f8-881c-8e4670bab333).

## O Assistente de Concessionária Ford

Sobre o _chatbot_ desenvolvido.

### Funções

O _bot_ disponibiliza três funções\* para auxiliar o cliente:

**Recomendação de modelos:** recomendar uma lista de modelos, além de descrevê-los, de acordo com um critério do cliente. O _bot_ consegue avaliar três critérios de seleção: finalidade, categoria e capacidade de passageiros.

**Agendamento de test-drive:** agendar uma data e horário para realizar o test-drive dum modelo específico na concessionária fictícia. O _bot_ solicita ao cliente que indique um modelo, uma data e um horário para a realização do test-drive. No lugar de informar um modelo inicialmente, o cliente também pode requisitar uma recomendação.

**Aquisição de veículo:** realizar a compra dum veículo. O _bot_ solicita ao cliente que indique o modelo do veículo. Opcionalmente, esse também pode solicitar uma recomendação de modelos.

\* Observe que, por tratar-se dum trabalho acadêmico, essas funções são versões deveras simplificadas de suas contrapartes reais.

## Informações

Sobre o conteúdo deste repositório.

### Diagramas

Na pasta `diagrama`, você encontrará os diagramas do fluxo de diálogo do _chatbot_. O diagrama está dividido em **cinco** partes, representando as três macrotarefas e as duas microtarefas do _bot_.

Macrotarefas:

- **Recomendação de modelos:** arquivo `diagrama/fluxo-recomendar-modelo.png`;
- **Agendamento de test-drive:** arquivo `diagrama/fluxo-agendar-testdrive.png`;
- e **Aquisição de veículo:** arquivo `diagrama/fluxo-comprar-carro.png`.

Microtarefas (rotinas compartilhadas pelas macrotarefas):

- **Capturar o modelo informado:** realiza a captura do modelo indicado pelo cliente e redireciona para o próximo da macrotarefa. Arquivo `diagrama/fluxo-capturar-modelo.png`;
- **Requisitar escolha de modelo:** inquire o cliente sobre o modelo que interessa-lhe na macrotarefa em execução. Se solicitado, esta rotina também direciona o fluxo para a recomendação de modelos. Arquivo `diagrama/fluxo-requisitar-escolha-modelo.png`.
