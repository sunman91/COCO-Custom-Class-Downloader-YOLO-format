import os
import requests
from pycocotools.coco import COCO
import sys

def make_directory(dir_name):
    try:
        os.mkdir(dir_name)
        print(f"\nMade {dir_name} Directory.\n")
    except:
        pass

def get_images_from_classes(class_names):
    make_directory('downloaded_images')

    coco = COCO('instances_train2017.json')
    images = []

    for class_name in class_names:
        cat_ids = coco.getCatIds(catNms=[class_name])
        img_ids = coco.getImgIds(catIds=cat_ids)
        images.extend(coco.loadImgs(img_ids))

    print(f"Total Images: {len(images)} for classes: {', '.join(class_names)}")

    for im in images:
        image_file_name = im['file_name']
        label_file_name = im['file_name'].split('.')[0] + '.txt'
        
        img_data = requests.get(im['coco_url']).content
        s = ""
        for class_name in class_names:
            cat_ids = coco.getCatIds(catNms=[class_name])
            ann_ids = coco.getAnnIds(imgIds=im['id'], catIds=cat_ids, iscrowd=None)
            anns = coco.loadAnns(ann_ids)
            for i in range(len(anns)):
                # Yolo Format: class center-x center-y width height
                # All values are relative to the image.
                topLeftX = anns[i]['bbox'][0] / im['width']
                topLeftY = anns[i]['bbox'][1] / im['height']
                width = anns[i]['bbox'][2] / im['width']
                height = anns[i]['bbox'][3] / im['height']

                class_index = class_names.index(class_name)
                s += f"{class_index} {((topLeftX + (topLeftX + width)) / 2)} {(topLeftY + (topLeftY + height)) / 2} {width} {height}\n"

        with open(f'downloaded_images/{image_file_name}', 'wb') as image_handler:
            image_handler.write(img_data)
        with open(f'downloaded_images/{label_file_name}', 'w') as label_handler:
            label_handler.write(s)
        print(f"Generated label for {image_file_name}")

if __name__ == '__main__':
    classes = sys.argv[1:]  # Get classes from command-line arguments

    if not classes:
        print("Please provide one or more classes as command-line arguments.")
        sys.exit(1)

    get_images_from_classes(classes)
    print("Done.")
