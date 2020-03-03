>## fala-parlamentar

Obtém os discursos dos parlamentares via webscraping

>## instalação

`git clone https://github.com/Jefersonalves/fala-parlamentar.git`

`cd fala-parlamentar`

`pip install .`

>## como usar

```
In [1]: from fala_parlamentar import get_discursos_senador

In [2]: discursos = get_discursos_senador(3830, "2019-01-01", "2020-01-01") #id do Davi Alcolumbre

In [3]: discursos[1]
Out[13]: 
{'titulo': 'Pronunciamento de Davi Alcolumbre em 12/12/2019',
 'url_texto': 'http://www25.senado.leg.br/web/atividade/pronunciamentos/-/p/texto/463401',
 'transcricao': 'O SR. PRESIDENTE  (Davi Alcolumbre. Bloco/DEM - AP) – Eu gostaria de agradecer a todos que nos honraram com a presença nesta sessão solene. \nE declaro encerrada esta sessão.'}
```