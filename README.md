# Chatbot — Assistente de Concessionária

Este é meu trabalho final da disciplina _Chatbots_ do curso _Especialização em Data Science_, pela Universidade Regional de Blumenau — FURB. O trabalho consiste em desenvolver um _chatbot_ para atender às necessidades dum domínio específico, diagramar seu fluxo de diálogo e fornecer indicadores e/ou métricas de seu desempenho.

O _chatbot_ pode ser visualizado [aqui](https://web-chat.global.assistant.watson.cloud.ibm.com/preview.html?region=us-south&integrationID=3a368ba3-96ec-46f3-b9ac-c4ca0ce59126&serviceInstanceID=a2550b64-1b49-49f8-881c-8e4670bab333).

-----

## 1 - O Assistente de Concessionária Ford

O _Assistente de Concessionária_ é um _chatbot_ desenvolvido pensando no atendimento virtual online duma concessionária de automóveis especializada na montadora Ford. Ele inclui o atendimento duns poucos serviços que poderiam, teoricamente, ser ofertados por meio dum _chatbot_. Talvez a aquisição do veículo por meio do _bot_ pareça forçada, mas devemos lembrar que alguns desses já realizam transações bancárias, e uns outros poucos até realizam compras.

### 1.1 - Funções

O _bot_ disponibiliza três funções\* para auxiliar o cliente:

| Função | Descrição |
| :--- | :--- |
| Recomendação de modelos | Recomendar uma lista de modelos, além de descrevê-los, de acordo com um critério do cliente. O _bot_ consegue avaliar três critérios de seleção: finalidade, categoria e capacidade de passageiros. |
| Agendamento de test-drive | Agendar uma data e horário para realizar o test-drive dum modelo específico na concessionária fictícia. O _bot_ solicita ao cliente que indique um modelo, uma data e um horário para a realização do test-drive. No lugar de informar um modelo inicialmente, o cliente também pode requisitar uma recomendação. |
| Aquisição de veículo | Realizar a compra dum veículo. O _bot_ solicita ao cliente que indique o modelo do veículo. Opcionalmente, esse também pode solicitar uma recomendação de modelos. |

\* Observe que, por tratar-se dum trabalho acadêmico, essas funções são versões deveras simplificadas de suas contrapartes reais.

-----

## 2 - Conteúdo

Sobre o conteúdo deste repositório.

### 2.1 - Análise

No diretório [`analise`](./analise/), você encontrará a análise sobre algumas das conversas realizadas com o _chatbot_. Visite o diretório para mais detalhes.

### 2.2 - Código-fonte

No diretório [`src`](./src/), você encontrará os códigos-fonte deste trabalho, incluindo aqueles do _chatbot_ e do _web service_ consultado por ele. Visite o diretório para mais detalhes.

### 2.3 - Diagramas

No diretório [`diagrama`](./diagrama/), você encontrará os diagramas do fluxo de diálogo do _chatbot_. Visite o diretório para mais detalhes.

### 2.4 - Documentação

No diretório [`docs`](./docs/), você encontrará a documentação relacionada a este trabalho, como os requisitos e a arquitetura. Visite o diretório para mais detalhes.
