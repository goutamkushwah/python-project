import json

# print("Enter your choice\n1. create todo\n2. update\n3. delete\n4. read\n ")
# choice = int(input("Enter your choice . "))
with open("task.json", "r") as f:
    tasks = json.load(f)  
task={
    "id": 1,
    "todo" : "buy tomato",
    "descrition" : "go market",
}   
def create(): 
    with open("task.json","w") as f:
        json.dump(task,f,indent=4)
def read():     
    with open("task.json","r") as f:
        print("your todo's")
        print(task)
