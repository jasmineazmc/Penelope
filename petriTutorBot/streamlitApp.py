import streamlit as st
from responses import getBotResponses
import time

#NSU COLORS
NSU_GREEN ="#007A33"
NSU_YELLOW = "#FFD100"



if "page" not in st.session_state:
    st.session_state.page = "landing"
if "history" not in st.session_state:
    st.session_state.history = []

def show_landing():
    st.markdown(f"""
        <div style='background: linear-gradient(135deg, {NSU_GREEN} 30%, {NSU_YELLOW} 100%); min-height: 100vh; display: flex; flex-direction: column; align-items: center; justify-content: center; padding-top: 40px;'>
            <h1 style='color: {NSU_YELLOW}; font-size: 2.5rem; margin-bottom: 0.5rem; font-weight: 800; letter-spacing: 1px;'>PENELOPE</h1>
            <h2 style='color: {NSU_YELLOW}; font-size: 1.3rem; margin-top: 0; margin-bottom: 1.2rem; font-weight: 700;'>The Petri Net Tutor Bot</h2>
            <div style='background: rgba(255,255,255,0.95); border-radius: 18px; padding: 24px 32px; max-width: 480px; box-shadow: 0 2px 16px rgba(0,0,0,0.07); margin-bottom: 24px;'>
                <p style='color: #222; font-size: 1.1rem; text-align: center; margin-bottom: 0.7rem;'>
                    Welcome to <b>Penelope</b>, your friendly Petri Net tutor!<br><br>
                    <b>Penelope can:</b>
                    <ul style='text-align:left; color: 222; font-size:1rem; margin: 0 0 0 1.2em;'>
                        <li>Explain Petri net concepts in simple terms</li>
                        <li>Help you analyze and debug Petri nets</li>
                        <li>Quiz you or answer your questions</li>
                        <li>Guide you through reachability, liveness, and more</li>
                    </ul>
                    <br>
                    <span style='color:{NSU_GREEN}; font-weight:600;'>Created by Jasmine McDuffie, Norfolk State University</span>
                </p>
            </div>
        </div>
    """, unsafe_allow_html=True)
    # Button to go to chat
    if st.button("Start Chatting", key="startchatbtn", help="Start Chatting", use_container_width=True):
        st.session_state.page = "chat"
        st.rerun()

def show_chat():
    st.markdown(f"""
        <div style='width: 100%; text-align: center; margin-top: 18px; margin-bottom: 18px;'>
            <h1 style='font-size: 2.2rem; color: {NSU_GREEN}; margin-bottom: 0.3rem; margin-top: 0;'>PENELOPE - The Petri Net Tutor Bot</h1>
            <p style='font-size: 1.1rem; color: #444; max-width: 480px; margin: 0 auto;'>Ask me questions about Petri nets! Example: 'What is a Petri Net?'</p>
        </div>
    """, unsafe_allow_html=True)
    if st.button("← Back to Landing Page", key="backtolanding", help="Return to landing page", use_container_width=True):
        st.session_state.page = "landing"
        st.rerun()
        return

    userInput = st.chat_input("You:")
    if userInput:
        st.session_state.history.append(("You", userInput))
        # indicator at the bottom
        thinking_placeholder = st.empty()
        thinking_html = f"""
        <div style='position: fixed; bottom: 30px; left: 0; width: 100vw; z-index: 9999; display: flex; justify-content: center;'>
            <div style='background: "#; color: #1C69E1; padding: 12px 28px; border-radius: 24px; font-size: 18px; box-shadow: 0 2px 8px rgba(0,0,0,0.07); font-weight: 600;'>
                <span style='margin-right: 10px;'>🤔</span>Penelope is thinking...
            </div>
        </div>
        """
        thinking_placeholder.markdown(thinking_html, unsafe_allow_html=True)
        response = getBotResponses(userInput)
        time.sleep(0.5)
        thinking_placeholder.empty()
        st.session_state.history.append(("Penelope", response))

    # Chat bubble styling
    chat_bubble_css = f"""
    <style>
    .chat-container {{
        display: flex;
        flex-direction: column;
        gap: 10px;
        margin-bottom: 32px;
    }}
    .bubble {{
        max-width: 600px;
        width: fit-content;
        min-width: 120px;
        padding: 8px 20px 8px 20px;
        border-radius: 20px;
        font-size: 16px;
        margin-bottom: 0px;
        word-break: break-word;
        box-shadow: 0 2px 8px rgba(0,0,0,0.04);
        display: inline-block;
        line-height: 1.4;
    }} 
    .bubble-user {{
        background: #FFF9DB;
        color: #111;
        align-self: flex-end;
        border-bottom-right-radius: 6px;
        margin-left: auto;
        margin-right: 0;
    }}
    .bubble-bot {{
        background: #FFF9DB;
        color: #222;
        align-self: flex-start;
        border-bottom-left-radius: 6px;
        margin-right: auto;
        margin-left: 0;
    }}
    .sender-label {{
        font-weight: 700;
        font-size: 14px;
        margin-bottom: 1px;
        margin-left: 2px;
    }}
    .sender-bot {{
        color: {NSU_GREEN};
    }}
    .sender-user {{
        color: {NSU_GREEN};
        text-align: right;
    }}
    </style>
    """
    st.markdown(chat_bubble_css, unsafe_allow_html=True)

    chat_html = "<div class='chat-container'>"
    for sender, message in st.session_state.history:
        if sender == "You":
            chat_html += f"<div class='bubble bubble-user'><div class='sender-label sender-user'>{sender}</div>{message}</div>"
        else:
            chat_html += f"<div class='bubble bubble-bot'><div class='sender-label sender-bot'>{sender}</div>{message}</div>"
    chat_html += "</div>"
    st.markdown(chat_html, unsafe_allow_html=True)

    st.markdown(f"""
        <style>
            .block-container h1 {{
                font-size: 28px;
                text-align: center;
                color: {NSU_GREEN};
            }}
            .block-container p{{
                text-align: center;
                font-size: 16px;
                color: #444;
            }}
        </style>
        <script>
            // Auto-scroll to the bottom of the chat
            window.addEventListener('load', function() {{
                var chatContainer = window.parent.document.querySelector('.block-container');
                if (chatContainer) {{
                    chatContainer.scrollTop = chatContainer.scrollHeight;
                }}
            }});
            // Also scroll on update
            const observer = new MutationObserver(function() {{
                var chatContainer = window.parent.document.querySelector('.block-container');
                if (chatContainer) {{
                    chatContainer.scrollTop = chatContainer.scrollHeight;
                }}
            }});
            observer.observe(window.parent.document.body, {{ childList: true, subtree: true }});
        </script>
    """, unsafe_allow_html=True)

# Main logic
if st.session_state.page == "landing":
    show_landing()
elif st.session_state.page == "chat":
    show_chat()

