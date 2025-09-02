with categories as (
    select * from {{ source('platzi_api', 'categories') }}
)
select * from categories
