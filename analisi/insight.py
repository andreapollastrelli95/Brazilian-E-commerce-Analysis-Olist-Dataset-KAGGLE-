"""Calcola gli insight del README dai CSV originali di Olist (non inclusi: scaricali da Kaggle).

Uso: python analisi/insight.py percorso/cartella_csv
Considera solo gli ordini consegnati.
"""
import sys
from pathlib import Path

import pandas as pd


def main(cartella):
    d = Path(cartella)
    date = ["order_purchase_timestamp", "order_delivered_customer_date", "order_estimated_delivery_date"]
    ordini = pd.read_csv(d / "olist_orders_dataset.csv", parse_dates=date)
    ordini = ordini[(ordini.order_status == "delivered") & ordini.order_delivered_customer_date.notna()]
    clienti = pd.read_csv(d / "olist_customers_dataset.csv")
    pagamenti = pd.read_csv(d / "olist_order_payments_dataset.csv").groupby("order_id").payment_value.sum()
    recensioni = pd.read_csv(d / "olist_order_reviews_dataset.csv").groupby("order_id").review_score.mean()

    x = (ordini.merge(clienti, on="customer_id")
         .join(pagamenti, on="order_id").join(recensioni, on="order_id"))
    x["giorni_consegna"] = (x.order_delivered_customer_date - x.order_purchase_timestamp).dt.total_seconds() / 86400
    x["in_ritardo"] = x.order_delivered_customer_date.dt.normalize() > x.order_estimated_delivery_date

    per_stato = x.groupby("customer_state").agg(
        ricavi=("payment_value", "sum"), ordini=("order_id", "count"),
        consegna=("giorni_consegna", "median"), ritardo=("in_ritardo", "mean"),
        voto=("review_score", "mean"),
    ).sort_values("ricavi", ascending=False)
    per_stato["quota_ricavi"] = per_stato.ricavi / per_stato.ricavi.sum()

    print(f"Ordini consegnati: {len(x):,}; ricavi: {x.payment_value.sum():,.0f} BRL")
    print(f"Quota ricavi primi 3 stati: {per_stato.quota_ricavi.head(3).sum():.1%}\n")
    print(per_stato.head(5).round(3).to_string())
    print("\nVoto medio e ordini per puntualita':")
    print(x.groupby("in_ritardo").agg(voto=("review_score", "mean"), ordini=("order_id", "count")).round(2).to_string())
    print(f"\nQuota ordini in ritardo: {x.in_ritardo.mean():.1%}")
    voto_basso = x.assign(basso=x.review_score <= 2).groupby("in_ritardo").basso.mean()
    print(f"Voti 1-2: {voto_basso[False]:.1%} se puntuali, {voto_basso[True]:.1%} se in ritardo")
    lenti = per_stato[per_stato.ordini >= 500].sort_values("consegna", ascending=False).head(3)
    print("\nStati piu' lenti (almeno 500 ordini):")
    print(lenti[["ordini", "consegna", "ritardo", "voto"]].round(2).to_string())


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
