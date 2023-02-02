# Reporting API
First of all, I appreciate for giving me a chance to be interviewed by you.

In the project, there are 5 endpoints that I can request. I couldn't use the 2nd endpoint which is Transaction Report because of the internal server problem of the 
endpoint. When I try to request with the parameters and a token, response as a JSON is shown below.
{
    "code": 9,
    "status": "DECLINED",
    "message": "10.72.23.66:27017: The 'cursor' option is required, except for aggregate with the explain argument"
}
I think the endpoint uses MongoDB(port 27017) and the error comes from the MongoDB!

- I have successfully consume the 4 endpoints. 

- I have successfully host my website through the link below:
https://akutayural.github.io/Flask-Interview/templates/

- I have successfully commit my project from VSCode with a main branch as I'm the only worker of the project and version control have been made and everthing is
up-to-date

# Please Consider 
- Although I know Pure Python, Data Science and Machine Learning libraries(such as: numpy,pandas,scikit-learn) and I used Django before to develop a web app,
this is my first time developing a web app with flask. I'm a fast learner and I have passion for it. Although I work 32 hours in a restaurant and have 12 hours course
university in a week, I tried to finish the interview questions. I love coding so much! I have experience of these things given in the project with JAVA Spring. 


# HOW TO IMPROVE THE CODE PROVIDED?
- I could use try and except structure to make the 'POST' request better as shown below but as I mentioned above I hardly find time for the project. Session Control
can be added.

>try:
    r = requests.get(url, headers=header, data=data, )
except requests.exceptions.Timeout:
    '''Maybe set up for a retry, or continue in a retry loop'''
except requests.exceptions.TooManyRedirects:
    '''Tell the user their URL was bad and try a different one'''
except requests.exceptions.RequestException as e:
    '''catastrophic error. bail.'''
    raise SystemExit(e)

- Tests can be done as each unit can be tested.

