{{ 
    config(
        tags=['comercial'],
        docs={'node_color': 'red'}
    ) 
}}

with vendas as (
    select 
        *
    from {{ ref('int_vendas') }}
)

select 
    *
from vendas
