# PEDAC: Main page; getting users and interests

P:
Parse the .yaml file that contains the list of users and thier interests, getting the users. Render the html home page so that it contains the users as hyperlinks to the users page.

I: .yaml page, imports as a dict when we open the yaml file using `open`
o: Users names to be used in html home page

E:
Given yaml file:
jamy:
  email: jamy.rustenburg@gmail.com
  interests:
    - woodworking
    - cooking
    - reading
nora:
  email: nora.alnes@yahoo.com
  interests:
    - cycling
    - basketball
    - economics
hiroko:
  email: hiroko.ohara@hotmail.com
  interests: []

output once imported (dict structure)
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

D: Working with a dictionary structure

A:
- open the file (helper function that all funcs can use? Using `g`)
To get just the names we only need to get the keys of the main dict:
- Use a comprehension to get a list of the names:
    for name in users_dict.keys():
        append name to list

- pass this list of users to 
C: