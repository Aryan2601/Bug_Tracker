#Bug Tracker  :confused:

## What is Bug Tracker :question: :question:


####:arrow_right: This is Not a actual bug tracker as by name this is a person work loading and he will be uploading his work after loggin in using google.

##Steps to run Server :thumbsup: :thumbsup:

###:pushpin:First open terminal then go to django_project folder.

###:pushpin:Then run command python3 manage.py runserver.

###:pushpin:Then copy the url link and run it in your browser.

###:pushpin:Now You are  at main site.


#:arrow_down: :arrow_down: :arrow_down:

##Features  :smile: :smile:


###:pushpin: You can Upload and make a Folder With Giving name of the your folder
![image](/home/aryan/Pictures/Screenshot from 2020-03-04 23-38-33.png)

###:pushpin: You can also set the profile pic of your folder


###:pushpin: You can click on Download button and look at your file details


###:pushpin: You can Upload Your File in any format


###:pushpin: You can also delete the folder created


## TO add a Oauth service provider do the following ##


#### :pushpin:Djando framework offers various sign in options google,facebook,github,...etc.
#### :pushpin:In this project i will be signing in through google so i will tell about it.
#### :pushpin:add some things to installed apps in settings of the project
####  :pushpin: 'allauth',
####  :pushpin:  'allauth.account',
####  :pushpin:  'allauth.socialaccount',
####   :pushpin: 'allauth.socialaccount.providers.google',
####   :pushpin: 'login',
####:pushpin:SITE_ID=1
####:pushpin:LOGIN_REDIRECT_URL='http://127.0.0.1:8000/polls/'
####:pushpin: After adding all this you when you runserver you will get a socialapp sections
####:pushpin: Now add that provider as google and all the details required name the url as localhost:8000
####:pushpin: Now get client id and secret id from https://console.developers.google.com/ .Here i will not be mentioning my client id and 
####:pushpin:secret id as it might be used in some undesirable manner if needed ask me for it personally.
####:pushpin: Add  client id and secret id .
####:pushpin: Now LOGIN_REDIRECT_URL='http://127.0.0.1:8000/upload/' is for redirecting you to the page which should appear just after you google sign. The above is what is my redirect page.
####:pushpin: This is it we are now able to sign in through google into our site.

##How to create an app:-
```Python manage.py startapp (appname)```

##Two http methods are as under:-
####:pushpin:post and get
####:pushpin:Get is for fetching the data from server
####:pushpin:Post is for adding new data to server

##To create superuser:-
####:pushpin:Python manage.py createsuperuser

##To start a project:-

####:pushpin:Django-admin startproject mysite

