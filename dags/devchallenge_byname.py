from airflow import DAG
from airflow.operators.docker_operator import DockerOperator
from airflow.operators.python_operator import PythonOperator
from datetime import timedelta
from airflow.utils.dates import days_ago

from airflow.models import Variable

beer_name = Variable.get("beer_name", "Punk")


default_args = {
        'owner': 'Muhammad Faizan Khan',
        'description': 'Use of the DockerOperator',
        'depend_on_past': False,
        'start_date': days_ago(2),
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 2,
        'retry_delay': timedelta(minutes=1)
}


dag = DAG(
    'DevChallenge3',
    default_args=default_args,
    description='A simple tutorial DAG',
    schedule_interval='@daily',
)


t1 = DockerOperator(
    task_id='DockerOperator',
    image='devchallenge_devchallenge',
    api_version='auto',
    auto_remove=True,
    command="byname -n " + str(beer_name),
    docker_url="unix://var/run/docker.sock",
    network_mode="bridge",
    dag=dag
)


def perform_calculation(**context):
    # print(brewed_until)
    print('hi')


t2 = PythonOperator(
    task_id='PythonOperator',
    python_callable=perform_calculation,
    provide_context=True,
    dag=dag
)

t1 >> t2
