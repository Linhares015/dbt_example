{% snapshot pedido_snapshot %}
    {{
        config(
            target_schema='historico',
            target_database='datawarehouse',
            unique_key='id_pedido',
            strategy='timestamp',
            updated_at='data_atualizacao'
        )
    }}

    SELECT 
        id_pedido,
        status,
        valor,
        data_atualizacao
    FROM pedidos

{% endsnapshot %}
