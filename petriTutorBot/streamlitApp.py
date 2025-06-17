import streamlit as st
from responses import getBotResponses

#TITLE
st.title ("PENELOPE - The Petri Net Tutor Bot")

#instructions
st.write ("Ask me questions about Petri nets! Example: 'What is a Petri Net?'")

if "history" not in st.session_state:
 st.session_state.history = []

userInput = st.chat_input ("You:")

if userInput:
 response = getBotResponses(userInput)

 st.session_state.history.append(("You", userInput))
 st.session_state.history.append(("Bot", response))

 for sender, message in st.session_state.history:
  if sender == "You":
   st.markdown(f"**{sender}:** {message}")
  else:
   st.markdown(f"<span style='color:green'><b>{sender}:<b> {message}</span>", unsafe_allow_html=True)

st.markdown("""
    <style>
        .block-container h1 {
            font-size: 28px;
            text-align: center;
            color: #007A33:
            }
            
       .block-container p{
            text-align: center;
            font-size: 16px;
            color: #444;
   """, unsafe_allow_html=True)