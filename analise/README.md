# Análise

Neste diretório, você encontra os artefatos da análise estatística realizada sobre uma amostra dalgumas das conversas realizadas com o _chatbot_.

- **Análise:** um _Jupyter Notebook_ com a análise estatística e a apresentação dalguns indicadores e métricas. Arquivo [`analise-desempenho.ipynb`](./analise-desempenho.ipynb);
- e **Mensagens:** arquivo CSV contendo uma amostra de mensagens de conversas realizadas com o _bot_. Essas são as mensagens analisadas no _notebook_. Arquivo [`mensagens.csv`](./mensagens.csv).

### Observações

No arquivo `mensagens.csv`, os campos disponíveis são:

1. `mensagem`: o texto da mensagem enviada pelo cliente;
2. `data`: data em que a mensagem foi recebida;
   - No formato **AAAA-MM-DD**;
3. `horario`: horário em que a mensagem foi recebida;
   - No formato **HH:MM**;
4. `intencoes`: lista de intenções identificadas pelo _bot_ na mensagem do cliente;
   - Os elementos são separados por ",";
   - Cada intenção é identificada como `#INTENÇÃO`;
5. `entidades`: lista de entidades identificadas pelo _bot_ na mensagem do cliente;
   - Os elementos são separados por ",";
   - Os elementos são pares `@ENTIDADE:VALOR`.

Esses campos são separados por ";".
