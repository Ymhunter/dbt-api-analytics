with users as (
    select * from {{ source('platzi_api', 'users') }}
)
select
id,
email,
password,
name,
role,
avatar,
 from users
