## Medical image segmentation: CLI and docker conversion

For the next step, we'll take your algorithm and turn it into a command-line interface (CLI) using python's
[argparse](https://docs.python.org/3/library/argparse.html#module-argparse) module.

1. Import `argparse` into your bone segmentation script and convert the script so that it receives two required
   command-line arguments: ``--input`` for a path to the input file, and ``--output`` for a path of where
   the output file should be written. When done, you should be able to call, e.g.
   
   `bone_segmentation.py --input ./head_ct_small.nii.gz --output ./head_ct_segmented.nii.gz`
   
1. Once that CLI works, check your script into a public repository under your GitHub user.

1. Register a user on [Docker Hub](https://hub.docker.com). This is a website that will host your docker images publicly and build them
   automatically from your GitHub repositories.

1. Once registered, use the menu in the upper right to **Create automated build**. Select **GitHub** automated build, and choose the
   repository you want to auto-build.
   
   ![](../images/create_autobuild.png)
   
   ![](../images/github_autobuild.png)

1. Download [docker]() (community edition) onto your local machine
