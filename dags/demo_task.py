from datetime import timedelta

from airflow import DAG
from airflow.utils.dates import days_ago

from airflow.operators.docker_operator import DockerOperator
from airflow.operators.python_operator import PythonOperator


default_args = {
        'owner': 'Muhammad Faizan Khan',
        'description': 'Use of the DockerOperator',
        'depend_on_past': False,
        'start_date': days_ago(1),
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 5,
        'retry_delay': timedelta(minutes=1)
}


dag = DAG(
    'Demo_Dag_Please_leave_it_as_it_is',
    default_args=default_args,
    description='Bitcap dag configuration',
    schedule_interval='@hourly',
)


t1 = DockerOperator(
    task_id='DockerOperator',
    image='hello-world',
    api_version='auto',
    auto_remove=True,
    docker_url="unix://var/run/docker.sock",
    network_mode="bridge",
    xcom_push=True,
    dag=dag
)


def perform_calculation(**context):
    output = context['ti'].xcom_pull(task_ids='DockerOperator')
    print(output)


t2 = PythonOperator(
    task_id='PythonOperator',
    python_callable=perform_calculation,
    provide_context=True,
    dag=dag
)

t1 >> t2
