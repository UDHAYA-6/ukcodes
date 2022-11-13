from django.shortcuts import render, redirect
from .models import Course, Learner, Instructor, Staff
import random , datetime , smtplib
from datetime import timedelta
from django.contrib.auth.models import User


def home(request):
    return render(request, "home.html")


def Learn(request):
    return render(request, 'Leaners_login.html')


def Instruct(request):
    return render(request, 'Instructor_login.html')


def courses(request):
    mycourse = Course.objects.all()
    return render(request, 'courses.html', {"courses": mycourse})


def terms(request):
    return render(request, "conditons.html")


def earnings(request):
    return render(request, "earning.html")



def pay(request):
    if request.method == 'POST':
        v1 = request.POST.get('feild1')
        v2 = request.POST.get('feild2')
        v3 = request.POST.get('feild3')
        v4 = request.POST.get('feild4')
        v5 = request.POST.get('feild5')
        v6 = request.POST.get('feild6')
        v7 = request.POST.get('feild7')
        v8 = request.POST.get('feild8')
        v9 = request.POST.get('feild9')
        v11 = request.POST.get('s_date')
        request.session['End']=v11
        s = v11
        user = Learner.objects.filter(Email=v3)
        v10="s"
        request.session['email']=v3
        for i in range(3):
            rand = random.randint(0, 9)
            v10 = v10 + str(rand)
        v10 = v10 + v1[-1]
        if user:
            message = "User already exist"
            return render(request, "enrollment.html", {"msg": message})

        else:
            object_learn = Learner()
            object_learn.Name = v1
            object_learn.Gender = v2
            object_learn.Email = v3
            object_learn.DoB = v4
            object_learn.Profession = v5
            object_learn.Country = v6
            object_learn.Number = v7
            object_learn.Course = v8
            object_learn.Language = v9
            object_learn.Password = v10
            object_learn.start = s
            object_learn.save()
            return render(request, 'payments.html')


def success(request):
    v3 = request.session['email']
    filter = Learner.objects.filter(Email=v3)
    data = Instructor.objects.filter(Status='Approved')
    Nam = Learner.objects.only('Name').get(Email=v3).Name
    Cou = Learner.objects.only('Course').get(Email=v3).Course
    pas = Learner.objects.only('Password').get(Email=v3).Password
    jn = Learner.objects.only('joined_on').get(Email=v3).joined_on
    t = jn + timedelta(3)
    st=t.strftime('%d/%m/%y')
    request.session['sto']=st
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login("shopskill.learn@gmail.com", "wwpk mkoh ecwv vxzq")
    server.sendmail("shopskill.learn@gmail.com", v3,
                        "\nHey!" + " " + "\n" + Nam + " " + "You payment for the course " + Cou + " has been successfully completed."
                        +" \n Your course will be commence on"+ st
                        + " " + "Here is your username and password for your course."
                        + "  " + "\n Username: " + v3 + "\n Password: " + pas
                        + " " + "\nThrough which you can directly log in to our website no need to register again."
                        + " " + "Or  you can directly log in to your account by clicking http://Shopskill.learn.com"
                        + " " + "For any queries mail at shopskill.learn@gmail.com our team will respond you"
                        + " " + "shortly. \n Thank You.")
    return render(request,"thank_you.html", {"data":data})



def done1(request):
    st = request.session['sto']
    if request.method=="POST":
        staff_id = request.POST.get('pok')
        v3 = request.session['email']
        Lname = Learner.objects.only('Name').get(Email=v3).Name
        Lcourse = Learner.objects.only('Course').get(Email=v3).Course
        filter = Learner.objects.filter(Email=v3)
        filter.update(Staff=staff_id)
        ins = Instructor.objects.filter(Email=staff_id)
        n = Instructor.objects.only('Name').get(Email=staff_id).Name
        p = Instructor.objects.only('Password').get(Email=staff_id).Password
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login("shopskill.learn@gmail.com", "wwpk mkoh ecwv vxzq")
        server.sendmail("shopskill.learn@gmail.com", staff_id,
                        "Hey "+n+"\n"+Lname+" has chosen you as an instructor for the course "+Lcourse+
                        "We have scheduled the course on"+st+"\nYou can log in to our site using your email and password"
                        +"\nEmail: "+ staff_id
                        +"\nPassword: "+p+
                        "\n Happy Learning."
                        + " " + "For any queries mail at shopskill.learn@gmail.com our team will respond you"
                        + " " + "shortly. \n Thank You."
                        )
    return render(request,"done1.html")


