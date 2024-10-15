SELECT *
FROM vendas
WHERE data_venda >= '{{ var("data_minima", "2023-01-01") }}'


--- 

{{ config(
    schema=var('schema_nome', 'desenvolvimento_schema')
) }}

SELECT *
FROM vendas


{{ this }}
{{ target }}
{% if is_incremental() %}...{% endif %}

SELECT 
    id_pedido,
    data_venda,
    valor,
    '{{ this }}' AS nome_tabela,
    '{{ target.name }}' AS ambiente_atual
FROM vendas
