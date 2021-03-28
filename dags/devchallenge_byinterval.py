from airflow import DAG
from airflow.operators.docker_operator import DockerOperator
from airflow.operators.python_operator import PythonOperator
from datetime import timedelta
from airflow.utils.dates import days_ago
import json

from airflow.models import Variable

brewed_from = Variable.get("brewed_from", "10-2011")
brewed_until = Variable.get("brewed_until", "09-2013")


default_args = {
        'owner': 'Muhammad Faizan Khan',
        'description': 'Use of the DockerOperator',
        'depend_on_past': False,
        'start_date': days_ago(2),
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 5,
        'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    'BeerByInterval',
    default_args=default_args,
    description='A simple tutorial DAG',
    schedule_interval='@daily',
)


t1 = DockerOperator(
    task_id='DockerOperator',
    image='bitcap',
    api_version='auto',
    auto_remove=True,
    command='byinterval -f "{}" -u "{}"'.format(brewed_from, brewed_until),
    docker_url="unix://var/run/docker.sock",
    network_mode="bridge",
    xcom_push=True,
    dag=dag
)


def perform_calculation(**context):
    output = json.loads(context['ti'].xcom_pull(task_ids='DockerOperator'))
    avg_ibu_ibv = json.dumps({
        "avg_ibu": sum([i['ibu'] for i in output]) / (len(output) or 1),
        "avg_abv": sum([i['abv'] for i in output]) / (len(output) or 1)
    })
    context['ti'].xcom_push(key="AVG_IBU_ABV", value=avg_ibu_ibv)
    print(avg_ibu_ibv)


t2 = PythonOperator(
    task_id='PythonOperator',
    python_callable=perform_calculation,
    provide_context=True,
    dag=dag
)

t1 >> t2
