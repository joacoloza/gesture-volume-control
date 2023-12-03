import cv2
import mediapipe as mp
import pyautogui


x1=x2=y1=y2= 0
# open the camera
camera = cv2.VideoCapture(0)

# detect hands
my_hands = mp.solutions.hands.Hands()
draw = mp.solutions.drawing_utils

while True:
    ret, image = camera.read()  # get the image from the camera
    image = cv2.flip(image,1)
    frame_heigth, frame_width, _ = image.shape
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # change format from bgr 2 rgb
    output = my_hands.process(rgb)  # process the image in its format
    hands = output.multi_hand_landmarks    # capture all hands

    if hands:   # if get any hand
        for hand in hands:
            draw.draw_landmarks(image, hand)  # draw landmarks on the hands
            landmarks = hand.landmark

            for id,landmark in enumerate(landmarks):   #collect all the landmarks from the hand
                # get the coordinates for the landmark
                x = int(landmark.x * frame_width)
                y = int(landmark.y * frame_heigth)

                # draw a circle over the important fingers
                if id == 8:     # 8 forefinger
                    cv2.circle(img=image,center=(x, y), radius=8,color=(255,255,0),thickness=3)
                    x1=x
                    y1=y
                if id == 4:  # 4 thumb
                    cv2.circle(img=image, center=(x, y), radius=8,color=(255,255,0),thickness=3)
                    x2=x
                    y2=y

        distance = ((x2-x1)**2) + ((y2-y2)**2) ** (0.5)//4   # this calculates the distance between fingers
        cv2.line(image,(x1,y1),(x2,y2),color=(0,255,0), thickness=3)
        if distance > 50:
            pyautogui.press('volumeup')
        else:
            pyautogui.press('volumedown')


    cv2.imshow('controlador', image)  # show the image
    cv2.waitKey(5)

