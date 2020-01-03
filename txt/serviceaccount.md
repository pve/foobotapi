# Creating our service accounts
The objective here is to create dedicated service accounts for least privilege
access.

Following https://cloud.google.com/functions/docs/securing/function-identity
we first create a runtime service account for the function identity.
This will be the only one that should have access to the secrets buckets.
In our project we name it
 `foobotfunction@imp-iot-project.iam.gserviceaccount.com`.

For that we need the `Storage Object Viewer` role

Our function also accesses BigQuery to store data in. That requires the
`BigQuery Data Editor` role (potentially a little less than that).

We could potentially make a custom role that is even more strict.

(next step: reduce other role/members that have access to the bucket)
