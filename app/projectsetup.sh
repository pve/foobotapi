# create project
# clone ?  repo
$REPO_NAME


gcloud beta builds triggers create cloud-source-repositories \
    --repo=$REPO_NAME \
    --branch-pattern=".*" \
    --build-config=[BUILD_CONFIG_FILE] \
