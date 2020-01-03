# API is the interface between systems
Both the
Foobot, and io.AdaFruit APIs are examples of RESTful APIs.
That means that they work through HTTP calls that carry a JSON payload.
Data in motion protection is provided through the use of HTTPS.
Access control is through an API secret key that is provisioned from the respective services.

In this implementation I elected to not use any wrapper libraries in order to
simplify the code. The Python requests library is quite adequate in handling
with the lower level stuff. Getting the data from Foobot is simply a single HTTP GET request with an appropriate header and URL, and will return a JSON reply.
```
incoming = requests.get(fooboturl, fooheaders)
```

## Configuration and secrets

The header does contain the API secret. In the code, these secrets as well as
the specifics of the URL endpoints are not hard-coded but put in a configuration
file. In a DevOps or Continuous Delivery model this requires additional consideration
to make this secure.

See [deployment parameters and secrets](deploymentparams.md) for more details.

## Data formats and unit tests
Other than the specifics of the API calls, the work is in data format conversions.
This is the stuff that can be written down in a very concise way in Python, thanks to dicts and iterators.
Getting it right is harder. And that is where Test Driven Design comes in.

The workflow is easy. Define a test like the following, including the sample data that
was shown to work manually with the API.
```
def test_transform2adafruit():
    x = sampleinput
    y = sampleadafruit
    r = transform2adafruit(x)
    assert(y == r)
```
Then write the function `transform2adafruit()`, test it and fix any errors.
Rinse and repeat until ready.

See the [tooling](txt/tooling.md) section for more details
on the `pytest` tool.


Conventions around timestamps.
`"created_at": "2019-12-23T21:46:23Z",`
is what you can stick in and get back from adafruit

The foobot API gives back a 'time' sensor value in epoch format, e.g. `1490861042`


Inspiration for some code:
http://stackoverflow.com/questions/17301938/making-a-request-to-a-restful-api-using-python
http://support.initialstate.com/knowledgebase/articles/590091-how-to-stream-events-via-restful-api

## Integration testing
Some tests require other services and systems, the most obvious case here being the Foobot service.

Running the actual tests requires configuration information.
This will be different between local testing and testing in the continuous delivery pipeline (see [deployment parameters and secrets](deploymentparams.md)).
