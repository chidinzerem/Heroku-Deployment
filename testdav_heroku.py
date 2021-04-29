import requests
import json

#with heroku
r = requests.post('https://sleepy-escarpment-98224.herokuapp.com/predict', json={'newdata': testdata})
data = r.json()
prediction = data['prediction']
print(f'probability is {prediction}')
