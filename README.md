# reddit_data

Serverless data pipeline to extract Reddit data from r/dataengineering. 

## architecture

1. Lambda: Data extracted from subreddit and loaded to S3 as CSV 
2. Snowpipe: S3 event triggers snowpipe, copying S3 file into Snowflake staging table
3. dbt: daily job runs in dbt to create reporting table

## output

