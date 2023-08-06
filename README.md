# ROI Calculator
#### Using ["BiggerPockets" 4 Square method](https://www.youtube.com/watch?v=T_7vhsSBi7c):

This project was a weekend project for Coding Temple.  The minimum requirements were to make a CLI based ROI calculator using a given videos methodology (linked above).  The demonstrated app allowed for an initial input to be edited, or to start a new calculation.  After completing the initial ask, I decided to try to get a little bit further with learning how to use tkinter. I built a basic 2 page app that completed the same task, although it doesn't use all of the methodologies from the initial CLI app.

I wanted to add some features and truly implement editing in tkinter rather than just passing the data back and forth between pages, but I have been dealing with mold remediation in the space that I work so I could not work for the majority of Saturday and Sunday. 

## Project description:
In this repository there are 2 files that will allow you to calculate the ROI on a rental property (using a 6 year old videos basic methodology).  

The structure of the code is simple.  The main function `calculate_roi()` creates an instance of the `ROI_calculator` class, which then requests input to then create a `Property` class which stores the input data.  The calculator class then calculates and stores the ROI.

Currently I am not allowing you to create multiple properties to view at once, but by storing the property data in a separate class, it makes it easier to do expand upon. If you look back at my [Blackjack Apps](https://github.com/robertblindt/blackjack-app) multi player method, a very similar methodology could be used to store and view multiple properties at once by using a list of property instances.  

My tkinter app does not utilize all of the methods that I created for the CLI app, as I am still learning how to use tkinter.  This time around I learned how to use frames, clearing methods, and extra functions to go between different 'pages'.  If the functionality is expanded to store multiple properties, using a sidebar to show some kind of property preview could 

## Installing, Running, and How to use:
You should be able to just clone this repository and run this as long as you are using Python 3.8 or newer. I started developing my functions in Jupyter notebook using Python 3.8 and eventually moved over to VSCode where I was using 3.9.

To run the CLI app, open up the Jupyter Notebook file, and run the cells containing class and function, and then call the function.

To run the tkinter app, from the command line, run: `python tkinter_roi.py`

Once either is running there should be text prompts guiding you what to do next.  As of writing this README I have not set up a pop out window for the tkinter app to tell you exactly what is wrong with your inputs, and it just throws an error in your terminal.  There is a text prompt below that tells you to only use whole numbers without commas or dollar sings though.  

## Future Improvement:
- Add pop out window for 'whats wrong' for submitting an incomplete form or a form with letters in it.
- Storing multiple properties at once
- Add sidebar and editing in the tkinter app
    - Currently it just passes the data back and forth


## Credits:
[Calculating Numbers on a Rental Property [Using The Four Square Method!]](https://www.youtube.com/watch?v=T_7vhsSBi7c)