import cv2
import pyautogui
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.7)

while True:
    success, img = cap.read()
    if not success:
        print("Error: Unable to access the camera.")
        break

    hands, img = detector.findHands(img)

    if hands:
        center = hands[0]['center']
        cv2.circle(img, center, 15, (0, 255, 0), cv2.FILLED)

        screen_width, screen_height = pyautogui.size()
        x = int(center[0] * screen_width / img.shape[1])
        y = int(center[1] * screen_height / img.shape[0])
        pyautogui.moveTo(x, y)

        fingers = detector.fingersUp(hands[0])
        print(fingers)

        if fingers == [1, 0, 0, 0, 0]:
            pyautogui.press("volumeup")
            cv2.putText(img, "Volume Up", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        elif fingers == [0, 0, 1, 0, 0]:
            pyautogui.press("volumedown")
            cv2.putText(img, "Volume Down", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        elif fingers == [0, 1, 0, 0, 0]:
            pyautogui.click()
            cv2.putText(img, "Click", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    cv2.imshow("Image", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
