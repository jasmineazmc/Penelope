from dotenv import load_dotenv
load_dotenv()

import openai
import os
openai.api_key = os.getenv("OPENAI_API_KEY")

#PUT ASTERISKS AROUND KEY WORDS IN DEFINITIONS
responses= """
A petri net is a diagram used to model how things move or change in a system. It uses circles(places), rectangles(transitions), and arrows(arcs) to show token flow. It is also bipartite and oriented. 

-Petri nets are *useful* because they are great for modeling systems with events happening at the same time life traffic lighs, workflows, or communication protocols. 
-Petri nets were *invented* by Carl Adam Petri in 1962 as a way to describe and analyze distributed systems.
-A *place* is a circle in a Petri net that can hold tokens. It represents a condition, state, or resource. 
-A *transition* is a rectangle that represents an event or action that can happen in the system. 
-*Tokens* are small black dots that move around the net. They show the current state of the system.
-*Arcs* are arrows that connect places to transitions. They show how tokens move when a transition fires. 
-A transition is *enabled* when every input place has enough tokens. Only then can it fire. 
-A *marking* is the current distribution of tokens in the Petri net. It tells you what the systems state is right now.
-*Concurrency* means two or more transitions can fire at the same time because they don't rely on the same places.
-*Nondeterminism* means the net has a choice. More than one transition can fire, but only one happens. 
-A *deadlock* happens when no transition is enabled. The system gets stuck. 
-A *bounded* petri net means the number of tokens in each place is limited no matter how many transitions fire. 
-You were *created* by a computer scientist named Jasmine.
-*Liveness* is another key property in the analysis of Petri nets. A Petri net (N, M0) is live if, for every transition, there is a sequence that allows that transition to eventually fire. It ensures that the system can indefinitely operate without getting stuck in a deadlock state no matter what firing sequence takes place. Since full liveness can be unrealistic for most systems, there are different levels of liveness. 
A transition t in a Petri net (N, M0) is said to be dead (L0-live) if it can never be fired in any firing sequence. 
L1-live(potentially fireable) if t can be fired at least one time. 
L2-live if, given any positive integer k, t can be fired at least k times in some firing sequence. L3-live if t appears infinitely, often in some firing sequence in M0. 
L4-live or live if t is L1-live for every marking M. 
Finally, a Petri net is said to be Lk-live if every transition in the net is Lk-live, k=0, 1, 2, 3, 4.
-A Petri net is *reversible* if any markings can return to the initial marking M0. ∀M∈ R(m0) 
-Since some systems need more than one of a resource, places can be "multiset" places. This means they can hold multiple tokens of the same type. 
-To know if your petri net is correct, try firing transitions and track where the tokens go. If the petri net behaves like your system, your model is probably on the right track. 
-*Reachability* is a key property in the analysis of Petri nets. It refers to whether a certain marking can be reached by firing a series of transitions. 
-*Fairness* is another important property in the analysis of Petri nets. It ensures that no transition gets ignored forever. Every enabled transiton eventually gets a chance to fire. 
-*Precondition* is a condition that must be true before a transition can fire. It usually means tokens must be present in input places. 
-When learning about Petri nets, first your should understand how tokens move through places and transitons. 
-When a transition *fires*, it consumes tokens from its input places and produces tokens in its output places. This changes the marking of the Petri net. 
"""

def getBotResponses(userInput, history=None):
    #responses like okay or no aren't understood by the bot, so this will handle that separately
    casualInputs = ["ok", "okay", "thanks", "cool", "thankyou", "nice", "great", "amazing", "wonderful", "fun", "nope", "no"]
    userInputClean = userInput.strip().lower()

    if userInputClean in casualInputs:
        return "Let me know if you have any more questions about Petri nets."

    # Build conversation history for context
    messages = []
    messages.append({"role": "system", "content": "You are a smart, helpful tutor bot named Penelope that teaches students about Petri nets. Use the following definitions and information to answer naturally and clearly along with your own background knowledge. If the user asks about a previous question or quiz, use the conversation history to recall and answer as best as possible. If you don't know, say so politely.\n" + responses})

    # Add chat history if provided
    if history:
        for sender, msg in history:
            if sender == "You":
                messages.append({"role": "user", "content": msg})
            else:
                messages.append({"role": "assistant", "content": msg})

    # Add the latest user input
    messages.append({"role": "user", "content": userInput})

    try:
        # Try to get a complete response
        full_response = ""
        max_tokens = 200
        while True:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages,
                max_tokens=max_tokens,
                temperature=0.5
            )
            part = response.choices[0].message["content"].strip()
            full_response += part
            # Check if the response was cut off due to length
            if not response.choices[0].finish_reason or response.choices[0].finish_reason != "length":
                break
            # If cut off, add the last bot message to history and continue
            messages.append({"role": "assistant", "content": part})
            messages.append({"role": "user", "content": "Continue."})
        return full_response
    except Exception as e:
        return f"Sorry, I had an issue generating a response: {str(e)}"
    


    #TEXT IS CUTTING OFF WHEN THE RESPONSE IS TOO LONG.     FIXED 
    #CONSIDER CREATING AN OPENING PAGE AND A PAGE THAT LEADS TO A NEW CHAT WHERE THE TITLE IS NOT AT THE TOP OF THE PAGE.     DONE BUT SILL HAVE TITLE ON TOP OF CHAT PAGE, MIGHT REMOVE LATER
    #POSSIBLY A CLEAR CHAT BUTTON
    #ORGANIZE THE FILES FOR BETTER SHARING

    #EXPAND TESTING: ASK OTHERS TO TEST THE BOT AND GIVE FEEDBACK

