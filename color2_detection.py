import cv2
import pandas as pd
import os


img_path = r"C:\Users\Admin\Downloads\Color-Detection-OpenCV-main\Color-Detection-OpenCV-main\colorpic.jpg"
img = cv2.imread(img_path)


if img is None:
    print("Error: Image file not found at:", img_path)
    exit()


csv_path = r"C:\Users\Admin\Downloads\Color-Detection-OpenCV-main\Color-Detection-OpenCV-main\colors.csv"


if not os.path.exists(csv_path):
    print("Error: colors.csv file not found at:", csv_path)
    exit()


index = ["color", "color_name", "hex", "R", "G", "B"]
csv = pd.read_csv(csv_path, names=index, header=None)


clicked = False
r = g = b = x_pos = y_pos = 0


def get_color_name(R, G, B):
    minimum = 10000
    cname = "Unknown"
    for i in range(len(csv)):
        d = abs(R - int(csv.loc[i, "R"])) + abs(G - int(csv.loc[i, "G"])) + abs(B - int(csv.loc[i, "B"]))
        if d < minimum:
            minimum = d
            cname = csv.loc[i, "color_name"]
    return cname


def draw_function(event, x, y, flags, param):
    global b, g, r, x_pos, y_pos, clicked
    if event == cv2.EVENT_LBUTTONDBLCLK:
        clicked = True
        x_pos = x
        y_pos = y
        b, g, r = img[y, x]
        b, g, r = int(b), int(g), int(r)


cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_function)

while True:
    cv2.imshow("image", img)
    
    if clicked:
       
        cv2.rectangle(img, (20, 20), (750, 60), (b, g, r), -1)

        
        text = get_color_name(r, g, b) + ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)

       
        text_color = (255, 255, 255) if (r + g + b) < 600 else (0, 0, 0)
        cv2.putText(img, text, (50, 50), 2, 0.8, text_color, 2, cv2.LINE_AA)

        clicked = False

    
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
