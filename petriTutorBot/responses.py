def getBotResponses(userInput):
    userInput = userInput.lower()

    if "what is a petri net" in userInput:
        return "A Petri net is a mathematical model used to represent distributed systems using places, transitions, and tokens. " 
    elif "place" in userInput:
        return "A place in a Petri net holds tokens and represents a condition or state."
    elif "transition" in userInput:
        return "A transition is an event in a Petri net that can occur and change the distribution of tokens."
    elif "token" in userInput:
        return "Tokens represent the state of the system and move through places when transitions fire."
    elif "fire" in userInput or "firing" in userInput:
        return "Firing a transitions means moving tokens from input places to output places according to the net's structure."
    elif "marking" in userInput:
        return "A marking is a snapshot of how tokens are distributed across places in a Petri net."
    else:
        return "I'm still learning! Try asking something about Petri nets, places, transitions, or tokens."
    

#TEST CODE
if __name__ == "__main__":
    print ("Penelope is ready! (type 'exit' to quit)")
    while True:
        msg = input("You: ")
        if msg.lower() == "exit":
            print ("Goodbye")
            break
        print("Bot:", getBotResponses(msg))
