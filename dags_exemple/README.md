### README: Integração DBT e Apache Airflow

Este guia oferece uma visão geral sobre como integrar DBT (Data Build Tool) com Apache Airflow para orquestração de pipelines de dados. Ele abrange conceitos, melhores práticas e exemplos de como rodar comandos DBT de maneira eficiente utilizando o Airflow.

---

### **Conceitos Básicos**
- **DBT**: Uma ferramenta para transformar dados em um data warehouse. Permite criar, gerenciar e executar transformações SQL de forma modular e reutilizável.
- **Apache Airflow**: Um orquestrador de workflows que ajuda a automatizar tarefas como execução de pipelines de dados, monitoramento e controle de dependências.

Ao integrar DBT com Airflow, você pode automatizar e agendar execuções, tornando seus pipelines de dados mais robustos e escaláveis.

---

### **Principais Comandos DBT**
- `dbt run`: Executa os modelos DBT (transformações).
- `dbt test`: Valida os dados usando testes definidos no projeto DBT.
- `dbt deps`: Faz o download de dependências definidas no projeto.
- `dbt seed`: Carrega dados estáticos em tabelas do warehouse.

---

### **Melhores Práticas**
1. **Evitar Execuções Globais**:
   - Use o argumento `--select` para rodar apenas os modelos necessários:
     - Por tag: `--select tag:<nome_da_tag>`
     - Por nome de modelo: `--select <nome_do_modelo>`
     - Hierarquias: `--select <modelo_pai>+` (inclui dependências).

2. **Exclusões**:
   - Use `--exclude` para ignorar modelos específicos:
     ```bash
     dbt run --select tag:finance --exclude modelo_a_excluir
     ```

3. **Combinação de Critérios**:
   - Combine múltiplas condições:
     ```bash
     dbt run --select tag:finance+ country:US
     ```

4. **Uso de Variáveis**:
   - Utilize `--vars` para passar parâmetros dinâmicos:
     ```bash
     dbt run --select tag:daily_reports --vars '{"execution_date": "2025-01-01"}'
     ```

5. **Gerenciamento de Perfis e Projetos**:
   - Configure corretamente o diretório de perfis (`--profiles-dir`) e o diretório do projeto (`--project-dir`) para evitar problemas de configuração.

---

### **Estratégias de Segmentação**
1. **Execução por Tags**:
   - Organize seus modelos usando tags para identificar transformações relacionadas.
   - Exemplos:
     - `tag:finance`: Modelos relacionados a finanças.
     - `tag:daily_reports`: Relatórios diários.

2. **Execução Incremental**:
   - Use o argumento `--state` para rodar apenas modelos alterados:
     ```bash
     dbt run --state /path/to/previous/state
     ```

3. **Execução Hierárquica**:
   - Use `+` para incluir dependências:
     - `--select modelo+`: Executa o modelo e seus descendentes.
     - `--select +modelo`: Executa o modelo e seus ascendentes.

---

### **Fluxo Típico de Pipeline com Airflow**
Um pipeline típico de DBT no Airflow pode incluir as seguintes etapas:
1. `dbt deps`: Baixar dependências do projeto.
2. `dbt seed`: Carregar dados estáticos.
3. `dbt run`: Executar transformações específicas.
4. `dbt test`: Validar dados após transformações.

Cada etapa pode ser implementada como uma tarefa separada no Airflow, permitindo controle e monitoramento granular.

---

### **Melhores Práticas na Integração com Airflow**
1. **Defina Variáveis de Ambiente**:
   - Configure variáveis como `DBT_PROFILES_DIR` e `DBT_PROJECT_DIR` no Airflow para evitar dependências explícitas nos scripts.

2. **Use Tarefas Pequenas e Modulares**:
   - Divida pipelines em várias tarefas para maior controle e facilidade de manutenção.

3. **Implemente Reexecuções e Tolerância a Falhas**:
   - Configure `retries` e `retry_delay` no Airflow para lidar com falhas transitórias.

4. **Capte Logs**:
   - Certifique-se de que os logs do Airflow capturam a saída dos comandos DBT para depuração.

---

### **Considerações Finais**
Integrar DBT com Airflow pode aumentar significativamente a eficiência de seus pipelines de dados. Ao aplicar as práticas e estratégias descritas, você garantirá pipelines escaláveis, bem organizados e fáceis de monitorar.

Para mais informações sobre DBT, visite [dbt documentation](https://docs.getdbt.com/).