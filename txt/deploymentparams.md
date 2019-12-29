# Secrets and credentials
Deploying the software to production requires configuration. This includes for example the name of the database to store
results in, URL endpoints of APIs, and more specifically,
API secrets.
These secrets are the key (pun intended) unlocking access to all the data. In a cloud world,
leaking secrets is one of the significant ways in which data
can leak.

One anti-pattern is to hardcode secrets in the code or in a file with the code. They will then end up in version control,
from which they will never disappear (the whole point of version control is to be able to go back to earlier versions). And you might want the source code to be public,
like the example that I am creating now.

Another reason to separate out this information is to allow for multiple deployments, for example to a test and a production environment. These will each have their own configuration items, including secrets.

A major complicating requirement is continuous delivery, as this requires these secrets to be provisioned automatically, implying that they have to be stored somewhere other than in the deployed code.

An often used approach is to use environment variables for the deployed code. Again, limiting access to the scripts where these are stored is hard.

In the end, access control to secrets is best based on the identity of the user of the secrets.
## Roles
For API access control, we have to rely on some kind of shared secret. This implies that we have a key management,
distribution, and access control problem.

Within a cloud provider ecosystem, we have _another option_ and that is based on internally trusted identities. In our example our cloud function will be executed with a specific role, which has privileges and access rights associated with it. For example, the function can write to the database, but other than that, we'd like to restrict that access. The database service trusts the other services on the function identity and its privileges.

In this example we have roles for the following entities. We are using these to reduce the risk that secrets leak out.
1. The project owner
2. The executing function
3. The code deployment role
4.

`cloudbuild.gserviceaccount.com` has to have the rights required to run the tests.
build steps have their own environment variables, and roles.

The essence of the approach taken here is as follows.
We store the secrets and configuration in a file (object) called `foobotsecrets.json` in Google Cloud Storage.
In an environment variable we'll tell the function what the name of the configuration file is.
Only the executing function should have read access to its contents. With a bit of luck we can actually restrict the project owner (or whoever is impersonating them) from accessing these secrets. And the deployment role definitely does not need secrets access.

## Key rotation
You may need to replace keys, potentially on a regular basis.
Apparently, in the approach in this code, one limitation is that these secrets are only read during initial deployment of the cloud function, and not at every function invocation. (However there is a technical argument why these secrets potentially could be re-read at seemingly random moments in the lifecycle.) This is not different for secrets in environment
variables though. Both require a redeploy of the function to rotate the secrets.

Logic could be added to re-read the secrets every hour or so.

## Permissions granularity
In the Google Cloud Platform the project is the elementary unit for defining roles and entitlements. An account can have a role in many projects, and those roles could be different. This is in contrast to AWS where entitlements, by default, are for the entire account.

Example permissions for this example....


In contrast, it is less obvious how to restrict entitlements, such as database access, to a specific resource, such as a named database.   

One tip: make a .gitignore rule to ignore any file with the word 'secret' in it.

---
