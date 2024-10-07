SELECT 
    id_pedido,
    data_criacao,
    data_entrega,
    {{ calc_diff('data_criacao', 'data_entrega') }} AS dias_entrega
FROM pedidos
