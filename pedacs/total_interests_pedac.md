# PEDAC - Update total interests footer so that it is dynamic

P:
Determine the amount of total users and interests to display as a footer in the layout.html page
- use a view helper method, total_interests to determine total number of interests
- use another view helper to calculate total number of users

E:

output once imported (dict structure) from yaml
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

total_interests: 6
total_users: 3

D:
- will be working with a nested dictionary to get total users and thier interests:
- 'interests' is a list. Can use len() to get length of interests for eachc user

A:
Should all happen in a before_request function:

- SET `g.total_users` to length of users_dict (number of users)
- SET `g.total_interests` to 0
> Loop through users in users_dict, getting the interest list:
    - Add length of interest list to `total_interest`

- pass total_users and total_interests to layout.html and each html page