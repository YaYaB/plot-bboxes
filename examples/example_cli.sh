IMG_TEST="../images/image_1.jpg"

echo "Display bounding box for image ${IMG_TEST}."
plot-bboxes --input_file ${IMG_TEST} --bbox 100 100 200 500
