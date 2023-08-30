from flask import Flask
app = Flask(__name__) 

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo_function():
    return 'Dojo!'

#BONUS NINJAS
@app.route('/say/<string:name>')
def name_function(name):
    return 'Hello, ' + name

#BONUS NINJAS
@app.route('/repeat/<int:num>/<string:name>')
def repeat_function(num, name):
    name= name + '<br>'
    return  f'<h2>{name * num}</h2>'

# BONUS SENSEI 
@app.errorhandler(404) # we specify in parameter here the type of error, here it is 404
def page_not_found(error): # (error) is important because it recovers the instance of the error that was thrown
    return f"Sorry! No response. Try again"

if __name__=="__main__":
    app.run(debug=True)