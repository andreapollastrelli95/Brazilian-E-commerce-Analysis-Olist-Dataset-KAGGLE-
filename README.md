# Analisi e-commerce brasiliano (Olist)

Dashboard Power BI e analisi Python sul [dataset pubblico di Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce): dove si concentrano i ricavi e quanto pesano le consegne sulla soddisfazione dei clienti.

<img width="1867" height="680" alt="image" src="https://github.com/user-attachments/assets/54e73976-37a5-474c-b614-cea7e60a8136" />

## Risultati principali

Calcolati su 96.470 ordini consegnati tra il 2016 e il 2018, per circa 15,4 milioni di BRL di pagamenti.

- **Ricavi concentrati:** São Paulo genera il 37,4% dei ricavi e i primi tre stati (SP, RJ, MG) il 62,5%.
- **Ritardi e recensioni:** il 6,8% degli ordini arriva dopo la data stimata. Il voto medio è 4,29 per gli ordini puntuali e 2,27 per quelli in ritardo; i voti 1-2 passano dal 9,2% al 60,9%.
- **Differenze territoriali:** la consegna mediana è di 7,2 giorni a SP, 12,0 a RJ e 21,1 in Pará. Rio de Janeiro ha il 12,1% di ritardi contro il 4,5% di SP, e un voto medio di 3,97 contro 4,25.

## Cosa suggeriscono

Sono associazioni osservate, non prove di causa. Un test su RJ potrebbe verificare se migliorare la puntualità alza le recensioni: è il secondo mercato per ricavi e ha il tasso di ritardo più alto tra i primi cinque.

## Contenuto

| File | Descrizione |
|---|---|
| `Brasilian e commerce mappe e fatturato.pbix` | Report di una pagina: ricavi per stato, due mappe, due card e filtro per data, con un modello di 10 tabelle |
| `analisi/insight.py` | Calcola i risultati riportati qui |
| `analisi/ordini_per_mese_e_stato.sql` | Ordini e clienti unici per mese e stato |

## Riprodurre l'analisi

Scarica i CSV da Kaggle (non sono nel repository), poi:

```bash
pip install pandas
python analisi/insight.py percorso/cartella_csv
```

I ricavi sono i pagamenti degli ordini consegnati. Un ordine è in ritardo se la data di consegna supera la data stimata.

## Licenza

La licenza MIT copre gli elaborati di questo repository. Il dataset resta soggetto ai termini indicati da Olist su Kaggle.
