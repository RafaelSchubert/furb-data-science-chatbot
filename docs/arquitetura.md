# Arquitetura

Este documento aborda brevemente a arquitetura do _chatbot_ desenvolvido neste trabalho.

-----

## 1 - _Chatbot_

O _chatbot_ é o assistente virtual inteligente que desempenha o intermédio entre o cliente e as funções disponibilizadas por um serviço. No caso deste trabalho, a interação cliente–_bot_ se dá por meio de conversão num chat online, como ocorreria, por exemplo, num serviço de mensagens instantâneas.

### 1.1 - Watson Assistant

O _chatbot_ foi desenvolvido usando o serviço **Watson Assistant**, da IBM, com os recursos disponíveis numa conta gratuita do serviço **IBM Cloud**. O serviço permite desenvolver assistentes de conversação inteligentes, com conjuntos de habilidades específicas (_skills_, como o serviço as chama), movidos pela plataforma de serviços cognitivos **Watson**, também da IBM.

O _bot_ desenvolvido é voltado para a prestação de serviços online duma concessionária fictícia da montadora Ford. Para tal, implementou-se uma _skill_ para compreender e atender as funções que foram estipuladas (recomendação de modelos, compra e agendamento de test-drive) por conversação com o cliente. A _skill_, então, foi associada a um assistente (_assistant_), que foi implantado com um _web chat_.

O _assistant_ pode ser incorporado a uma aplicação por meio de _web chat_, como foi feito neste trabalho, ou interagindo com a API do Watson Assistant. Optou-se pelo _web chat_ por simplicidade e praticidade.

### 1.2 - Persistência das conversas

As conversas entre cliente e _chatbot_ são armazenadas pelo próprio serviço IBM Cloud, mantendo-as para análise estatística e para a curadoria das _skills_ associadas ao _assistant_.

As mensagens podem ser acessadas pelos painéis apropriados do serviço Watson Assistant, que já oferece alguns indicadores e métricas, ou coletadas por meio da API do mesmo serviço. Observer, entretanto, que o acesso às conversas por meio da API não é fornecido para contas gratuitas do serviço IBM Cloud.

-----

## 2 - Web service

O _web service_ (WS) usado no trabalho é, na verdade, um _mock_ que finge uma consulta a um serviço fictício da Ford. Esse WS possui dois parâmetros: `operacao` e `modelo`.

O parâmetro `operacao` determina a operação a ser executada pelo WS — apenas a operação `"consultar_modelo"` foi implementada. Essa ação busca os dados dum modelo de veículo da montadora Ford e retorna uma descrição, suas palavras-chave e seu preço em dólares.

O parâmetro `modelo` é complementar a `operacao` e apenas especifica de qual modelo as informações devem ser consultadas. Os modelos que podem ser informados são todos aqueles que constam nas listas de recomendações de modelos oferecidas pelo _bot_.

### 2.1 - IBM Cloud Functions

O _mock_ de _web service_ foi desenvolvido em **Python** e é hospedado e executado pelo serviço **IBM Cloud Functions**, da IBM. Usou-se os recursos disponíveis numa conta gratuita do serviço **IBM Cloud**.
