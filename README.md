# Plot bboxes on images
> Simply display bounding boxes on images


This tool helps you display bounding boxes on images.
This can be done in CLI or using a config file.

## Installation

OS X, Linux & Windows:
No specific requirements except python3 (3.5 and later).

```sh
pip install git+https://github.com/YaYaB/plot-bboxes
```


## Usage example

```sh
usage: Display bounding boxes on images (one image and one bbox in CLI, several using a config file)
       [-h] [--input_file INPUT_FILE] [--bbox BBOX [BBOX ...]]
       [--output_file OUTPUT_FILE] [--config_file CONFIG_FILE]

optional arguments:
  -h, --help            show this help message and exit
  --input_file INPUT_FILE
                        Path to image input file
  --bbox BBOX [BBOX ...]
                        Bounding box to display with the following order (xmin
                        ymin xmax ymax)
  --output_file OUTPUT_FILE
                        Path to output image file with bounding boxes
  --config_file CONFIG_FILE
                        Config file containing path to images and bounding
                        boxes to display

```

Please refer to [here](https://github.com/YaYaB/plot-bboxes/tree/master/examples) for examples.


## Meta

YaYaB

Distributed under the Apache license v2.0. See ``LICENSE`` for more information.

[https://github.com/YaYaB/plot-bboxes](https://github.com/YaYaB/plot-bboxes)
