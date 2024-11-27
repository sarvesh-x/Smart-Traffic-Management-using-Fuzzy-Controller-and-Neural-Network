import cv2
import numpy as np
import os
import FuzzyController, traffic
from PIL import Image
import pandas as pd
from ultralytics import YOLO

img = None
start_x, start_y = -1, -1
end_x, end_y = -1, -1
is_drawing = False

def count_vehicles_in_image(cropped_img):
    img_cv = cv2.cvtColor(np.array(cropped_img), cv2.COLOR_RGB2BGR)
    model = YOLO('yolo11n.pt')  
    results = model(img_cv)
    vehicle_count = sum([1 for result in results[0].boxes if result.cls == 2 or result.cls == 4 or result.cls == 6 or result.cls == 8])
    return vehicle_count

def mouse_callback(event, x, y, flags, param):
    global img, start_x, start_y, end_x, end_y, is_drawing

    if event == cv2.EVENT_LBUTTONDOWN:  
        start_x, start_y = x, y
        is_drawing = True

    elif event == cv2.EVENT_MOUSEMOVE:  
        if is_drawing:  
            end_x, end_y = x, y
            img_copy = img.copy()
            cv2.rectangle(img_copy, (start_x, start_y), (end_x, end_y), (0, 255, 0), 2)
            cv2.imshow("Image", img_copy)

    elif event == cv2.EVENT_LBUTTONUP:  
        end_x, end_y = x, y
        is_drawing = False
        cv2.rectangle(img, (start_x, start_y), (end_x, end_y), (0, 255, 0), 2)
        cv2.imshow("Image", img)

def crop_roi_from_image():
    global start_x, start_y, end_x, end_y
    if start_x == -1 or start_y == -1 or end_x == -1 or end_y == -1:
        print("Error: No ROI selected!")
        return None
    cropped_img = img[start_y:end_y, start_x:end_x]
    cropped_img_pil = Image.fromarray(cropped_img)  
    return cropped_img_pil

def read_images_from_directory(directory):
    images = []
    for filename in os.listdir(directory):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
            file_path = os.path.join(directory, filename)
            img = cv2.imread(file_path)
            images.append((filename, img))
    return images

def read_cropped_images(directory):
    cropped_images = []
    for filename in os.listdir(directory):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
            file_path = os.path.join(directory, filename)
            img = Image.open(file_path)
            cropped_images.append((filename, img))
    return cropped_images

def display_and_save_image(cropped_img, output_dir, image_name):
    cropped_img.show()
    output_path = os.path.join(output_dir, f"ROI_{image_name}")
    cropped_img.save(output_path)
    print(f"Cropped image saved to: {output_path}")

def main():
    global img
    results = []
    input_directory = "intersection"
    output_directory = "FramesWithROI"
    ROI_Images = read_cropped_images(output_directory)
    
    
    if not os.path.exists(input_directory):
        print("Directory does not exist.")
        return
    
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    images = read_images_from_directory(input_directory)
    
    for image_name, img in images:
        global start_x, start_y, end_x, end_y, is_drawing
        print(f"Processing image: {image_name}")
        cv2.imshow("Image", img)
        cv2.setMouseCallback("Image", mouse_callback)

        while True:
            key = cv2.waitKey(1) & 0xFF
            if key == 27:  # Press 'Esc' to exit
                print("Exiting...")
                cv2.destroyAllWindows()
                return
            elif key == 13:  
                cropped_img = crop_roi_from_image()
                if cropped_img:
                    display_and_save_image(cropped_img, output_directory, image_name)
                    vehicle_count = count_vehicles_in_image(cropped_img)
                    results.append({"Image Name": image_name, "Vehicle Count": vehicle_count})

                break
        
    df = pd.DataFrame(results)
    df.to_csv("vehicle_count.csv", index=False)
    FuzzyController.FuzzyController()
    traffic.ANN()

if __name__ == "__main__":
    main()
