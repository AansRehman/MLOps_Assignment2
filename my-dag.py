from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import os

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 5, 12),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'dagrun_timeout': timedelta(days=1),
}


def extract():
    # Run two python files for extraction
    os.chdir("~")
    os.chdir("Assignment02")
    os.system("pip install requests beautifulsoup4 pandas")
    os.system("python3 bbc_scrapper.py")
    os.system("python3 dawn_scrapper.py")

def transform():
    # Run two python files for transformation
    os.system("python3 cleaning_bbc_dataset.py")
    os.system("python3 cleaning_dawn_dataset.py")
    os.system("python3 combining_files.py")

def load():
    # Run bash commands to load data to GDrive using DVC and push changes to Git
    os.system("dvc add data\\merged_data.csv")
    os.system("dvc push -r gdrive")
    os.chdir("data")
    os.system("git add merged_data.csv.dvc")
    os.system("git commit -m 'Update data'")
    os.system("git push")

with DAG('my_dag', default_args=default_args, schedule_interval='@daily', catchup=False) as dag:
    extract_task = PythonOperator(
        task_id='extract_task',
        python_callable=extract
    )

    transform_task = PythonOperator(
        task_id='transform_task',
        python_callable=transform
    )

    load_task = PythonOperator(
        task_id='load_task',
        python_callable=load
    )

    extract_task >> transform_task >> load_task
