from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import pandas as pd
import os

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 5, 12),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

def extract():
    # Run two python files for extraction
    os.system("python ../bbc_scrapper.csv")
    os.system("python ../dawn_scrapper.csv")

def transform():
    # Run two python files for transformation
    os.system("python ../bbc_scrapper_cleaned.csv")
    os.system("python ../dawn_scrapper_cleaned.csv")

def load():
    # Run bash commands to load data to GDrive using DVC and push changes to Git
    os.system("dvc add ../data/merged_data.csv")
    os.system("dvc push")
    os.system("git add .")
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
