# PEDAC: main pedac for project
Project Requirements

- When a user loads the home page, they should be redirected to a page that lists all of the users' names. Load the users from the users.yaml file (content below).
- Each of the users' names should be a link to a page for that user.
- On each user's page, display their email address. Also, display their interests, with a comma appearing between each interest.
- At the bottom of each user's page, list links to all of the other users pages. Do not include the user whose page it is in this list.
- Add a layout to the application. At the bottom of every page, display a message like this: "There are 3 users with a total of 9 interests."
- Update the message printed out in #5 to determine the number of users and interests based on the content of the YAML file.
    Use a view helper method, total_interests, to determine the total number of interests across all users.Add a new user to the users.yaml file. Verify that the site updates accordingly.

# html files:
layout.html:
    - This will the layout file that all other files will extend.
    - Have a header at the top and a footer at the bottom, as per requirements

home.html:
    - Have a title for the page: Home, so we know where we are
    - list all the users names from the .yaml file
    - each name should be a link to that users page

user.html:
    - Display the users name
    - Display the users email address
    - display the users interests:
        - comma appearing between each interest
    - Include links to other users pages


