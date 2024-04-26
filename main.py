from fastapi import FastAPI
import schemas

app = FastAPI()

fakeDatabase = {
    1:{'task':'Clean car'},
    2:{'task':'Write blog'},
    3:{'task':'Start stream'},
}

@app.get("/")
def getItems():
    return fakeDatabase

@app.get("/{id}")
def getItem(id:int):
    return fakeDatabase[id]

# #option #1
# @app.post("/")
# def addItem(task:str):
#     newId = len(fakeDatabase.keys())+1
#     fakeDatabase[newId] = {"task":task}
#     return fakeDatabase

# #option #2
@app.post("/")
def addItem(item:schemas.Item):
    newId = len(fakeDatabase.keys())+1
    fakeDatabase[newId] = {"task":item.task}
    return fakeDatabase

#option #3
# @app.post("/")
# def addItem(body = Body()):
#     newId = len(fakeDatabase.keys())+1
#     fakeDatabase[newId] = {"task":body['task']}
#     return fakeDatabase

@app.put("/{id}")
def updateItem(id:int,item:schemas.Item):
    fakeDatabase[id]['task'] = item.task
    return fakeDatabase