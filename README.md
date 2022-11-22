# classificador_telegram

> Bot do telegram que consome o classificador de imagens construído durante a disciplina de Redes Neurais do Mestrado da FACOM - UFMS.

[Este](https://colab.research.google.com/drive/1uigSrhs4uh04VU3Xr-PTpDqlOO0Lvke7) é o colab com o código que realiza o treino da rede, e também informa algumas métricas como precisão, revocação, e uma matriz de confusão para melhor visualização. No colab, também existe uma melhor descrição do processo de criação do dataset.

## Configuração

Adicione o arquivo `best_model.pth` na raíz desse repositório.

Crie um arquivo `.env`, contendo seu token do Telegram, seguindo como exemplo o arquivo `.env.example`.

No arquivo [`src/classifier.py`](/src/classifier.py#L13), defina a variável  `intencoes`, como sendo uma lista com as intenções disponíveis.

## Execução

Para instalar as dependências, utilize o gerenciador de pacotes `poetry`, com o seguinte comando:

```sh
poetry install
```

Para executar o bot, utilize o seguinte comando:

```sh
poetry run python chatbot_telegram/main.py
```

Caso não esteja utilizando o `poetry`, adapte para o seu gerenciador de pacotes.
