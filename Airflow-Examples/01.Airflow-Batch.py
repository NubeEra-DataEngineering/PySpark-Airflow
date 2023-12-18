from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'batch_operator_dag',
    default_args=default_args,
    description='DAG to demonstrate BatchOperator',
    schedule_interval=timedelta(days=1),
)

# Define a BashOperator to execute a batch command
batch_command = """
echo "Hello, Batch!" > README.md
# Add your batch command here
"""

execute_batch_command = BashOperator(
    task_id='execute_batch_command',
    bash_command=batch_command,
    dag=dag,
)

if __name__ == "__main__":
    dag.cli()
