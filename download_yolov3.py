# Download YOLOv3 model files if not present
import os
import urllib.request

def download_file(url, filename):
    if not os.path.exists(filename):
        print(f"Downloading {filename}...")
        urllib.request.urlretrieve(url, filename)
        print(f"Downloaded {filename}")
    else:
        print(f"{filename} already exists.")

# URLs for YOLOv3
cfg_url = "https://github.com/pjreddie/darknet/raw/master/cfg/yolov3.cfg"
weights_url = "https://pjreddie.com/media/files/yolov3.weights"
names_url = "https://github.com/pjreddie/darknet/raw/master/data/coco.names"

# Filenames
cfg_file = "yolov3.cfg"
weights_file = "yolov3.weights"
names_file = "coco.names"

download_file(cfg_url, cfg_file)
download_file(weights_url, weights_file)
download_file(names_url, names_file)
print("All YOLOv3 files are ready.")
