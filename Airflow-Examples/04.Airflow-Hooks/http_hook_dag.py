from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.hooks.http_hook import HttpHook
import json

# Define the HTTP Hook
class MyHttpHook(HttpHook):
    def __init__(self, method, http_conn_id='http_default'):
        super(MyHttpHook, self).__init__(method=method, http_conn_id=http_conn_id)

    def get_data(self, endpoint, data):
        response = self.run(endpoint, data=json.dumps(data))
        return response.json()

# Define a function to use the HTTP Hook
def make_api_request():
    http_hook = MyHttpHook(method='GET', http_conn_id='http_default')
    
    # Replace the URL with your API endpoint
    endpoint = 'https://jsonplaceholder.typicode.com/posts/1'

    # Make the API request
    response = http_hook.get_data(endpoint, data={})
    
    print("API Response:", response)

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'http_hook_dag',
    default_args=default_args,
    description='DAG to demonstrate HTTP Hook in Apache Airflow',
    schedule_interval=timedelta(days=1),
)

# Define a PythonOperator to execute the API request
api_request_task = PythonOperator(
    task_id='make_api_request',
    python_callable=make_api_request,
    dag=dag,
)

if __name__ == "__main__":
    dag.cli()

# airflow trigger_dag http_hook_dag
