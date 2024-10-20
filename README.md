**Dougn n Drizzle**

AM I RESPONSIVE PHOTO HERE

**Table of Contents**

-   Project Introduction
    -   [Dough n Drizzle]
    -   Link to Live Project
    -   Objective
-   UX/UI Design
    -   The Strategy Plane
    -   The Scope Plane
    -   The Skeleton Plane
    -   The Structure Plane
    -   The Surface Plane
-   Features
-   Future Enhancements
-   Testing
-   Agile Development
-   Bugs and Potential Issue
-   Technologies and Languages used
-   Developement
-   Deployment on Heroku
-   Credits
-   Acknowledgements

# PROJECT INTRODUCTION

Dough n' Drizzle is a comprehensive e-commerce web application designed for selling artisanal baked goods and confectionery products. Built using the Django framework, the project offers a streamlined user experience, allowing customers to browse and purchase items online with ease. The website supports essential e-commerce features such as product listings, shopping cart functionality, order management, secure payment processing via Stripe, and user authentication through social accounts.

The project follows best practices for web development, incorporating features such as form handling with Django Crispy Forms, media management through AWS S3 via django-storages, and secure deployment with Gunicorn and PostgreSQL. It's a robust, scalable, and user-friendly platform that serves both customers and administrators efficiently.

Key Features

-   Product Listings: A clean and responsive interface for browsing baked goods with detailed product pages.
-   Shopping Cart: Users can add and manage products in their cart, modify quantities, and proceed to checkout.
-   Wishlist: Allows users to save their favorite items for future purchases.
-   Stripe Integration: Secure payment processing with Stripe API for handling transactions.
-   User Authentication: Django Allauth enables social login functionality (e.g., Facebook, Google) and regular account management.
-   Responsive Design: The front end is fully responsive, ensuring a smooth experience on both desktop and mobile devices.
-   Admin Control: Superusers can manage product listings, categories, and view order details via Django's admin interface.
-   Media Management: AWS S3 is used to handle static and media files, ensuring scalability and performance.

Technology Stack

-   Backend: Django 4.2 (Python web framework)
-   Frontend: HTML5, CSS3, Bootstrap 4
-   Database: PostgreSQL
-   Payment Gateway: Stripe API
-   Authentication: Django Allauth
-   Storage: AWS S3 for static and media file handling
-   Deployment: Gunicorn (WSGI HTTP Server), Boto3 for AWS S3
-   Hosting: The app can be deployed on platforms like Heroku or AWS EC2.

