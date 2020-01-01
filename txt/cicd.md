# Continuous Delivery pipeline
Perhaps one of the more important paradigm shifts in modern software development is *Continuous Delivery*, as it truly enables DevOps and Agile working.

The core idea is that a version controlled commit triggers an automatic sequence of steps that result in a reliable version of the software being available in production. This is called the pipeline.

There are many variations of this idea, depending on how many manual influence one wants to have. And cutting over a large live audience to a new version requires a bit more sophistication.

The objective of this project is to demonstrate how functional and security tests can be integrated into this pipeline.

In line with the rest of this project we are using the GCP services, in particular [Cloud Build](https://cloud.google.com/cloud-build/docs/build-config).

Cloud Build executes a build script, which is typically maintained in your software repository. The script can be started manually, but the more interesting
case is to trigger it when a new version of th es
