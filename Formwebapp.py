import Markup

from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('Form.html')    


    
@app.route("/Breakfast ")
def render_response():
    c1 = request.args['choice1'] 
    c2 = request.args['choice2'] 
    c3 = request.args['choice3']
    
    if c1 == 'Eggs' and c2 == 'French toast' and c3 == 'Syrup':
    return render_tepmlate,('PTJ.html'Meal = Markup('<img src="EFTS.jpg" alt="You have made French toast with Syrup" width="500" height="600">
    <p> Where does this go?</p>))
 @app.route("/Breakfast ")
def render_response():
    c1 = request.args['choice1'] 
    c2 = request.args['choice2'] 
    c3 = request.args['choice3']
    
    if c1 == 'Bananas' and c2 == 'Syrup' and c3 == 'Waffles':
    return render_tepmlate,('PTJ.html'Meal = Markup('<img src="BSW.jpg" alt="You have made Waffle with Syrup" width="500" height="600">
    <p> Where does this go?</p>))   
    
@app.route("/Breakfast ")
def render_response():
    c1 = request.args['choice1'] 
    c2 = request.args['choice2'] 
    c3 = request.args['choice3']
    
    if c1 == 'Yogurt' and c2 == 'Oatmeal' and c3 == 'Bananas':
    return render_tepmlate,('PTJ.html'Meal = Markup('<img src="YOB.jpg" alt="You have made Oatmeal with Bananas " width="500" height="600">
    <p> Where does this go?</p>))

@app.route("/Breakfast ")
def render_response():
    c1 = request.args['choice1'] 
    c2 = request.args['choice2'] 
    c3 = request.args['choice3']
    
    if c1 == 'Bananas' and c2 == 'Syrup' and c3 == 'Pancakes':
    return render_tepmlate,('PTJ.html'Meal = Markup('<img src="BSP.jpg" alt="You have made Pancakes with Bananas " width="500" height="600">
    <p> Where does this go?</p>))
    
    if __name__=="__main__":
    app.run(debug=True)

 
 
