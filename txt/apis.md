# API is the interface between systems
This project is about connecting systems, and APIs are the canonical way to
connect cloud services.
Both the
Foobot, and io.AdaFruit APIs are examples of RESTful APIs.
That means that they work through HTTP calls that carry a JSON payload, rather
than a more dedicated protocol.

This architectural choice has some security implications.
Data in motion protection is provided through the use of HTTPS.
Access control is through an API secret key that is provisioned from the respective services.

In this implementation I elected to not use any wrapper libraries in order to
simplify the code. Instead we work directly with URLs that represent the
API endpoints.
The Python requests library is quite adequate in handling the lower level stuff. Getting the data from Foobot is simply a single HTTP GET request with an appropriate header and URL, and will return a JSON reply.
The code does not get more complicated than this.
```
incoming = requests.get(fooboturl, fooheaders)
```

## Configuration and secrets

The header in the HTTP request does contain the API secret. In the code, these secrets as well as
the specifics of the URL endpoints are not hard-coded but put in a configuration
file. In a DevOps or Continuous Delivery model this requires additional consideration
to make this secure.

Jump ahead to [deployment parameters and secrets](deploymentparams.md) for more details.

Continue to [triggering the function](cron.md).
