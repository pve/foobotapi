## Identities and accounts
Each project has one or more owners, and their identities
are likely to be natural persons having an @gmail.com address or so.

The other two entities (Cloud Builder and Cloud Function) correspond to _service accounts_.

As a project owner, we can do many things, such as making
sure that a Cloud Function gets started.
However, the Cloud Function should not inherit all the
powers of the project owner, but just a limited subset.
For example the Cloud Function should be able to write to
our database, but should not be able to create projects.
That is why, during execution, we want the Cloud function
to assume a role or roles that will give it more limited capabilities.
This is one of the reasons why there are 'service accounts'.

The opposite also happens:  we want our cloud functions to
be able to have more capabilities than the cloud builder that installs them.
## Service accounts
In GCP as well as in other cloud systems, access rights are considerably more detailed and complicated than in your old-school Linux world.
This is a necessary consequence of the much higher level of automation that the cloud has.
In Linux a user has read, write and/or execute access to a file, it is as simple as that.
A little trickier is what happens when a user (manually) runs a program or command.
By default Linux gives that program the same rights as the user executing it. However, if the 'set user id' bit is set on the program, permissions are now based on the _owner_ of the program, rather than the _user_ of the program.
That means that if the owner of the program can read a file, the program can read that file too, even if the user executing the program cannot.

Service accounts can be seen as a generalisation of that. In a cloud world it is typically not a user that runs a program, but it is another program, often through an API, and not necessarily initiated from with the same provider.
What are the access rights of that program?

In Linux terms this would be like specifying _another_ user under whose identity the program will run: a user that is neither the executing user nor the owner of the program.
In cloud what also changes is that we don't run programs, but rather invoke services, for which the whole idea of ownership is much different.

So how are roles and access rights associated with identities?

# Creating our service accounts
The objective here is to create dedicated service accounts for least privilege
access.

Following https://cloud.google.com/functions/docs/securing/function-identity
we first create a runtime service account for the function identity.
This will be the only one that should have access to the secrets buckets.
In our project we name it
 `foobotfunction@imp-iot-project.iam.gserviceaccount.com`.

For that we need the `Storage Object Viewer` role.

Primitive role needed:
storage.buckets.get role role/viewer
You can apply primitive roles at the project or service resource levels by using Cloud Console, the API and the gcloud command-line tool.

Our function also accesses BigQuery to store data in. That requires the
`BigQuery Data Editor` role (potentially a little less than that).

We could potentially make a custom role that is even more strict.

## random notes

(next step: reduce other role/members that have access to the bucket; some are inherited, from what?)

Note: to add project wide storage permissions to a service account
is done in Console IAM, for bucket level permissions you have to do that
at Console Storage.
```
gsutil iam ch -d group:readers@example.com:legacyBucketReader \
                  group:viewers@example.com:objectViewer gs://staging.imp-iot-project.appspot.com

gsutil iam ch -d user:john.doe@example.com gs://staging.imp-iot-project.appspot.com
```
