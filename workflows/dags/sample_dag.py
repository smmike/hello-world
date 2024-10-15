from airflow.decorators import dag
from airflow.utils.dates import days_ago
from airflow.operators.bash import BashOperator


default_args = {
    'owner': 'airflow',
}

# added comment
@dag(default_args=default_args, schedule_interval="@daily", start_date=days_ago(2), tags=['sample'])
def sample_dag():
    def sample_task():
        _task = BashOperator(
            task_id="hello_world",
            bash_command="echo 'hello world!'"
        )
        return _task

    task = sample_task()

sample_dag = sample_dag()
