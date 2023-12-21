from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import paho.mqtt.publish as publish
import paho.mqtt.subscribe as subscribe

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'mqtt_demo',
    default_args=default_args,
    description='A simple MQTT demo with Apache Airflow',
    schedule_interval=timedelta(minutes=1),
)

def publish_message(**kwargs):
    publish.single("airflow/mqtt_demo", "Hello, MQTT!", hostname="localhost")

def subscribe_message(**kwargs):
    msg = subscribe.simple("airflow/mqtt_demo", hostname="localhost")
    print(f"Received message: {msg.payload}")

publish_task = PythonOperator(
    task_id='publish_message',
    python_callable=publish_message,
    provide_context=True,
    dag=dag,
)

subscribe_task = PythonOperator(
    task_id='subscribe_message',
    python_callable=subscribe_message,
    provide_context=True,
    dag=dag,
)

publish_task >> subscribe_task