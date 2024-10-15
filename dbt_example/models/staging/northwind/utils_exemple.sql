SELECT 
    id_cliente,
    dbt_utils.star(from=ref('clientes'), except=['id_cliente']) -- Seleciona todas as colunas exceto a 'id_cliente'
FROM {{ ref('clientes') }}
