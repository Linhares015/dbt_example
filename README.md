[Curso de dbt](https://www.udemy.com/course/dbt-core-completo-modelagem-e-automacao-de-dados/)

# dbt_example

Esse projeto é um exemplo de como utilizar o dbt para transformar dados.

Possui um modelo de dados simples e complexos, com exemplos de como utilizar o dbt para transformar dados.

## Como rodar o projeto

1. Crie uma venv:
```bash
python3 -m venv .venv
```

2. Ative a venv:
```bash
source .venv/bin/activate
```

3. Instale as dependências do projeto:
```bash
pip install -r requirements.txt
```

## Configuração do dbt

Vamos usar o dbt com o BigQuery, então é necessário configurar o dbt para usar o BigQuery.

1. Mude o arquivo `profiles.yml` para adicionar as credenciais do BigQuery.

2. Configure o dbt_project.yml ao seu gosto.

3. Rode o comando para certificar que o dbt está configurado corretamente:
```bash
dbt debug
```

4. Rode os seeds para criar as tabelas de exemplo:
```bash
dbt seed
```

5. Use os modelos de exemplo ou criem os seus próprios.

6. Rode o comando para rodar os modelos:
```bash
dbt run -s <modelo>
```

Use ao seu gosto, os exemplos tem vários modelos de dados para vocês se basearem.