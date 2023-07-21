from flask import Flask,render_template
import json
app = Flask(__name__)


with open('C:\\Users\\avina\\OneDrive\\Desktop\\Projects\\Exam\\homeconfig.json','r') as r:
    params = json.load(r)
    college=params['college']
    point=params['point']
    para=params['para']
    details=params["detail"]
    detail=details["stream"]
    s1=detail['s1']
    s2=detail['s2']
    s3=detail['s3']
    para1=detail['para']
    feedbacks=params['feedback']
    contact=params['contact']
    c1=contact['c1']
    c2=contact['c2']
    c3=contact['c3']
    c4=contact['c4']
    admission1=params['admission']

@app.route("/")
def home():
    # return render_template("admission2.html",college=college,para=para1,para1=para,admission=admission1)
    # return render_template('Exam1.html',college=college,point=point,para=para)

    # return render_template("addlogin2.html",college=college,point=point,para=para)
    # return render_template("Details.html",college=college,s1=s1,s2=s2,s3=s3,para=para1,para1=para)
    # return render_template("admission1.html",college=college,para=para1,para1=para,admission=admission1)
    return render_template("contact.html",college=college,para=para1,para1=para,c1=c1,c2=c2,c3=c3,c4=c4)


    # return render_template('home.html',college=college,point=point,para=para)
    # return render_template('home.html',college=college,point=point)



app.run(debug=True)

    
