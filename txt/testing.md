## Data formats and unit tests
Other than the specifics of the API calls, the work is in data format conversions.
This is the stuff that can be written down in a very concise way in Python, thanks to dicts and iterators.
Getting it right is harder. And that is where Test Driven Design comes in.

The workflow is easy. Define a test like the following, including the sample data that
was shown to work manually with the APIs.
```
def test_transform2adafruit():
    x = sampleinput
    y = sampleadafruit
    r = transform2adafruit(x)
    assert(y == r)
```
Then write the function `transform2adafruit()`, test it and fix any errors.
Rinse and repeat until ready.

See the [tooling](tooling.md) section for more details
on the `pytest` tool.

Conventions around timestamps:
* `"created_at": "2019-12-23T21:46:23Z",`
is what you can stick in and get back from adafruit.

* The Foobot API gives back a 'time' sensor value in epoch format, e.g. `1490861042`

The actual transformations happen in [transform.py](../app/transform.py). Timestamps not handled yet.

Inspiration for some code:
http://stackoverflow.com/questions/17301938/making-a-request-to-a-restful-api-using-python
http://support.initialstate.com/knowledgebase/articles/590091-how-to-stream-events-via-restful-api

## Integration testing
Some tests require other services and systems, the most obvious case here being the Foobot service.

Running the actual tests requires configuration information.
Next up we will discuss continuous delivery.
Right now, understand that the testing configuration information
will be different between local testing and testing in the continuous delivery pipeline.
Continue to [continuous delivery](cicd.md).
