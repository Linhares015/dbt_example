{{ config(
    pre_hook=[
        "CREATE TABLE IF NOT EXISTS temp_clientes AS SELECT * FROM clientes LIMIT 100"
    ],
    post_hook=[
        "DROP TABLE IF EXISTS temp_clientes"
    ]
) }}

SELECT *
FROM temp_clientes

----

{{ config(
    pre_hook=[
        "CREATE TEMP TABLE temp_clientes AS SELECT * FROM clientes LIMIT 100",
        "UPDATE temp_clientes SET ativo = true WHERE status = 'ativo'"
    ],
    post_hook=[
        "ANALYZE temp_clientes",
        "DROP TABLE IF EXISTS temp_clientes"
    ]
) }}

SELECT *
FROM temp_clientes


---

{{ config(
    post_hook=[
        "INSERT INTO log_execucoes(modelo, data_execucao, status) VALUES ('{{ this.name }}', CURRENT_TIMESTAMP, 'SUCESSO')"
    ]
) }}

SELECT *
FROM clientes

---

{{ config(
    post_hook=[
        "CALL send_email('time@empresa.com', 'Modelo {{ this.name }} executado com sucesso!', 'Modelo finalizado em {{ run_started_at }}.')"
    ]
) }}

SELECT *
FROM vendas


---

{{ config(
    post_hook=[
        "{% if target.name == 'prod' %} INSERT INTO log_execucoes(modelo, data_execucao, status) VALUES ('{{ this.name }}', CURRENT_TIMESTAMP, 'SUCESSO') {% endif %}"
    ]
) }}

SELECT *
FROM vendas
