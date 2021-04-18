import json

def getID():
    print("Input Organization ID or Name:")
    
    name = input()

    f = open("university list.json")
    universities_dict = json.load(f)


    for university in universities_dict["Universities"]:
        if (university["ID"] == name or university["University"] == name):
            print(university["ID"], university["University"])
            return university["ID"]
        

