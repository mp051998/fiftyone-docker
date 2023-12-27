# FiftyOne in Docker

Use this repository to build a Docker image for [FiftyOne](https://voxel51.com/docs/fiftyone/).

## Installation

1. Clone this repository.

2. Head over to the `Dockerfile` file and add flags depending on what your requirements are in the final CMD command use to open the `app.py` file. Also ensure to modify the app.py file's zoo configuration appropriately depending on what classes you required and the dataset to use.

```
  --detections
  --segmentations
  --points
```

3. Run `docker-compose up` to build the image and start the container.

4. Open a browser and navigate to `localhost:5151` to access the FiftyOne App.

## Notes

- Any time you update the app.py file, make sure to run `docker-compose up --build` to rebuild the image and start the container.
