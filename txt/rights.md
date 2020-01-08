## Roles and identities can control access to secrets
For API access control, we generally have to rely on some kind of shared secret. This implies that we have key management,
distribution, and access control problems.

Within a cloud provider ecosystem, we have _another option_, which is based on internally trusted identities. In our example our cloud function will be executed with a specific role/identity, which has privileges and access rights associated with it.
For example, the function can write to the database, but other than that, we'd like to restrict that access. The database service trusts the other services on the function identity and its privileges. We then don't need any secrets such as API keys to
manage for this trust relation.

The essence of the approach taken here is as follows.
We store the secrets and configuration in a file (object) called `foobotsecrets.json` in Google Cloud Storage.
This object will not be publicly accessible.

In an environment variable we'll tell the deployed function what the location of the configuration file is.
Only the executing function should have read access to its contents.
We do this by giving it a role that allows it to access the secrets file.
The code in [settings.py](app/settings.py) looks like this:
```
config = os.environ.get('CONFIGBUCKET') # supposedly a GS bucket.
secrets = getsecrets(config, "foobotsecrets.json")
```
It is run with a service account that will give it access to that data object.

With a bit of luck we can actually restrict the project owner (or whoever is impersonating them) from accessing these secrets.
And the deployment role definitely does not need production secrets access.
(It might be necessary to have a different dedicated project to hold all the secrets)

(graphic required here)

# Identities

In this example we have the following entities, each with different access rights. We are using these to reduce the risk that secrets leak out.
1. The project owner
2. The code deployment role (cloud build)
3. The executing function
For more info on the difference: https://cloud.google.com/functions/docs/securing/
<!---
-->
Continue to [service accounts](txt/serviceaccount.md).

## permissions and roles

Every project has a name, a 'project ID', and a 'project number'. Of these, only the name does not have to be globally unique. This explains why many of the service accounts either have the project ID or the project name in their identities. Example: `12345@cloudbuild.gserviceaccount.com`.

Service accounts each have many roles. And each role can have many permissions. It is not that easy to figure out the details, because the GCP documentation has the details of this scattered all over the documentation of the API.
Hierarchical inheritance also makes this harder to understand.

We want service accounts to have minimal roles and permissions. `12345@cloudbuild.gserviceaccount.com` has to have the rights required to run the tests.
This has the following roles (as part of the project IAM policy):
<!---
Following result by
gcloud projects get-iam-policy imp-iot-project  --flatten="bindings[].members" --format='table(bindings.role)' --filter="bindings.members:528
747726418@cloudbuild.gserviceaccount.com"
-->
```
ROLE
roles/bigquery.admin
roles/cloudbuild.builds.builder
roles/cloudfunctions.developer
roles/iam.serviceAccountUser
```
we want the executing function to run under a service account that can access
the specific object.

## Permissions granularity
In the Google Cloud Platform the project is the elementary unit for defining
roles and entitlements.
An account can have a role in many projects, and those
roles could be different by project.
This is why it is called a 'project IAM
policy'.
This is in contrast to AWS where entitlements, by default, are for the
entire account.

As an example, the standard role `roles/storage.objectViewer` has the following permissions (as demonstrated by `gcloud iam roles describe roles/storage.objectViewer`):
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
These are 'resource policies'


?In contrast, it is less obvious how to restrict entitlements, such as database access, to a specific resource, such as a named database.   
The latter actually requires a bucket level policy.
Listing roles and members that have access to a resource looks like this:
`gsutil iam get gs://imp-iot-project.appspot.com`.
Note that there seems to be no equivalent way to list all permissions
on a resource, as permissions are always linked through a role.

Question: with resources versus service account policies. Do you need both or
one of them? In other words: Is the actual permission the intersection of the permissions of the account and the resources policy?
Also confusing is that policies are meant to restrict potential behaviour.
No policy therefore means: no restrictions.??
However this is not completely true as permissions by default are
only granted within a project.
No: resources are part of a project, if you allow access on the project level you will also allow access on the resource level.

https://cloud.google.com/iam/docs/overview#policy_hierarchy

Note: the GCP IAM console tells you which permissions within a
role are not being used, and can be removed or revoked.

One tip: make a .gitignore rule to ignore any file with the word 'secret' or 'private' in it.

Continue to [monitoring](txt/monitoring.md)

---
Related resources:

https://cloud.google.com/cloud-build/docs/securing-builds/configure-access-control

Alternate architectures.
https://cloud.google.com/secret-manager/docs/
