import argparse
import fiftyone as fo
import fiftyone.zoo as foz

# Create the parser
parser = argparse.ArgumentParser(description='Load a dataset with specific label types')

# Add optional boolean arguments
parser.add_argument('--detections', action='store_true', help='Include detections labels')
parser.add_argument('--segmentations', action='store_true', help='Include segmentations labels')
parser.add_argument('--points', action='store_true', help='Include points labels')

# Add optional limit argument
parser.add_argument('--limit', type=int, default=None, help='Limit the number of samples')

# Parse the arguments
args = parser.parse_args()

# By default, include 'detections'
label_types = []

# If the corresponding flags are provided, add the label types
if args.segmentations:
  label_types.append('segmentations')
if args.points:
  label_types.append('points')
  
if not label_types:
  label_types.append('detections')

# Load the dataset
dataset = fo.zoo.load_zoo_dataset(
  "open-images-v7",
  split="validation",
  label_types=label_types,
  # classes=["Cat", "Dog"],
  classes=["Vehicle registration plate", "Vehicle", "Car", "Motorcycle", "Truck", "Bus", "Scooter"],
  max_samples=100,
)

session = fo.launch_app(dataset)
session.wait()
