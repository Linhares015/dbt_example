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

## Principais Comandos DBT

Aqui está uma lista organizada de **comandos DBT Core**, começando pelos mais básicos e avançando para comandos mais complexos e úteis no dia a dia de um projeto:

---

### **Comandos Básicos**
1. **`dbt init`**
   Inicializa um novo projeto DBT.
   ```bash
   dbt init nome_do_projeto
   ```

2. **`dbt run`**
   Executa os modelos configurados no projeto.
   ```bash
   dbt run
   ```

3. **`dbt test`**
   Roda os testes configurados no projeto.
   ```bash
   dbt test
   ```

4. **`dbt compile`**
   Compila os modelos DBT em arquivos SQL no diretório `target`.
   ```bash
   dbt compile
   ```

5. **`dbt debug`**
   Verifica se o projeto está corretamente configurado.
   ```bash
   dbt debug
   ```

6. **`dbt clean`**
   Remove o diretório `target` e outros arquivos gerados automaticamente.
   ```bash
   dbt clean
   ```

7. **`dbt list`**
   Lista os recursos do projeto, como modelos, testes e snapshots.
   ```bash
   dbt list
   ```

---

### **Comandos Intermediários**
8. **`dbt seed`**
   Carrega arquivos CSV na base de dados como tabelas.
   ```bash
   dbt seed
   ```

9. **`dbt deps`**
   Baixa pacotes DBT listados no arquivo `packages.yml`.
   ```bash
   dbt deps
   ```

10. **`dbt snapshot`**
    Executa as definições de snapshot para criar tabelas versionadas.
    ```bash
    dbt snapshot
    ```

11. **`dbt build`**
    Combinação de `run`, `test`, e `snapshot` em uma única execução.
    ```bash
    dbt build
    ```

12. **`dbt source freshness`**
    Verifica a "frescura" das tabelas fontes definidas no projeto.
    ```bash
    dbt source freshness
    ```

13. **`dbt run-operation`**
    Executa macros específicas diretamente da linha de comando.
    ```bash
    dbt run-operation nome_da_macro
    ```

---

### **Comandos Avançados**
14. **`dbt docs generate`**
    Gera a documentação do projeto, incluindo lineage.
    ```bash
    dbt docs generate
    ```

15. **`dbt docs serve`**
    Abre a documentação gerada em um servidor local.
    ```bash
    dbt docs serve
    ```

16. **`dbt test --data`**
    Executa apenas os testes de dados.
    ```bash
    dbt test --data
    ```

17. **`dbt test --schema`**
    Executa apenas os testes de esquema.
    ```bash
    dbt test --schema
    ```

18. **`dbt compile --select`**
    Compila apenas modelos selecionados.
    ```bash
    dbt compile --select nome_do_modelo
    ```

19. **`dbt run --full-refresh`**
    Força a atualização completa de tabelas incrementais.
    ```bash
    dbt run --full-refresh
    ```

20. **`dbt run --select`**
    Executa modelos específicos.
    ```bash
    dbt run --select nome_do_modelo
    ```

21. **`dbt run --exclude`**
    Executa todos os modelos, exceto os excluídos.
    ```bash
    dbt run --exclude nome_do_modelo
    ```

22. **`dbt test --select`**
    Executa testes apenas para modelos específicos.
    ```bash
    dbt test --select nome_do_modelo
    ```

23. **`dbt build --select`**
    Constrói um conjunto específico de modelos.
    ```bash
    dbt build --select tag:minha_tag
    ```

24. **`dbt run-operation --args`**
    Passa argumentos para uma macro.
    ```bash
    dbt run-operation nome_da_macro --args '{"chave": "valor"}'
    ```

---

### **Comandos para Depuração e Logs**
25. **`dbt debug --config-dir`**
    Verifica o diretório de configuração DBT.
    ```bash
    dbt debug --config-dir
    ```

26. **`dbt debug --profiles-dir`**
    Verifica o diretório de perfis do DBT.
    ```bash
    dbt debug --profiles-dir ~/.dbt
    ```

27. **`dbt list --select`**
    Lista apenas os modelos selecionados.
    ```bash
    dbt list --select tag:minha_tag
    ```

28. **`dbt compile --state`**
    Compara o estado atual com o estado de execução anterior.
    ```bash
    dbt compile --state target/
    ```

---

Com esses comandos, você pode começar com o básico, explorar funcionalidades intermediárias e implementar automações avançadas no seu projeto. Para mais detalhes, consulte a [documentação oficial do DBT](https://docs.getdbt.com/).

Use ao seu gosto, os exemplos tem vários modelos de dados para vocês se basearem.