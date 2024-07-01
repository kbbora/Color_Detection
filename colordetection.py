import cv2
import numpy as np
import tkinter as tk
from PIL import Image, ImageTk

colors = {
    'Yesil': 0,
    'Mavi': 0,
    'Kirmizi': 0,
    'Sari': 0,
    'Turuncu': 0,
    'Mor': 0,
    'Pembe': 0

}

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

detection_interval = 10
is_running = False

prev_objects = {}
object_in_right = {
    'Yesil': False,
    'Mavi': False,
    'Kirmizi': False,
    'Sari': False,
    'Turuncu': False,
    'Mor': False,
    'Pembe': False
}

area_thresholds = {
    'Yesil': 1000,
    'Mavi': 1000,
    'Kirmizi': 1000,
    'Sari': 1000,
    'Turuncu': 1000,
    'Mor': 1000,
    'Pembe': 1000
}

kernel = np.ones((2, 2), np.uint8)
gaussian_kernel = (5, 5)

def update_interface_counts():
    label_green_count.config(text=f"Yesil: {colors['Yesil']} adet")
    label_blue_count.config(text=f"Mavi: {colors['Mavi']} adet")
    label_red_count.config(text=f"Kirmizi: {colors['Kirmizi']} adet")
    label_yellow_count.config(text=f"Sari: {colors['Sari']} adet")
    label_Orange_count.config(text=f"Turuncu: {colors['Turuncu']} adet")

    label_Purple_count.config(text=f"Mor: {colors['Mor']} adet")
    label_Pink_count.config(text=f"Pembe: {colors['Pembe']} adet")


    total_objects = sum(colors.values())
    total_label.config(text=f"Toplam Nesne Sayisi: {total_objects}")

def reset_colors():
    for color in colors:
        colors[color] = 0
    update_interface_counts()


