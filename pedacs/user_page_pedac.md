# PEDAC - User page

P: Render a page for a user that contains:
    - their email address. 
    - their interests, with a comma appearing between each interest.
    - Links to other users (not including the current one)

E:
/user/users_name

Welcome to User_names page!

- email address

User_names interests are:
Flying, eating, cats, dogs.

Other users:
- name
- name


D:
- interests will be in a list
- We will be using a layout.html for the bones of the page, updating the contents for each user
- The main contents that will be updated for each user page is the name, email and interests (these elements will be common across all the users pages)
- We also display as links the other users
- We also want the URL to display /users/jamy (for example)

A:
1. Displaying the users name:
- From the users_dict, get the name, the email and the interests (as a list)
- pass the name, email and interests to render_template to be rendered by jinja2
- In the users page; interpolate name into the title, email and interests.

Given the users_dict, get the nested dict belonging to the user of the given name:

E.g:
{
    jamy : {
        email : jamy.rusted...,
        interests : [
            woodworking,
            cooking,
            etc
        ]
    }
    nora : {
        email : email...,
        interests : [
            cycling,
            basketball,
            economics
        ]
    }
    hiroko: {
        email: etc...
        interests: []
    }
}

user_info = {
        email : jamy.rusted...,
        interests : [
            woodworking,
            cooking,
            etc
        ]
    }

- Get the user details as `user_info`
- SET 'email' to user_info["email"]
- SET 'interests' to joined string from user_info["interests"]

- Get the remaining users names from the users_dict:
- Use a comprehension to get a list of the names that are not current users name
C