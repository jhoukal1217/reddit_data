### distinct authors
select 
    date(created_at) as created_at
,   count(distinct author) as distinct_authors
from 
    dataengineering
group by 
    1
order by 
    1
    
### total posts 
select 
    count(*) as total_posts
from 
  dataengineering
  
### top posters 
select 
    author
,   avg(score) as avg_score
from 
    dataengineering
group by 
    1 
order by 
    2 desc 
limit 
    10 
    
### top posts by upvote_ratio
select 
    title
,   upvote_ratio
,   num_comments
from 
    dataengineering
order by 
    2 desc 
limit 
  10

### posts by day
select
    date(created_at) as created_at
,   count(*) as post_count
from 
    dataengineering
group by 
    1
order by 
    1

### upvote/comment ratio
select 
    ups
,   num_comments
,   title
from 
  dataengineering
  
 

