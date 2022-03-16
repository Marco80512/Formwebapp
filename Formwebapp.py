

from flask import Flask, url_for, render_template, request,Markup

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('Form.html')    


    
@app.route("/Breakfast")
def render_response():
    c1 = request.args['choice1'] 
    c2 = request.args['choice2'] 
    c3 = request.args['choice3']
    
    if c1 == 'Eggs' and c2 == 'French toast' and c3 == 'Syrup':
        return render_template('PTJ.html',Meal = Markup('<img src="/static/EFTS.jpg" alt="You have made French toast with Syrup" width="500" height="600"><p> Where does this go?</p>'))

    
    if c1 == 'Bananas' and c2 == 'Syrup' and c3 == 'Waffles':
        return render_template('PTJ.html',Meal = Markup('<img src="/static/BSW.jpg" alt="You have made Waffle with Syrup" width="500" height="600"><p> Where does this go?</p>'))  
     
   
    if c1 == 'Yogurt' and c2 == 'Oatmeal' and c3 == 'Bananas':
        return render_template('PTJ.html',Meal = Markup('<img src="/static/YOB.jpg" alt="You have made Oatmeal with Bananas " width="500" height="600"><p> Where does this go?</p>'))
    

    if c1 == 'Bananas' and c2 == 'Syrup' and c3 == 'Pancakes':
        return render_template('PTJ.html',Meal = Markup('<img src="/static/BSP.jpg" alt="You have made Pancakes with Bananas " width="500" height="600">  <p> Where does this go?</p>'))
  
  
  
  
  
    
if __name__=="__main__":
    app.run(debug=True)

 
 
