# -*- coding: utf-8 -*-

"""Script que contém o procedimento completo para detectar links quebrados"""

# %%
from scielo_scraper import (
    get_oldest_issue,
    get_all_articles_from_issue,
    extract_links,
    test_if_link_works,
)
import pandas as pd

# %%
# Vamos fazer o teste no periódico Ocean and Coastal Research (ISSN 2675-2824)

oldest_issue = get_oldest_issue("2675-2824")
artigos = get_all_articles_from_issue(oldest_issue)
df = extract_links(artigos)

# %%
# Esse passo demora um bocado, principalmente se a conexão for ruim que nem a minha
# Ele basicamente vai de link em link no dataframe testando se ele tá funcionando.

df["link_funciona"] = df["links"].apply(lambda url: test_if_link_works(url))
