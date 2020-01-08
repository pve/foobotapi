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

An often used approach is to use environment variables for the deployed code. Again, a disadvantage of this is that limiting access to the scripts where these are stored is hard.

In the end, access control to secrets is best based on the identity of the user of the secrets.
Before we explain in more detail how that can be made to work, we wrap up this section by discussing key rotation.

## Key rotation
You may need to replace keys, potentially on a regular basis.
Apparently, in the approach in this code, one limitation is that these secrets are only read during initial deployment of the cloud function, and not at every function invocation. (However there is a technical argument why these secrets potentially could be re-read at seemingly random moments in the lifecycle.) This is not different for secrets in environment
variables though. Both require a redeploy of the function to rotate the secrets.

Logic could be added to re-read the secrets every hour or so.

Continue to [roles, permissions and access rights](rights.md).
