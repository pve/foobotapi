# Secrets and credentials
<!---
-->
Deploying the software to production requires configuration.
This configuration includes for example the name of the database to store
results in, URL endpoints of APIs, and more specifically,
API secrets.
These secrets are the key (pun intended) for unlocking access to all the data. In a cloud world,
leaking secrets is one of the significant ways in which data
can leak.

One anti-pattern is to hardcode secrets in the code or in a file with the code. They will then end up in version control,
from which they will never disappear (the whole point of version control is to be able to go back to earlier versions). And you might want the source code to be public,
like the example that I am creating now.

Another reason to separate out this information is to allow for multiple deployments, for example to a test and a production environment. These will each have their own configuration items, including secrets.

A major complicating requirement is continuous delivery, as this requires these secrets to be provisioned automatically, implying that they have to be stored somewhere other than in the deployed code.

An often used approach is to use environment variables for the deployed code. Again, limiting access to the scripts where these are stored is hard.

In the end, access control to secrets is best based on the identity of the user of the secrets.

## Roles and identities can control access to secrets
For API access control, we have to rely on some kind of shared secret. This implies that we have key management,
distribution, and access control problems.

Within a cloud provider ecosystem, we have _another option_ and that is based on internally trusted identities. In our example our cloud function will be executed with a specific role, which has privileges and access rights associated with it. For example, the function can write to the database, but other than that, we'd like to restrict that access. The database service trusts the other services on the function identity and its privileges. We then don't need any secrets to
manage for this trust relation.

The essence of the approach taken here is as follows.
We store the secrets and configuration in a file (object) called `foobotsecrets.json` in Google Cloud Storage.
This object will not be publicly accessible.

In an environment variable we'll tell the deployed function what the name of the configuration file is.
Only the executing function should have read access to its contents.
We do this by giving it a role that allows it to access the secrets file.

With a bit of luck we can actually restrict the project owner (or whoever is impersonating them) from accessing these secrets. And the deployment role definitely does not need secrets access.

(graphic required here)

## Key rotation
You may need to replace keys, potentially on a regular basis.
Apparently, in the approach in this code, one limitation is that these secrets are only read during initial deployment of the cloud function, and not at every function invocation. (However there is a technical argument why these secrets potentially could be re-read at seemingly random moments in the lifecycle.) This is not different for secrets in environment
variables though. Both require a redeploy of the function to rotate the secrets.

Logic could be added to re-read the secrets every hour or so.

# More on roles

In this example we have roles for the following entities. We are using these to reduce the risk that secrets leak out.
1. The project owner
2. The executing function
3. The code deployment role
For more info on the difference: https://cloud.google.com/functions/docs/securing/
<!---
Function identity: https://cloud.google.com/functions/docs/securing/function-identity
-->


Each project has one or more owners, and their identities
are likely to be natural persons having an @gmail.com address or so.

Every project has a name, a 'project ID', and a 'project number'. Of these, only the name does not have to be globally unique. This explains why many of the service accounts either have the project ID or the project name in their identities. Example: `12345@cloudbuild.gserviceaccount.com`.
As a project owner, we can do many things, such as making
sure that a Cloud Function gets started.
However, the Cloud Function should not inherit all the
powers of the project owner, but just a limited subset.
For example the Cloud Function should be able to write to
our database, but should not be able to create projects.
That is why, during execution, we want the Cloud function
to assume a role or roles that will give it more limited capabilities.
This is why there are 'service accounts'.

Service accounts each have many roles. Each role can have many permissions. The GCP documentation has the details on
all of this scattered over the documentation of the API.

We want service accounts to have minimal roles. `12345@cloudbuild.gserviceaccount.com` has to have the rights required to run the tests.
This has the following roles (as part of the project IAM policy):
<!---
gcloud projects get-iam-policy imp-iot-project  --flatten="bindings[].members" --format='table(bindings.role)' --filter="bindings.members:528
747726418@cloudbuild.gserviceaccount.com"
-->
```
ROLE
roles/cloudbuild.builds.builder
roles/cloudfunctions.developer
roles/iam.serviceAccountUser
```
we want the executing function to run under a service account that can access
the specific object.

build steps can have their own roles.


## Permissions granularity
In the Google Cloud Platform the project is the elementary unit for defining
roles and entitlements.
An account can have a role in many projects, and those
roles could be different by project.
This is why it is called a 'project IAM
policy'.
This is in contrast to AWS where entitlements, by default, are for the
entire account.

As an example, the standard role `roles/storage.objectViewer` has the permissions
```
resourcemanager.projects.get
resourcemanager.projects.list
storage.objects.get
storage.objects.list
```
If you would leave out the `storage.objects.get` permission, the content of an
object would not be readable.

Permissions (roles) can also be granted on a resource level, such as a specific
bucket.


?In contrast, it is less obvious how to restrict entitlements, such as database access, to a specific resource, such as a named database.   
The latter actually requires a bucket level policy.
`gsutil iam get gs://imp-iot-project.appspot.com`

Question: with resources versus service account policies. Do you need both or
one of them?

Note: the GCP IAM console tells you which permissions within a
role are not being used, and can be removed or revoked.

One tip: make a .gitignore rule to ignore any file with the word 'secret' in it.

---
Related resources:

https://cloud.google.com/cloud-build/docs/securing-builds/configure-access-control

Alternate architectures.
https://cloud.google.com/secret-manager/docs/
