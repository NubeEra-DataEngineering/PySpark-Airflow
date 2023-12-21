from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

def extract():
    print("Extracting data from source")

def transform():
    print("Transforming data")

def load():
    print("Loading data into destination")

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'simple_data_pipeline',
    default_args=default_args,
    description='Simple data pipeline DAG',
    schedule_interval=timedelta(days=1),
)

extract_task = PythonOperator(
    task_id='extract_task',
    python_callable=extract,
    dag=dag,
)

transform_task = PythonOperator(
    task_id='transform_task',
    python_callable=transform,
    dag=dag,
)

load_task = PythonOperator(
    task_id='load_task',
    python_callable=load,
    dag=dag,
)

extract_task >> transform_task >> load_task
