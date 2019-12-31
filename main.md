<!---
your comment goes here
alternate approaches (building a server, etc).
do structured logging to Stackdriver

risk based approach.
what is the development workflow (edit -> local test -> GCF test-> prod)

next level: generate the project and its contents, including the logging.
-->

# Overall architecture
The overall architecture of the solution has the following components:
- At the core of the architecture is a 'serverless' function that regularly pulls data from the
Foobot API and sends it to an AdaFruit dashboard for viewing and a BigQuery database
for later analysis. This is a Google Cloud Platform (GCP) function, though it could probably
be implemented in a similar way in Amazon Web Services (AWS) Lambda.
- The function is triggered on a regular basis. In Google Cloud this is done
through a specific service (cron) that is related to the Google App Engine service,
and communicates through PubSub, the GCP messaging service.
In AWS all this is part of Lambda.
- BigQuery data storage was selected because its cost is proportional to usage, and there is
no hourly charge (in contrast to ....).
- Part of the operation is to monitor production and alert on anomalies.
- In developing and updating the system we want the feature velocity to be high:
from the push to the source code repository to production should be as frictionless
as possible. In fact, it should be automatic, including testing.

See the following sections for more details:
* [API and testing](txt/apiandtesting.md)
* [triggering the events](txt/cron.md)
* [tooling](txt/tooling.md)
* [CI/CD pipeline](txt/cicd.md)
* [deployment parameters and secrets](deploymentparams.md)
* [monitoring](txt/monitoring.md)

## Alternative architectures
* You could run code like this on a server. In fact, an earlier version of this ran on a Raspberry Pi. This implies an
operational responsibility for that machine and all the software that runs
on it. It remains to be seen if this is more or less work than running it on GCP.
In terms of scalability however, the server approach is either vastly
overprovisioned or underprovisioned. Both are a waste.
* There may be SaaS/PaaS level solutions to do this API integration.
Zapier and IFTTT come to mind. However, in general these cannot be relied upon
to support the specific API services that you need.
* Within GCP, we could consider logging our API JSON files into StackDriver, and then use its functionality to create our reports.
However, we'd need to
figure out how long term data retention works in StackDriver.
