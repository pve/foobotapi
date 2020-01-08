# Continuous Delivery pipeline
Perhaps one of the more important paradigm shifts in modern software development is *Continuous Delivery*, as it truly enables DevOps and Agile working.

The core idea is that a version controlled commit triggers an automatic sequence of steps that result in a reliable version of the software being available in production. This sequence is called the pipeline.

There are many variations of this concept, depending on how much manual influence one wants to have. And cutting over a large live audience to a new version requires a bit more sophistication.

The objective of this project is to demonstrate how functional and security tests can be integrated into this pipeline.

In line with the rest of this project we are using the GCP services, in particular [Cloud Build](https://cloud.google.com/cloud-build/docs/build-config).

Cloud Build executes a build script, which is typically maintained in your software repository. The script can be started manually, but the more interesting
case is to trigger the build automatically whenever a new version of the software is committed to the source code repository.

It turns out that setting up this trigger is slightly easier from the Google Cloud Source Repository, than from Github.

We also want to be notified of build progress, e.g. through Slack. While StackdDriver
does give us those features, Cloud Build surprisingly does not have that. Cloud Build only
pushes a message to a PubSub topic. It takes just another [specific Google Cloud Function](https://cloud.google.com/cloud-build/docs/configure-third-party-notifications) to
push that to Slack. Managing that function can be done in a similar way as we are doing in this project, which makes this a bit recursive.

In this project there are three build steps:
1. running all functional tests
2. running all security tests
3. pushing the code to the production environment.

Step one in the `cloudbuild.yaml` file runs a small container to execute the
tests (see below). Note the use of the `CONFIGBUCKET` to make the test run in
an acceptance environment. This points to a GCP Storage bucket that holds
configuration files, including API secrets.
```
- name: python:3.7-slim
  id: unittest
  entrypoint: 'bash'
  args: ['-c', 'pip install -r ./app/requirements.txt && pytest -v .']
  env:
    - CONFIGBUCKET=staging.imp-iot-project.appspot.com
```
In the reality of this project, we don't bother to have a separate environment
as there is no data or test that we would pollute the production database with.
There are some interesting details on the ownership and access rights of the
configuration files.
Those are discussed elsewhere.

When `pytest` fails, the build step fails, the entire build is aborted, and
the latest correct version of the software will still be in production.

The security testing is about as simple. The essential command line is
```
args: ['-c', 'pip install -r ./app/requirements.txt && bandit -l -s B101 -r .']
```
The essence of the parameters here is that they suppress false positives.
With the default configuration files of `bandit`, the code `B101` stands for `assert` statements.
Bandit does not like them, but we use them in the functional testing.

Finally, the last step installs the software in production. This is done by
running a container that runs the GCP API, which we give the proper
commands.
```
- name: 'gcr.io/cloud-builders/gcloud'
  id: function deployment
  dir: app
  args: ['functions', 'deploy', 'foobotapi',
  '--trigger-topic=foobotcron',
  '--runtime=python37',
  '--service-account=foobotfunction@imp-iot-project.iam.gserviceaccount.com',
  '--region=us-central1',
  '--entry-point=oneshot']
  env:
    - CONFIGBUCKET=imp-iot-project.appspot.com
```
In this step `gcr.io` stands for the 'Google Container Registry', which hosts the container that runs the GCP API. The arguments of `gcloud` are [described in more detail here](https://cloud.google.com/functions/docs/deploying/filesystem) (note that the local machine from which the code is deployed is now actually the container ran by Cloud Build in this build step, hence the `app` directory).

(Again, we have an interesting set of roles and access rights
to deal with here. In addition to the rights of the running software, we have different access rights for the builder, i.e. the process running `gcloud`.)

Continue to [deployment parameters](deploy) for more in-depth
dicussion on XXX
