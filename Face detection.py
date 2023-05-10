import cv2
import tkinter as tk
from tkinter import filedialog

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def selectAndDetection():
    file_path = filedialog.askopenfilename()

    if file_path != '':
        if file_path.lower().endswith('.mp4') or file_path.lower().endswith('.avi') or file_path.lower().endswith('.mov'):
            cap = cv2.VideoCapture(file_path)
            while True:
                ret, frame = cap.read()
                if ret:
                    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
                    for (x, y, w, h) in faces:
                        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
                    cv2.imshow('frame', frame)
                    if cv2.waitKey(25) & 0xFF == ord('q'):
                        break
                else:
                    break
            cap.release()
            cv2.destroyAllWindows()
        elif file_path.lower().endswith('.jpg') or file_path.lower().endswith('.jpeg') or file_path.lower().endswith('.png'):
            img = cv2.imread(file_path)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
            cv2.imshow('img', img)
            cv2.waitKey()
        else:
            print('Invalid file format')
    else:
        print('No file selected')

root = tk.Tk()
btn = tk.Button(root,text="Select image or video",command=selectAndDetection)
btn.pack()
root.mainloop()