def regdone(request):
    if request.method == "POST":
        f1 = request.POST.get('form1')
        f2 = request.POST.get('form2')
        f3 = request.POST.get('form3')
        f4 = request.POST.get('form4')
        f5 = request.POST.get('form5')
        f6 = request.POST.get('form6')
        f7 = request.POST.get('form7')
        f8 = request.POST.get('form8')
        f12 = request.POST.get('form12')
    if len(request.FILES) != 0:
        f9 = request.FILES.get('form9')
        f10 = request.FILES.get('form10')
        f11 = request.FILES.get('form11')
        user1 = Instructor.objects.filter(Email=f3)
        if user1:
            message = "User already exist"
            return render(request, "earning.html", {"msg": message})
        else:
            server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
            server.login("shopskill.learn@gmail.com", "wwpk mkoh ecwv vxzq")
            server.sendmail("shopskill.learn@gmail.com", f3,
                            "Hey" + " " + f1 + " " + "You have successfully registered to shop skill earning community"
                            + " " + "Your application will be verified in 3 to 4 business days."
                            + "  " + "Once all your certifications are verified, you will be provided a password"
                            + " " + "through which you can directly login to our website no need to register again"
                            + " " + "For any queries mail at shopskill.learn@gmail.com our team will respond you "
                            + " " + "shortly. \n Thank You.")
            pas = "L"
            for i in range(3):
                rand = random.randint(0, 9)
                pas = pas + str(rand)
            pas = pas + f1[-1]
            object_Instruct = Instructor()
            object_Instruct.Name = f1
            object_Instruct.Gender = f2
            object_Instruct.Email = f3
            object_Instruct.Country = f4
            object_Instruct.Contact = f5
            object_Instruct.Course = f6
            object_Instruct.Qualification = f7
            object_Instruct.Language = f8
            object_Instruct.Graduate = f9
            object_Instruct.Experience = f10
            object_Instruct.Profile = f11
            object_Instruct.Password = pas
            object_Instruct.Bio = f12
            object_Instruct.save()
            return render(request, "reg done.html", {"name": f1})


def enrol(request):
    if request.method == "GET":
        course = request.GET.get('pass')
        return render(request, "enrollment.html", {"cor": course})


def welcome_learn(request):
    if request.method == "POST":
        term1 = request.POST.get('email1')
        term2 = request.POST.get('pass1')
        valid1 = Learner.objects.filter(Email=term1)
        valid2 = Learner.objects.filter(Password=term2)
        if valid1 and valid2:
            p_k1 = Learner.objects.get(Email=term1)
            p_k2 = Learner.objects.get(Password=term2)
            if p_k1.pk == p_k2.pk:
                data = Learner.objects.filter(Email=term1)
                c_name = Learner.objects.only('Course').get(Email=term1).Course
                join = Learner.objects.only('joined_on').get(Email=term1).joined_on
                week = int(Course.objects.only('Duration').get(Course_Name=c_name).Duration)
                Start = Learner.objects.only('Start').get(Email=term1).Start
                End2 = Start + timedelta(week*7)
                days = End2-Start
                day = days.days
                data1 = Course.objects.filter(Course_Name=c_name)
                return render(request, "Welcome learner.html", {"data":data,"data1":data1,"Start":Start,"End":End2,"Days":day,"weeks":week})
            else:
                message = "Email/Password incorrect"
                return render(request, "Leaners_login.html", {"msg": message})
        else:
            message = "Records not found!"
            return render(request, "Leaners_login.html", {"msg":message})


def welcome_earn(request):
    if request.method=="POST":
        t1 = request.POST.get('email2')
        t2 = request.POST.get('pass2')
        validation1 = Instructor.objects.filter(Email=t1)
        if validation1:
            validation2 = Instructor.objects.filter(Password=t2)
            if validation2:
                p_k1 = Instructor.objects.get(Email=t1)
                p_k2 = Instructor.objects.get(Password=t2)
                if p_k1.pk == p_k2.pk:
                    name = Instructor.objects.filter(pk=p_k1.pk)
                    em = Instructor.objects.only('Email').get(pk=p_k1.pk).Email
                    learn = Learner.objects.filter(Staff=em)
                    c_name = Learner.objects.only('Course').get(Staff=em).Course
                    course = Course.objects.filter(Course_Name=c_name)
                    week = int(Course.objects.only('Duration').get(Course_Name=c_name).Duration)
                    Start = Learner.objects.only('Start').get(Staff=em).Start
                    End2 = Start + timedelta(week*7)
                    return render(request,"Welcome instructor.html", {"Name":name, "learn":learn, "course":course ,"End":End2})
                else:
                    message = "Email/password incorrect"
                    return render(request,"Instructor_login.html", {"msg": message})
        else:
            message = "No records found"
            return render(request, "Instructor_login.html", {"msg": message})


def staff(request):
    return render(request, "staff.html")


def verify(request):
    datas = Instructor.objects.all()
    if request.method == "POST":
        email = request.POST.get('nm2')
        pas = request.POST.get('pa2')
        auth = Staff.objects.filter(Staff_Name=email)
        if auth:
            auth2 = Staff.objects.filter(Password=pas)
            if auth2:
                id1 = Staff.objects.get(Staff_Name=email)
                id2 = Staff.objects.get(Password=pas)
                if id1.pk == id2.pk:
                    return render(request, "verify.html", {"datas":datas})
                else:
                    message = "Email/Password incorrect"
                    return render(request, 'staff.html', {"msg": message})

            else:
                message = "Password incorrect"
                return render(request, 'staff.html', {"msg": message})
        else:
            message = "No records found"
            return render(request, 'staff.html', {"msg": message})


def approve(request):
    if request.method == 'POST':
        instructor = Instructor.objects.filter(pk=request.POST.get("pk"))
        instructor.update(Status="Approved")
        datas = Instructor.objects.all()
        return render(request, 'verify.html', {"datas": datas})

def reject(request):
    if request.method == 'POST':
        instructor = Instructor.objects.filter(pk=request.POST.get("pk"))
        instructor.update(Status="Rejected")
        datas = Instructor.objects.all()
        return render(request, 'verify.html', {"datas": datas})


def paired(request):
    datas= Learner.objects.exclude(Staff__isnull=True)
    return render(request,"paired.html",{"datas":datas})




