## Second task: image comparison

Now that we've created our image segmentation algorithm, in the spirit of evaluating its efficacy, one thing we might consider doing
is comparing how our algorithm performs on data against some known [ground truth](https://en.wikipedia.org/wiki/Ground_truth) data.
In the case of medical image segmentation, such ground truth might be provided by a manual segmentation done by a clinical radiologist.

We want to actually *quantify* our algorithm's performance against the ground truth, and to do that we will need some metrics for
comparing our segmentation results against the ground truth segmentation results. Since we are comparing binary images that are the
same size and dimensions, one sensible (if naive) image similarity metric to use would be the [Jaccard index](https://en.wikipedia.org/wiki/Jaccard_index),
which, in general, compares two [mathematical sets](https://en.wikipedia.org/wiki/Set_(mathematics)). In our case, the sets we want to
compare are the sets of "which pixels in each image are set to value 1", which you could think of as a set of pixel coordinates for
each such pixel.

1. Just as in the first task you created, begin by prototyping an algorithm in a python script or Jupyter notebook. This algorithm
   will read in two images -- the test image and the ground truth image - and compute the Jaccard index and then print it to
   standard output. *I don't have a "true" ground truth image created by an expert, but for the sake of this exercise we'll use
   [this image](http://34.229.214.79/#item/596653014d2d8d0db53d35e0) as our ground truth for comparison.*
   
1. Repeat the steps from the previous task to turn your script into a command-line interface that can be called with two arguments,
   `--test` and `--truth`, both of which are paths to image files.
   
   ```bash
   python compare_images.py --test path_to_test_image.nii.gz --truth ./segmentation_ground_truth.nii.gz
   ```
   
   To sanity check your algorithm, point the test and truth arguments to the same file; you should get an output value of `1`,
   indicating the images are identical.

1. Change the algorithm so that instead of just printing the value, it prints a JSON Object that looks like:

   ```json
   {
     "Jaccard": 0.94
   }
   ```
   
   This can be done by creating a python dictionary and using `json.dumps` to turn the dictionary into a JSON string that
   can be printed to standard output.

1. Repeat the steps from the previous task to wrap your task inside a Docker image. This time for the Dockerfile, let's use the
   base image `FROM zachmullen/resonant_course`, which already has the pip dependencies installed, so you can skip that `RUN`
   step. Create a new repository and new automated build of it in Docker Hub. Once it's been built on Docker Hub, you should
   be able to run something that looks like:
   
   ```bash
   docker run -v .:/data zachmullen/compare_images --test /data/test_image.nii.gz --truth /data/segmentation_ground_truth.nii.gz
   ```

1. Create another Task item under the Tasks folder you created in Part 1. Add the `isItemTask: true` metadata field and a second
  `itemTaskSpec` JSON field that will look like the following, but with your own docker image name substituted:
  
  TODO
   
