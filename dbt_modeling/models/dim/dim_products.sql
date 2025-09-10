with products as (
    select *
    from {{ ref('src_products') }}
)

select
{{ dbt_utils.surrogate_key(['product_id', 'product_name', 'price', 'category_name']) }}
    product_id,                                                   
    product_name,
    price,
    category_name
from products
