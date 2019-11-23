# foobotapi
Foobot is an indoor air pollution sensor device.
InitialState is a dashboard for IOT.
Xively is a dashboard for IOT (no longer used)

Data is pulled by a Google Cloud Function into BigQuery.

Deployment of the code is through Google Cloud Build (ideally).

This code will map [Foobot](http://foobot.io) data to [InitialState](http://initialstate.com) and to Xively.
You will need accounts on all.

API keys are in environment variables.
Use settings.env to source these.

Moving to client_secrets.json in GS for secrets.

Uses pytest for testing.

Uses loggly for logging.

Inspiration for some code:
http://stackoverflow.com/questions/17301938/making-a-request-to-a-restful-api-using-python
http://support.initialstate.com/knowledgebase/articles/590091-how-to-stream-events-via-restful-api

Logging the build: XXX

cloudbuild.gserviceaccount.com has to have the rights required to run the tests.
build steps have their own environment variables, and roles.  

Using Stackdriver: https://medium.com/@duhroach/getting-google-cloud-functions-times-in-stackdriver-61ec1b33a92

Using tracing on Python functions. https://medium.com/faun/tracing-python-cloud-functions-a17545586359
