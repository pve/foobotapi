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
<!---
pyenv, pytest
https://cloud.google.com/error-reporting/docs/setup/python
Uses pytest for testing.

Uses bandit for security analysis.

Uses loggly for logging, moving to StackDriver.

-->
