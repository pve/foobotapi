# Using the Foobot API with Google Cloud Functions and CD
The Foobot is an indoor air pollution sensor device.
Io.Adafruit is a dashboard for IOT.

![foobot picture](/txt/foobotpicture.jpg)

This code pulls [Foobot](http://foobot.io) data from its API and sends it to [io.adafruit.com](http://io.adafruit.com) and a Google BigQuery database. As the picture suggests, this is in live production.  

<!---
your comment goes here
In the readme, the audience is those who wish to
figure out if they should read any further
-->

The second objective of this code is to demonstrate **cloud native development**. In this case we are working with '_serverless_' functions, including continuous delivery, and
this time we are focussing on the Google code ecosystem. More tutorial explanation is in [here](main.md), where I dissect the full approach theme by theme, topic by topic.

Technologies and techniques used:
- Google Cloud functions
- Continuous delivery through Google Cloud Build
- Automated unit, integration and security testing
- BigQuery
- Foobot API, Io.Adafruit API
- Continuous monitoring through StackDriver
- Slack integration for build and run notifications
- Secrets and credentials management in a DevSecOps world
- Workflow for Python based development (atom, pyenv, pytest, bandit)

You should be able to replicate this setup yourself, if you have accounts for
these services.

Continue reading [here](main.md).
