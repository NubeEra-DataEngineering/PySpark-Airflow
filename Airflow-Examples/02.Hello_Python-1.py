from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

def print_hello():
    print("Hello, World!")

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'hello_world_dag',
    default_args=default_args,
    description='A simple DAG to print Hello, World!',
    schedule_interval=timedelta(days=1),  # Set the schedule interval as needed
)

hello_task = PythonOperator(
    task_id='hello_task',
    python_callable=print_hello,
    dag=dag,
)

# Define the task dependencies (if any)
# hello_task.set_upstream(...)

if __name__ == "__main__":
    dag.cli()
