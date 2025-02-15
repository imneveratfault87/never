from gtts import gTTS
import time
import os
from google import genai
import speech_recognition as sr


os.environ['PYTHONWARNINGS']='ignore'
os.environ['GPRC_VERBOSITY']='ERROR'
os.environ['GLOG_minloglevel']='2'
os.environ['ALSA_LOG_LEVEL']='0'



API='AIzaSyCdx7oSFOXW2ZFfKbHLZwhfSUc2OrPeBOM'
client = genai.Client(api_key=API)


r = sr.Recognizer() 


# Loop infinitely for user to
# speak

while(1):    
    
    # Exception handling to handle
    # exceptions at the runtime
    try:
        
        # use the microphone as source for input.
        with sr.Microphone() as source:
            
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level 
            r.adjust_for_ambient_noise(source, duration=0.2)
            
            #listens for the user's input 
            audio2 = r.listen(source)
            
            # Using google to recognize audio
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
            response = client.models.generate_content(
                    model="gemini-2.0-flash", contents=MyText+ ';be very very short'
            )

            text=response.text
            tts = gTTS(text=text, lang="en")

            # Save as an MP3 file
            tts.save("../temp_audio/output.mp3")



            os.system("mpg321 ../temp_audio/output.mp3")

            #time.sleep(2)

            os.remove("../temp_audio/output.mp3")
            
            time.sleep(3)
            
    except sr.RequestError as e:
        print(f"Could not request results")
        
    except sr.UnknownValueError:
        print(f"unknown error occurred")