def update_frames():
    global is_running
    if is_running:
        ret, frame = cap.read()
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        lower_green = np.array([30, 100, 50])
        upper_green = np.array([80, 255, 255])
        green_mask = cv2.inRange(hsv_frame, lower_green, upper_green)
        green_mask = cv2.erode(green_mask, kernel, iterations=2)
        green_mask = cv2.dilate(green_mask, kernel, iterations=2)
        green_mask = cv2.GaussianBlur(green_mask, gaussian_kernel, 0)
        green = cv2.bitwise_and(frame, frame, mask=green_mask)

        lower_blue = np.array([84, 98, 0])
        upper_blue = np.array([120, 255, 255])
        blue_mask = cv2.inRange(hsv_frame, lower_blue, upper_blue)
        blue_mask = cv2.erode(blue_mask, kernel, iterations=2)
        blue_mask = cv2.dilate(blue_mask, kernel, iterations=2)
        blue_mask = cv2.GaussianBlur(blue_mask, gaussian_kernel, 0)
        blue = cv2.bitwise_and(frame, frame, mask=blue_mask)


        lower_red1 = np.array([0, 100, 100])
        upper_red1 = np.array([5, 255, 255])
        red_mask1 = cv2.inRange(hsv_frame, lower_red1, upper_red1)

        lower_red2 = np.array([175, 100, 100])
        upper_red2 = np.array([180, 255, 255])
        red_mask2 = cv2.inRange(hsv_frame, lower_red2, upper_red2)

        red_mask = cv2.bitwise_or(red_mask1, red_mask2)
        red_mask = cv2.erode(red_mask, kernel, iterations=2)
        red_mask = cv2.dilate(red_mask, kernel, iterations=2)
        red_mask = cv2.GaussianBlur(red_mask, gaussian_kernel, 0)
        red = cv2.bitwise_and(frame, frame, mask=red_mask)


        lower_yellow = np.array([22, 100, 100])
        upper_yellow = np.array([38, 255, 255])
        yellow_mask = cv2.inRange(hsv_frame, lower_yellow, upper_yellow)
        yellow_mask = cv2.erode(yellow_mask, kernel, iterations=2)
        yellow_mask = cv2.dilate(yellow_mask, kernel, iterations=2)
        yellow_mask = cv2.GaussianBlur(yellow_mask, gaussian_kernel, 0)
        yellow = cv2.bitwise_and(frame, frame, mask=yellow_mask)


        lower_orange = np.array([8, 100, 100])
        upper_orange = np.array([15, 255, 255])
        orange_mask = cv2.inRange(hsv_frame, lower_orange, upper_orange)
        orange_mask = cv2.erode(orange_mask, kernel, iterations=2)
        orange_mask = cv2.dilate(orange_mask, kernel, iterations=2)
        orange_mask = cv2.GaussianBlur(orange_mask, gaussian_kernel, 0)
        orange = cv2.bitwise_and(frame, frame, mask=orange_mask)


        lower_purple = np.array([125, 100, 100])
        upper_purple = np.array([150, 255, 255])
        purple_mask = cv2.inRange(hsv_frame, lower_purple, upper_purple)
        purple_mask = cv2.erode(purple_mask, kernel, iterations=2)
        purple_mask = cv2.dilate(purple_mask, kernel, iterations=2)
        purple_mask = cv2.GaussianBlur(purple_mask, gaussian_kernel, 0)
        purple = cv2.bitwise_and(frame, frame, mask=purple_mask)



        lower_pink = np.array([140, 100, 100])
        upper_pink = np.array([175, 255, 255])
        pink_mask = cv2.inRange(hsv_frame, lower_pink, upper_pink)
        pink_mask = cv2.erode(pink_mask, kernel, iterations=2)
        pink_mask = cv2.dilate(pink_mask, kernel, iterations=2)
        pink_mask = cv2.GaussianBlur(pink_mask, gaussian_kernel, 0)
        pink = cv2.bitwise_and(frame, frame, mask=pink_mask)


        green_threshold = area_thresholds['Yesil']
        contours, _ = cv2.findContours(green_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if len(contours) > 0:
            max_contour = max(contours, key=cv2.contourArea)
            if cv2.contourArea(max_contour) > green_threshold:
                x, y, w, h = cv2.boundingRect(max_contour)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                center_x = x + w // 2
                center_y = y + h // 2
                cv2.circle(frame, (center_x, center_y), 3, (0, 0, 0), -1)

                if center_x > 300 and not object_in_right['Yesil']:
                    object_in_right['Yesil'] = True
                    colors['Yesil'] += 1
                    cv2.putText(frame, str(colors['Yesil']), (center_x, center_y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0),
                                2)
                elif center_x <= 300:
                    object_in_right['Yesil'] = False


        blue_threshold = area_thresholds['Mavi']
        contours, _ = cv2.findContours(blue_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if len(contours) > 0:
            max_contour = max(contours, key=cv2.contourArea)
            if cv2.contourArea(max_contour) > blue_threshold:
                x, y, w, h = cv2.boundingRect(max_contour)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                center_x = x + w // 2
                center_y = y + h // 2
                cv2.circle(frame, (center_x, center_y), 3, (0, 0, 0), -1)

                if center_x > 300 and not object_in_right['Mavi']:
                    object_in_right['Mavi'] = True
                    colors['Mavi'] += 1
                    cv2.putText(frame, str(colors['Mavi']), (center_x, center_y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
                elif center_x <= 300:
                    object_in_right['Mavi'] = False


        red_threshold = area_thresholds['Kirmizi']
        contours, _ = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if len(contours) > 0:
            max_contour = max(contours, key=cv2.contourArea)
            if cv2.contourArea(max_contour) > red_threshold:
                x, y, w, h = cv2.boundingRect(max_contour)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
                center_x = x + w // 2
                center_y = y + h // 2
                cv2.circle(frame, (center_x, center_y), 3, (0, 0, 0), -1)

                if center_x > 300 and not object_in_right['Kirmizi']:
                    object_in_right['Kirmizi'] = True
                    colors['Kirmizi'] += 1
                    cv2.putText(frame, str(colors['Kirmizi']), (center_x, center_y), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                (0, 0, 0), 2)
                elif center_x <= 300:
                    object_in_right['Kirmizi'] = False

        yellow_threshold = area_thresholds['Sari']
        contours, _ = cv2.findContours(yellow_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if len(contours) > 0:
            max_contour = max(contours, key=cv2.contourArea)
            if cv2.contourArea(max_contour) > yellow_threshold:
                x, y, w, h = cv2.boundingRect(max_contour)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
                center_x = x + w // 2
                center_y = y + h // 2
                cv2.circle(frame, (center_x, center_y), 3, (0, 0, 0), -1)

                if center_x > 300 and not object_in_right['Sari']:
                    object_in_right['Sari'] = True
                    colors['Sari'] += 1
                    cv2.putText(frame, str(colors['Sari']), (center_x, center_y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
                elif center_x <= 300:
                    object_in_right['Sari'] = False
        orange_threshold = area_thresholds['Turuncu']
        contours, _ = cv2.findContours(orange_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if len(contours) > 0:
            max_contour = max(contours, key=cv2.contourArea)
            if cv2.contourArea(max_contour) > orange_threshold:
                x, y, w, h = cv2.boundingRect(max_contour)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 128, 255), 2)
                center_x = x + w // 2
                center_y = y + h // 2
                cv2.circle(frame, (center_x, center_y), 3, (0, 0, 0), -1)

                if center_x > 300 and not object_in_right['Turuncu']:
                    object_in_right['Turuncu'] = True
                    colors['Turuncu'] += 1
                    cv2.putText(frame, str(colors['Turuncu']), (center_x, center_y), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                (0, 0, 0), 2)
                elif center_x <= 300:
                    object_in_right['Turuncu'] = False

        purple_threshold = area_thresholds['Mor']
        contours, _ = cv2.findContours(purple_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if len(contours) > 0:
            max_contour = max(contours, key=cv2.contourArea)
            if cv2.contourArea(max_contour) > purple_threshold:
                x, y, w, h = cv2.boundingRect(max_contour)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (128, 0, 128), 2)
                center_x = x + w // 2
                center_y = y + h // 2
                cv2.circle(frame, (center_x, center_y), 3, (0, 0, 0), -1)

                if center_x > 300 and not object_in_right['Mor']:
                    object_in_right['Mor'] = True
                    colors['Mor'] += 1
                    cv2.putText(frame, str(colors['Mor']), (center_x, center_y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0),
                                2)
                elif center_x <= 300:
                    object_in_right['Mor'] = False


        pink_threshold = area_thresholds['Pembe']
        contours, _ = cv2.findContours(pink_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if len(contours) > 0:
            max_contour = max(contours, key=cv2.contourArea)
            if cv2.contourArea(max_contour) > pink_threshold:
                x, y, w, h = cv2.boundingRect(max_contour)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 192, 203), 2)
                center_x = x + w // 2
                center_y = y + h // 2
                cv2.circle(frame, (center_x, center_y), 3, (0, 0, 0), -1)

                if center_x > 300 and not object_in_right['Pembe']:
                    object_in_right['Pembe'] = True
                    colors['Pembe'] += 1
                    cv2.putText(frame, str(colors['Pembe']), (center_x, center_y), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                (0, 0, 0), 2)
                elif center_x <= 300:
                    object_in_right['Pembe'] = False

        line_start = (300, 0)
        line_end = (300, frame.shape[0])
        cv2.line(frame, line_start, line_end, (0, 255, 0), 2)

        video_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        video_frame = Image.fromarray(video_frame)
        video_frame = ImageTk.PhotoImage(image=video_frame)

        video_label.configure(image=video_frame)
        video_label.image = video_frame

        update_interface_counts()

    root.after(detection_interval, update_frames)

def toggle_fullscreen(event):
    root.attributes("-fullscreen", not root.attributes("-fullscreen"))

def toggle_run():
    global is_running
    is_running = not is_running
    if is_running:
        start_button.config(text="Durdur", bg="red")
    else:
        start_button.config(text="Baslat", bg="green")

root = tk.Tk()
root.title("Renk Tespiti Uygulamasi")

# Bind the F11 key to toggle fullscreen
root.bind("<F11>", toggle_fullscreen)
root.attributes("-fullscreen", False)

frame = tk.Frame(root, bg='White')
frame.pack(padx=100, pady=100)

video_label = tk.Label(frame)
video_label.pack(side=tk.LEFT, padx=5)
"""
label_green = tk.Label(frame, text="Yesil", fg='#00FF00')
label_blue = tk.Label(frame, text="Mavi", fg='#0000FF')
label_red = tk.Label(frame, text="Kirmizi", fg='#FF0000')
label_yellow = tk.Label(frame, text="Sari", fg='#cccc00')
label_Pink = tk.Label(frame, text="Pembe", fg='#FFC0CB')
label_Purple = tk.Label(frame, text="Mor", fg='#800080')
label_Orange = tk.Label(frame, text="Turuncu", fg='#FFA500')
label_Gray = tk.Label(frame, text="Gri", fg='#808080')

label_green.pack(side=tk.LEFT, padx=10)
label_blue.pack(side=tk.LEFT, padx=10)
label_red.pack(side=tk.LEFT, padx=10)
label_yellow.pack(side=tk.LEFT, padx=10)
label_Pink.pack(side=tk.LEFT, padx=10)
label_Orange.pack(side=tk.LEFT, padx=10)
label_Purple.pack(side=tk.LEFT, padx=10)
label_Gray.pack(side=tk.LEFT, padx=10)
"""


panel = tk.Frame(root, bg='white')
panel.pack(padx=10, pady=5)

label_green_count = tk.Label(panel, text="Yesil: 0 adet", fg='#00FF00')
label_blue_count = tk.Label(panel, text="Mavi: 0 adet", fg='#0000FF')
label_red_count = tk.Label(panel, text="Kirmizi: 0 adet", fg='#FF0000')
label_yellow_count = tk.Label(panel, text="Sari: 0 adet", fg='#cccc00')
label_Pink_count = tk.Label(panel, text="Pembe: 0 adet", fg='#FFC0CB')
label_Purple_count = tk.Label(panel, text="Mor: 0 adet", fg='#800080')
label_Orange_count = tk.Label(panel, text="Turuncu: 0 adet", fg='#FFA500')


label_green_count.pack(side=tk.LEFT, padx=20)
label_blue_count.pack(side=tk.LEFT, padx=20)
label_red_count.pack(side=tk.LEFT, padx=20)
label_yellow_count.pack(side=tk.LEFT, padx=20)
label_Pink_count.pack(side=tk.LEFT, padx=20)
label_Purple_count.pack(side=tk.LEFT, padx=20)
label_Orange_count.pack(side=tk.LEFT, padx=20)


total_label = tk.Label(root, text="Toplam Nesne Sayisi: 0", font=("Helvetica", 16))
total_label.pack(pady=50)

start_button = tk.Button(root, text="Baslat", command=toggle_run, bg="green")
start_button.pack(side=tk.LEFT, padx=50)
exit_button = tk.Button(root, text="Cikis", command=root.destroy, bg="gray")
exit_button.pack(side=tk.RIGHT, padx=50)
reset_button = tk.Button(root, text="Sıfırla", command=reset_colors)
reset_button.pack(side=tk.LEFT, padx=50)
reset_button.config(text="Sıfırla", bg="yellow")

update_frames()

root.mainloop()
print("Tespit Edilen Renkler ve Sayilari:")
print(f"/*/*/*/*/*/*/*/*/*/*/*/*/*/")
for renk, sayi in colors.items():
    print(f"{renk}: {sayi} adet")

toplam_sayi = sum(colors.values())
print(f"/*/*/*/*/*/*/*/*/*/*/*/*/*/")
print("Toplam Nesne Sayisi:", toplam_sayi)