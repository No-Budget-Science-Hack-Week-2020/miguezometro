# %%
import pandas as pd


def get_br_journals(file="journals_list.csv"):
    """
    Lê o arquivo csv com os periodicos da Scielo e adiciona uma 
    coluna de identificadores. 

    Returns:

        br_journals: Uma dataframe do pandas com periódicos e ids. 


    """
    br_journals = pd.read_csv(file).rename(columns=lambda x: x.strip())
    br_journals["identificador"] = (
        br_journals["scielo_url"]
        .str.extract(r"(\&pid\=.*&lng)")
        .replace("&pid=", "", regex=True)
        .replace("&lng", "", regex=True)
    )
    return br_journals


# %%
get_br_journals("../data/Journals - Ciências Biológicas.csv").to_csv(
    "../data/journals_cienciabio.csv"
)
