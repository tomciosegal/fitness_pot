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

## **2.2.2 USER STORIES** ##
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

1. The website consists of 5 pages:

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
|------------------------------------------------------------------------------------------------------|
|Technologies  Used           |Sourced From                                                            |
|-----------------------------|------------------------------------------------------------------------|
|HTML                         |[w3schools](https://www.w3schools.com/)                                 |
|CSS                          |[w3schools](https://www.w3schools.com/)                                 |
|Javascript                   |[developer mozilla](https://developer.mozilla.org/en-US/docs/Web/JavaScript)                                                                        |
|Jquery                       |[jQuery website](https://code.jquery.com/)                              |
|Bootstrap                    |[Bootstrap website](https://getbootstrap.com/)                          |
|Font Awesome                 |[Font Awesome website](https://fontawesome.com/)                        |
|Google fonts                 |[Google fonts](https://fonts.google.com/)                               |
|AutoPrefixer                 |[Autoprefixer website](https://autoprefixer.github.io/)                 |
|Python                       |[Python docs](https://docs.python.org/3/library/stdtypes.html#range)    |
|mongodb database             |[mongodb website](https://www.mongodb.com/)                             |
|------------------------------------------------------------------------------------------------------|
