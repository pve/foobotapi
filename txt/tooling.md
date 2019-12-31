# Tooling
## Editor
I am not doing much software development, so I am not interested in diving into a fully
featured development environment with a steep learning curve.
On top of that, we are targeting a runtime environment in the cloud, so there is limited local development.
Having said that, I am reasonably pleased with [Atom](https://atom.io) and its packages.
<!---
your comment goes here
pyenv, pytest
stackdriver monitoring
-->


## Software repository
Git is the number one tool here. For reasons explained elsewhere (integration
with Google, and publishing),
I am using both github, as well as the Google Cloud Source Repository.

Through Git's [multiple remote features](https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes), this is manageable. For example, this command shows all my 'remote' repositories.
```
peter$ git remote -v
google	ssh://peter@peterhjvaneijk.nl@source.developers.google.com:2022/p/imp-iot-project/r/foobot (fetch)
google	ssh://peter@peterhjvaneijk.nl@source.developers.google.com:2022/p/imp-iot-project/r/foobot (push)
origin	git@github.com:pve/foobotapi.git (fetch)
origin	git@github.com:pve/foobotapi.git (push)
```
I can then selectively push the master branch to either of these origins. In practice, I do this from an Atom plugin (or package as it is called).
```
peter$ git push origin master
peter$ git push google master
```
## Python and tools
On my Mac I use [pyenv](https://github.com/pyenv/pyenv) to manage Python versions. It is simple and efficient. It is also necessary, as the system version of Python is basically wrong, and this allows me to synchronise the local Python version with the one that is used
in the GCP environment.
As an alternative you might want to consider 'virtualenv'.

For testing Python code, I am using the relatively simple [pytest](https://docs.pytest.org/en/latest/index.html).
This allows us to write test cases in Python itself.
This project has three types of tests
- tests for data conversion
- tests related to reading and parsing configuration options
- tests related to the external APIs
In a development workflow, you want to run the first two types first.
In the deployment workflow, that does not matter much: they all need to pass.

In my opinion, you should embrace security checks in any DevOps pipeline. While more sophisticated (and more expensive) tools exist, in this proof of concept project we can get along nicely with the [bandit](https://bandit.readthedocs.io/en/latest/index.html) tool for Python. It does require a bit of tweaking in its configuration to minimize false positives. For example, it does not like `assert` statements, which is what `pytest` uses extensively.

## Other tools
Included in the ecosystem are more tools, such as logging tools, builder tools, and so on. These are covered in some of the other sections in the overview of this project.

<!---
https://cloud.google.com/error-reporting/docs/setup/python

Uses loggly for logging, moving to StackDriver.

-->
