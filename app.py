import streamlit as st
import Jarvis  # import your backend file
import speech_recognition as sr

st.set_page_config(page_title="Jarvis AI", page_icon="🎙️")

st.title("🎙️ Jarvis Voice Assistant")
st.write("Press the button and speak...")

# Button for voice input
if st.button("Start Listening 🎤"):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        st.write("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        st.success(f"User said: {query}")

        # Call backend Jarvis actions
        query = query.lower()

        if 'wikipedia' in query:
            Jarvis.speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = Jarvis.wikipedia.summary(query, sentences=2)
            Jarvis.speak("According to Wikipedia")
            st.write(results)
            Jarvis.speak(results)

        elif 'open youtube' in query:
            Jarvis.webbrowser.open("https://youtube.com")
            Jarvis.speak("Opening YouTube")

        elif 'open google' in query:
            Jarvis.webbrowser.open("https://google.com")
            Jarvis.speak("Opening Google")

        elif 'open stackoverflow' in query:
            Jarvis.webbrowser.open("https://stackoverflow.com")
            Jarvis.speak("Opening StackOverflow")

        elif 'play music' in query:
            music_dir = "D:\\songs\\Favorite"  # same path as backend
            songs = Jarvis.os.listdir(music_dir)
            Jarvis.os.startfile(Jarvis.os.path.join(music_dir, songs[0]))
            Jarvis.speak("Playing music")

        elif 'the time' in query:
            strTime = Jarvis.datetime.datetime.now().strftime("%H:%M:%S")
            Jarvis.speak(f"Sir, the time is {strTime}")
            st.write(f"🕒 {strTime}")

        else:
            Jarvis.speak("Sorry, I didn't get that")

    except Exception as e:
        st.error("Could not recognize your voice. Please try again.")
        print(e)
