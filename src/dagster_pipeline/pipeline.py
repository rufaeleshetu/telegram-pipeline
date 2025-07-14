
from dagster import op, job

@op(config_schema={"name": str})
def greet_op(context):
    name = context.op_config["name"]
    context.log.info(f"Hello, {name}!")
    return f"Hello, {name}!"

@job
def greet_job():
    greet_op()
