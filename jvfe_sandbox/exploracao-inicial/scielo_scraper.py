# -*- coding: utf-8 -*-

import requests
import pandas as pd
from bs4 import BeautifulSoup as bsoup


def parse_page(url):
    """Utilitário que simplesmente pega a página e extrai todo o html dela."""
    response = requests.get(url)
    parsed_response = bsoup(response.content, parser="html.parser")

    return parsed_response


def return_issue_numbers(url):
    """Retorna o link da edição mais antiga de um journal presente no scielo a partir de uma url"""

    # CSS Path da tabela das edições:
    # .content > table:nth-child(3) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > table:nth-child(2)

    try:

        journal_issue_table = parse_page(url)

        anchors = journal_issue_table.select_one(
            ".content > table:nth-child(3) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > table:nth-child(2)"
        ).select("a[href]")

    except Exception:
        raise Exception(f"Não consegui raspar o journal {url}!")

    else:

        issues_links = [a["href"] for a in anchors]

        return issues_links[-1]


def get_oldest_issue(id):
    """Retorna o link da edição mais antiga de um journal presente no scielo a partir do id do journal.

    Essa ainda é a função mais propensa ao erro - visto que, por alguma razão, 
    o scielo possui mais de um domínio. Estou ajustando várias coisas."""

    try:
        url = f"https://www.scielo.br/scielo.php?script=sci_issues&pid={id}&lng=en&nrm=iso"

        return return_issue_numbers(url)

    except Exception:

        print("Vou tentar outra url base...")

        url = f"http://www.scielo.org.co/scielo.php?script=sci_issues&pid={id}&lng=en&nrm=iso"

        return return_issue_numbers(url)


def get_all_articles_from_issue(issue_url):
    """Retorna o texto bruto (html) de todos os artigos de uma dada edição

    Retorna uma dataframe no molde "link para o artigo // texto do artigo", o que
    pode ser útil para análises posteriores.
    """

    issue_page_parsed = parse_page(issue_url).find_all("a", string="text in  English")

    article_links = [a["href"] for a in issue_page_parsed]

    text = []
    for article in article_links:
        try:
            article_text = parse_page(article).find("div", class_="content")
            text.append([article, article_text])
        except:
            pass

    result_df = pd.DataFrame.from_records(text, columns=["article_link", "text"])

    return result_df


def extract_links(dataframe_with_texts, column="text"):
    """ Extrai links de uma coluna de dataframe contendo informação
    textual."""

    df = dataframe_with_texts.copy(deep=True)

    # Isso tá ineficiente, pode ser melhorado. Bastante.

    df["links"] = df["text"].apply(
        lambda x: [
            a["href"]
            for a in bsoup(str(x), parser="html.parser").find_all("a", href=True)
        ]
    )

    # Mantendo apenas urls únicas
    df = df.explode("links").drop_duplicates(subset=["links"])

    # Filtrando apenas urls "verdadeiras",
    # sem contar emails e outras coisas contidas em hrefs
    df = df[df["links"].str.contains("http")].reset_index(drop=True)

    return df


def test_if_link_works(url):

    try:
        response = requests.get(url)
    except:
        return False
    else:
        if response.status_code != requests.codes.ok:
            return False
        else:
            return True
