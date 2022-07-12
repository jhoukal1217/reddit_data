# reddit_data

- an ETL pipeline designed to extract data from the r/dataengineering subreddit.

## architecture

- eventbridge (cron) -> lambda -> s3 (stage) -> snowpipe -> snowflake -> dbt -> snowflake 

1. eventbridge: cron kicks off lambda once per day
2. lambda: data extracted from subreddit and loaded to S3 (external stage) as flat file
3. snowpipe: s3 create event triggers snowpipe, which copies S3 data to staging table
4. dbt: dbt (re)constructs reporting table from staging material courtesy of daily dbt cron
5. snowflake: simple dashboard built on top of reporting table using basic queries 

## output
- output is a simple snowflake dashboard:

![image](https://user-images.githubusercontent.com/35942230/178358513-a6e8ca45-5ffe-466a-b59f-c48007430de6.png)

## notes 

- this serverless pipeline is configured to run once daily. 
- each extract job pulls a week's worth of data from the reddit api. this allows us to track updated post stats for popular posts with longer lifespans. 
- we "expose" the latest data using window functions. 
