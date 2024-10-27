import pandas as pd
from faker import Faker
import random
import numpy as np

# Inicializando o Faker
faker = Faker('pt_BR')

# Função para gerar usuários
def gerar_usuarios(n):
    usuarios = []
    for _ in range(n):
        usuarios.append({
            'id': faker.unique.random_int(min=1, max=100000),
            'nome': faker.name(),
            'email': faker.unique.email(),
            'telefone': faker.phone_number(),
            'endereco': faker.address(),
            'data_registro': faker.date_this_decade()
        })
    return pd.DataFrame(usuarios)

# Função para gerar produtos
def gerar_produtos(n):
    categorias = ['Eletrônicos', 'Roupas', 'Livros', 'Casa e Cozinha', 'Esportes', 'Beleza']
    produtos = []
    for _ in range(n):
        produtos.append({
            'id': faker.unique.random_int(min=1, max=100000),
            'nome': faker.word().capitalize(),
            'categoria': random.choice(categorias),
            'preco': round(random.uniform(10, 1000), 2),
            'estoque': random.randint(0, 1000),
            'data_cadastro': faker.date_this_decade()
        })
    return pd.DataFrame(produtos)

# Função para gerar pedidos
def gerar_pedidos(n, usuarios_ids, produtos_df):
    pedidos = []
    for _ in range(n):
        usuario_id = random.choice(usuarios_ids)
        data_pedido = faker.date_this_year()
        status = random.choice(['concluído', 'pendente', 'cancelado'])
        total = 0
        produtos = random.sample(list(produtos_df['id']), random.randint(1, 5))
        for produto_id in produtos:
            quantidade = random.randint(1, 5)
            preco = produtos_df[produtos_df['id'] == produto_id]['preco'].values[0]
            total += quantidade * preco
        pedidos.append({
            'id': faker.unique.random_int(min=1, max=100000),
            'usuario_id': usuario_id,
            'data_pedido': data_pedido,
            'status': status,
            'total': round(total, 2)
        })
    return pd.DataFrame(pedidos)

# Função para gerar itens dos pedidos
def gerar_itens_pedidos(pedidos_df, produtos_df):
    itens = []
    for _, pedido in pedidos_df.iterrows():
        produtos = random.sample(list(produtos_df['id']), random.randint(1, 5))
        for produto_id in produtos:
            quantidade = random.randint(1, 5)
            preco = produtos_df[produtos_df['id'] == produto_id]['preco'].values[0]
            itens.append({
                'pedido_id': pedido['id'],
                'produto_id': produto_id,
                'quantidade': quantidade,
                'preco_unitario': preco,
                'subtotal': round(quantidade * preco, 2)
            })
    return pd.DataFrame(itens)

# Função para gerar pagamentos
def gerar_pagamentos(pedidos_df):
    pagamentos = []
    metodos_pagamento = ['Cartão de Crédito', 'Boleto', 'Pix']
    for _, pedido in pedidos_df.iterrows():
        status = random.choice(['pago', 'pendente', 'recusado'])
        pagamentos.append({
            'id': faker.unique.random_int(min=1, max=100000),
            'pedido_id': pedido['id'],
            'valor': pedido['total'],
            'metodo': random.choice(metodos_pagamento),
            'status': status,
            'data_pagamento': faker.date_between(start_date=pedido['data_pedido'])
        })
    return pd.DataFrame(pagamentos)

# Gerando os dados
n_usuarios = 500  # Definir número de usuários
n_produtos = 100  # Definir número de produtos
n_pedidos = 1000  # Definir número de pedidos

# Gerar tabelas
usuarios_df = gerar_usuarios(n_usuarios)
produtos_df = gerar_produtos(n_produtos)
pedidos_df = gerar_pedidos(n_pedidos, usuarios_df['id'].tolist(), produtos_df)
itens_pedidos_df = gerar_itens_pedidos(pedidos_df, produtos_df)
pagamentos_df = gerar_pagamentos(pedidos_df)

# Salvando em CSV
usuarios_df.to_csv('usuarios.csv', index=False)
produtos_df.to_csv('produtos.csv', index=False)
pedidos_df.to_csv('pedidos.csv', index=False)
itens_pedidos_df.to_csv('itens_pedidos.csv', index=False)
pagamentos_df.to_csv('pagamentos.csv', index=False)

print("Dados gerados e salvos em CSV.")
