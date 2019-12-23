# Using the foobotapi
The Foobot is an indoor air pollution sensor device.
InitialState is a dashboard for IOT. This code connects the
Foobot to several data sinks.

<!---
your comment goes here
In the readme, the audience is those who wish to
figure out if they should read any further
-->

The second objective of this code is to demonstrate cloud native development. In this case we are working with 'serverless' functions, and we are focussing on the Google code ecosystem. More tutorial explanation is in [here](main.md).

Data is pulled by a Google Cloud Function into BigQuery.

Deployment of the code is through Google Cloud Build.

This code maps [Foobot](http://foobot.io) data to [InitialState](http://initialstate.com), and a Google BigQuery database.
InitialState no longer has free plans.
To replicate this setup you will need accounts on all.

API keys are in a file clientsecrets.json in GS for secrets.

Uses pytest for testing.

Uses bandit for security analysis.

Uses loggly for logging, moving to StackDriver.

Inspiration for some code:
http://stackoverflow.com/questions/17301938/making-a-request-to-a-restful-api-using-python
http://support.initialstate.com/knowledgebase/articles/590091-how-to-stream-events-via-restful-api

Logging the build: XXX

cloudbuild.gserviceaccount.com has to have the rights required to run the tests.
build steps have their own environment variables, and roles.  

Using Stackdriver: https://medium.com/@duhroach/getting-google-cloud-functions-times-in-stackdriver-61ec1b33a92

Using tracing on Python functions. https://medium.com/faun/tracing-python-cloud-functions-a17545586359
