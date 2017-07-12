## Medical image segmentation: Exposing in Resonant

This is the final step of our pipeline, where we expose our algorithm for use within Resonant.

1. In your **Tasks** folder that you created back in Part 1, create a new item called something like "CT bone segmentation".
   This item will represent a task by virtue of special metadata we will attach to it.
1. Navigate into your new item, and add a *simple* metadata entry:

   `isItemTask: true`
   
   This field is used in a [MongoDB index](https://docs.mongodb.com/manual/indexes/) on the server so that we can quickly query (in O(log n))
   to find all of the Tasks available in the system. This is a good example of leveraging the flexibility of a schemaless/document-oriented DBMS.
   
1. Add a *JSON* metadata field with the key ``itemTaskSpec``. For the value, set the editor into **Code** mode, and copy the following
   JSON object into it.
   
   ```
   {
    "docker_image": "zachmullen/ct_bone_segmentation",
    "container_args": [
      "--input",
      "$input{InputImage}",
      "--output",
      "$output{SegmentedImage}",
      "--threshold",
      "$input{Threshold}",
      "--closing-radius",
      "$input{ClosingRadius}"
    ],
    "inputs": [
      {
        "description": "A CT image without contrast",
        "id": "InputImage",
        "name": "Input image",
        "target": "filepath",
        "type": "file"
      },
      {
        "default": {
          "data": 200
        },
        "description": "Segmentation threshold in Hounsfield units",
        "id": "Threshold",
        "name": "Threshold value",
        "type": "integer"
      },
      {
        "default": {
          "data": 2
        },
        "description": "Radius of the structuring element used in morphological closing",
        "id": "ClosingRadius",
        "name": "Closing radius",
        "type": "number-enumeration",
        "values": [
          1,
          2,
          3,
          4
        ]
      }
    ],
    "mode": "docker",
    "outputs": [
      {
        "description": "Binary mask representing the segmentation of the bones from the input image.",
        "id": "SegmentedImage",
        "metadata": {
          "XTK": {
            "type": "volume2d"
          }
        },
        "name": "Segmented image",
        "target": "filepath",
        "type": "new-file"
      }
    ]
   }
   ```

1. In the JSON Object you set in the ``itemTaskSpec`` field, modify the ``docker_image`` field to the value of your
   own docker image that you created in the previous section.
1. Click the **Tasks** tab on the left side of the application. You should now see your task appear in the list.
   Click on it, and you will be presented with the auto-generated user interface that will allow running your task.
1. Select the input file from **DeCART Resonant course data/Data/head_ct_small.nii.gz** using the input file chooser dialog.
1. Choose the output destination to be the **Private** directory in your user's home directory, and name it something that
   ends in **.nii.gz**. Modify the threshold or closing radius if you want.
1. Click "Execute Task". The task should run and hopefully succeed. Provenance info will be recorded in the job log itself, and
   the resulting output item will contain a link back to the job that created it.
