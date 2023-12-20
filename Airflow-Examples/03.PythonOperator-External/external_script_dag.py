from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

# Import the function from the external script
from external_script import print_hello

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'external_script_dag',
    default_args=default_args,
    description='DAG to execute an external Python script',
    schedule_interval=timedelta(days=1),
)

# Define a PythonOperator to execute the external script
execute_external_script = PythonOperator(
    task_id='execute_external_script',
    python_callable=print_hello,  # Reference the function from the external script
    dag=dag,
)

if __name__ == "__main__":
    dag.cli()

# airflow webserver -p 8080
# airflow scheduler
# airflow trigger_dag external_script_dag