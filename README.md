# coordinate-finder
flask app for finding coordinates for pixel placement in a two dimensional rectangular grid

# To Run App

pull repository and build using docker

to build docker and name it rads-flask-app:

``` docker build -t rads-flask-app . ```

to build docker and name it something else:

``` docker build -t something_else . ```

once docker successfully builds you can run the app using either the name you assigned the image:

``` docker run <name of image> ```

or using the imageID:
``` docker run <imageID> ```

a link should appear in your terminal open link in web browser

# troubleshooting

if you are not able to run the flask app due to port issues try 

```docker run -p 5000:5000 -d <name or imageID>```


# interacting with app in browser
use numerical values for height and width of image
and type in the coordinate pairs for the corners of rectangle in standard coordinate format, seperating each by a comma, 
the order of the four coordinate pairs is not important

example: (3,2),(3,5),(1,2),(1,5)

press submit

# future versions
this project is a rough draft and the first working version while calcultations it outputs are correct it has much room for improvement, such future changes to make include:
* formatting / beautifying layout / adjusting sizes of input boxes, making output visually easier to read
* adding two dimensional image of a grid with marked coordinate pairs mapped over it on coordinates.html template
* adding more tests
* error message for inappropriate entries on form
