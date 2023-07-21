from flask import Flask, render_template, request,session,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json
import os
from werkzeug.utils import secure_filename


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

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/college'
app.secret_key="super-secret-key"
data = SQLAlchemy(app)

class Homeblog(data.Model):
    title = data.Column(data.String(100), nullable=False)
    content = data.Column(data.String(300), nullable=False)
    date = data.Column(data.String(12), nullable=True)
    name = data.Column(data.String(30), nullable=False)
    sn = data.Column(data.Integer, primary_key=True)
class Feedback(data.Model):
    name = data.Column(data.String(30), nullable=False)
    email = data.Column(data.String(30), nullable=False)
    feedback = data.Column(data.String(30), nullable=True)
    feedbackword = data.Column(data.String(30), nullable=False)
    date = data.Column(data.String(12), nullable=True)
    sn = data.Column(data.Integer, primary_key=True)
class User(data.Model):
    username = data.Column(data.String(30), nullable=False)
    password = data.Column(data.String(30), nullable=False)
    email = data.Column(data.String(40), nullable=False)
    sn = data.Column(data.Integer, primary_key=True)
class Form(data.Model):
    username=data.Column(data.String(100), nullable=False)
    admissiontype=data.Column(data.String(100), nullable=False)
    section=data.Column(data.String(100), nullable=False)
    class1=data.Column(data.String(100), nullable=False)
    division=data.Column(data.String(100), nullable=False)
    fee=data.Column(data.String(100), nullable=False)
    caste=data.Column(data.String(100), nullable=False)
    inhouse=data.Column(data.String(100), nullable=False)
    board=data.Column(data.String(100), nullable=False)
    adhar=data.Column(data.String(100), nullable=False)
    studentname=data.Column(data.String(100), nullable=False)
    gender=data.Column(data.String(100), nullable=False)
    studentemail=data.Column(data.String(100), nullable=False)
    studentmobile=data.Column(data.String(100), nullable=False)
    birthdate=data.Column(data.String(100), nullable=False)
    birthplace=data.Column(data.String(100), nullable=False)
    natinality=data.Column(data.String(100), nullable=False)
    maritalstatu=data.Column(data.String(100), nullable=False)
    mothertongue=data.Column(data.String(100), nullable=False)
    religion=data.Column(data.String(100), nullable=False)
    address1=data.Column(data.String(100), nullable=False)
    address2=data.Column(data.String(100), nullable=False)
    location=data.Column(data.String(100), nullable=False)
    taluka=data.Column(data.String(100), nullable=False)
    district=data.Column(data.String(100), nullable=False)
    state=data.Column(data.String(100), nullable=False)
    country=data.Column(data.String(100), nullable=False)
    pincode=data.Column(data.String(100), nullable=False)
    fathername=data.Column(data.String(100), nullable=False)
    mothername=data.Column(data.String(100), nullable=False)
    parentemail=data.Column(data.String(100), nullable=False)
    parentmobile=data.Column(data.String(100), nullable=False)
    parentaddress1=data.Column(data.String(100), nullable=False)
    parentaddress2=data.Column(data.String(100), nullable=False)
    parentlocation=data.Column(data.String(100), nullable=False)
    parenttaluka=data.Column(data.String(100), nullable=False)
    parentdistrict=data.Column(data.String(100), nullable=False)
    parentstate=data.Column(data.String(100), nullable=False)
    parentcountry=data.Column(data.String(100), nullable=False)
    parentpincode=data.Column(data.String(100), nullable=False)
    guardianname=data.Column(data.String(100), nullable=False)
    relation=data.Column(data.String(100), nullable=False)
    guardianemail=data.Column(data.String(100), nullable=False)
    guardianmobile=data.Column(data.String(100), nullable=False)
    guardianaddress1=data.Column(data.String(100), nullable=False)
    guardianaddress2=data.Column(data.String(100), nullable=False)
    date=data.Column(data.String(100), nullable=True)
    sn=data.Column(data.Integer, primary_key=True)

li1={}
li2={}
li3={}
li4={}
li5={}
li=[]

@app.route('/')
def home():
    posts = Homeblog.query.filter_by().all()
    last = len(posts)
    # 4
    page = request.args.get('page')

    if (not str(page).isnumeric()):
        page = 1
    page = int(page)

    posts = posts[(page-1):(page-1)*1+1]
    print(posts)
    if page==1:
        prev = "#"
        next = "/?page="+ str(page+1)
    elif page==last:
        prev = "/?page="+ str(page-1)
        next = "#"
    else:
        prev = "/?page="+ str(page-1)
        next = "/?page="+ str(page+1)
    return render_template('home.html',college=college,point=point,para=para,post=posts, prev=prev, next=next)


