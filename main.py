from distutils.log import debug
from flask import Flask, render_template
from flask import request
import numpy as np

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/coordinates', methods=['POST'])
def findcoords():
    
    x_values=[]
    y_values=[]
    corner_points=[]
    
    #take in values from form
    h = int(request.form['height'])
    w = int(request.form['width'])
    corner_points = list(eval(request.form['corner_points']))
    
    #rearrange/tidyup corner points 
    for i,j in corner_points:
        x_values.append(i)
        y_values.append(j)
    x=np.array(x_values)
    y=np.array(y_values)
    x=np.unique(x)
    y=np.unique(y)
    
    #calculate and organize all coordinate pairs for pixel placement
    xs=np.linspace(x[0],x[1],w)
    ys=np.linspace(y[0],y[1],h)
    Xs,Ys = np.meshgrid(xs,ys)
    xy = np.vstack((Xs.flatten(), Ys.flatten())).T
    xys=np.reshape(xy, (h,w,2))
    coordinates=np.flip(xys,0)

    return render_template("coordinates.html", coordinates=coordinates)


if __name__ == "__main__":
    app.run(debug=True)
    app.run(debug=True, host='0.0.0.0', port=port)
