# Triggering the function
The function is triggered by a cron type of function, through a message on a PubSub topic.
The message itself is empty.

The PubSub message will then trigger the Google Cloud function.

One of the error modes is when the function fails without consuming the message.
This causes a backlog of messages, which is why you want those messages to have very short
retention.

Unfortunately, the subscription to the cron topic is generated automatically,
and it does not appear to be possible to modify the retention period from its
default (1 week).

Anecdote: at one point, the core function failed to execute properly for more
than a week. When I got it to work again, the system tried to catch up by
executing all triggers really quickly. Needless to say, this avalanche
is useless, and it
populated the database with many duplicates. On top of that, it hit the Foobot
rate limiter, which works through a 24 hour quota.
This effectively shut the system down until midnight.

One mitigation for this is to discard stale triggers. But if there is adequate
monitoring later in the process (see 'monitoring'), this does not add much value.
On larger systems we do need something to prevent an avalanche
like this, because we don't want incidents
like those to saturate downstream services. Search for 'circuit breaker pattern'
if you want to look deeper into this.

Continue to [tooling](txt/tooling.md)
