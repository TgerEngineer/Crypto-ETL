from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def hello():
    print("Hello from Airflow DAG")

with DAG('test_dag', start_date=datetime(2023, 1, 1), schedule_interval=None, catchup=False) as dag:
    run = PythonOperator(
        task_id='say_hello',
        python_callable=hello
    )
