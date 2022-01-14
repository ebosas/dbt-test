with orders as (

    select * from {{ ref('stg_orders') }}

),

customer_orders as (

    select
        customer_id,
        {{ dbt_utils.datediff("'2018-01-01'", "'2018-01-20'", 'day') }} as date_diff
    from orders

)

select
    *
from customer_orders