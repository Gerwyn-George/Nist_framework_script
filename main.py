# The libraries are specified here. The json library is used to access json data used in this script.  

import json
import os
from unicodedata import name

# This script, at its most basic performs the following actions. 
# 1. Open the Data.json file. 
# 2. extract the data from the json file for each NIST SP 800-160 construct type (i.e. Goals, Objectives).
# 3. For each construct type, create class object for each of these individual element (i.e objective - Prevent/avoid).
# 4. Insert these class objects into a list for that construct. 
# 5. With the class objects in a class. It is then easier to compare constructs and their interactions. 


with open('Data.json', 'r') as f:

    data = json.load(f)

# The empty lists for the NIST SP 800 - 160 constructs are created here.  

list_goals = []
list_objectives = []
list_strat_principles = []
list_struct_principles = []
list_techniques = []
list_approaches = []

# The class objects are defined here for each construct. defaults have been put in for each attribute of the class. 
# i.e dicts and strings. Dicts are used to store mapping, while the strings are used to put in text. 
# The names of the classes are self explanitory.  

class Nist_800_160_Goal:
    def __init__(self,name = "name",  objectives = {}, description = "" ):
        self.name = name
        self.objectives = objectives 
        self.description = description

class Nist_800_160_Objective:
    def __init__(self, name = "", description = "", discussion = ""):
        self.name = name
        self.description = description
        self.discussion = discussion

class Nist_800_160_Stategic_design_principle:
    def __init__(self, name = "", risk_response_priorities = {}, key_ideas = ""):
        self.name = name 
        self.risk_response_priorities = risk_response_priorities
        self.key_ideas = key_ideas

class Nist_800_160_Structural_design_principle: 
    def __init__(self, name = "", strategic_design_principles = {}, key_ideas = ""):
        self.name = name 
        self.strategic_design_principles = strategic_design_principles
        self.key_ideas = key_ideas

class NIST_800_160_Technique: 
    def __init__(self, name = "", definition = "", purpose = "", objectives = {}, approaches = {} ):
        self.name = name 
        self.defintion = definition
        self.purpose = purpose
        self.objectives = objectives
        self.approaches = approaches  

class NIST_800_160_Approach:
    def __init__(self, name = "", definition = "", purpose = "", objectives = {}, approaches = {}):
        self.name = name
        self.defintion = definition
        self.purpose = purpose
        self.objectives = objectives 
        self.approaches = approaches 


# This objectives list, is used later in the script so that users of the script can define their chosen objectives. 
# by default, they are set fo 'false'.  

objectives_list = {"Prevent/Avoid":False, "Prepare":False, "Continue":False, "Constrain":False, "Reconstitute":False, "Understand":False, "Transform":False, "Re-architect":False}


# The functions below that are prefixed with 'get' are focused on the collection of data located in the Data.json file. 
# All of these functions are based around the same function. The description of how the function works is outlined in the first 
# function, this is the same for the rest of the 'get' functions. 

def get_goals_data():
    
    # This identifies where in the json file to collect data from. 

    goals = data["NIST 800-160 Goals"]
 
    # For each goal outlined in data.json do the following. 
    
    for goal in goals:
        
        name = goal["name"]
        list_goals.append( Nist_800_160_Goal(name)) # Add the name collected to the name attribute. 

        for y in list_goals:
            if len(y.description) == 0:
                y.description = goal["description"] # If the description is empty, assign the value of descriptions.  
                
            if len(y.objectives) == 0:
                y.objectives = goal["objectives"] # If the objective is empty, assign the value of objectives. 


def get_objectives_data():

    # This identifies where in the json file to collect data from. 

    objectives = data["NIST 800-160 Objectives"]

    # For each goal outlined in data.json do the following. 

    for obj in objectives:

        name = obj["name"]
        list_objectives.append (Nist_800_160_Objective(name)) # Add the name collected to the name attribute. 

        for y in list_objectives:
            if len(y.description) == 0:
                y.description = obj["Description"] # If the description is empty, assign the value of descriptions.

            if len(y.discussion) == 0:
                y.discussion = obj["Discussion"] # If the discussion is empty, assign the value of discussion. 

def get_stat_design_principles():

    # This identifies where in the json file to collect data from. 

    stat_design = data["NIST 800-160 Stategic design principles"]

    # For each goal outlined in data.json do the following. 

    for principle in stat_design:

        name = principle["name"]
        list_strat_principles.append (Nist_800_160_Stategic_design_principle(name)) # Add the name collected to the name attribute.

        for y in list_strat_principles:
            if len(y.risk_response_priorities) == 0:
                y.risk_response_priorities = principle["Risk response priorities"] # If the risk response priorite is empty, assign the value of risk responce priorities.

            if len(y.key_ideas) == 0:
                y.key_ideas = principle["key_ideas"] # If the key_idease is empty, assugn the value of the key_ideas.
        
                
