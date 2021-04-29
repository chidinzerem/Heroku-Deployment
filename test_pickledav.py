import pickle
import json

with open('pipe.pickle', 'rb') as f:
    pipe = pickle.load(f)


with open('testdata.json', 'r') as f:
    testdata = json.load(f)

print(pipe.predict([testdata]))
