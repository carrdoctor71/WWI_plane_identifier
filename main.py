# Assignment 1 AI & ML
# Ken Carr

# import the wikipedia library for research
import wikipedia
from sklearn import tree

print("\n*** Your AI Assitant ***\n")

run = True
while bool(run) == True:
    choice = input("Select what AI can help you with:\n1 - Research\n2 - Check For Attacks\nE - EXIT\n")
    if choice == '1':
        print("\n=== Research Assistant ===\n")
        topic = input("\nWhat topic do you need help with?  ")
        print("\nI can help you research " + topic + "!")
        research_result = wikipedia.summary(topic)
        print("\nHere is what I found:\n" + research_result + "\n\n")
    elif choice == '2':
        print("\n=== Air Defense Check ===")
        # Training Data
        features = [[42,60],[35,55],[29,35],[23,24],[26,28],[22,25]]
        # Training Markers: 1 = bomber & 0 = fighter
        plane_identifier = [1,1,1,0,0,0]
        # Create a decision tree classifier to train on the data
        tree_classifier = tree.DecisionTreeClassifier()
        tree_classifier = tree_classifier.fit(features,plane_identifier)
        # data to process to draw prediction
        wingspan = input("\nWhat is the Wingspan in FT? ")
        fuselage = input("\nWhat is the Fuselage length in FT? ")
        # make and feedback prediction to user
        prediction = tree_classifier.predict([[wingspan,fuselage]])
        # turn number clasification into user understood feedback
        if prediction == 1:
            plane = "BOMBER"
        else:
            plane = "FIGHTER"
        print("\n*** A " + plane + " IS COMMING! ***\n")
    elif choice.lower() == 'e': # accounts for upper and lower case e
        print("\n*** Goodbye ***\n")
        run = False
    else:
        print("*** Not A Valid Selection ***\n*** Try Again ***\n")