@app.route("/admin1", methods=['GET', 'POST'])
def admin1():
    username=""
    password=""
    if username in session and session[username]==password:
        post=Homeblog.query.all()
        return render_template("blogtable.html",college=college,point=point,para=para,post=post)

    if request.method=='POST':
        username=request.form.get('username')
        password=request.form.get('password')
        with open("user.txt",'w') as r2:
            r2.write(username)
        user=User.query.filter_by().all()
        for u in user:
            li2.update({u.username:u.password})
        if li2[username]==password:
            post=Homeblog.query.all()
            session[username]=password
            return render_template("blogtable.html",college=college,point=point,para=para,post=post)
        else:
            return render_template("addlogin1.html",college=college,point=point,para=para)
        
    return render_template("addlogin1.html",college=college,point=point,para=para)



@app.route("/admin2", methods=['GET', 'POST'])
def admin2():
    username1=""
    password1=""
    if username1 in session and session[username1]==password1:
        post=Homeblog.query.all()
        return render_template("blogtable.html",college=college,point=point,para=para,post=post)

    if request.method=='POST':
        username1=request.form.get('username')
        password1=request.form.get('password')
        email=request.form.get('email')
        entry=User(username=username1,password=password1,email=email)
        data.session.add(entry)
        data.session.commit()
        user=User.query.filter_by().all()
        for u in user:
            li1.update({u.username:u.password})
        print(li1)
        with open("user.txt",'w') as r2:
            r2.write(username1)
        if li1[username1]==password1:
            post=Homeblog.query.all()
            session[username1]=password1
            return render_template("blogtable.html",college=college,point=point,para=para,post=post)
    return render_template("addlogin2.html",college=college,point=point,para=para)

@app.route('/edit/<string:sn>',methods=['GET', 'POST'])
def edit(sn):
    with open("user.txt",'r') as r2:
        username=r2.read()
    user=User.query.filter_by().all()
    for u in user:
        li3.update({u.username:u.password})
    password=li3[username]
    if username in session and session[username]==password:
        if request.method=="POST":
            title=request.form.get("title")
            content=request.form.get("content")
            name=request.form.get("name")
            post=Homeblog.query.filter_by(sn=sn).first()
            post.title=title
            post.content=content
            post.name=name
            data.session.commit()
            return redirect(f"/admin1")
        post=Homeblog.query.filter_by(sn=sn).first()
        return render_template('edit.html',college=college,point=point,para=para,post=post)

@app.route('/logout')
def home3():
    with open("user.txt",'r') as r2:
        username1=r2.read()
    session.pop(username1)
    # getting = User.query.filter_by(username=username1).first()
    # data.session.delete(getting)
    # data.session.commit()
    return redirect("/admin1")

@app.route('/add',methods=['GET','POST'])
def add():
    if(request.method=='POST'):
        name=request.form.get('name')
        title=request.form.get('title')
        content=request.form.get('content')
        entry=Homeblog(title=title,content=content,date=datetime.now(),name=name)
        data.session.add(entry)
        data.session.commit()
    return render_template('addblog.html',college=college,point=point,para=para)

@app.route("/delete/<string:sn>", methods=['GET','POST'])
def delete_requesting(sn):
    getting = Homeblog.query.filter_by(sn=sn).first()
    data.session.delete(getting)
    data.session.commit()
    post=Homeblog.query.all()
    return render_template("blogtable.html",college=college,point=point,para=para,post=post)

@app.route('/detail')
def detail():
    return render_template("Details.html",college=college,s1=s1,s2=s2,s3=s3,para=para1,para1=para)
@app.route('/feedback' ,methods=['GET','POST'] )
def feedback():
    if request.method=='POST':
        name=request.form.get('name')
        email=request.form.get('email')
        feedback1=request.form.get('feedback')
        feedbackword=request.form.get('feedbackword')
        entry=Feedback(name=name,email=email,feedback=feedback1,feedbackword=feedbackword,date=datetime.now())
        data.session.add(entry)
        data.session.commit()
    return render_template("feedback.html",college=college,s1=s1,s2=s2,s3=s3,para=para1,para1=para,feedback=feedbacks)
@app.route('/contact')
def contact():
    return render_template("contact.html",college=college,para=para1,para1=para,c1=c1,c2=c2,c3=c3,c4=c4)

