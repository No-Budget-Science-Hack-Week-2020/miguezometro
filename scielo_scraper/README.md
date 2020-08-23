# SciELO scraper

Uma coleção de códigos em Python que extraem conteúdo de artigos indexados no SciELO, 
no sentido de realizar uma análise de *link rotting* nos links encontrados. 


# Reproduzindo a extração de dados

* Clone o repositório

```git clone --recurse-submodules https://github.com/gabriellovate/miguezometro```

* Entre no diretório

```cd miguezometro/scielo_scraper```

* [Como instalar o gerenciador conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)

* Criando o ambiente a partir do arquivo nobudgetsci-migue.yml, digite no seu terminal:

```conda env create -f nobudgetsci-migue.yml```

* Uma vez instalado, ative o ambiente:

```conda activate nobudgetsci-migue```

* Entre no script `src/journal_data_extraction.py` e siga os passos descritos.
