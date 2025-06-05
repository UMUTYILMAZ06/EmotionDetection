import streamlit as st
import joblib
import speech_recognition as sr

# Load the trained model and vectorizer
model = joblib.load('emotion_classifier_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

# Streamlit interface
st.title('Emotion Detection App')

st.write("Choose how you want to enter the text:")

# Ses tanıma için mikrofon kullanma
if st.button('Use Microphone for Voice Input'):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Listening...")
        audio = recognizer.listen(source)
        st.write("Recognizing...")

    # Ses kaydını metne dönüştür
    try:
        user_input = recognizer.recognize_google(audio, language="en-US")
        st.write("You said:", user_input)
    except sr.UnknownValueError:
        st.write("Could not understand audio")
    except sr.RequestError:
        st.write("Could not request results; check your network connection")

# Manuel olarak metin girişi
else:
    user_input = st.text_area('Or enter your text here')

# Metin varsa tahmin yap
if st.button('Analyze'):
    if user_input:
        # Girdi metnini vektöre dönüştür
        user_input_vectorized = vectorizer.transform([user_input])
        
        # Modeli kullanarak tahmin yap
        prediction = model.predict(user_input_vectorized)

        st.write(f'Predicted Emotion: {prediction[0]}')
    else:
        st.write("Please provide input either through the microphone or text box.")
