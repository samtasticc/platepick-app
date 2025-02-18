# PlatePick - A Django CRUD App

<img width="864" alt="Screenshot 2025-02-18 at 3 04 17 PM" src="https://github.com/user-attachments/assets/9aa7405b-535f-4092-9ecd-97b18db230c8" />

## Project Description
> PlatePicks is the ultimate platform for food lovers to organize their dining experiences. Whether you're planning your next foodie adventure or reminiscing about past restaurant visits, PlatePicks makes it easy to add, manage, and track your favorite spots. Save restaurants you’ve discovered, rate and review the ones you’ve visited, and build a personalized dining wish list—all in one convenient place. With PlatePicks, every meal is a story waiting to be told!

## Getting Started
[PlatePick - GitHub Repo](https://github.com/samtasticc/platepick-app)

## Wire Frames
> 
![Sign_In_Landing_Page_(AAU) drawio](https://github.com/user-attachments/assets/159fa171-9d4b-434b-bc05-0aac1c07d81a)

![Index_Page_(AAU) drawio](https://github.com/user-attachments/assets/52e30570-438c-47a6-85ff-ffef78fe0572)

![Index_Page_(Restaurants)_(AAU) drawio](https://github.com/user-attachments/assets/b6240bac-4686-4816-95b1-699e8164caa7)

![Show_Page_(AAU) drawio](https://github.com/user-attachments/assets/cc858a8e-ce32-4f79-867e-1b59aa8111e1)

![New_Page_(AAU) drawio](https://github.com/user-attachments/assets/e453b18b-1d53-4bd5-8c64-e6d3afeabca1)


## Deployed Site
![Heroku Deployed](https://platepick-928b2bc524fd.herokuapp.com/)

## ERD
>
![Screenshot 2025-01-26 at 2 20 33 PM](https://github.com/user-attachments/assets/6ba6a10c-b52b-45ec-be44-9b8db24fe68b)


## User Stories
> 
* As a guest, I want to be able to sign up create an account so that I can access additional features like adding destinations and saving restaurants
* AAU, I should be able to sign into my account
* AAU, I should be able to log out of my account
* AAU, I want to be able to add destinations to hold restaurants in various locations that I want to visit, have listed, want to remember
*  AAU, I want to be able to add restaurant details so I can keep track of places I want to visit or have visited
*  AAU, I should be able to view a list destinations of all locations (city, state, country) that once clicked on, shows all restaurants in the specific locations I have added so that I can manage and review my restaurant entries without searching through entire restaurant list + categorize by cuisine type
*  AAU, I should be able to view a list of all restaurants in a specific destination I have added so that I can manage and review my entries without searching through multiple apps/ platforms
*  AAU, I want to categorize restaurant entries as "Want to Try" or "Visited" so that I can track which restaurants I've already been to and which ones I still want to try
*  AAU, I want to categorize restaurants by city, state and country so that I can easily find places when I travel to different places
*  AAU, I want to be able to edit the details of my restaurant entries to correct / update information
*  AAU, I want to have the ability to delete restaurant entries that I no longer would like to track within a specific destination
AAU, I want to have the ability to delete destination entries that I no longer would like to track


## Trello Board
>[PlatePick](https://trello.com/b/HnrnfJS2/unit-4-project-planning-platepick-django)

### MVP Goals
> 
* The app utilizes Django templates for rendering templates to users.
* PostgreSQL is used as the database management system.
* The app uses Django’s built-in session-based authentication.
* Authorization is implemented in the app. Guest users (those not signed in) should not be able to create, update, or delete data in the application or access functionality allowing those actions.
* The app has at least one data entity in addition to the User model. At least one entity must have a relationship with the User model.
* The app has full CRUD functionality.
* The app is deployed online so that the rest of the world can use it.

### Stretch Goals
> 
* AAU, I want to save and organize recipes that I already know, friends share with me or recipes I find on social media platforms
* AAU, I want to be able to access a restaurants menu to see if it meets my dietary requirements.
* AAU, I want to create a trip and add restaurants to it so that I can plan places I'm eating at before I get there
* Email requiremnt when signing up
* AAU, I want to be able to view other restaurant entries added by other users so that I can discover new places in whichever area that I'm visiting
* Users categorize restaurants (like “Brunch,” “Date Night,” “Street Food”)
* Mobile Friendly Application - Integration with Instagram/TikTok to make saving easier for the user
* Allow users ability to log in with social media accounts (Google, Facebook, TikTok, Instagram, etc)
* AAU, I would like to add a review of the restaurant so I can remember my experience
* AAU, I want a warning page/popup if I attempt to add a destination that already exists to confirm if I want to add the destination again.
* API for city, states, locations that auto-fill to ensure there are no double records/ misspellings

### Attributions
* [Django](https://docs.djangoproject.com/en/5.1/)
* [Django Get_Query](https://stackoverflow.com/questions/19707237/use-get-queryset-method-or-set-queryset-variable))
* [Dotenv](https://www.npmjs.com/package/dotenv)
* [Morgan](https://www.npmjs.com/package/morgan)
* [Bcrypt](https://www.npmjs.com/package/bcrypt)

* Image: "PlatePick"
    Created by: OpenAI
    Date: February 10th 2025

### Technologies Used
* Django
* PostgreSQL
* HTML
* CSS
* Django Authentication
* Dotenv
* Trello

