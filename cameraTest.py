import cv2

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("error camera cannot open")
else:
    print("Camera opened successfully.")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture frame.")
            break
        cv2.imshow("Camera", frame)
        if cv2.waitKey(1) == ord("q"):
            break
    cap.release()
    cv2.destroyAllWindows()
