import requests
import json


#with open('model.pkl', 'rb') as f:
 # newdata = pickle.load(f)

#response = requests.post("http://127.0.0.1:5000/predict", json = {'data': newdata})
#data  = response.json()
#prediction = data['prediction']
#print("Good day to you. The prediction for the data is:", prediction)

#with open('testdata.json', 'r') as f:
#    testdata = json.load(f)

#r = requests.post('http://127.0.0.1:5000/predict', json = {'newdata': testdata})
#data = r.json
#prediction = data['prediction']
#print(f'probability is {prediction}')
#pritn(prediction)

with open('testdata.json', 'r') as f:
    testdata = json.load(f)

#without heroku
#r = requests.post('http://127.0.0.1:5000/predict', json={'newdata': testdata})


#with heroku
r = requests.post('https://sleepy-escarpment-98224.herokuapp.com/predict', json={'newdata': testdata})
data = r.json()
prediction = data['prediction']
print(f'probability is {prediction}')
