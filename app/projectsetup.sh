# create project
# clone ?  repo
$REPO_NAME

# trigger builds
gcloud beta builds triggers create cloud-source-repositories \
    --repo=$REPO_NAME \
    --branch-pattern=".*" \
    --build-config=[BUILD_CONFIG_FILE] \
