import openai
import pyttsx3
import speech_recognition as sr

openai.api_key = "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"
engine = pyttsx3.init()


def transcribe_speech_to_text(filename):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)

    try:
        return recognizer.recognize_google(audio)
    except:
     print('Are you dumb')

def generate_response(prompt):
   response = openai.Completion.create (
      engine = "text-davinci-003",
      prompt =prompt,
      max_tokens = 4000,
      n =1,
      stop = None,
      temperature = 0.5,
   )
   return response["choices"][0]["text"]

def speak_text(text):
   engine.say(text)
   engine.runAndWait()

def main():
   while True:
      print("Yello 'Bibi'")
      with sr.Microphone() as source:
         recognizer = sr.Recognizer()
         audio = recognizer.listen(source)
         try:
            transcription = recognizer.recognize_google(audio)
            if transcription.lower() == "bibi":
               filename = "input.wav"
               print("What's up") 
               with sr.Microphone() as source:
                  recognizer = sr.Recognizer()
                  source.pause_threshold = 1
                  audio = recognizer.listen(source, phrase_time_limit=None, timeout=None)
                  with open(filename, "wb") as f:
                     f.write(audio.get_wav_data())

               text = transcribe_speech_to_text(filename)
               if text:
                  print(f"You said: {text}")
                 
                  response = generate_response(text)
                  print(f"Bibi says {response}")

                  speak_text(response)
         except Exception as e:
            print("Hmm...: {}",format(e))

if __name__ == "__main__":
   main()

