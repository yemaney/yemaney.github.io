# Elastic Container Service (ECS)

## Introduction to Containers

Virtual machines virtualize operating systems.
- os consume a lot of the resources (bloat)

Container engine runs as a process within host os.
- containers run on top of container engine
- `doesn't create full new os` for each instance
- much `lighter` than virtual machines

`Docker Image`
- created using a `docker file`
- created from base image or scratch
- images contain read only layers, `(file system layers)`
- each set of changes adds another layer to the docker image
  - changes are layered onto the image using a differential architecture
- used to create a `docker container`

`Docker Container`
- running copy of a docker image
- has an addition `read write file system layer`
  - allows containers to run
- multiple containers can be created from the same docker image
  - the difference between containers created from the same docker image is only the final read write layer
  - similar `layers are reused` across containers
- portable, self contained, always run as expected
- ports are `exposed` to the host and beyond
- applications stacks can be multi-container

`Container Registry (dockerhub)`
- registry of container images
- where images are uploaded and downloaded from
  - download centos base image from here for example