@app.route('/admission1',methods=['GET','POST'] )
def admission1():
    if request.method=='POST':
        username1=request.form.get('username')
        password2=request.form.get('password')
        if(not(os.path.exists(f"C:\\Users\\avina\\OneDrive\\Desktop\\Projects\\Exam\\static\\img\\{username1}"))):
            os.mkdir(f"C:\\Users\\avina\\OneDrive\\Desktop\\Projects\\Exam\\static\\img\\{username1}")
        with open("user1.txt",'w') as r2:
            r2.write(username1)
        return redirect("/form")
    return render_template("addlogin3.html",college=college,point=point,para=para)

@app.route('/form',methods=['GET','POST'] )
def form():  
    with open("user1.txt",'r') as r2:
        username1=r2.read()
    if request.method=='POST':
        admissiontype=request.form.get("admissiontype")
        section=request.form.get("section")
        class1=request.form.get("class1")
        division=request.form.get("division")
        fee=request.form.get("fee")
        caste=request.form.get("caste")
        inhouse=request.form.get("inhouse")
        board=request.form.get("board")
        adhar=request.form.get("adhar")
        studentname=request.form.get("studentname")
        gender=request.form.get("gender")
        studentemail=request.form.get("studentemail")
        studentmobile=request.form.get("studentmobile")
        birthdate=request.form.get("birthdate")
        birthplace=request.form.get("birthplace")
        natinality=request.form.get("natinality")
        maritalstatu=request.form.get("maritalstatu")
        mothertongue=request.form.get("mothertongue")
        religion=request.form.get("religion")
        address1=request.form.get("address1")
        address2=request.form.get("address2")
        location=request.form.get("location")
        taluka=request.form.get("taluka")
        district=request.form.get("district")
        state=request.form.get("state")
        country=request.form.get("country")
        pincode=request.form.get("pincode")
        fathername=request.form.get("fathername")
        mothername=request.form.get("mothername")
        parentemail=request.form.get("parentemail")
        parentmobile=request.form.get("parentmobile")
        parentaddress1=request.form.get("parentaddress1")
        parentaddress2=request.form.get("parentaddress2")
        parentlocation=request.form.get("parentlocation")
        parenttaluka=request.form.get("parenttaluka")
        parentdistrict=request.form.get("parentdistrict")
        parentstate=request.form.get("parentstate")
        parentcountry=request.form.get("parentcountry")
        parentpincode=request.form.get("parentpincode")
        guardianname=request.form.get("guardianname")
        relation=request.form.get("relation")
        guardianemail=request.form.get("guardianemail")
        guardianmobile=request.form.get("guardianmobile")
        guardianaddress1=request.form.get("guardianaddress1")
        guardianaddress2=request.form.get("guardianaddress2")
        entry=Form(username=username1,admissiontype=admissiontype,section=section,class1=class1,division=division,fee=fee,caste=caste,inhouse=inhouse,board=board,adhar=adhar,studentname=studentname,gender=gender,studentemail=studentemail,studentmobile=studentmobile,birthdate=birthdate,birthplace=birthplace,natinality=natinality,maritalstatu=maritalstatu,mothertongue=mothertongue,religion=religion,address1=address1,address2=address2,location=location,taluka=taluka,district=district,state=state,country=country,pincode=pincode,fathername=fathername,mothername=mothername,parentemail=parentemail,parentmobile=parentmobile,parentaddress1=parentaddress1,parentaddress2=parentaddress2,parentlocation=parentlocation,parenttaluka=parenttaluka,parentdistrict=parentdistrict,parentstate=parentstate,parentcountry=parentcountry,parentpincode=parentpincode,guardianname=guardianname,relation=relation,guardianemail=guardianemail,guardianmobile=guardianmobile,guardianaddress1=guardianaddress1,guardianaddress2=guardianaddress2,date=datetime.now())
        data.session.add(entry)
        data.session.commit()
    return render_template("admission1.html",college=college,para=para1,para1=para,admission=admission1)

@app.route('/admission2',methods=['GET','POST'] )
def admission2():
    if request.method=='POST':
        username1=request.form.get('username')
        password2=request.form.get('password')
        with open("user1.txt",'w') as r2:
            r2.write(username1)
        return redirect("/update")

    return render_template("addlogin4.html",college=college,point=point,para=para)

