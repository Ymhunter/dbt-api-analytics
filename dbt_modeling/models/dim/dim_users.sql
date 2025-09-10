with users as (
    select *
    from {{ ref('src_sales_customer_users') }}
)

select
{{ dbt_utils.surrogate_key(['user_id', 'name', 'email', 'role']) }}
    user_id,                                                   
    name,
    email,
    role
from users
