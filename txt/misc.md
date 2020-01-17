# Miscellaneous
Actual costs.

With the metrics explorer on `metric.type="cloudfunctions.googleapis.com/function/user_memory_bytes"`
we can see that the memory consumption is less than 80MByte.
Consequently, to reduce our pretty low cost even more, we can halve the allocated
memory in the deployment by using the deployment flag `--memory=128MB`.

More threat models (i.e. CSA IL); According to Google, access control is
the most relevant security control: https://cloud.google.com/functions/docs/securing/

Restrict developers from leaking secrets?
accidentally, purposely?
Government action?

minimalistic

Generating a project like this.
With the Gcloud API creating a project is simple. With Python a bit more flexible and complicated
```
gcloud projects create PROJECT_ID --organization=ORGANIZATION_ID
```
