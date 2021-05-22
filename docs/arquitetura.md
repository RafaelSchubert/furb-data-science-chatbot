# Arquitetura

Este documento aborda brevemente a arquitetura do _chatbot_ desenvolvido neste trabalho.

-----

## _Chatbot_

### Watson Assistant

O _bot_ foi desenvolvido por meio do serviço **Watson Assistant**, da IBM, usando os recursos disponíveis numa conta gratuita do serviço **IBM Cloud**.

### Persistência

As conversas entre cliente e _bot_ são armazenadas pelo próprio serviço IBM Cloud, mantendo-as para análise estatística e para curadoria.

-----

## Web Service

O _web service_ (WS) usado no trabalho é, na verdade, um _mock_ que finge uma consulta a um serviço fictício da Ford. Esse WS possui dois parâmetros: `operacao` e `modelo`.

O parâmetro `operacao` determina a operação a ser executada pelo WS — apenas a operação `"consultar_modelo"` foi implementada. Essa ação busca os dados dum modelo de veículo da montadora Ford e retorna uma descrição, suas palavras-chave e seu preço em dólares.

O parâmetro `modelo` é complementar a `operacao` e apenas especifica de qual modelo as informações devem ser consultadas. Os modelos que podem ser informados são todos aqueles que constam nas listas de recomendações de modelos oferecidas pelo _bot_.

### IBM Cloud Functions

O _mock_ de _web service_ foi desenvolvido em **Python** e é hospedado e executado pelo serviço **IBM Cloud Functions**, da IBM. Usou-se os recursos disponíveis numa conta gratuita do serviço **IBM Cloud**.
