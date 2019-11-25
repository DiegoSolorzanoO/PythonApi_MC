import json

def readData(file):
    try:
        f = open(file, "r")
        if f.mode == 'r':
            contents = f.read()
            return json.loads(contents) 
        return None
    except:
        return False

def saveData(file, data):
    f = open(file,"w+")
    f.write(json.dumps(data))
    f.close()