@app.route('/update',methods=['GET','POST'] )
def update():
    with open("user1.txt",'r') as r2:
        username=r2.read()

    if request.method=="POST":
        admissiontype=request.form.get("admissiontype")
        section=request.form.get("section")
        class1=request.form.get("class1")
        division=request.form.get("division")
        fee=request.form.get("fee")
        caste=request.form.get("caste")
        inhouse=request.form.get("inhouse")
        board=request.form.get("board")
        adhar=request.form.get("adhar")
        studentname=request.form.get("studentname")
        gender=request.form.get("gender")
        studentemail=request.form.get("studentemail")
        studentmobile=request.form.get("studentmobile")
        birthdate=request.form.get("birthdate")
        birthplace=request.form.get("birthplace")
        natinality=request.form.get("natinality")
        maritalstatu=request.form.get("maritalstatu")
        mothertongue=request.form.get("mothertongue")
        religion=request.form.get("religion")
        address1=request.form.get("address1")
        address2=request.form.get("address2")
        location=request.form.get("location")
        taluka=request.form.get("taluka")
        district=request.form.get("district")
        state=request.form.get("state")
        country=request.form.get("country")
        pincode=request.form.get("pincode")
        fathername=request.form.get("fathername")
        mothername=request.form.get("mothername")
        parentemail=request.form.get("parentemail")
        parentmobile=request.form.get("parentmobile")
        parentaddress1=request.form.get("parentaddress1")
        parentaddress2=request.form.get("parentaddress2")
        parentlocation=request.form.get("parentlocation")
        parenttaluka=request.form.get("parenttaluka")
        parentdistrict=request.form.get("parentdistrict")
        parentstate=request.form.get("parentstate")
        parentcountry=request.form.get("parentcountry")
        parentpincode=request.form.get("parentpincode")
        guardianname=request.form.get("guardianname")
        relation=request.form.get("relation")
        guardianemail=request.form.get("guardianemail")
        guardianmobile=request.form.get("guardianmobile")
        guardianaddress1=request.form.get("guardianaddress1")
        guardianaddress2=request.form.get("guardianaddress2")
        post=Form.query.filter_by(username=username).first()
        post.admissiontype=admissiontype
        post.section=section
        post.class1=class1
        post.division=division
        post.fee=fee
        post.caste=caste
        post.inhouse=inhouse
        post.board=board
        post.adhar=adhar
        post.studentname=studentname
        post.gender=gender
        post.studentemail=studentemail
        post.studentmobile=studentmobile
        post.birthdate=birthdate
        post.birthplace=birthplace
        post.natinality=natinality
        post.maritalstatu=maritalstatu
        post.mothertongue=mothertongue
        post.religion=religion
        post.address1=address1
        post.address2=address2
        post.location=location
        post.taluka=taluka
        post.district=district
        post.state=state
        post.country=country
        post.pincode=pincode
        post.fathername=fathername
        post.mothername=mothername
        post.parentemail=parentemail
        post.parentmobile=parentmobile
        post.parentaddress1=parentaddress1
        post.parentaddress2=parentaddress2
        post.parentlocation=parentlocation
        post.parenttaluka=parenttaluka
        post.parentdistrict=parentdistrict
        post.parentstate=parentstate
        post.parentcountry=parentcountry
        post.parentpincode=parentpincode
        post.guardianname=guardianname
        post.relation=relation
        post.guardianemail=guardianemail
        post.guardianmobile=guardianmobile
        post.guardianaddress1=guardianaddress1
        post.guardianaddress2=guardianaddress2
        data.session.commit()
        # return redirect(f"/")
    post=Form.query.filter_by(username=username).first()
    return render_template("admission2.html",college=college,para=para1,para1=para,admission=admission1,post=post)
   
@app.route('/file',methods=['GET','POST'])
def filefill():

    if request.method=="POST":
        with open("user1.txt",'r') as r2:
            username=r2.read()
        f1=request.files['file1']
        f2=request.files['file2']
        f3=request.files['file3']
        # os.rename( 'avi.jpg',f1.filename)
        f1.filename="1.jpg"
        f2.filename="2.jpg"
        f3.filename="3.jpg"
        print(f1.filename)
        f1.save(os.path.join(f"C:\\Users\\avina\\OneDrive\\Desktop\\Projects\\Exam\\static\\img\\{username}",secure_filename(f1.filename)))
        f2.save(os.path.join(f"C:\\Users\\avina\\OneDrive\\Desktop\\Projects\\Exam\\static\\img\\{username}",secure_filename(f2.filename)))
        f3.save(os.path.join(f"C:\\Users\\avina\\OneDrive\\Desktop\\Projects\\Exam\\static\\img\\{username}",secure_filename(f3.filename)))

        return render_template("admission1.html",college=college,para=para1,para1=para,admission=admission1,)

@app.route('/teacherlogin',methods=['GET','POST'])
def teacherlogin():
    # if(request.method=='POST'):
    #     name=request.form.get('name')
    #     title=request.form.get('title')
    #     content=request.form.get('content')
    #     entry=Homeblog(title=title,content=content,date=datetime.now(),name=name)
    #     data.session.add(entry)
    #     data.session.commit()
    return render_template('Exam1.html',college=college,point=point,para=para)


app.run(debug=True)