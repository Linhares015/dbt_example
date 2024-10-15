{% test has_sales(model, column_name) %}

WITH cliente_sem_vendas AS (
    SELECT {{ column_name }} AS id_cliente
    FROM {{ model }} AS c
    LEFT JOIN vendas AS v ON c.{{ column_name }} = v.id_cliente
    WHERE v.id_cliente IS NULL
)

SELECT COUNT(*)
FROM cliente_sem_vendas

{% endtest %}
