from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.sensors.http_sensor import HttpSensor
from airflow.operators.dummy_operator import DummyOperator

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'sensor_example_dag',
    default_args=default_args,
    description='DAG to demonstrate the usage of Sensors in Apache Airflow',
    schedule_interval=timedelta(days=1),
)

# Define a HttpSensor to wait for a website to become available
website_sensor_task = HttpSensor(
    task_id='wait_for_website',
    http_conn_id='http_default',  # Connection ID for HTTP parameters (define in Airflow UI)
    # endpoint='/path/to/your/website',  # Replace with the endpoint to check
    endpoint = 'https://jsonplaceholder.typicode.com/posts/1',
    timeout=120,  # Maximum time (in seconds) that the sensor will wait for the website to become available
    poke_interval=30,  # Time (in seconds) between pokes to the website
    mode='poke',  # The mode determines the strategy used to poke for availability
    soft_fail=True,  # Return False immediately on failure or log failure and continue checking
    retries=3,  # Number of retries before declaring the website unavailable
    dag=dag,
)

# Define a DummyOperator as a placeholder for the next steps in the DAG
next_steps_task = DummyOperator(
    task_id='next_steps',
    dag=dag,
)

# Set task dependencies
website_sensor_task >> next_steps_task

if __name__ == "__main__":
    dag.cli()
