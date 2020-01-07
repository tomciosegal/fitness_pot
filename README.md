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

1. The website consists of 4 pages:

   [i]   It opens with a **Home** page which:
         - Gives an introduction to the site 
         - Gives user instructions what you can find the site
         - The home page designed to hold six recipes per page. In order to check more recipes you click next or prevoius button
         - When loggen in user will see all recipes and also 'My Recipe' button will apear.
                
   [ii]  The Recipes List page:
   
         - Displays a card for each recipe in the country / category, sorted by country / category
         - The recipe card shows an image, meal category, preperation time, how many serves and a short introduction to the recipe
         - Each recipe has a view recipe button that will bring the user to the recipe details
            
   [iii] The Recipes Details page:
   
         -  Displays the selected recipe's details. If this page is called when the user is viewing their own 
            recipes, it allows them to edit or delete the recipe. Only users recipes can be edited or deleted.
            Buttons visible on users recipes only.

   [iv]  The 'My Recipes' page located in navbar, allows the user to view, their existing recipes.
         Button only visible when logged in. 
   

2. The select category dropdown will allow user to browse recipes by categories(breakfast,dinner dessert, drinks, vegan)
    In that dropdown you can display 'All recipes' at all time.
3. The nav link selected by the user will change color to green, so that the user remembers which selection they have made
4. When the country dropdown is enabled, its selection will be changed to green to highlight the user's selection
5. The website displays 6 recipes per page and allows to view another recipes by clicking on 'Next' button

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

## **7.1 Code Validation

- I used the [W3C HTML Validator tool](https://validator.w3.org/#validate_by_input) to validate my HTML code.
    - The W3C Validator tool doesn't recognise the Jinja templating, which has resulted in it showing a lot of errors in relation to the Jinja code. However, all other code is validating fine.
- I used the [W3C CSS Validator tool](https://jigsaw.w3.org/css-validator/#validate_by_input) to validate my CSS code.
- I used the [Pep8 Online tool](http://pep8online.com/) to validate my Python syntax.

## ** 7.2 Pagination Test (manual)

1. Test the pagination page by page and verify that the same amoutn of recipes are always appearing on the same page number
2. Test the pagination next / previous page functionality and verify that the same recipes are always appearing on the same page number
3. Test the 'next' button to check if disapear on last page, and 'prevoius' button if disapear on first page.
