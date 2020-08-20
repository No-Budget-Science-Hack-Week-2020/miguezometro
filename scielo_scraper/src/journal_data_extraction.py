# -*- coding: utf-8 -*-

"""Script que contém o procedimento completo para detectar links quebrados"""

# %%
from scielo_scraper import (
    get_issue_dictionary,
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
def return_2010_or_oldest(dict_journals):
    try:
        issue_2010 = dict_journals["2010"][0]
    except:
        last_key = list(dict.keys())[-1]
        oldest_issue = dict_journals[last_key]
        return oldest_issue
    else:
        return issue_2010


# %%
# Para cada journal na lista, extraímos os dados
df_list = []
for identificador in so_br["identificador"]:

    try:
        all_issues = get_issue_dictionary(str(identificador))

        # Pega edição de 2010 ou, caso não haja, a mais antiga
        oldest_issue = return_2010_or_oldest(all_issues)
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

