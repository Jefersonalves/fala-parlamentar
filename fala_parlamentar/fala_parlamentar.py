import re
import requests
#import datetime
import pandas as pd
from bs4 import BeautifulSoup
from xml.etree import ElementTree

def get_transcricao_discurso_senado(url):
    """
    obtém via webscraping a transcrição de um discurso de um senador dada a url

    Parâmetros
    ----------
    url : string
        url de um discurso de senador

    Retornos
    -------
    discurso : dict
        Dicionário com o título e a transcrição do discurso
    """
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    
    texto = None
    titulo = None

    try:
        texto_element = soup.find(class_='texto-integral')
        texto = texto_element.text.strip()
        texto = re.sub(r'\xa0\xa0\xa0\xa0', '\n', texto)
    
        titulo_element = soup.find(class_='titulo-pagina')
        titulo = (titulo_element.text).strip()
    except:
        pass
    
    discurso = {'titulo': titulo, 'texto': texto}
    return discurso

def get_discursos_senador(codigo_parlamentar, data_inicio, data_fim):
    """
    retorna uma lista dos discursos de um senador dado o identificador da API do senado (codigoParlamentar)

    Parâmetros
    ----------
    codigo_parlamentar : int or string
        código identificador do senador na API do senado
        - Ex: 3830
    data_inicio : string
        data de início no formato AAAA-MM-DD
        - Ex: '2019-01-01'
    data_fim : string
        data fim no formato AAAA-MM-DD
        - Ex: '2019-12-31'

    Retornos
    -------
    list_discursos_senador : list of dicts
        Lista dos discursos do senador no intervalo de tempo fornecido
        - Ex:   [
                    {
                        'titulo': 'Pronunciamento de Davi Alcolumbre em 03/02/2020'},
                        'urlTexto': 'http://www25.senado.leg.br/web/atividade/pronunciamentos/-/p/texto/463644',
                        'transcricao': 'O SR. PRESIDENTE  (Davi Alcolumbre. Bloco/DEM - AP) – Eu gostaria de
                                        agradecer a todos que nos honraram com a presença nesta sessão solene. \n
                                        E declaro encerrada esta sessão.'
                    }
                ]
    """
    
    data_inicio = re.sub(r'-', '', data_inicio)
    data_fim = re.sub(r'-', '', data_fim)
    
    #as urls dos discursos podem ser obtidos via API
    discursos_url = 'https://legis.senado.leg.br/dadosabertos/senador/{}/discursos?dataInicio={}&dataFim={}'.format(str(codigo_parlamentar), data_inicio, data_fim)
    r = requests.get(discursos_url)
    root = ElementTree.fromstring(r.content)
    
    #obtenção das urls dos discursos
    links_discursos_elements = root.findall('Parlamentar/Pronunciamentos/Pronunciamento/UrlTexto')
    links_discursos = [texto.text for texto in links_discursos_elements] #variável com as urls
    
    #adição dos discursos numa lista contendo os seus dados 
    list_discursos_senador = []
    for link in links_discursos:
        discurso = get_transcricao_discurso_senado(link)
        
        list_discursos_senador.append(
            {
             'titulo': discurso['titulo'],
             'url_texto': requests.utils.requote_uri(link),
             'transcricao': discurso['texto']
            }
        )

    return list_discursos_senador