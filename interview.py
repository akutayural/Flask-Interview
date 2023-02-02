from flask import Flask, make_response, session, render_template, request
import requests
import json

app = Flask(__name__)

app.secret_key= 'dljsaklqk24e21cjn!Ew@@dsa5'

@app.route('/', methods=['GET'])
def home():
    return render_template("index.html")

# Login
@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        #I could have gotten the API request parameters from url by the following code below however I wanted to gather it with html forms
        #email = request.args.get('email')
        #password = request.args.get('password')

        #Read the inputs from html form
        email = request.form.get('email')
        password = request.form.get('password')

        #Prepare API request paramaters
        url = "https://sandbox-reporting.rpdpymnt.com/api/v3/merchant/user/login"
        data = {'email' : email,
                'password' : password}
        header = ""

        #Post request to endpoint and have the response from endpoint 
        r = requests.post(url, data=data)

        #Needed information gathered from the json response
        status = r.json()['status']

        #Make decision and print the corresponding result
        if status == "APPROVED":
            token = r.json()['token']
            session['token'] = token
            return '''Login Successful! Status = ''' + status + ''' Generated Token from the endpoint ''' + token + '''<a href="http://localhost:5000/getClient">Click here for Client Info.</a>''' + ''' <a href="http://localhost:5000/getClient">Click here for Client Information.</a> ''' + ''' <a href="http://localhost:5000/transactionQuery">Click here for Transaction Query.</a> '''

        elif status == "DECLINED":
            return '''Login Failed! Status = ''' + status

        else:
            return '''Something went wrong!'''
    
    return render_template('login.html')

# Get Client
@app.route('/getClient', methods=['POST','GET'])
def getClient():
    if request.method == 'POST':
        #I could have gotten the API request parameters from url by the following code below however I wanted to gather it with html forms
        #transactionId = request.args.get('transactionId')
        

        #Read the input from html form
        transactionId = request.form.get('transactionId')

        url = "https://sandbox-reporting.rpdpymnt.com/api/v3/client"
        data = {'transactionId' : transactionId}
        header = {'Authorization' : session.get("token", None)}
        r = requests.post(url, headers=header, data=data)
        return r.json()
        
    return render_template('getClient.html')


# Get transaction
@app.route('/getTransaction', methods=['POST','GET'])
def getTransaction():
    if request.method == 'POST':
        #I could have gotten the API request parameters from url by the following code below however I wanted to gather it with html forms
        #transactionId = request.args.get('transactionId')
        

        #Read the input from html form
        transactionId = request.form.get('transactionId')

        url = "https://sandbox-reporting.rpdpymnt.com/api/v3/client"
        data = {'transactionId' : transactionId}
        header = {'Authorization' : session.get("token", None)}

        r = requests.post(url, headers=header, data=data)
        return r.json()
        
    return render_template('getTransaction.html')

#Transaction Query
@app.route('/transactionQuery', methods=['POST','GET'])
def transactionQuery():
    if request.method == 'POST':
        #Read the input from html form
        fromDate = request.form.get('fromDate') or None
        toDate = request.form.get('toDate') or None
        status = request.form.get('status') or None
        operation = request.form.get('operation') or None
        merchantId = request.form.get('merchantId') or None
        acquirerId = request.form.get('acquirerId') or None
        paymentMethod = request.form.get('paymentMethod') or None
        errorCode = request.form.get('errorCode') or None
        filterField = request.form.get('filterField') or None
        filterValue = request.form.get('filterValue') or None
        page = request.form.get('page') or None

        for key, value in request.form.items():
            print(f'{key}: {value}')
        
        url = "https://sandbox-reporting.rpdpymnt.com/api/v3/client"
        header = {'Authorization' : session.get("token")}

        if fromDate is None and toDate is None and merchantId is None and acquirerId is None and status is None and operation is None and paymentMethod is None and errorCode is None and filterField is None and filterValue is None and page is None:
            data = {}
            r = requests.post(url, headers=header)
            return r.json()


        if errorCode is None:
            if fromDate is not None and toDate is not None and merchantId is not None and acquirerId is not None and status is not None and operation is not None and paymentMethod is not None and filterField is not None and filterValue is not None and page is not None:
                data = {'fromDate' : fromDate,
                        'toDate' : toDate,
                        'merchantId' : merchantId,
                        'acquirerId' : acquirerId,
                        'operation' : operation,
                        'paymentMethod' : paymentMethod,
                        'filterField' : filterField,
                        'filterValue' : filterValue,
                        'page' : page}
                r = requests.post(url, headers=header, data=data)
                return r.json()

            elif fromDate is not None and toDate is not None and merchantId is not None and acquirerId is not None:
                data = {'fromDate' : fromDate,
                        'toDate' : toDate,
                        'merchantId' : merchantId,
                        'acquirerId' : acquirerId
                        }
                r = requests.post(url, headers=header, data=data)
                return r.json()

            elif fromDate is not None and toDate is not None:
                data = {'fromDate' : fromDate,
                        'toDate' : toDate
                        }
                r = requests.post(url, headers=header, data=data)
                return r.json()

            else:
                return '''Provided request parameters are not in a form that endpoint can give response!'''
        
        else:
            if status is not None and operation is not None:
                data = {'status' : status,
                        'operation' : operation,
                        'errorCode' : errorCode
                        }
                return r.json()
            else:
                return '''Provided request parameters are not in a form that endpoint can give response!'''
    


    return render_template('transactionQuery.html')



if __name__ == '__main__':
   app.run(debug = True)