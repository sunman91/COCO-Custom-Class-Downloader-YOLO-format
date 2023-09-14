
# COCO-Custom-Class-Downloader-YOLO-format

- Download specific classes from the **Coco Dataset** for custom object detection needs.
- Pickup where you left off if your connection is interrupted.
- Referenced from "https://github.com/KaranJagtiani/YOLO-Coco-Dataset-Custom-Classes-Extractor.git". But it gives annotations of only one instance of a class and downloads each class in a separate folder. This implementation annotates all instances of all given classes in a singel image.

## Packages Required
**1. pycocotools**  
`pip install pycocotools`

## Usage
#### 1. Clone this repository:  
`git clone https://github.com/sunman91/COCO-Custom-Class-Downloader-YOLO-format.git`
#### 2. Download the **[2017 Train/Val annotations \[241MB\]](https://huggingface.co/datasets/merve/coco/blob/main/annotations/instances_train2017.json)** zip file and put the **instances_train2017.json** file in the cloned repository's main directory.
#### 3. See the various classes available:  
`python coco-extractor.py --help` 
#### 4. Download a specific class:  
`python coco-extractor.py "person"`
#### 5. Download multiple classes:  
`python coco-extractor.py "person" "sports ball" "zebra"`

Test your downloaded images and the bounding boxes with **[draw-YOLO-box](https://github.com/waittim/draw-YOLO-box)**.

### Happy Detecting!
