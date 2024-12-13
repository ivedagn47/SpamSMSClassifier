import streamlit as st
import joblib
import string

# Load the trained SVM model and TF-IDF vectorizer
loaded_data = joblib.load('model_and_vectorizer.pkl')
model = loaded_data['model']
tfidf_vect = loaded_data['vectorizer']

def preprocess_text(text):
    """Preprocess text by removing punctuation and converting to lowercase."""
    text = ''.join([char for char in text if char not in string.punctuation])
    text = text.lower()
    return text

# CSS to inject contained in a string, including background image
page_style = """
<style>
body {
    color: #fff;
    
}
.css-18e3th9 {
    padding-top: 0rem;
    padding-bottom: 5rem;
    padding-left: 5rem;
    padding-right: 5rem;
}
.stTextInput>label, .stButton>label {
    color: #4CAF50;
}
.stTextInput>div>div>input {
    color: #fff;
}
.stButton>button {
    color: #4CAF50;
    border: 1px solid #4CAF50;
    border-radius: 10px;
    height: 3em;
    width: 10em;
    font-size: 16px;
    background-color: transparent;
}
.stMarkdown {
    font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
}
</style>
"""

# Injecting the style on the page
st.markdown(page_style, unsafe_allow_html=True)

# Streamlit app interface
st.title('📱 SMS Spam Detection App')
st.markdown("""
This app analyzes SMS messages to determine if they are spam or not. 
Enter your message below and click predict to check.
""")

input_sms = st.text_area("Enter the SMS text:")

# Suppress button output
btn = st.button('Predict')
if btn:
    # Preprocess the input
    processed_input = preprocess_text(input_sms)
    # Transform the input for the model
    vector_input = tfidf_vect.transform([processed_input])
    # Make prediction
    prediction = model.predict(vector_input)
    if prediction[0] == 'spam':
        st.error("This SMS is Spam! ⚠️")
    else:
        st.success("This SMS is not Spam! ✅")
