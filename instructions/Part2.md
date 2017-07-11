## Medical image segmentation: algorithm prototyping phase

In this task, we'll create a simplistic algorithm for segmentation of bones from a CT image.

1. Download [this sample input image](http://34.229.214.79/#item/5963f36c4d2d8d07eb720b09) from our Girder instance to your local
   machine. This is a CT image of a head taken without contrast agent; it's a 3-dimensional image where each pixel is a single
   channel, 16-bit integral value that is the [radiodensity](https://en.wikipedia.org/wiki/Radiodensity) at that point, measured in
   [Hounsfield Units (HU)](https://en.wikipedia.org/wiki/Hounsfield_scale) and rounded to the nearest integer.
1. Create a python script that, when run, reads in an image using [nibabel](http://nipy.org/nibabel/), a python library for reading
   medical image formats including NIFTI, which is the one we'll be using. For now, you can hard-code this script to point to
   the path where you downloaded the input image.
1. Run a [binary thresholding](https://en.wikipedia.org/wiki/Thresholding_(image_processing)) operation on the input image to separate
   high-valued pixels from low-valued ones. Since bones are essentially linearly separable from other tissue in terms of radiodensity,
   this is basically sufficient for segmentation in this case. *Hint: The Hounsfield scale wikipedia page is a good place to look to
   determine an appropriate threshold value.*
1. In order to clean up some noise in the image, we want to remove very small "holes" that appear after the thresholding. To do this, 
   we'll use a [Morphological closing](https://homepages.inf.ed.ac.uk/rbf/HIPR2/close.htm) operation with a ball-shaped structuring
   element. The [scikit-image](http://scikit-image.org/) library
1. Write out the resulting file back to your filesystem. For now, you can simply hard-code the output path to be wherever you want.
   The output path should end with **.nii.gz** or **.nii**. (Don't make the output image have the same name as the input one or it will 
   overwrite it.)
1. Upload your result image back to your personal user space on Girder. Tag it with the following JSON metadata:

    ``XTK: {"type": "volume"}``
   
   and refresh the page. That should cause your output image to be rendered using the [XTK]() library so you can visualize your results.
   
1. OPTIONAL -- if you get done very quickly and want something else to do, switch from naive binary thresholding to use the more advanced [Otsu's method thresholding](https://en.wikipedia.org/wiki/Otsu%27s_method))
1. OPTIONAL -- if you still want more to do, try writing the output file back, but instead of using the same affine transform as the
   original image, rotate it 45 degrees around an axis of your choosing.
   
### Example solution

TODO
