>## fala-parlamentar

Obtém os discursos dos parlamentares via webscraping mantendo a url para a publicação do texto

>## instalação

`pip install fala-parlamentar`

>## como usar
>### discursos senadores
```
In [1]: from fala_parlamentar import get_discursos_senador

In [2]: discursos = get_discursos_senador(3830, "2019-01-01", "2020-01-01") #id do Davi Alcolumbre

In [3]: discursos[0]
Out[3]: 
{'titulo': 'Pronunciamento de Davi Alcolumbre em 12/12/2019',
 'url_texto': 'http://www25.senado.leg.br/web/atividade/pronunciamentos/-/p/texto/463401',
 'transcricao': 'O SR. PRESIDENTE  (Davi Alcolumbre. Bloco/DEM - AP) – Eu gostaria de agradecer a todos que nos honraram com a presença nesta sessão solene. \nE declaro encerrada esta sessão.'}
```

>### discursos deputados
```
In [1]: from fala_parlamentar import get_discursos_deputado

In [2]: discursos = get_discursos_deputado("Rodrigo Maia", "2019-01-01", "2020-01-01")

In [3]: discursos[18]
Out[3]: 
{'urlTexto': 'https://www.camara.leg.br/internet/sitaqweb/TextoHTML.asp?etapa=5&nuSessao=11.2019&nuQuarto=77720&nuOrador=11&nuInsercao=11&dtHorarioQuarto=17:00&sgFaseSessao=OD&Data=20/02/2019&txApelido=RODRIGO%20MAIA%20(PRESIDENTE),%20DEM-RJ&txFaseSessao=Ordem%20do%20Dia&txTipoSessao=Deliberativa%20Ordin%C3%83%C2%A1ria%20-%20CD&dtHoraQuarto=17:00&txEtapa=',
 'transcricao': 'O SR. PRESIDENTE (Rodrigo Maia. Bloco/DEM - RJ) - Eu já recolhi a sua questão de ordem e vou indeferi-la, porque, por mais que boa parte do texto esteja prejudicada, ainda sobra algo que permanece.Então, infelizmente, não tem como deferir a sua questão de ordem.',
 'titulo': 'Pronunciamento de Rodrigo Maia em 20/02/2019'}
```