CONFIG_FILE="./config_file.json"

echo "Display bounding box for image ${CONFIG_FILE}."
plot-bboxes --config_file ${CONFIG_FILE}
