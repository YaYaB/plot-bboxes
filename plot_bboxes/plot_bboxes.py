import os
import argparse
import sys
import cv2
import json


def get_args():
    parser = argparse.ArgumentParser(
        "Display bounding boxes on images (one image and one bbox in CLI, several using a config file)"
    )
    parser.add_argument("--input_file", type=str, help="Path to image input file")
    parser.add_argument("--bbox", type=int, help="Bounding box to display with the following order (xmin ymin xmax ymax)", nargs='+')
    parser.add_argument("--output_file", type=str, help="Path to output image file with bounding boxes", default=None)
    parser.add_argument("--config_file", type=str, help="Config file containing path to images and bounding boxes to display", default=None)

    args = parser.parse_args()
    return args


def is_bbox_correct(bbox, width, height):
    """
        :param bbox: bbox composed of 4 integer values [xmin, ymin, xmax, ymax]
        :param height: height of the image
        :param width: width of the image
        :return: True if bbox inside image, False otherwise
    """
    # Check bbox inside image
    if bbox[0] < 0 or bbox[0] >= width:
        return False
    if bbox[2] < 0 or bbox[2] >= width:
        return False
    if bbox[1] < 0 or bbox[1] >= height:
        return False
    if bbox[3] < 0 or bbox[3] >= height:
        return False

    # Check bbox coherence
    if bbox[3] < bbox[1]:
        return False
    if bbox[2] < bbox[0]:
        return False

    # If everything is correct return True
    return True


def display_bbox(img, bbox):
    """
        :param img: image as a numpy array
        :param bboxes: bbox composed of 4 integer values
        :return: image with bbox added on it
    """
    height, width = img.shape[:2]
    # Verify that bounding box is insde the shape of the image
    assert is_bbox_correct(bbox, width, height), "Bbox out of bounds or not correctly formated"

    # Print rectangle
    cv2.rectangle(img, (bbox[0], bbox[1]), (bbox[2], bbox[3]), (0, 0, 0), 2)

    return img


def prepare_output(input_file, output_file):
    if output_file is None:
        output_file = ".".join(input_file.split('.')[:-1]) + "_bbox.jpeg"

    # Create repository if it does not exist
    output_folder = os.path.dirname(output_file)
    if not os.path.isdir(output_folder):
        os.makedirs(output_folder)

    return output_file


def display_input_cli(opt):
    """
        :param opt: dict containing parameters of the program
    """
    input_file = opt.input_file
    bbox = opt.bbox

    output_file = opt.output_file

    # Checks
    assert os.path.exists(input_file), "The file '{}' indicated does not exist".format(input_file)
    assert len(bbox) == 4, "Indicate exaclty four integers for the bbox"

    # Prepare output
    output_file = prepare_output(input_file, output_file)

    # Read image
    img = cv2.imread(input_file)
    assert img is not None, "File {} does not seem to be an image".format(input_file)

    # Display bboxes
    img_bbox = display_bbox(img, bbox)
    # Dump images to file
    cv2.imwrite(output_file, img_bbox)


def display_input_config(opt):
    """
        :param opt: dict containing parameters of the program
    """

    config_file = opt.config_file
    assert os.path.exists(config_file), "The file '{}' indicated does not exist".format(config_file)

    # Read config file
    with open(config_file, 'r') as f:
        elements = json.load(f)

    # Loop images and bboxes
    for img_bbox in elements:
        # Read image
        input_file = img_bbox['path']
        img = cv2.imread(input_file)
        assert img is not None, "File {} does not seem to be an image".format(input_file)

        # Prepare output
        output_file = prepare_output(input_file, None)

        # Display bboxes
        for bbox in img_bbox["bbox"]:
            img_bbox = display_bbox(img, bbox)

        # Dump images to file
        cv2.imwrite(output_file, img_bbox)


def main():
    """
        Main function of the program
    """

    # Get arguments passed in CLI
    opt = get_args()

    # Read information from config file
    if opt.config_file is not None:
        display_input_config(opt)
    # Read information from CLI directly (limited to one image and one bbox)
    else:
        display_input_cli(opt)

    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        print("[ERR] Uncaught error waiting for scripts to finish")
        print(e)
        raise
