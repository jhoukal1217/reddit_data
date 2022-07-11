# reddit_data

A serverless data pipeline to extract Reddit data from r/dataengineering. 

## architecture

1. lambda: data extracted from subreddit and loaded to S3 as CSV 
2. snowpipe: S3 event triggers snowpipe and copies S3 file into snowflake staging table
3. dbt: daily job runs in dbt to create reporting table

## output
output is a simple snowflake dashboard:

![image](https://user-images.githubusercontent.com/35942230/178358513-a6e8ca45-5ffe-466a-b59f-c48007430de6.png)
