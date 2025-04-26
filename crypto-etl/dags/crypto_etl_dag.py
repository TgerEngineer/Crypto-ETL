import sys
sys.path.append('/opt/airflow')


from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from etl.etl_raw_crypto import etl_raw_crypto
from etl.load_dim_crypto import load_dim_crypto
from etl.transform_load_fact import transform_load_fact


default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 4, 18),
    'retries': 1,
}

with DAG(
    dag_id='crypto_etl_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
) as dag:

    task_raw_etl = PythonOperator(
        task_id='etl_raw_crypto',
        python_callable=etl_raw_crypto
    )

    task_dim = PythonOperator(
        task_id='load_dim_crypto',
        python_callable=load_dim_crypto
    )

    task_fact = PythonOperator(
        task_id='transform_load_fact',
        python_callable=transform_load_fact
    )

    task_raw_etl >> task_dim >> task_fact
