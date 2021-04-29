from flask import Flask, request
import pickle
app = Flask(__name__)

with open('pipe.pickle', 'rb') as f:
    pipe = pickle.load(f)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/Json_test')
def Json_test():
    return {'prediction': .05}

#@app.route('/predict', methods=['POST'])
#def predict():
    #if request.method == 'POST':
        #the_data=request.get_json(force=True)
        #newdata = the_data['newdata']
        #prediction = pipe.predict([newdata])
        #return {'prediction': prediction.tolist()}


#for herokuapp
import flask

@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        the_data=request.get_json(force=True)
        newdata = the_data['newdata']
        prediction = pipe.predict([newdata])
        return {'prediction': prediction.tolist()}
    return render_template('template.html')


if __name__ == '__main__':
    import os
    port = os.getenv('PORT')
    app.run(port=port)
