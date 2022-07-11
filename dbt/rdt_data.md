{% docs rdt_data_events %}

This table contains data r/dataengineering subreddit data.

All records are extracted from the reddit api through the PRAW library via lambda function, loaded to an S3 bucket, and moved via snowpipe to a snowflake database. 

We extract a week's worth of data at a time--this allows us to better track scores, comment counts, etc. We grab the latest value via window function.

{% enddocs %}
