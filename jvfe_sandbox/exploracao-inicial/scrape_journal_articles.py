# -*- coding: utf-8 -*-

# %%
import requests
import pandas as pd
from bs4 import BeautifulSoup as bsoup

# %%
def parse_page(url):
    """Utilitário que simplesmente pega a página e extrai todo o html dela."""
    response = requests.get(url)
    parsed_response = bsoup(response.content, parser="html.parser")

    return parsed_response


# %%
def get_oldest_issue(id):
    """Retorna o link da edição mais antiga de um journal presente no scielo a partir do id do journal.

    Essa ainda é a função mais propensa ao erro - visto que, por alguma razão, 
    o scielo possui mais de um domínio. Estou ajustando várias coisas."""

    # CSS Path da tabela das edições:
    # .content > table:nth-child(3) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > table:nth-child(2)

    try:
        url = f"https://www.scielo.br/scielo.php?script=sci_issues&pid={id}&lng=en&nrm=iso"

        journal_issue_table = parse_page(url)

        anchors = journal_issue_table.select_one(
            ".content > table:nth-child(3) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > table:nth-child(2)"
        ).select("a[href]")
    except:
        print("Vou tentar outra url base...")

        try:
            url = f"http://www.scielo.org.co/scielo.php?script=sci_issues&pid={id}&lng=en&nrm=iso"

            journal_issue_table = parse_page(url)

            anchors = journal_issue_table.select_one(
                ".content > table:nth-child(3) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > table:nth-child(2)"
            ).select("a[href]")
        except:
            print(f"Não consegui raspar o journal {id}!")

        else:

            issues_links = [a["href"] for a in anchors]

            return issues_links[-1]

    else:

        issues_links = [a["href"] for a in anchors]

        return issues_links[-1]


# %%
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


# %%

### TESTES ###

# 0120-548X
oldest_issue = get_oldest_issue("0120-548X")
texto = get_all_articles_from_issue(oldest_issue)

# %%
# 1415-4757
oldest_issue = get_oldest_issue("1415-4757")
texto = get_all_articles_from_issue(oldest_issue)


# %%
