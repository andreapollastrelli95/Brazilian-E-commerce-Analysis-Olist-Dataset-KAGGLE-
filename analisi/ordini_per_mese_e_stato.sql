SELECT 
    strftime('%Y-%m', o.order_purchase_timestamp) AS mese_anno,
    c.customer_state AS stato,
    COUNT(o.order_id) AS numero_ordini,
    COUNT(DISTINCT c.customer_unique_id) AS clienti_unici
FROM olist_orders_dataset o
JOIN olist_customers_dataset c ON o.customer_id = c.customer_id
WHERE o.order_status = 'delivered'
GROUP BY mese_anno, stato
ORDER BY mese_anno DESC, numero_ordini DESC
LIMIT 20;