def get_struct_design_principles():

    # This identifies where in the json file to collect data from.

    struct_design = data["NIST 800-160 Structural Design Principles"]

    # For each goal outlined in data.json do the following. 

    for principle in struct_design:

        name = principle["name"]
        list_struct_principles.append(Nist_800_160_Structural_design_principle(name)) # Add the name collected to the name attribute.

        for y in list_struct_principles:
            if len(y.strategic_design_principles) == 0:
                y.strategic_design_principles = principle["strategic design principles"] # If the desing principle is empty, assugn the value of the design principles.

            if len(y.key_ideas) == 0:
                y.key_ideas = principle["key_ideas"] # If the key_idease is empty, assugn the value of the key_ideas.


def compare():

    # Set all goals to False as defult
    Anticipate = {"Prevent/Avoid":False, "Prepare":False, "Continue":False, "Constrain":False, "Reconstitute":False, "Understand":False, "Transform":False, "Re-architect":False}
    Withstand = {"Prevent/Avoid":False, "Prepare":False, "Continue":False, "Constrain":False, "Reconstitute":False, "Understand":False, "Transform":False, "Re-architect":False}
    Recover = {"Prevent/Avoid":False, "Prepare":False, "Continue":False, "Constrain":False, "Reconstitute":False, "Understand":False, "Transform":False, "Re-architect":False}
    Adapt = {"Prevent/Avoid":False, "Prepare":False, "Continue":False, "Constrain":False, "Reconstitute":False, "Understand":False, "Transform":False, "Re-architect":False}

    for x in list_goals: 

        for y in x.objectives: 

            if x.objectives.get(y) == True and objectives_list.get(y) == True and x.name == "Adapt":

                # For the goal adapt, compares the data from the json from the objective list inputted.
                # If both objectives are True set adapt for that objective to be True.

                Adapt[y] = True
               

            if x.objectives.get(y) == True and objectives_list.get(y) == True and x.name == "Recover":

                # For the goal recover, compares the data from the json from the objective list inputted.
                # If both objectives are True set recover for that objective to be True.

                Recover[y] = True
             

            if x.objectives.get(y) == True and objectives_list.get(y) == True and x.name == "Withstand":

                # For the goal withstand, compares the data from the json from the objective list inputted.
                # If both objectives are True set withstand for that objective to be True.

                Withstand[y] = True
            

            if x.objectives.get(y) == True and objectives_list.get(y) == True and x.name == "Anticipate":

                # For the goal anticipate, compares the data from the json from the objective list inputted.
                # If both objectives are True set anticipate for that objective to be True.

                Anticipate[y] = True
          
    
    anticipate_list = []

    adapt_list = []
  
    recover_list = []

    withstand_list =[]

    
    for key,value in Anticipate.items():
        if value == True: 
           
            anticipate_list.append(key) # Makes a copy of the anticipate dictionary as a list.

    for key,value in Adapt.items():
        if value == True: 
       
            adapt_list.append(key) # Makes a copy of the adapt dictionary as a list.

    for key,value in Recover.items():
        if value == True: 
         
            recover_list.append(key) # Makes a copy of the recover dictionary as a list.

    for key,value in Withstand.items():
        if value == True: 
    
            withstand_list.append(key) # Makes a copy of the withstand dictionary as a list.

    goal_ctr = {"Anticipate":len(anticipate_list), "Adapt":len(adapt_list), "Recover":len(recover_list), "Withstand":len(withstand_list)} # Makes a dictionary of the lengths of each goal list

    goal_ctr = (sorted(goal_ctr.items(),key=lambda x:x[1], reverse=True)) # sorts the dictionary in reverse order of value "key:value".
 

    # Desplaying the results from the algrathium. 

    for key in range(0,4): # The number of goals is 4.
            
        print("")

        # goal_ctr[key][0] is the goal name and goal_ctr[key][1] is the number of objectives 
        print(("The {} GOAL Meets: {} NIST 800-160 OBJECTIVES.").format(goal_ctr[key][0],goal_ctr[key][1])) 
        print("These are:")
        print("")

        if goal_ctr[key][0] == "Anticipate":
            for i in anticipate_list:
                print(("         * {}").format(i)) # Prints all the objectives met for anticipate.
    
        if goal_ctr[key][0] == "Adapt":
            for i in adapt_list:
                print(("         * {}").format(i)) # Prints all the objectives met for adapt.
    
        if goal_ctr[key][0] == "Recover":
            for i in recover_list:
                print(("         * {}").format(i)) # Prints all the objectives met for recover.
    
        if goal_ctr[key][0] == "Withstand":
            for i in withstand_list:
                print(("         * {}").format(i)) # Prints all the objectives met for withstand.



