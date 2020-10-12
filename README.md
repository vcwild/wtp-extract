
<h2 style="text-align: left">

  [Apresentação](#ovr) | [Procedimento](#proc) | [Próxima »](https://github.com/vcwild/wtp-clean)

</h2>

# Apresentação <a name="ovr">

## Extração de Dados

Serão utilizadas planilhas de mensuração da qualidade da água em uma Estação de Tratamento de Esgoto entre os anos de 2013 a 2019. <br/>
Os dados de origem foram escritos em documentos “xlsx”, dispostos em formato tabular, cujas entidades e parâmetros receberam nomes e unidades distintos ao longo do tempo.

## Objetivo

O objetivo inicial é mapear os dados originais como são, localizando as abas e tabelas dentro delas, retirando os dados das tabelas e exportando para arquivos "csv" individuais, conforme indica o fluxograma:

![Fluxograma](./.github/fluxograma.png)

As particularidades de cada tabela foram excluídas do fluxograma, mas podem ser consultadas nos [logs](./Logs) do [extrator](extractor.py). Ao todo foram encontrados 18 formatos únicos de tabela.

# Procedimento <a name="proc">

O extrator localizou os seguintes conjuntos de dados referente a **parâmetros** nos arquivos de origem:

- [Acidez](./Logs/acidez.ipynb)
- [Alcalinidade](./Logs/alcalinidade.ipynb)
- [Coliformes](./Logs/coliformes.ipynb)
- [Compostagem](./Logs/compostagem.ipynb)
- [Cor Verdadeira](./Logs/Cor_verdadeira.ipynb)
- [DBO](./Logs/DBO.ipynb)
- [DQO](./Logs/DQO.ipynb)
- [Fósforo](./Logs/fosforo.ipynb)
- [Nitrogênio](./Logs/nitrogênio.ipynb)
- [Óleos](./Logs/óleos.ipynb)
- [pH](./Logs/pH.ipynb)
- [Sólidos](./Logs/sólidos.ipynb)
- [Surfactantes](./Logs/surfactantes.ipynb)

O extrator localizou os seguintes dados referentes a **localidades** nos arquivos de origem:

- [CONSEMA](./Logs/toda_consema.ipynb)
- [Leito de Secagem](./Logs/leito_de_secagem.ipynb)
- [PTEL](.Logs/ptel.ipynb)

## Próximas Etapas

- [Tratamento de Dados](https://github.com/vcwild/wtp-clean)
- [Análise Exploratória](https://github.com/vcwild/wtp-eda)
- [Modelagem de Séries Temporais](https://github.com/vcwild/wtp-model)