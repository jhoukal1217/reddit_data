{{ config(materialized='table', sort='created_at') }}

with rdt_posts as (
    select 
        author
    ,   dateadd('s',created_utc,'1970-01-01') as created_at
    ,   upvote_ratio
    ,   score 
    ,   num_comments
    ,   ups
    ,   downs
    ,   row_number() over (
            partition by id 
            order by load_time desc 
        ) as record_order
    from REDDIT_DATA.DATAENGINEERING.DATA_ENGINEERING_STG
)

select 
    author
,   created_at
,   upvote_ratio
,   score 
,   num_comments
,   ups
,   downs
from rdt_posts
where record_order = 1
