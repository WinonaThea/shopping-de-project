#from datetime import datetime
#from airflow import DAG
#from airflow.operators.bash import BashOperator

#with DAG(
#    dag_id="shopping_pipeline",
#    start_date=datetime(2026, 4, 1),
#    schedule=None,
#    catchup=False,
#    tags=["shopping", "postgres", "dbt"],
#) as dag:

#    load_raw = BashOperator(
#        task_id="load_raw",
#        bash_command="""
#        set -e
#        source /home/thea2701/venvs/jupyter-env/bin/activate
#        python /home/thea2701/project-data/scripts/load_raw.py
#        """
#    )

#    run_dbt = BashOperator(
#        task_id="run_dbt",
#        bash_command="""
#        set -e
#        source /home/thea2701/venvs/jupyter-env/bin/activate
#        cd /home/thea2701/project-data/dbt_shopping/shopping_dbt
#        dbt run --profiles-dir /home/thea2701/.dbt
#        """
#    )

#    load_raw >> run_dbt

from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="shopping_pipeline",
    start_date=datetime(2026, 4, 1),
    schedule=None,
    catchup=False,
    tags=["shopping", "postgres", "dbt"],
) as dag:

    load_raw = BashOperator(
        task_id="load_raw",
        bash_command="""
        set -e
        python /opt/airflow/project-data/scripts/load_csv_to_db.py
        """
    )

    run_dbt = BashOperator(
        task_id="run_dbt",
        bash_command="""
        set -e
        cd /opt/airflow/project-data/dbt_shopping/shopping_dbt
        dbt run --profiles-dir /opt/airflow/.dbt
        """
    )

    load_raw >> run_dbt