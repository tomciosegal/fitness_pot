# FITNESS POT
![alt text](/static/img/some_recipies/dumbell.jpg "Fitness Pot")

## **1.1 PURPOSE**
The purpose of [Fitness Pot](https://fitness-pot.herokuapp.com/) is to host healthy recipes for people who want to
who like to eat delicious and nutrition food. The primary target audience are people doing gym 
and lead a healthy lifestyle, but after all i seems like there is a wast comunity looking for this sort of recipies.

## **2.2 WEBSITE REQUIREMENTS**

### **2.2.1 High Level Requirements**

The website will:

1. Display recipes entered by users in 5 categgories.
2. Recipes are divided into the following categories - Breakfast, Dinner, Drinks, Dessert,Vegan
3. Display the recipe list category order
4. Allow users to browse the site and filter by category,and user
5. Allow users to add, edit, and delete their own recipes

### **2.2.2 Future Enhancements**
1. Allow users to comment on other users recipes
2. Allows users to make suggestions or improvements
3. Allows users to request feedback on recipes they've entered
4. Allow users to like / dislike recipes
5. Allow users to give likes, share,tweet
6. Allow visitor to browse by allergens
7.Let user give comments about the dish under recipies

## **2.2.3 USER STORIES** ##
-   New to the website i am looking for healthy meals
-	As user, I would like to check out different recipes
-	As viewer , I would like to browse recipes by different categories
-	As user, I would like to add my recipes
-	I want to be able  to edit existing recipes on webpage
-	As user, I would like to delete existing receipes on webpage
-	New to the website i am looking to register on the webpage
-	As a user, I would like to login to the webpage
-	My goal was to create user friendly , easily accessible, data driven web application
-   I enjoy healthy nutritious meals that are so important
-   As new user I have many good healthy recipes I would like to share with people who would appreciate them.

# **3. FEATURES**
## **3.1 FITNESS POT**

1. The website consists of 6 pages:

   [i]   It opens with a **Home** page which:
         - Gives an introduction to the site 
         - Gives user instructions what you can find the site
         - The home page designed to hold six recipes per page. In order to check more recipes you click next or prevoius button
         - When loggen in user will see all recipes and also 'My Recipe' button will apear.
                
   [ii]  The Recipes List page:
   
         - Displays a card for each recipe in the cooking time, how many serves, category
         - The recipe card shows an image, meal category, preperation time, how many serves and a short introduction to the recipe
         - Each recipe has a view recipe button that will bring the user to the recipe details
            
   [iii] The Recipes Details page:
   
         -  Displays the selected recipe's details. If this page is called when the user is viewing their own 
            recipes, it allows them to edit or delete the recipe. Only users recipes can be edited or deleted.
            Buttons visible on users recipes only.

   [iv]  The 'My Recipes' page located in navbar, allows the user to view, edit, delete their existing recipes.
         Button only visible when logged in. 
   

2. The select category dropdown will allow user to browse recipes by categories(breakfast,dinner dessert, drinks, vegan)
    In that dropdown you can display 'All recipes' at all time.
3. The nav link selected by the user will change color to green, so that the user remembers which selection they have made
4. When the country dropdown is enabled, its selection will be changed to green to highlight the user's selection
5. The website displays 6 recipes per page and allows to view another recipes by clicking on 'Next' button
6.[Wireframes](https://github.com/tomciosegal/fitness_pot/tree/master/wireframes) 
for the dashboard can be found in separate folder of the repository.

## **3.7 OVERVIEW OF DATABASES **
-   title: recipe title displayed on recipe list & details   
-   category: allows filtering by category
-   image: Image file name. Prefixed with /static/img/some_recipies to display on recipe list & details.<br/>
    for recipies added by users, URL needs to be provided
-   cooking_time: holds time for preperation
-   serves: tells for how many people is recipe created
-   author: hold the recipe owner
-   ingredients: displayed on recipe details (list of items needed to create a dish)
-   instructions: displayed on recipe details (list of steps needed to prepare dish)
-   user_email: will be used to identify user when login

# **4. TECHNOLOGIES USED**

- [**HTML**](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
    - The project uses **HTML** to create the basic elements and content of my app.
- [**CSS**](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3)
    - The project uses **CSS** to apply the custom styles created with **SCSS** to my app. The base.html file is linked directly to the main.min.css stylesheet.
- [**Bootstrap**](https://getbootstrap.com/)
    - The project uses the **Bootstrap** framework to add a responsive grid system, prebuilt components, plugins built on jQuery, and Bootstrap styles to my app, before adding my custom styles.
- [**jQuery**](https://jquery.com)
    - The project uses **jQuery** as the primary JavaScript functionality. This is both the standard jQuery that is built with Materialize components, and my custom jQuery used in my script.js file.
- [**Python**](https://www.python.org/)
    - The project uses **Python** as the back-end programming language for my app.
- [**PyMongo**](https://api.mongodb.com/python/current/)
    - The project uses **PyMongo** as the Python API for MongoDB. This API enables linking the data from the back-end database to the front-end app.
- [**Flask**](https://flask.palletsprojects.com/en/1.0.x/)
    - The project uses **Flask**, which is a Python microframework.
- [**Jinja**](https://jinja.palletsprojects.com/en/2.10.x/)
    - The project uses **Jinja** for templating with Flask in the HTML code. I used **Jinja** to simplify my HTML code, avoid repetition, and allow simpler linking of the back-end to the front-end.
- [**MongoDB**](https://cloud.mongodb.com/)
    - The project uses **MongoDB** to store the database in the cloud. The information displayed in the front-end app is pulled from the database store.
- [**Google Fonts**](https://fonts.google.com/)
    - The project uses **Google Fonts** to style the text and suit my chosen theme. The brand logo uses the *_Dancing Script_* font and the rest of the site uses the *_Roboto_* font.
- [**Font Awesome**](https://fontawesome.com/)
    - The project uses **Font Awesome** for the various icons in my app.
- [**Gitpod**](https://www.gitpod.io/)
    - I've used **Gitpod** as the development environment to write the code for my website.

# **5. Mockups

# **6. Version Control

- [**Git**](https://git-scm.com/)
    - I've used **Git** as a version control system to regularly add and commit changes made to project in Gitpod, before pushing them to GitHub.
- [**GitHub**](https://github.com/)
    - I've used **GitHub** as a remote repository to push and store the committed changes to my project from Git.

# **6.1 Hosting

- [**Heroku**](https://www.heroku.com/)
    - I've used **Heroku** as the hosting platform to deploy my app.

# **7. TESTING**

I used Google Chrome's Development tools to constantly test each change that I<br/> 
made to my project and to ensure that it appeared in the desired way on different screen sizes. <br/>
I also tested my app on different screen sizes (mobile, tablet and desktop) to ensure <br/>
it appeared in the desired way on different devices.
I also wrote automated test for validators.py file. Test is located in tests.py file.

## **7.1 Code Validation

- I used the [W3C HTML Validator tool](https://validator.w3.org/#validate_by_input) to validate my HTML code.
    - The W3C Validator tool doesn't recognise the Jinja templating, which has resulted in it showing a lot of errors in relation to the Jinja code. However, all other code is validating fine.
- I used the [W3C CSS Validator tool](https://jigsaw.w3.org/css-validator/#validate_by_input) to validate my CSS code.
- I used the [Pep8 Online tool](http://pep8online.com/) to validate my Python syntax.

## ** 7.2 Pagination Test (manual)

1. Test the pagination page by page and verify that the same amoutn of recipes are always appearing on the same page number
2. Test the pagination next / previous page functionality and verify that the same recipes are always appearing on the same page number
3. Test the 'next' button to check if disapear on last page, and 'prevoius' button if disapear on first page.

# 8. DEPLOYMENT

## 8.1 DEPLOYING FROM GITHUB 

1. Log onto Github
2. Select the respository you want to deploy
3. On the repository page, click on "Settings" and scroll down to "Github Pages"
4. From the "Source" dropdown select "Master Branch" and click "Save"
5. The message "Your site is ready to be published at https://username.github.io/Repository Name/" will 
   appear under Github Pages

## 8.2 CLONING FROM GITHUB 

1. Follow this link to my [Project Repository on Github](https://github.com/tomciosegal/fitness_pot)
2. On the repository page click "Clone or Download"
3. In the Clone with HTTPs section, copy the clone URL for the repository.
4. In your local IDE open Git Bash.
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type git clone, and then paste the URL you copied in Step 3 - 
    "git clone https://kittymcdonagh.github.io/Third-Milestone-Project/"
7. Press enter and your local clone will be created.
 

## 8.3 DEPLOYING TO HEROKU 

1. Type 'heroku ps:scale web=1' into bash terminal
2. Create 'requirements.txt' (sudo pip3 freeze --local > requirements.txt)
3. Create a 'Procfile' (echo web: python run.py > Procfile)
4. Log onto Heroku.com
5. Click on Create New App
6. Enter App Name (global-irish-cafe)
7. Click on Create App
8. Go to the CLI and type "sudo snap install --classic heroku"
9. Type "Heroku login --interactive"
10. Go to Deploy (under your app on heroku.com) and under Create New Repository copy the command:
11  "heroku git:remote -a global-irish-café"
12. Copy this into the bash terminal
13. Go to heroku website dashboard for your app and click Settings
14. Copy the heroku git url (https://git.heroku.com/fitness-pot.git)
15. In the bash terminal type "git remote add http://fitness-pot.herokuapp.com/"
16. Type "git push -u heroku master"
17. In the app dashboard, click Settings
18. Click on Reveal Config Vars
19. Enter "IP" in first key box. Enter "0.0.0.0" into corressponding value box. Click Add
20. Enter "PORT" into 2nd key box, enter "5000" into corresponding value box. Click add.
21. Enter "MONGO_URI" in key box, enter mongodb details in value box
22. Enter "MONGO_URI" in key box, enter 
   mongodb+srv://tomciosegal:cucharec7164@myfirstcluster-nbawd.mongodb.net/fitness_pot?retryWrites=true&w=majority
22. Enter "SECRET" into the key box, enter the secret key into the value box.

# **9. CREDITS**

## **9.1 RECIPES & PHOTOGRAPHS**

The photos and recipes have been copied from the following websites:
- [Healthy Fitness Meals](https://healthyfitnessmeals.com/) - all recipes and meal images
- [Pixabay](https://pixabay.com/) - deafault image if none added to recipe

## **9.2 Content

Git Branch - https://www.atlassian.com/git/tutorials/using-branches 


## **10. Acknowledgements

- I received inspiration for the style of my project from [Healthy Kitchen](https://healthyfitnessmeals.com/)
- Thanks to everybody on SLACK that help me when I was stuck and needed assistance. Thanks Tutors aswell. They help me to debug my Python code.
- Big thanks to my mentor Ignatius Ukwuoma, for his feedback on my project's scope, design and so many useful information shared.
- And finally thanks to my wife who gave me precious time so I can work on my project, shey is biggest support I can imagine.

### Disclaimer

This project is for educational purposes only.