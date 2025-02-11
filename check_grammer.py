import streamlit as st
import streamlit as st
from langchain_groq import ChatGroq

def correct_grammar(text):
    llm = ChatGroq(
        model="gemma2-9b-it",
        temperature=0,
        groq_api_key="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"  # Replace with your actual API key
    )
    
    prompt = f"Check the grammar of the following text. If it's correct, return it as is. If it has grammar mistakes, correct them without changing the meaning or adding extra words. Also, list the incorrect words and provide feedback on what went wrong.\nText: {text}"
    
    response = llm.invoke(prompt)
    corrected_text = response.content
    
    return corrected_text

def extract_incorrect_words(response_text):
    incorrect_words = []
    lines = response_text.splitlines()
    for line in lines:
        if "incorrect" in line.lower():
            incorrect_words.append(line.strip())
    return incorrect_words

st.title("Grammar Checker")
st.write("Enter a sentence below to check for grammar mistakes.")

user_input = st.text_area("Your Sentence:", "")

if st.button("Check Grammar"):
    if user_input.strip():
        corrected_text = correct_grammar(user_input)
        
        if corrected_text.strip() == user_input.strip():
            st.success("Your sentence is grammatically correct!")
        else:
            st.write("### Corrected Sentence:")
            st.write(corrected_text)
            
            incorrect_words_feedback = extract_incorrect_words(corrected_text)
            if incorrect_words_feedback:
                st.write("### Incorrect Words and Feedback:")
                for feedback in incorrect_words_feedback:
                    st.write(f"- {feedback}")
    else:
        st.warning("Please enter a sentence to check.")