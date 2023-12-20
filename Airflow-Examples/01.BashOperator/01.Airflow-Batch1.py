from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

# import datetime
# d = datetime.date(2022, 12, 25)
# print(d)

# after_2_year = datetime.now() + timedelta(days = 730)

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 12, 20),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'bash_operator_single_dag',
    default_args=default_args,
    description='Simple Hello World DAG',
    schedule_interval=timedelta(days=1),
)

hello_task = BashOperator(
    task_id='hello_task',
    bash_command='echo "Hello, World!"',
    dag=dag,
)
