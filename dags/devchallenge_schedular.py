from airflow import DAG
from airflow.operators.docker_operator import DockerOperator
from datetime import timedelta, date, datetime
from airflow.utils.dates import days_ago

default_args = {
        'owner': 'Muhammad Faizan Khan',
        'description': 'Use of the DockerOperator',
        'depend_on_past': False,
        'start_date': days_ago(1),
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 2,
        'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    'DevChallenge',
    default_args=default_args,
    description='A simple tutorial DAG',
    schedule_interval=timedelta(days=1),
)
t1 = DockerOperator(
    task_id='DevChallengeDockerCommand',
    image='devchallenge',
    api_version='auto',
    auto_remove=True,
    command="/bin/sleep 2",
    docker_url="unix://var/run/docker.sock",
    network_mode="bridge",
    dag=dag
)
