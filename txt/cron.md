The function is triggered by a cron type of function, through a pub sub topic.
The message itself is empty.

One of the error modes is if the function fails without consuming the message.
This causes a backlog, which is why you want those messages to have very short
retention.

Unfortunately, the subscription to the cron topic is generated automatically,
and it does not appear to be possible to modify the retention period.
