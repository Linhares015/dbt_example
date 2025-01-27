from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG('dbt_advanced_example', start_date=datetime(2025, 1, 1), schedule_interval=None) as dag:
    dbt_run_filtered = BashOperator(
        task_id='dbt_run_filtered',
        bash_command=(
            'dbt run --profiles-dir /path/to/profiles --project-dir /path/to/project '
            '--select tag:finance+ country:US '
            '--exclude model_name_to_skip'
        )
    )
