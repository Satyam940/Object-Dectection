import google.generativeai as genai
import PIL.Image
import cv2 
import os
import pyttsx3
def object():

    def speak(talk):
        engine= pyttsx3.init('sapi5')
        engine.setProperty('rate', 190)
        engine.setProperty('volume',1.0)
        voices= engine.getProperty('voices')
        engine.setProperty('voice',voices[1].id)
        engine.say(talk)
        engine.runAndWait()


    image_counter = 0
    cap = cv2.VideoCapture(0)
    while True:
        _, frame = cap.read()
        cv2.imshow("frame", frame)
        cv2.moveWindow('frame', -1000,-1000)
        cv2.waitKey(1)
    
        if image_counter == 1:
            break
        else:
            cv2.imwrite(f"image{image_counter}.jpg ", frame)
            if image_counter ==0:
                pass
            else:
                os.remove(f"image{image_counter}.jpg")
            image_counter += 1
    cap.release()

    
    GOOGLE_API_KEY = "API key"
    genai.configure(api_key=GOOGLE_API_KEY)
    image = PIL.Image.open('image0.jpg')
    model = genai.GenerativeModel("gemini-pro-vision")
    result = model.generate_content(image)

    response = result
    print(response.text[0:50])
    speak(response.text[0:50])

    response = model.generate_content(
        ["what is in my hand. i want only 1 or 2 words.", image],
        stream=True
    )
    response.resolve()
    os.remove("image0.jpg")

object()






