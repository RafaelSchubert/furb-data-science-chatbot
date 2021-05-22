# Chatbot — Assistente de Concessionária

Este é meu trabalho final da disciplina _Chatbots_ do curso _Especialização em Data Science_, pela Universidade Regional de Blumenau — FURB. O trabalho consiste em desenvolver um _chatbot_ para atender às necessidades dum domínio específico, diagramar seu fluxo de diálogo e fornecer indicadores e/ou métricas de seu desempenho.

O _chatbot_ pode ser visualizado [aqui](https://web-chat.global.assistant.watson.cloud.ibm.com/preview.html?region=us-south&integrationID=3a368ba3-96ec-46f3-b9ac-c4ca0ce59126&serviceInstanceID=a2550b64-1b49-49f8-881c-8e4670bab333).

-----

## O Assistente de Concessionária Ford

O _Assistente de Concessionária_ é um _chatbot_ desenvolvido pensando no atendimento virtual online duma concessionária de automóveis especializada na montadora Ford. Ele inclui o atendimento duns poucos serviços que poderiam, teoricamente, ser ofertados por meio dum _chatbot_. Talvez a aquisição do veículo por meio do _bot_ pareça forçada, mas devemos lembrar que alguns desses já realizam transações bancárias, e uns outros poucos até realizam compras.

### Funções

O _bot_ disponibiliza três funções\* para auxiliar o cliente:

| Função | Descrição |
| :--- | :--- |
| Recomendação de modelos | Recomendar uma lista de modelos, além de descrevê-los, de acordo com um critério do cliente. O _bot_ consegue avaliar três critérios de seleção: finalidade, categoria e capacidade de passageiros. |
| Agendamento de test-drive | Agendar uma data e horário para realizar o test-drive dum modelo específico na concessionária fictícia. O _bot_ solicita ao cliente que indique um modelo, uma data e um horário para a realização do test-drive. No lugar de informar um modelo inicialmente, o cliente também pode requisitar uma recomendação. |
| Aquisição de veículo | Realizar a compra dum veículo. O _bot_ solicita ao cliente que indique o modelo do veículo. Opcionalmente, esse também pode solicitar uma recomendação de modelos. |

\* Observe que, por tratar-se dum trabalho acadêmico, essas funções são versões deveras simplificadas de suas contrapartes reais.

-----

## Conteúdo

Sobre o conteúdo deste repositório.

### _Chatbot_

No diretório [`bot`](./bot/), você encontrará o arquivo JSON descrevendo a _skill_ associada ao _Watson Assistant_ desenvolvido como parte deste trabalho. Com ele, você mesmo pode replicar o _bot_ no serviço _IBM Cloud_ importando a definição da _skill_.

### Diagramas

No diretório [`diagrama`](./diagrama/), você encontrará os diagramas do fluxo de diálogo do _chatbot_. Visite o diretório para mais detalhes.

-----

## Entregas e Requisitos

O trabalho exige as entregas e requisitos a seguir:

### _Chatbot_

- [x] Utilizar uma das tecnologias vistas em aula (ou discutir com o profesor sobre outra):
  - Dialogflow;
  - LUIS;
  - RASA;
  - Watson Assistant;
- [x] Deve ser dum domínio fechado:
  - exceto restaurantes/lanchonetes, pois elaboramos um _bot_ para tal em aula;
- [ ] Deve possuir uma interface de usuário;
- [x] Deve integrar com algum _web service_:
  - local ou público;
  - real ou _mock_;
- [x] Deve armazenar as conversas com os usuários;
- [x] O código-fonte deverá ser disponibilizado num repositório público:
  - no caso dum [_Watson Assistant_](https://www.ibm.com/br-pt/cloud/watson-assistant) (como este trabalho), deve-se disponibilizar os arquivos JSON das _skills_ do _bot_.

### Documentação

- [x] Elaborar um diagrama do fluxo de diálogo do _bot_;
- [ ] Descrever a arquitetura do _bot_ num documento.

### Análise

- [ ] Fornecer pelo menos **3** indicadores e/ou métricas de desempenho:
  - deve ser feito num _Jupyter Notebook_;
  - devem ser demonstrados graficamente.