[**Link to Live project**](https://pp5-dough-n-drizzle-257d1212e951.herokuapp.com/)

## Objective

The primary objective of Dough N Drizzle is to create an intuitive and efficient online platform for selling artisanal baked goods and confectionery products. The project aims to deliver a seamless shopping experience for customers while providing store owners with the tools to manage product listings, orders, and user interactions effectively. By leveraging modern technologies like Django, AWS S3, and Stripe for secure payments, the platform focuses on scalability, security, and performance, ensuring it meets the needs of both small businesses and their growing customer base.

# UX/UI Design

## The Strategy Plane

### VISION

### OBJECTIVES

### USER NEEDS

## The Scope Plane

### FEATURES:

### CUSTOM FEATURES:

-   **Subscription** - This allow users to sign up to receive emails about news, offers, and get a 10% discount on their first order. It store the user's email, subscription status, and track whether they have used the 10% discount on their first order.

### CONTENT REQUIREMENTS:

### FUNCTIONAL SPECIFICATIONS

### USER STORIES

-   **MoSCoW Prioritization**
    -   **Must Have:**
    -   **Should Have:**
    -   **Could Have:**
    -   **Won't Have:**
-   **As a User:**
-   **As a**
-   **As an admin:**

## The Skeleton Plane

### LAYOUT AND WIREFRAME STRUCTURE

-   **Home Page:** TEXT HERE PHOTO HERE
-   **Login Page:** TEXT HERE PHOTO HERE
-   **Register Page:** TEXT HERE PHOTO HERE

### WIREFRAMES

**Mobile and Tablet Wireframes:**

### ENTITY RELATIONSHIP MODEL

ERD Diagram PHOTO HERE

### KEY POINTS

-   **User:**
    -   Has a one-to-one relationship with Profile.
    -   Has a one-to-many relationship with Ticket.
    -   Has a one-to-many relationship with Comment.
-   **Profile:** - Linked to User with a one-to-one relationship.

### SEO STRAGETIES

SEO strategies for Dough n Drizzle to improve its search visibility and attract more organic traffic:

1.  **Optimize Website for Search Engines**
    -   **Title Tags & Meta Descriptions:** Ensure that the base template has unique, keyword-rich title tags and meta descriptions. For example:
        -   **Title:** "Custom Cakes & Artisan Desserts - Dough n Drizzle"
        -   **Meta:** "Order custom cakes, pastries, and gourmet cookies. Dough n Drizzle offers delivery and pick-up options for fresh, handcrafted desserts."
            -   **Key SEO Additions:**
                1.  **Meta Title & Description:** Relevant to the Dough n' Drizzle business, targeting keywords like custom cakes, cookies, and desserts.
                2.  **Keywords:** Keywords relevant to the bakery business like "custom cakes," "cake delivery," "artisan desserts," and "online bakery."
                3.  **Open Graph & Twitter Meta Tags**: Optimizes the website for sharing on social media platforms like Facebook, ensuring that when someone shares the site, it shows a title, description, and an image.
    -   **Headings (H1, H2, H3):** Use primary keywords in H1 and secondary keywords in H2/H3 tags. Structure the content clearly for users and search engines.
2.  **Keyword Research & Optimization**
    -   **Target Primary & Long-Tail Keywords**: Identify relevant keywords for custom cakes, delivery options, and other baked goods. For example:
        -   Primary: "Custom cakes," "Cake delivery," "Gourmet cookies"
        -   Long-tail: "Best custom birthday cakes near me," "Online bakery for weddings"
    -   **Integrate Keywords Naturally**: Place keywords in key areas (page titles, product descriptions, URLs, headings, alt tags for images) without overstuffing.
3.  **Content Marketing**
    -   Create detailed FAQs addressing customer needs. This will also rank for long-tail queries like “What products do you offer?”
4.  **Mobile Optimization**
    -   **Mobile-Friendly Design**: Ensure the website is fully responsive on mobile devices. Since many users may order via mobile, optimize loading times and usability.
    -   **Page Speed Optimization**: Compress images, leverage browser caching, and use content delivery networks (CDNs) to improve website speed.
5.  **On-Page SEO for Product Pages**
    -   **Product Descriptions**: Write unique, descriptive content for each product, incorporating primary keywords and long-tail variations. Focus on the benefits and features of the cakes or desserts.
    -   **Alt:** all images have alt attribut
    -   **Schema Markup**: Implement schema for products and reviews to enhance rich snippets in search results (e.g., category, product prices).
6.  **E-Commerce SEO**
    -   **Optimized URLs**: Use clean, descriptive URLs (e.g., “/signature-cakes/” instead of “/product1234”).

### WEB MARKETING STARTEGIES

1.  

## The Structure Plane

### INFORMATION ARCHITECTURE

-   **Global Navigation:**

### CONTENT ORGANIZATION

### INTERFACE ELEMENTS:

-   **Forms:**
    -   **User Registration Form:** Input validation for email, username, password and password confirmation fields
    -   **Login Form:** Input validation for email and password fields
    -   **Ticket Form:** Input validation for subject and description fields and status (hidden field or dropdown for tech support).
    -   **Comment Form:** Input validation for comment text
-   **Buttons:**
    -   **Primary** buttons for actions like "Register", "Log In", "Logout", "Create Ticket", "Submit", "Edit", "Delete", "Next", "Last", "First", and "Previous".
    -   **Secondary** buttons for action like "Cancel", "Close", and "Save Changes".
-   **Tables:**
    -   **Ticket List:** Columns for Ticket ID, Status, Subject, Created On (date only), and User. Clickable rows to view ticket details, pagination.
    -   **Ticket List for Mobile:** Columns for Ticket ID and Status.
-   **Modals:**
    -   For editing comments to avoid navigating away from the ticket detail page. Opens when the "Edit" button is clicked on a comment, contains the comment text pre-filled, and has a save button to update the comment
    -   For deleting ticket and comments.
-   **Alerts:**
    -   For success and error messages, displayed using Bootstrap alerts for actions like creating tickets, adding comments, updating tickets, etc..
    -   For Access Denied and 404 Error using a customised page.

### INTERACTION DESIGN:

-   **Ticket Creation:**
    -   User fills out the ticket form and submits.
    -   System validates input and creates a ticket.
    -   Success message is shown.
    -   System will display newly created ticket with an option to edit/delete.
-   **Editing Ticket:**
    -   User clicks "Edit" on a ticket
    -   Redirect to a page to update ticket with the text pre-filled.
    -   User updates the ticket with the option to update status if admin/staff and then save changes
    -   System validates and updates the ticket.
    -   Success message is shown, and the updated ticket is displayed.
-   **Commenting:**
    -   User adds a comment via the form.
    -   System validates input and adds the comment.
    -   Comment appears below the ticket details with an option to edit/delete (if allowed).
-   **Editing Comments:**
    -   User clicks "Edit" on a comment.
    -   Modal opens with the comment text pre-filled.
    -   User updates the comment and saves changes.
    -   System validates and updates the comment.
    -   Success message is shown, and the updated comment is displayed.

## The Surface Plane

### COLOUR SCHEME

PHOTO HERE

-   **Primary Colors:**
-   **Secondary Colors:**
-   **Text Colors:**
-   **Buttons:**
-   **Alerts and Modals:**
    -   Alerts:
        -   Background Color: Varies based on message type (e.g., success, danger)
        -   Text Color: White
    -   Modals:
        -   Text Color: White
        -   Body Background: \#ffffff (white)
-   **Footer:**

### TYPOGRAPHY

-   Primary Font: Titillium Web
    -   Used for headers, body text, and UI elements
        -   Provides a clean, modern look suitable for various UI components
        -   Font Family: "Titillium Web", sans-serif
        -   Headings:
            -   Font Weight: 600 to 700
            -   Size: Varies (e.g., h1: 2.5em, h2: 2em)
        -   Body Text:
            -   Font Weight: 400
            -   Size: 1em
        -   Buttons and Links:
            -   Font Weight: 600
            -   Size: 1em

### IMAGES

-   **Background**
-   **Logo**
-   **Products** -

# FEATURES

# FUTURE ENHANCEMENTS

## SEO

1.  **Content Marketing**
    -   **Blog**: Regularly update the blog with relevant, engaging content such as cake design trends, how to choose wedding cakes, cake care tips, or seasonal dessert ideas. Include targeted keywords and long-tail search queries.
        -   Example blog posts:
            -   "Top 5 Wedding Cake Trends for 2024"
            -   "How to Store and Serve Your Custom Cakes"
2.  **Local SEO Optimization**
    -   **Google My Business (GMB)**: Create or optimize your GMB listing. Ensure that the business name, address, phone number, and hours are accurate. Include high-quality images of your bakery and products.
    -   **Local Keywords**: Focus on local keywords like “Best custom cakes near [City Name]” or “Artisan bakery in [City Name].”
    -   **Local Listings & Reviews**: Encourage satisfied customers to leave reviews on Google and Yelp. Positive reviews improve trust and local rankings.
3.  **Backlink Building**
    -   **Collaborate with Local Influencers**: Partner with local food bloggers or event planners to generate backlinks and social mentions.
    -   **Guest Blogging**: Write guest posts for local publications or industry websites to build credibility and backlinks to your site.
    -   **Submit to Local Directories**: Ensure your business is listed on relevant directories (Yelp, TripAdvisor, etc.) with accurate information.
4.  **E-Commerce SEO**
    -   **Internal Linking**: Strategically link to relevant product pages, blog posts, and categories to keep users on your site longer and help search engines crawl your content.
    -   **Breadcrumb Navigation**: Implement breadcrumb navigation to improve user experience and help search engines understand your site’s structure.
5.  **Monitor and Improve**
    -   **Analytics & SEO Tools**: Regularly monitor performance using Google Analytics, Google Search Console, and tools like Ahrefs or SEMrush to track keyword rankings, site traffic, and user behavior.
    -   **Improve Based on Data**: Continuously optimize content based on the insights from these tools. Track which pages are performing well and refine those that are underperforming.
6.  **External Links**
    -   Calendar of upcoming wedding/party fairs that will be attending
    -   Tips & Advice for baking

# TESTING

-   Complete Testing documentation can be found here

# AGILE DEVELOPMENT

## Iteration 0: Planning and Setup

-   Goals:
-   Tasks:

## Iteration 1: User Authentication and Role Management

-   Goals:
-   Tasks:
-   Deliverables:

## Iteration 2: Ticket Management

-   Goals:
-   Tasks:
-   Deliverables:

## Iteration 3: Commenting and Interaction

-   Goals:
-   Tasks:
-   Deliverables: .

## Iteration 4: Admin and Tech Support Features

-   Goals:
-   Tasks:
-   Deliverables:

## Iteration 5: Testing and Bug Fixing

-   Goals:
-   Tasks:
-   Deliverables:

## Iteration 6: Deployment and Documentation

-   Goals:
-   Tasks:
-   Deliverables:

## Iteration 8: Feedback and Iteration

-   Goals:
-   Tasks:
-   Deliverables:

# BUGS AND ISSUES

## Increment/Decrement Button on product detail page

**Issue:** The +/- buttons on the quantity section is meant to update the quantity on this page, however when during the early stages these buttons are directly updating the cart page. You can see the update when the button was clicked the value on the cart increases. Both buttons increases the value of the cart.

**Remedies:**

**Resolution:**

## Problem after upgrading to django 5.0 "AttributeError: 'BlankChoiceIterator' object has no attribute "'len'"

**Issue:** This error comes up after I install django-countries==7.2.1. I accidentally upgraded to Django 5.0.

**Remedies:**

**Resolution:** I uninstall django-countries 7.2.1 and installed django-countries 7.6.1. This has the fix for this bug. You can reference on this [Github](https://github.com/SmileyChris/django-countries/issues/447) repo about Django Countries

## Django not connecting/uploading static files to AWS S3 Bucket.

**Issue:** After adding all the required configuration settings for AWS and deploying to Heroku, static filea re not uploading to my AWS S3 Bucket.

**Remedies:**

1.  I refactored AWS settings several times, disable and re-enable static_root folder.
    1.  I created another AWS S3 bucket incase I missed a step when following the walkthrough. Another student provided an updated instruction
    2.  

**Resolution:** I downgraded my Django version from 5.1.1 to Djano version 4.2. After pushing to Heroku, all my static files uploaded to my AWS S3 Bucket. Issue was fixed by Roman from Code Institute

## Heroku throws a server error 500

**Issue:** Deployed project throws a server error 500 when trying to access newsletter subscription in admin and after entering an email to test newsletter subscription functionality but works fine workspace

**Resolution:** Despite running database migrations in workspace, migrations have to be applied in heroku by running:

1.  Login to Heroku from workspace
2.  Run:

heroku run python3 manage.py migrate

# TECHNOLOGIES AND LANGUAGE

SOME TEXTS HERE

## Frontend

-   **HTML5:** For structuring the web pages and content.
-   **CSS3:** For styling the web pages, including layout, design, and responsiveness.
-   **JavaScript:** For interactive features and client-side logic.
    -   **jQuery:** For simplified DOM manipulation and event handling.
    -   **Bootstrap:** For responsive design and pre-styled components.

## Backend

-   **Python:** The main programming language used for backend development.
-   **Django:** A high-level Python web framework that encourages rapid development and clean, pragmatic design.
-   **Django REST Framework:** For building RESTful APIs.

## Database

-   **SQLite:** The default database used for development and testing
-   **PostgreSQL:** Used in production..

Version Control

-   **GitHub:** For hosting the code repository and facilitating collaboration.

## Deployment

-   \***Heroku:** For deploying the web application in a scalable and reliable manner.
-   **Gunicorn:** A Python WSGI HTTP Server for running the application on Heroku.

## Additional Tools and Libraries

-   **Crispy Forms:** For enhancing the rendering of Django forms.
-   **Cloudinary:** For managing media files like images.
-   **Font Awesome:** For scalable vector icons.
-   **Moment.js:** For parsing, validating, manipulating, and displaying dates and times in JavaScript.

# DEVELOPMENT

This application was develop in Code Institute Gitpod, hosted in GitHub and deployed in Heroku.

# DEPLOYMENT

The site was deployed via Heroku.

## Project Deployment

To deploy the project through Heroku:

-   Login to Heroku
-   Create a new Heroku application by going to the Dashboard and select New and Create New App
-   Give your app a name (pp4-techtackles-by-hc) and choose the region nearest to you (Europe). This will create an app in Heroku and will redirect you to the Deploy tab.
-   On the Deploy tab, connect your Github and search for your repository.
-   Manually deploy the main branch of this GitHub repo.
-   On the Resources tab, ensure eco-dyno is enabled and delete any Postgres database Add-on.
-   Add the KEY - DISABLE_COLLECTSTATIC with the Value - 1 to the config vars, this must be removed before final deployment.
-   Add the database to the app by going to Settings tab, under Config vars add the following: Key= Database_URL Value = your postgres url
-   In your Django app, make sure you install gunicorn\~=20.1 and freeze it to the requirements.txt file.
-   Create a new file env.py on the root directory and import the os library and set the environment variable for the DATABASE_URL the same as your settings in Heroku.
-   Add SECRET_KEY using the os.environ in the env.py and add the same SECRET_KEY on the settings tab in Heroku under Config vars
-   In the settings.py file within the django app, import Path from pathlib, import os and import dj_database_url
-   Insert the line if os.path.isfile("env.py"): import env
-   Update the default SECRET_KEY that Django has on settings.py and replace it with SECRET_KEY = os.environ.get('SECRET_KEY')
-   On settings.py, replace the database section with DATABASES = { 'default': dj_database_url.parse(os.environ.get("DATABASE_URL")) }
-   Settings.py file - add the STATIC files settings - the url, storage path, directory path, root path, media url and default file storage path.
-   Link the file to the templates directory in Heroku TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
-   Change the templates directory to TEMPLATES_DIR - 'DIRS': [TEMPLATES_DIR]
-   Add Heroku to the ALLOWED_HOSTS list the format will be the app name given in Heroku when creating the app followed by .herokuapp.com
-   Create a new file on the top level directory - Procfile
-   Add web: gunicorn projectname.wsgi in Procfile.
-   During production, do add, commit and push changes to your Github repo.
-   In Heroku, under Deploy tab, click Deploy Branch.
-   Watch out for any errors.
-   Heroku will now build the app for you. Once it has completed the build process you will see a 'Your App Was Successfully Deployed' message and a link to the app to visit the live site.

## Forking your repository

To fork a repository on GitHub, follow these steps:

1.  Navigate to the Repository: Go to the GitHub repository you want to fork. You can do this by entering the repository URL in your browser or by searching for the repository on GitHub.
2.  Find the "Fork" Button: On the repository page, you'll see a button labeled "Fork" in the top right corner of the page, next to the "Star" and "Watch" buttons. Click on the "Fork" button.
3.  Choose where to Fork: GitHub will prompt you to choose where you want to fork the repository. You can fork it to your personal GitHub account or to any organizations you're a member of. Select the desired location.
4.  Wait for the Fork to Complete: GitHub will create a copy of the repository in your account or organization. Depending on the size of the repository and the current server load, this process may take a few moments.
5.  Access Your Forked Repository: Once the forking process is complete, you'll be redirected to your forked copy of the repository. You can now clone the repository to your local machine, make changes, and push them to your fork.
6.  Keep Your Fork Synced: If you forked a repository to contribute changes back to the original repository, you may want to keep your fork up-to-date with the original repository. You can do this by configuring an "upstream" remote and pulling changes from it periodically.

That's it! You've successfully forked a repository on GitHub. You can now start working with the code in your fork, making changes, and contributing back to the original repository through pull requests.

## Clone Repository

Cloning a repository from GitHub allows you to copy a remote repository to your local machine. To clone a repository from GitHub to your local machine, follow these steps:

1.  Find the Repository: Go to the GitHub repository you want to clone. You can do this by entering the repository URL in your browser or by searching for the repository on GitHub.
2.  Copy the Repository URL: On the repository page, click on the "Code" button. This will reveal a URL for the repository. Click on the clipboard icon to copy the URL to your clipboard.
3.  Open Terminal (or Command Prompt): Open your terminal or command prompt on your local machine. You can usually find it in your applications or by searching for "Terminal" (on macOS and Linux) or "Command Prompt" (on Windows).
4.  Navigate to the Directory Where You Want to Clone the Repository: Use the cd command to navigate to the directory where you want to clone the repository. For example, if you want to clone the repository into a folder named "projects" in your home directory, you would use the following command:
5.  cd \~/projects
6.  Clone the Repository: Once you're in the directory where you want to clone the repository, use the git clone command followed by the repository URL you copied earlier. For example, if the repository URL is <https://github.com/username/repository.git>, you would use the following command:
7.  git clone <https://github.com/username/repository.git>
8.  Enter Your GitHub Credentials (if prompted): If the repository is private and requires authentication, you may be prompted to enter your GitHub username and password or personal access token.
9.  Wait for the Cloning Process to Complete: Git will clone the repository from GitHub to your local machine. Depending on the size of the repository and your internet connection speed, this process may take some time.
10. Access the Cloned Repository: Once the cloning process is complete, you'll have a local copy of the repository on your machine. You can navigate into the repository directory using the cd command and start working with the files.

That's it! You've successfully cloned a repository from GitHub to your local machine. You can now make changes to the files, commit them, and push them back to the repository on GitHub if you have write access.

# CREDITS

I used the following sources to complete this project.

-   [W3School](https://w3schools.com/) – code sources for python
-   [MD Bootstrap](https://mdbootstrap.com/) - bootstrap tables
-   [Stackoverflow](https://stackoverflow.com/) - for codes, tips and answers to some q&a.
-   [Eightshades Contrast Grid](https://contrast-grid.eightshapes.com/) - checked the colour combination contrast
-   [Adobe Color](https://color.adobe.com/) - created my palette by entering colors used on my website.
-   [Adobe Stock Photos](https://vscode-remote+hpcoloma-002dpp5doughndrizz-002dghhtuxykw47-002ews-002ecodeinstitute-002dide-002enet.vscode-resource.codeinstitute-ide.net/workspace/pp5-dough-n-drizzle/README.md) - for my background.
-   [Balsamiq](https://balsamiq.com/) - for wireframes
-   [ChatGPT](https://openai.com/) - for codes, tips, documentation advice and answers to some q&a.

# ACKNOWLEDGEMENTS

This project will not be live today without the help and support of the following people:

1.  Arnold Ambida - my husband, who looks after my 3 children while I do this course.
2.  Matt Bodden - my mentor who have made a significant impact on completing this projecs with all the tips and the encouragements.
3.  Roman and Tom Code Institute
