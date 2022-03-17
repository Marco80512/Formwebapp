

from flask import Flask, url_for, render_template, request, Markup

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('Form.html')    


    
@app.route("/Breakfast")
def render_response():
    c1 = request.args['choice1'] 
    c2 = request.args['choice2'] 
    c3 = request.args['choice3']
    
    if (c1 == 'Eggs' and c2 == 'French toast' and c3 == 'Syrup') or (c1 == 'Syrup' and c2 == 'Eggs' and c3 == 'French toast') or (c1 == 'French toast' and c2 == 'Syrup' and c3 == 'Eggs'):
        return render_template('PTJ.html',Meal = Markup('<img src="/static/EFTS.jpg" alt="You have made French toast with Syrup" width="500" height="600"><p> You have made French toast with Syrup</p>'))
    
    
    if (c1 == 'Bananas' and c2 == 'Syrup' and c3 == 'Waffles') or (c1 == 'Waffles' and c2 == 'Bananas' and c3 == 'Syrup') or ( c1 == 'Syrup' and c2 == 'Waffles' and c3 == 'Bananas'):
        return render_template('PTJ.html',Meal = Markup('<img src="/static/BSW.jpg" alt="You have made Waffle with Syrup" width="500" height="600"><p> You have made Waffle with Syrup</p>'))  
        
        
    if (c1 == 'Bananas' and c2 == 'Yogurt' and c3 == 'Oatmeal') or (c1 == 'Oatmeal' and c2 == 'Bananas' and c3 == 'Yogurt') or (c1 == 'Yogurt' and c2 == 'Oatmeal' and c3 == 'Bananas'):
        return render_template('PTJ.html',Meal = Markup('<img src="/static/YOB.jpg" alt="You have made Oatmeal with Bananas " width="500" height="600"><p> You have made Oatmeal with Bananas</p>'))   
        
 
    if (c1 == 'Bananas' and c2 == 'Syrup' and c3 == 'Pancakes') or (c1 == 'Pancakes' and c2 == 'Bananas' and c3 == 'Syrup') or (c1 == 'Syrup' and c2 == 'Pancakes' and c3 == 'Bananas'):
        return render_template('PTJ.html',Meal = Markup('<img src="/static/BSP.jpg" alt="You have made Pancakes with Bananas " width="500" height="600">  <p> You have made Pancakes with Bananas</p>'))
        
  
    if (c1 == 'Pancakes' and c2 == 'Bananas' and c3 == 'Syrup') or (c1 == 'Syrup' and c2 == 'Pancakes' and c3 == 'Bananas') or (c1 == 'Bananas' and c2 == 'Syrup' and c3 == 'Pancakes'):
        return render_template('PTJ.html',Meal = Markup('<img src="/static/MEB.png" alt="You have made Pancakes with Bananas " width="500" height="600">  <p> You have made Banana Cake</p>'))
        
      
    if (c1 == 'Milk' and c2 == 'Cheese' and c3 == 'Syrup') or (c1 == 'Syrup' and c2 == 'Milk' and c3 == 'Cheese') or (c1 == 'Cheese' and c2 == 'Syrup' and c3 == 'Milk'):
        return render_template('PTJ.html',Meal = Markup('<img src="/static/SF.png" alt="You have made Pancakes with Bananas " width="500" height="600">  <p> You can not make anything with these items</p>'))
        
        
    if (c1 == 'Eggs' and c2 == 'Yogurt' and c3 == 'Milk') or ( c1 == 'Milk' and c2 == 'Eggs' and c3 == 'Yogurt') or (c1 == 'Yogurt' and c2 == 'Milk' and c3 == 'Eggs'):
        return render_template('PTJ.html',Meal = Markup('<img src="/static/SF.png" alt="You have made Pancakes with Bananas " width="500" height="600">  <p> You can not make anything with these items</p>'))
        
        
    if (c1 == 'Eggs' and c2 == 'Yogurt' and c3 == 'Syrup') or ( c1 == 'Syrup' and c2 == 'Eggs' and c3 == 'Yogurt') or (c1 == 'Yogurt' and c2 == 'Syrup' and c3 == 'Eggs'):
        return render_template('PTJ.html',Meal = Markup('<img src="/static/SF.png" alt="You have made Pancakes with Bananas " width="500" height="600">  <p> You can not make anything with these items</p>'))
        
        
    if (c1 == 'Eggs' and c2 == 'Pancakes' and c3 == 'Waffles') or ( c1 == 'Waffles' and c2 == 'Eggs' and c3 == 'Pancakes') or (c1 == 'Pancakes' and c2 == 'Waffles' and c3 == 'Eggs'):
        return render_template('PTJ.html',Meal = Markup('<img src="/static/WPE.png" alt="You have made Pancakes with Bananas " width="500" height="600">  <p> You have made Waffles with Eggs and Pancakes</p>'))
        
    if (c1 == 'French toast' and c2 == 'Syrup' and c3 == 'Pancakes') or ( c1 == 'Pancakes' and c2 == 'French toast' and c3 == 'Syrup') or (c1 == 'Syrup' and c2 == 'Pancakes' and c3 == 'French toast'):
        return render_template('PTJ.html',Meal = Markup('<img src="/static/FTPS.png" alt="You have made Pancakes with Bananas " width="500" height="600">  <p> You can not make anything with these items</p>'))
  
  
    
if __name__=="__main__":
    app.run(debug=True)

 
 
