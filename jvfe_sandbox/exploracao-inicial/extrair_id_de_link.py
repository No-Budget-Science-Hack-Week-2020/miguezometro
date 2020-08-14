"""Mantendo aqui para referência futura, provavelmente vai ser útil"""

import pandas as pd

br_journals = pd.read_csv("journals_list.csv", sep=";").rename(
    columns=lambda x: x.strip()
)
br_journals["identificador"] = (
    br_journals["scielo_url"]
    .str.extract(r"(\&pid\=.*&lng)")
    .replace("&pid=", "", regex=True)
    .replace("&lng", "", regex=True)
)
