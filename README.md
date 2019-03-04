# Data-Centric Project

A Code Institute Project. Data-Centric.

## Getting Started
To get started lets make some preps. You'd need to have a basic understanding of the flask framework and and atleast a grasp on some frontend technologies. Besides the usual css and html, it would be handy to know a bit of bootstrap or materialise.css. In our case we will be using materialise.css for the front-end. 

 Since the Question specified an online cook-book, it's imperative we stay as close as we can within the scope of what has been prescribed, atleast in design. For the design i'm going to be using grids of 3squares per row, with a total of 6 squares per page. The materialise cards can do a good job with that. The cards will have 3 sections; being 1. the card-imge, 2. card-title, and 3.crud-section.
 The card-iamge has 2 sections, the actual image which will bear the recipe image and on the flipped side where i'll put my recipe ingredients. So if a user should click on the image of a card it will flip and the ingredients will be diplayed. The card title,  is where some details like recipe author, country of origin of the recipe, and name of recipe entries will placed.  
 And finally the crud section. This section will basically contain some crud buttons. Examples are the edit and delete buttons, which when clicked will send the user to the appropriate page or take the required action.
 
 
 
## Prerequisites

I'll ussually start by setting up the environment for my flask app by entering in my cli tool
``` 
$ [sudo]pip install virtualenv 
```
Virtual env is a tool that serves as a sandbox for your python projects. So, what this does is, it tricks your computer into looking for and installing packages in your project directory rather than in in your python directory. 
But unfornately we wont be working from it with this project.

Within the <head> tags place your title and various <links> to connect to your HTML. The bootstrap4 CSS or whatever cdn to be used will be placed in the head tags. It's important to place the script tags at the bottom of the page but right before the closing body tags.
To connect the css files flask has a twist from the ussual, it follows this structure;
 
```
 <link rel="stylesheet" href="{{url_for('static', filename='css/style.css')}}" type="text/css" media="screen,projection" />
 ```
 
 It's important to state that layout or base file should contain the static structure. We can extend the header and footer to the rest of the templates along with other needed functionalities placed within the base file. 
 

## Used Extensions for App

[Flask](http://flask.pocoo.org/) - render_template ,redirect, request, url_for, flash, session, Blueprint

[Flask-Paginate](https://pythonhosted.org/Flask-paginate/)- Pagination, get_page_args, current_app

[Pymomgo](https://api.mongodb.com/python/current/)- PyMongo, pymongo


## Database setup

For my database am using Mongodb looped by the flask extension called Pymongo.
The database is hosted by mongodb's Mlab. 
Mongo db is a very popular database, classified as a non relation database. 
It is basically an unstructured database, in common terms one can say it dumps the data without much stiffness.
To setup a database on mlab, it will require registration 

The document panel which becomes where your entries are setted up must be in a json-like format.
```
{
"name": "ernest"
}
```
After setup, mongodb will generate a link for you, and this link will go into your flask app.
```
mongodb://<dbuser>:<dbpassword>@ds163103.mlab.com:63103/mytestdb
```
Now you will place your link inside the flask app.py.
Voila! Your database is ready.


## Testing

Usually python apps are required to use test automation, and the python unittest libraries can be employed for the job.
But at this time all test were done manually. This isn't very efficient, but my experience with unittests isn't sufficient. 
In my code i leave comments and remarks to explain as best to any reeader to understand my motive for which ever code i've written.



## Deployment To Git & Heroku

After committing to git with the appropriate messages, 
I'll now perform a git push to my GitHub Repo.
To create a new repository;
* first assign a repository name on github since thats what i'm using.
* write a short description of the site to be uploaded.
* You will either select to initialize your repository with a README.md file. (optional)
* create your repository.
* You will perform a git remote login
* And finally, git push -u origin master.

Heroku is a cloud platform that lets you build, deliver, monitor and scale apps.
To deploy to heroku, there are two critical steps to perform even before your final commit message.
We have the Procfile and the requirement.txt files. 
These are critical neccesities if you are deploying to heroku.
* ```heroku login ```- if u've created an account, u'll need to provide the email.
* ```heroku git:clone -a cook-book123 ```
* ``` cd cook-book123 ```
* ``` git push heroku master ```

#### [Live Version](https://ingrido.herokuapp.com/)

#### Web App Site Map:

1. Home page > Log in to have crude access.


## Versioning

 Git


## Author

Ernest Bruce Brown


## Media

* Google Images


## Acknowledgments

* Chris. Z






 
 


i used the page variable from flask paginate to redirect urls back to the pages they came from. 

to create my like button i utilized the $inc pymongo trick to get my counts and left as is.
to not over complicate my project i will stick to my increment feature only. 

To have access to crude activity users will have to add a user name to login. The edit and delete buttons will be deactivated 



since the scope of the project laid very little emphasies on front-end i have 
limited my screen tests to iphone6/6+/7/7+/8/8+,Galaxy s5 and desktops.
