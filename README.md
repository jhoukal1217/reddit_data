# reddit_data

A serverless data pipeline to extract Reddit data from r/dataengineering. 

## architecture

lambda -> s3 (stage) -> snowpipe -> snowflake -> dbt -> snowflake 

1. lambda: data extracted from subreddit and loaded to S3 as flat file
2. s3: s3 bucket serves as snowflake external stage 
3. snowpipe: s3 create event calls snowpipe, which copies S3 data to staging table
4. dbt: dbt (re)builds reporting table from staging material each day
5. snowflake: simple dashboard built on top of reporting table using basic queries 

## output
output is a simple snowflake dashboard:

![image](https://user-images.githubusercontent.com/35942230/178358513-a6e8ca45-5ffe-466a-b59f-c48007430de6.png)
