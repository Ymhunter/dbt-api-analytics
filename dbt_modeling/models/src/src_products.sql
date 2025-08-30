with products as (
    select * from {{ source('platzi_api', 'products') }}
)
select * from products
