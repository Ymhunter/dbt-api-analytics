with users as (
    select *
    from {{ ref('src_sales_customer_users') }}
)

select
{{ dbt_utils.surrogate_key(['id', 'name', 'email', 'role']) }}
    id,                                                   
    name,
    email,
    role
from users
