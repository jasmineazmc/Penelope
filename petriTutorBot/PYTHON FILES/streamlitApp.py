import streamlit as st
from responses import getBotResponses
 
 #TITLE
st.title ("PENELOPE - The Petri Net Tutot Bot")

#instructions
st.write ("Ask me questions about Petri nets! Example: 'What is a Petri Net?'")

if "history" not in st.session_state:
 st.session_state.history = []

userInput = st.text_input ("You:", "")

if userInput:
 response = getBotResponses(userInput)

 st.session_state.history.append(("You", userInput))
 st.session_state.history.append(("Bot", response))

 #st.experimental_rerun()

 for sender, message in st.session_state.history:
  if sender == "You":
   st.markdown(f"**{sender}:** {message}")
  else:
   st.markdown(f"<span style='color:green'><b>{sender}:<b> {message}</span>", unsafe_allow_html=True)