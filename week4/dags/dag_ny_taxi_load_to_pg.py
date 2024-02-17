import pendulum

from airflow.models.dag import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator

from download_data import download_data
from upload_to_pg import upload_to_pg

with DAG(
    dag_id="ny_taxi-load_to_pg",
    schedule_interval=None,
    start_date=pendulum.datetime(2024, 2, 12, tz="UTC"),
    catchup=False,
    tags=["ny_taxi", "postgres", "load"],
) as dag:
    start = EmptyOperator(task_id="start")
    end = EmptyOperator(task_id="end")
    
    # download_data = PythonOperator(
    #     task_id="download_data",
    #     python_callable=download_data,
    #     op_kwargs={
    #         "base_url_green": "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/",
    #         "base_url_yellow": "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/"
    #         }
    # )
    
    upload_to_pg = PythonOperator(
        task_id="upload_to_pg",
        python_callable=upload_to_pg,
        op_kwargs={}
    )
        

    # start >> download_data >> upload_to_pg >> end
    start >> upload_to_pg >> end
    # start >> download_data >> end
    
    
    