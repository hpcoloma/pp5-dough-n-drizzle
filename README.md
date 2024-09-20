# Dougn n Drizzle

AM I RESPONSIVE PHOTO HERE

# Table of Contents
- [Project Introduction](#project-introduction)
  - [Dough n Drizzle]
  - [Link to Live Project](#link-to-live-project)
  - [Objective](#objective)
- [UX/UI Design](#uxui)
  - [The Strategy Plane](#the-strategy-plane)
  - [The Scope Plane](#the-scope-plane)
  - [The Skeleton Plane](#the-skeleton-plane)
  - [The Structure Plane](#the-structure-plane)
  - [The Surface Plane](#the-surface-plane)
- [Features](#features)
- [Future Enhancements](#future-enhancements)
- [Testing](#testing)
- [Agile Development](#agile-development)
- [Bugs and Potential Issue](#bugs-and-potential-issues)
- [Technologies and Languages used](#technologies-and-language)
- [Developement](#development)
- [Deployment on Heroku](#deployment)
- [Credits](#credits)
- [Acknowledgements](#acknowledgement)


## Project Introduction

Text goes here

The project will include front-end development with HTML, CSS, and JavaScript, and back-end development using Python and Django.

### [Link to Live project](https://pp4-techtackles-by-hc-ed362e72006b.herokuapp.com/)

### Objective
The primary objective of Dough n Drizzle


This application will be designed using a combination of front-end and back-end technologies, including HTML, CSS, JavaScript, Python, and Django

## UX/UI Design
### The Strategy Plane

#### VISION


#### OBJECTIVES

#### USER NEEDS


### The Scope Plane 
#### FEATURES


#### CONTENT REQUIREMENTS:


#### FUNCTIONAL SPECIFICATIONS


#### USER STORIES


- **MoSCoW Prioritization**

  - **Must Have:** 
  - **Should Have:** 
  - **Could Have:**
  - **Won't Have:** 

- **As a User:**
  

- **As a**
 
- **As an admin:**
  

### The Skeleton Plane 
#### LAYOUT AND WIREFRAME STRUCTURE

- **Home Page:**
TEXT HERE
PHOTO HERE

- **Login Page:**
TEXT HERE
PHOTO HERE

- **Register Page:**
 TEXT HERE
PHOTO HERE

- **User Dashboard (after login):**
 TEXT HERE
PHOTO HERE


**WIREFRAMES**

- **Mobile and Tablet Wireframes:**

**ENTITY RELATIONSHIP MODEL**



- **ERD Diagram**

  photo here

- **Key Points**
  - **User:**
    - Has a one-to-one relationship with Profile.
    - Has a one-to-many relationship with Ticket.
    - Has a one-to-many relationship with Comment.

  - **Profile:**
    - Linked to User with a one-to-one relationship.

 
### The Structure Plane

#### INFORMATION ARCHITECTURE

- **Global Navigation:**
  

#### CONTENT ORGANIZATION



#### INTERFACE ELEMENTS:
- **Forms:**
  - **User Registration Form:** Input validation for email, username, password and password confirmation fields
  - **Login Form:** Input validation for email and password fields
  - **Ticket Form:** Input validation for subject and description fields and status (hidden field or dropdown for tech support).
  - **Comment Form:**  Input validation for comment text

- **Buttons:**
  - **Primary** buttons for actions like "Register", "Log In", "Logout", "Create Ticket", "Submit", "Edit", "Delete", "Next", "Last", "First", and "Previous".
  - **Secondary** buttons for action like "Cancel", "Close", and "Save Changes".

- **Tables:**
  - **Ticket List:** Columns for Ticket ID, Status, Subject, Created On (date only), and User. Clickable rows to view ticket details, pagination.
  - **Ticket List for Mobile:** Columns for Ticket ID and Status.

- **Modals:**
  - For editing comments to avoid navigating away from the ticket detail page. Opens when the "Edit" button is clicked on a comment, contains the comment text pre-filled, and has a save button to update the comment
  - For deleting ticket and comments.

- **Alerts:**
  - For success and error messages, displayed using Bootstrap alerts for actions like creating tickets, adding comments, updating tickets, etc..
  - For Access Denied and 404 Error using a customised page.

#### INTERACTION DESIGN:
- **Ticket Creation:**
  - User fills out the ticket form and submits.
  - System validates input and creates a ticket.
  - Success message is shown.
  - System will display newly created ticket with an option to edit/delete.

- **Editing Ticket:**
  - User clicks "Edit" on a ticket
  - Redirect to a page to update ticket with the text pre-filled.
  - User updates the ticket with the option to update status if admin/staff and then save changes
  - System validates and updates the ticket.
  - Success message is shown, and the updated ticket is displayed.

- **Commenting:**
  - User adds a comment via the form.
  - System validates input and adds the comment.
  - Comment appears below the ticket details with an option to edit/delete (if allowed).

- **Editing Comments:**
  - User clicks "Edit" on a comment.
  - Modal opens with the comment text pre-filled.
  - User updates the comment and saves changes.
  - System validates and updates the comment.
  - Success message is shown, and the updated comment is displayed.

### The Surface Plane
#### COLOUR SCHEME
![Colour Palette](static/images/colourpalette.jpeg)
  - **Primary Colors:**
    - Background Color: #ffffff (White) for general background
    - Primary Button Background: #3864f5 (blue)
    - Footer Background: #6c757d (dark grey)
  - **Secondary Colors:**
    - Navbar Background: #fafafa (light grey)
    - Navbar Text: #666665 (grey)
    - Card Background: rgba(255, 255, 255, 0.8) (semi-transparent white)
    - Table Header Background: #6b7e9b (dark grey-blue)
  - **Text Colors:**
    - Primary Text: #000000 (Black) for high contrast and readability
    - Secondary Text: #6c757d (Dark Grey) for less prominent text
    - Link Text: #3864f5 (blue)
![Grid Contrast](static/images/color_gridcontrast.PNG)

  - **Buttons:**
    - Buttons:
      - Primary Button (e.g., Sign Up, Edit):
      - Background Color: #3864f5
      - Text Color: #fff
      - Padding: 10px 20px
      - Border Radius: 5px
  - **Alerts and Modals:**
    - Alerts:
      - Background Color: Varies based on message type (e.g., success, danger)
      - Text Color: White
    - Modals:
      - Text Color: White
      - Body Background: #ffffff (white)
  - **Footer:**
    - Background Color: #6c757d
    - Text Color: #ffffff
    - Padding: 1em
    - Text Alignment: Center
    - Social Media Icons:
      - Color: White
      - Spacing: 1em
  - **Responsive Design:**
    - Mobile Views:
      - Welcome Card Width: 90vw
      - Hide Mobile Elements: Class .hide-mobile used to hide elements on smaller screens

#### TYPOGRAPHY
- Primary Font: Titillium Web
  - Used for headers, body text, and UI elements
    - Provides a clean, modern look suitable for various UI components
    - Font Family: "Titillium Web", sans-serif
    - Headings:
      - Font Weight: 600 to 700
      - Size: Varies (e.g., h1: 2.5em, h2: 2em)
    - Body Text:
        - Font Weight: 400
        - Size: 1em
    - Buttons and Links:
        - Font Weight: 600
        - Size: 1em

#### IMAGES
- **[Background]('https://t4.ftcdn.net/jpg/04/80/76/81/360_F_480768188_1kpegKWaXFQ5LwTwsQ6MwARFdsaxV1UU.jpg')** - From Adobe Stock.
![Background for Home Page](static/images/homepage_background.jpg)
- **Logo** - Best viewed with white background. Image is a PNG with transaparent background. I designed this logo usinf Adobe Photoshop and put an icon that resembles an octopus. The logo name that sounds like "tentacles".
![Logo](static/images/techtackles_logo.png)

## Features
### Home Page
![Home Page](static/images/site_homepage.PNG)

### Navigation
![Navigation Bar](static/images/site_navigationbar.PNG)

### Responsive Nav
![Responsive Nav](static/images/site_responsivenav.PNG)

### Create Ticket
![Create Ticket](static/images/site_createticket.PNG)

### Ticket List
Ticket List view with filter status functionality
![Ticket List](static/images/site_filter.png)

### Ticket Detail

![Ticket Detail](static/images/site_ticketdetailview.PNG)

### Ticket Delete
![Ticket Delete](static/images/site_ticketdelete.png)

### Ticket Edit
![Ticket Edit](static/images/site_ticketupdate.PNG)
### Comment Edit
![Comment Edit](static/images/site_commentedit.png)
### Comment Delete
![Comment Delete](static/images/site_commentdelete.png)
### Access Denied
![Access Denied](static/images/site_access_denied.PNG)
### 404! Error
![Error Page](static/images/site_404.PNG)

## Future Enhancements
It is essential to plan for the future by considering potential features that can enhance Tech Tackle's functionality, usability and overall user experience. To remain competitive and adaptable to the changing needs of users, below are future feature considerations thta can be integrated to ensure continued growth of this application.

- **Customizable User Profiles**
  - **Feature:** Allow users to customize their profiles with additional information.
  - **Benefits:** Enhances user engagement and personalization. 
  - **Example:** Users can upload profile pictures, add bio information, company roles and set notification preferences.
- **Advanced Search and Filtering**
  - **Feature:** Implement advanced search and filtering options for tickets.
  - **Benefits:** Users can easily find specific tickets based on criteria like date range, status, user, keywords, etc.
  - **Example:** A search bar with dropdown filters for status, user, date 
  range, and keywords.
- **Notification System**
  - **Feature:** Develop a notification system for ticket updates.
  - **Benefits:** Users and staff will receive real-time notifications for ticket status changes, new comments, or assigned tickets.
  - **Example:** Email notifications, in-app notifications, or push notifications.
- **Analytics Dashboard**
  - **Feature:** Create an analytics dashboard to display ticket statistics.
  - **Benefits:** Provides insights into ticket trends, user activity, and system performance.
  - **Example:** Charts and graphs showing the number of open tickets, average resolution time, most common issues, etc.
- **Mobile App Integration**
  - **Feature:** Develop a mobile app or ensure the web application is fully responsive.
  - **Benefits:** Increases accessibility, allowing users to manage tickets on the go.
  - **Example:** A mobile-friendly interface or dedicated mobile app for both Android and iOS platforms.
- **Ticket Assignment Automation**
  - **Feature:** Automate ticket assignment based on predefined rules.
  - **Benefits:** Reduces manual workload and ensures tickets are assigned to the appropriate staff member.
  - **Example:** Automatically assign tickets based on the issue type, department, or staff availability.
- **Feedback and Rating System**
  - **Feature:** Implement a feedback and rating system for resolved tickets.
  - **Benefits:** Gathers user feedback on support quality and identifies areas for improvement.
  - **Example:** After ticket resolution, users can rate their experience and leave feedback.
- **Knowledge Base Integration**
  - **Feature:** Integrate a knowledge base where users can find solutions to common issues.
  - **Benefits:** Reduces the number of support tickets by providing self-help resources.
  - **Example:** Articles, FAQs, and how-to guides accessible within the platform.


## Testing
  - Complete Testing documentation can be found [here](TESTING.md)
## Agile Development

To ensure the TECH TACKLES IT Support Ticketing System is developed effectively and efficiently, I followed an agile approach. This involved iterative development cycles (sprints) where I continuously build, test, and refine the system. Here's how I can break down the development process into iterations:

#### Iteration 0: Planning and Setup
- Goals:
  - Define project objectives, user stories, and initial requirements.
  - Set up the development environment.
  - Create initial project structure and repository.

- Tasks:
  - Create and initialize a Git repository.
  - Set up Django project and application.
  - Create database and connect the database.
  - Create initial models for User, Ticket, and Comment.
  - Configure Django AllAuth for user authentication.
  - Set up static files and templates structure.

#### Iteration 1: User Authentication and Role Management
- Goals:
  - Implement user authentication.
  - Define and implement user roles (Admin, User, Tech Support).
- Tasks:
  - Implement login, signup, and logout functionality using Django AllAuth.
  - Create user roles and permissions.
  - Implement user management in the admin dashboard.
  - Test user authentication and role management.
- Deliverables:
  - Functional user authentication system.
  - User roles and permissions implemented.
  - Basic admin interface for user management.

#### Iteration 2: Ticket Management
- Goals:
  - Implement ticket creation, viewing, and listing.
- Tasks:
  - Create forms for ticket creation and updating.
  - Implement views for creating, listing, and viewing tickets.
  - Implement ticket status (Open, In Progress, Closed).
  - Test ticket creation and viewing functionalities.
- Deliverables:
  - Functional ticket creation form.
  - List view of tickets with status filters.
  - Detail view for individual tickets.

#### Iteration 3: Commenting and Interaction
- Goals:
  - Implement ticket commenting system.
  - Ensure interaction between users and tech support through comments.
- Tasks:
  - Create comment model and forms.
  - Implement views for adding and viewing comments.
  - Restrict comment access based on user roles.
  - Test commenting functionality.
- Deliverables:
  - Functional commenting system.
  - Users can add comments to their own tickets.
  - Tech support can add comments to all tickets.

#### Iteration 4: Admin and Tech Support Features
- Goals:
  - Implement additional features for admin and tech support users.
- Tasks:
  - Allow tech support to edit and delete opena nd in progress tickets.
  - Test admin and tech support features.
- Deliverables:
  - Admin and tech support can manage tickets.
  - Admin django  for user and ticket management.

#### Iteration 5: Testing and Bug Fixing
- Goals:
  - Ensure the system is fully functional and bug-free.
- Tasks:
  - Perform comprehensive testing of all features.
  - Fix any bugs or issues found during testing.
  - Ensure all user stories are met.
- Deliverables:
  - Fully tested and functional IT support ticketing system.
  - Documentation for testing procedures and results.

#### Iteration 6: Deployment and Documentation
- Goals:
  - Deploy the application to a production environment.
  - Create comprehensive documentation.
- Tasks:
  - Set up and configure the production environment.
  - Deploy the application.
  - Write detailed documentation for installation, usage, and contribution.
  - Create a README file with all necessary information.
- Deliverables:
  - Deployed application.
  - Comprehensive documentation and README.
#### Iteration 8: Feedback and Iteration
- Goals:
  - Get feedback from mentor and potential user.
  - Implement improvements based on feedback.
- Tasks:
  - Prioritize and implement changes based on feedback.
  - Plan for future iterations or updates.
- Deliverables:
  - Updated application with improvements based on feedback.

## Bugs and Potential issues
- Bootstrap CSS and JavaScript Loading Issues
  - Problem: The application has encountered issues loading Bootstrap CSS and JavaScript files correctly, resulting in error like:
    
    'Uncaught TypeError: Cannot read properties of undefined (reading 'backdrop').'
  - Steps taken to Resolve:
    - Checked the CDN URL directly in the browser by verifying that the url  "https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/css/bootstrap.min.css" displays raw CSS instead of HTM or error page. URL is accessible.
    - Verified Integrity attribute. I used the [SRI Hash Generator](https://www.srihash.org/) to verify the hash.
    - Checked Cross-Origin Attribute: Confirmed that the crossorigin="anonymous" attribute is used correctly, which is necessary for CORS with CDNs.
    - Attempted to Use Local Bootstrap File:
      - Downloaded the Bootstrap CSS file and placed it in the static folder of the project. - Updated the URL paths in the template accordingly.
      - Ran python manage.py collectstatic to ensure the static files are collected and served properly.
      - Encountered issues with local file serving, potentially due to misconfiguration or incorrect file paths.

![Bootstrap Error](static/images/bugs_js.PNG)
  - Resolution: Despite the above steps taken, error on the browser still appearing. Conclusion is that this is down to the Bootstrap library that I dont have control with.

## Technologies and Language
Tech Tackles is built using a combination of modern technologies and programming languages to ensure a robust and efficient application. Below is a list of the primary technologies and languages used in this project:
### Frontend
  - **HTML5:** For structuring the web pages and content.
  - **CSS3:** For styling the web pages, including layout, design, and responsiveness.
  - **JavaScript:** For interactive features and client-side logic.
      - **jQuery:** For simplified DOM manipulation and event handling.
      - **Bootstrap:** For responsive design and pre-styled components.
### Backend
  - **Python:** The main programming language used for backend development.
  - **Django:** A high-level Python web framework that encourages rapid development and clean, pragmatic design.
  - **Django REST Framework:** For building RESTful APIs.
### Database
  - **SQLite:** The default database used for development and testing
  - **PostgreSQL:** Used in production..
### Version Control
 - **GitHub:** For hosting the code repository and facilitating collaboration.
### Deployment
  - ***Heroku:** For deploying the web application in a scalable and reliable manner.
  - **Gunicorn:** A Python WSGI HTTP Server for running the application on Heroku.
### Additional Tools and Libraries
  - **Crispy Forms:** For enhancing the rendering of Django forms.
  - **Cloudinary:** For managing media files like images.
  - **Font Awesome:** For scalable vector icons.
  - **Moment.js:** For parsing, validating, manipulating, and displaying dates and times in JavaScript.

## Development
This application was develop in Code Institute Gitpod, hosted in GitHub and deployed in Heroku.
## Deployment on Heroku
The site was deployed via Heroku.
### Project Deployment
To deploy the project through Heroku:
- Login to Heroku
- Create a new Heroku application by going to the Dashboard and select New and Create New App
- Give your app a name (pp4-techtackles-by-hc) and choose the region nearest to you (Europe). This will create an app in Heroku and will redirect you to the Deploy tab.
- On the Deploy tab, connect your Github and search for your repository.
- Manually deploy the main branch of this GitHub repo.
- On the Resources tab, ensure eco-dyno is enabled and delete any Postgres database Add-on.
- Add the KEY - DISABLE_COLLECTSTATIC with the Value - 1 to the config vars, this must be removed before final deployment.
- Add the database to the app by going to Settings tab, under Config vars add the following:
  Key= Database_URL
  Value = your postgres url
- In your Django app, make sure you install gunicorn~=20.1 and freeze it to the requirements.txt file.
- Create a new file env.py on the root directory and import the os library and set the environment variable for the DATABASE_URL the same as your settings in Heroku.
- Add SECRET_KEY using the os.environ in the env.py and add the same SECRET_KEY on the settings tab in Heroku under Config vars
- In the settings.py file within the django app, import Path from pathlib, import os and import dj_database_url
- Insert the line if os.path.isfile("env.py"): import env
- Update the default SECRET_KEY that Django has on settings.py and replace it with SECRET_KEY = os.environ.get('SECRET_KEY')
- On settings.py, replace the database section with DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
}
- Settings.py file - add the STATIC files settings - the url, storage path, directory path, root path, media url and default file storage path.
- Link the file to the templates directory in Heroku TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
- Change the templates directory to TEMPLATES_DIR - 'DIRS': [TEMPLATES_DIR]
- Add Heroku to the ALLOWED_HOSTS list the format will be the app name given in Heroku when creating the app followed by .herokuapp.com
- Create a new file on the top level directory - Procfile
- Add web: gunicorn projectname.wsgi in Procfile.
- During production, do add, commit and push changes to your Github repo.
- In Heroku, under Deploy tab, click Deploy Branch.
- Watch out for any errors.
- Heroku will now build the app for you. Once it has completed the build process you will see a 'Your App Was Successfully Deployed' message and a link to the app to visit the live site.

### Forking your repository
To fork a repository on GitHub, follow these steps:

1. Navigate to the Repository: Go to the GitHub repository you want to fork. You can do this by entering the repository URL in your browser or by searching for the repository on GitHub.

2. Find the "Fork" Button: On the repository page, you'll see a button labeled "Fork" in the top right corner of the page, next to the "Star" and "Watch" buttons. Click on the "Fork" button.

3. Choose where to Fork: GitHub will prompt you to choose where you want to fork the repository. You can fork it to your personal GitHub account or to any organizations you're a member of. Select the desired location.

4. Wait for the Fork to Complete: GitHub will create a copy of the repository in your account or organization. Depending on the size of the repository and the current server load, this process may take a few moments.

5. Access Your Forked Repository: Once the forking process is complete, you'll be redirected to your forked copy of the repository. You can now clone the repository to your local machine, make changes, and push them to your fork.

6. Keep Your Fork Synced: If you forked a repository to contribute changes back to the original repository, you may want to keep your fork up-to-date with the original repository. You can do this by configuring an "upstream" remote and pulling changes from it periodically.

That's it! You've successfully forked a repository on GitHub. You can now start working with the code in your fork, making changes, and contributing back to the original repository through pull requests.

### Clone Repository
Cloning a repository from GitHub allows you to copy a remote repository to your local machine. To clone a repository from GitHub to your local machine, follow these steps:

1. Find the Repository: Go to the GitHub repository you want to clone. You can do this by entering the repository URL in your browser or by searching for the repository on GitHub.

2. Copy the Repository URL: On the repository page, click on the "Code" button. This will reveal a URL for the repository. Click on the clipboard icon to copy the URL to your clipboard.

3. Open Terminal (or Command Prompt): Open your terminal or command prompt on your local machine. You can usually find it in your applications or by searching for "Terminal" (on macOS and Linux) or "Command Prompt" (on Windows).

4. Navigate to the Directory Where You Want to Clone the Repository: Use the cd command to navigate to the directory where you want to clone the repository. For example, if you want to clone the repository into a folder named "projects" in your home directory, you would use the following command:

        cd ~/projects

5. Clone the Repository: Once you're in the directory where you want to clone the repository, use the git clone command followed by the repository URL you copied earlier. For example, if the repository URL is https://github.com/username/repository.git, you would use the following command:

        git clone https://github.com/username/repository.git
6. Enter Your GitHub Credentials (if prompted): If the repository is private and requires authentication, you may be prompted to enter your GitHub username and password or personal access token.

7. Wait for the Cloning Process to Complete: Git will clone the repository from GitHub to your local machine. Depending on the size of the repository and your internet connection speed, this process may take some time.

8. Access the Cloned Repository: Once the cloning process is complete, you'll have a local copy of the repository on your machine. You can navigate into the repository directory using the cd command and start working with the files.

That's it! You've successfully cloned a repository from GitHub to your local machine. You can now make changes to the files, commit them, and push them back to the repository on GitHub if you have write access.

## Credits

I used the following sources to complete this project.

- [W3School](https://w3schools.com) – code sources for python
- [Materializecss](https://materializecss.com/collapsible.html) - code sources
- [Jinja](https://jinja.palletsprojects.com/en/3.0.x/templates/#builtin-filters) - code sources
- [MD Bootstrap](https://mdbootstrap.com/) - bootstrap tables
- [Stackoverflow](https://stackoverflow.com/) - for codes, tips and answers to some q&a. 
- [Eightshades Contrast Grid](https://contrast-grid.eightshapes.com/) - checked the colour combination contrast
- [Adobe Color](https://color.adobe.com) - created my palette by entering colors used on my website.
- [Adobe Stock Photos]() - for my background.
- [Balsamiq](https://balsamiq.com/) - for wireframes
- [ChatGPT](https://openai.com/) - for codes, tips,documentation advice and answers to some q&a.

## Acknowledgement
This project will not be live today without the help and support of the following people:

1. Arnold Ambida - my husband, who looks after my 3 children while I do this course.
2. Matt Bodden - my mentor who have made a significant impact on completing this projecs with all the tips and the encouragements.
