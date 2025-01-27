from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG('dbt_intermediate_example', start_date=datetime(2025, 1, 1), schedule_interval=None) as dag:
    dbt_run_tagged_models = BashOperator(
        task_id='dbt_run_tagged_models',
        bash_command='dbt run --profiles-dir /path/to/profiles --project-dir /path/to/project --select tag:finance'
    )
