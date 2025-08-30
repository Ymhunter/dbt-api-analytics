with users as (
    select * from {{ source('platzi_api', 'users') }}
)
select * from users