def show_selected_objectives():
    
    # To show the user the objectives they have selected.
    # Set all the objectives to space

    ob_prevent = " "
    ob_prepare = " "
    ob_continue = " "
    ob_constrain = " "
    ob_reconsitute = " "
    ob_understand = " " 
    ob_transform = " "
    ob_rearchitect = " "

    # If the objective has been selected set it as x.

    for key, value in objectives_list.items():
        if key == "Prevent/Avoid" and value == True:
            ob_prevent = "x"

        if key == "Prepare" and value == True:
            ob_prepare = "x"
        
        if key == "Continue" and value == True:
            ob_continue = "x"

        if key == "Constrain" and value == True:
            ob_constrain = "x"

        if key == "Reconstitute" and value == True:
            ob_reconsitute = "x"
        
        if key == "Understand" and value == True: 
            ob_understand = "x"

        if key == "Transform" and value == True:
            ob_transform = "x"
        
        if key == "Re-architect" and value == True:
            ob_rearchitect = "x" 

    # Printing the objectives with an x if it has been selected to show the user their inputs.

    print("")
    print("You have selected the following NIST SP 800-160 Objectives.")
    print (("Prevent/Avoid [{}] - Prepare [{}] - Continue [{}] - Constrain [{}] - Reconstitute [{}] - Understand [{}] - Transform [{}] - Re-architect [{}]").format(ob_prevent,ob_prepare,ob_continue,ob_constrain,ob_reconsitute,ob_understand,ob_transform,ob_rearchitect))
    print("")
   

def set_objectives():

    print("")
    print("Choose NIST 800-160 objectives:")
    print("")
    
    # Getting the users inputs of objectives.

    ob_prevent = input("Prevent/Avoid? y for yes, n for no: ")
    if ob_prevent == "y":
        objectives_list.update({"Prevent/Avoid": True})
    else:
        objectives_list.update({"Prevent/Avoid": False}) # Any incorect input counts as n

    ob_prepare = input("Prepare? y for yes, n for no: ")
    if ob_prepare == "y":
        objectives_list.update({"Prepare": True})
    else:
        objectives_list.update({"Prepare": False})
    
    ob_continue = input("Continue? y for yes, n for no: ")
    if ob_continue == "y":
        objectives_list.update({"Continue": True})
    else:
        objectives_list.update({"Continue": False})
    
    ob_constrain = input("Constrain? y for yes, n for no: ")
    if ob_constrain == "y":
        objectives_list.update({"Constrain": True})
    else: 
        objectives_list.update({"Constrain": False})
    
    ob_reconsitute = input("Reconsitute? y for yes, n for no: ")
    if ob_reconsitute == "y":
        objectives_list.update({"Reconstitute": True})
    else:
        objectives_list.update({"Reconstitute": False})
    
    ob_understand = input("Understand? y for yes, n for no: ")
    if ob_understand == "y":
        objectives_list.update({"Understand": True})
    else:
        objectives_list.update({"Understand": False})
    
    ob_transform = input("Transform? y for yes, n for no: ")
    if ob_transform == "y":
        objectives_list.update({"Transform": True})
    else: 
        objectives_list.update({"Transform": False})

    ob_rearchitect = input("Re-architect? y for yes, n of no: ")
    if ob_rearchitect == "y":
        objectives_list.update({"Re-architect":True})
    else:
        objectives_list.update({"Re-architect":False})


def show(construct): 

    if construct == "objectives":
        print("Objectives:")
        print("")
        for i in list_objectives: # Loops through the list of objectives from the json file.
            print("")
            print("*",i.name)
            print("")
            print("description:",i.description)
        print("")
    
    if construct == "goals":
        print("Goals:")
        print("")
        for i in list_goals: # Loops through the list of goals from the json file.
            print("")
            print("*",i.name)
            print("")
            print("description:",i.description)
        print("")

    if construct == "strategic design principles":
        print("Stategic design principles:")
        print("")
        for i in list_strat_principles: # Loops through the list of strat principles from the json file.
            print("")
            print("*",i.name)
            print("")
            print("key ideas:",i.key_ideas)
        print("")

    if construct == "structural design principles":
        print("Structural design principles")
        print("")
        for i in list_struct_principles: # Loops through the list of struct principles  from the json file.
            print("")
            print("*",i.name)
            print("")
            print("key ideas:",i.key_ideas)
        print("")


if __name__ == "__main__":

    # Set up functions.

    get_stat_design_principles()
    get_struct_design_principles()
    get_goals_data()
    get_objectives_data()

    # Menue

    while True:

        print("")
        print("---------- Console application ----------")
        print("")
        print("NIST 800-160 v2")
        print("")
        print("Options:")
        print("1, choose NIST 800-160 objectives")
        print("2, see objectives")
        print("3, see goals")
        print("4, see strategic design principles")
        print("5, see structural design principles")
        print("")

        # User choosing their option in the menue.

        choose = input("please input your option: ")

        if choose == "1":        
            set_objectives()
            show_selected_objectives()
            compare()
        if choose == "2":
            show("objectives")
        if choose == "3":
            show("goals")
        if choose == "4":
            show("strategic design principles")
        if choose == "5":
            show("structural design principles")
        else:
            print(choose,"was not a vailid input")
        
        # Allows you to break from the loop.

        repeat = input("Do you want to select another option? y for yes, n for no: ")
        if repeat != "y":
            break