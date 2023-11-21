import re
from datetime import datetime
from unicodedata import normalize

import requests
from bs4 import BeautifulSoup


def remove_acentos(text):
    """
    remove os acentos do texto
    """
    return normalize("NFKD", text).encode("ASCII", "ignore").decode("ASCII")


def limpa_url(url_text):
    """
    remove caracteres indesejados nas urls
    """
    url_text = re.sub("[\t\n\r]", "", url_text)
    return url_text


def get_transcricao_discurso_camara(url, nomeParlamentar):
    """
    obtém via webscraping a transcrição de um discurso do deputado dada a url e o nome parlamentar
    """
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    texto = None
    titulo = None

    try:
        elementos = soup.select("font > span")
        elementos_texto = [
            elemento.text.strip().replace("\n", " ") for elemento in elementos
        ]
        texto = " ".join(elementos_texto)
        data = re.search(r"[0-9]{2}/[0-9]{2}/[0-9]{4}", url).group(0)
        titulo = "Pronunciamento de {} em {}".format(nomeParlamentar, data)
    except:
        pass

    discurso = {"titulo": titulo, "texto": texto}

    return discurso


def get_discursos_deputado(nomeParlamentar, data_inicio, data_fim):
    """
    obtém os discursos de um deputado dado o identificador na API da camara(ideCadastro) e retorna uma lista dos mesmos

    Parâmetros
    ----------
    nomeParlamentar : string
        nome parlamentar do deputado
        - Ex: "RODRIGO MAIA"
    data_inicio : string
        data de início no formato AAAA-MM-DD
        - Ex: '2019-01-01'
    data_fim : string
        data fim no formato AAAA-MM-DD
        - Ex: '2019-12-31'

    Retornos
    -------
    list_discursos_deputado : list of dicts
        Lista dos discursos do senador no intervalo de tempo fornecido
        - Ex:   [
                    {
                        ...
                    }
                ]
    """

    data_inicio_datetime = datetime.strptime(data_inicio, "%Y-%m-%d")
    data_inicio_formated = data_inicio_datetime.strftime("%d-%m-%Y")

    data_fim_datetime = datetime.strptime(data_fim, "%Y-%m-%d")
    data_fim_formated = data_fim_datetime.strftime("%d-%m-%Y")

    # obtenção das urls dos discursos via webscraping e busca por parlamentar
    nomeOrador = re.sub(" ", "+", remove_acentos(nomeParlamentar)).lower()
    url_busca_deputado = "https://www.camara.leg.br/internet/sitaqweb/resultadoPesquisaDiscursos.asp?txOrador={}&txPartido=&txUF=&dtInicio={}&dtFim={}&txTexto=&txSumario=&basePesq=plenario&CampoOrdenacao=dtSessao&PageSize=10000&TipoOrdenacao=DESC&btnPesq=Pesquisar#".format(
        nomeOrador, data_inicio_formated, data_fim_formated
    )
    r = requests.get(url_busca_deputado)

    # extração dos elementos que contém as urls dos discursos
    soup = BeautifulSoup(r.text, "html.parser")
    disc_tags_even = soup.findAll(class_="even")
    disc_tags_odd = soup.findAll(class_="odd")
    disc_tags = disc_tags_even + disc_tags_odd

    # extração das urls
    link_tags = [tag.find("a") for tag in disc_tags]
    urls = []
    for tag in link_tags:
        try:
            urls.append(tag["href"])
        except:
            pass

    # limpeza e adição de prefixo nas urls
    url_prefix = "https://www.camara.leg.br/internet/sitaqweb/"
    links_discursos = [url_prefix + limpa_url(url) for url in urls]

    list_discursos_deputado = []
    for link in links_discursos:
        discurso = get_transcricao_discurso_camara(link, nomeParlamentar)

        list_discursos_deputado.append(
            {
                "urlTexto": requests.utils.requote_uri(link),
                "transcricao": discurso["texto"],
                "titulo": discurso["titulo"],
            }
        )

    return list_discursos_deputado
