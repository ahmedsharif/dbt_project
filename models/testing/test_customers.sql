{{ config(materialized='incremental')}}

with source as (

    {#-
    Normally we would select from the table here, but we are using seeds to load
    our data in this project
    #}
    select * from {{ ref('raw_customers') }}

),

renamed as (

    select
        id as customer_id,
        first_name,
        last_name,
        curdate() as insert_date,
        curdate() as updated_date, 
        'raw_customers' as load_name 

    from source

)

select * from renamed
