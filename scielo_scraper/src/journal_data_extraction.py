# -*- coding: utf-8 -*-

"""Script que contém o procedimento completo para detectar links quebrados"""

# Esse script não está funcionando -> Em manutenção enquanto resolvemos o cutoff de ano
# %%
from scielo_scraper import (
    get_oldest_issue,
    get_all_articles_from_issue,
    extract_links,
)
import pandas as pd

# %%
# Lendo a lista total de journals extraída por Thayne
journals_list = pd.read_csv("../data/journals_cienciabio.csv", index_col=0)

# %%
# Filtrando apenas os journals brasileiros
so_br = journals_list[journals_list["revista brasileira?"] == "sim"].copy()
# %%
# Para cada journal na lista, extraímos os dados
df_list = []
for identificador in so_br["identificador"]:

    try:
        oldest_issue = get_oldest_issue(str(identificador))[-1]
        artigos = get_all_articles_from_issue(oldest_issue)
        df = extract_links(artigos)
        df["journal"] = identificador
        df_list.append(df)
    except Exception:
        print(f"Não consegui raspar {identificador}...")
        pass

# %%
# Juntamos todos os dados extraídos numa única dataframe
full_dataframe_brjournals = pd.concat(df_list)

# %%
# Dividimos o dado em diversos CSVs, no sentido de facilitar a colaboração.
for journal in set(full_dataframe_brjournals["journal"]):

    journal_df = full_dataframe_brjournals[
        full_dataframe_brjournals["journal"] == journal
    ].copy()

    journal_df.to_csv(f"../data/divided_by_journal/{journal}_info.csv", index=False)

# %%
# Vendo quais não consegui raspar

original = set(so_br["identificador"].to_list())
scraped = set(full_dataframe_brjournals["journal"].to_list())

remaining = original - scraped
