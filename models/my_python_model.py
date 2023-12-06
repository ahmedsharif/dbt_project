# models/my_python_model.py

def model(dbt):

    dbt.config(
        materialized='table'
    )

    # these are DAG-aware, and return dataframes
    dim_all_learners = dbt.ref("stg_customers")
    #source_thinkific_users = dbt.source("jaffle_shop", "stg_orders")

    philly_sample = dim_all_learners.filter(col("last_name"=="G.")).limit(1000)

    import numpy as np
	# your final 'select' statement
    df = philly_sample.select("*")

    return df