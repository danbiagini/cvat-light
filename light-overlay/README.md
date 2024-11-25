# Light overlay fork of CVAT

This overlay is used to run CVAT with a custom domain name with a reverse proxy terminating SSL.  This means that the CVAT server will not have to terminate SSL, and DJANGO should trust the origin

[More info](https://github.com/cvat-ai/cvat/pull/6322#issuecomment-2257131513)

## Using the cvat-light overlay
1. Clone the repo
```git clone https://github.com/danbiagini/cvat-light.git```
1. List the tags and pick the one you want to use
```git tag -l```
1. Checkout the tag
```git checkout light/v2.22.0```

## Maintainer Approach with an example of upgrading to v2.23.0
1. get the latest tags
```git fetch upstream --tags```
1. Work only from release tags on upstream cvat
```git checkout v2.23.0```
1. Create a new branch for each release
```git checkout -b light/v2.23.0```
1. Cherry pick the relevant commits from the cvat-light branch to the new release branch
```git cherry-pick light/v2.22.0```
1. Commit the changes and push to the remote repo
```git commit -am "Upgrade to v2.23.0"```
```git push origin light/v2.23.0```
1. Create a tag on the remote repo
```git tag -a light-v2.23.0 -m "Upgrade to v2.23.0"```
```git push origin light-v2.23.0```
