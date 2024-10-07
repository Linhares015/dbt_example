SELECT
    id_cliente,
    {{ to_snake_case('Nome Completo') }} AS nome_cliente_snake_case
FROM clientes
