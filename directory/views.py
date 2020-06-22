from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse, HttpResponse
from .models import registerAdmin,register,subject_detail,bulk_register
from .forms import registerForm,admin_registerForm
from django.db import connection
from django.contrib import messages
# import the logging library
import logging
import re
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

# Create your views here.
def home(request):
    if 'userid' in request.session:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM directory_bulk_register")
        row = cursor.fetchall()
        row = list(row)
        print(row)
        data = []
        for item in row:
            item = list(item)
            data.append(list(item))
        for item in data:
            item[7]=list(item[7].split(","))
        return render(request, "home.html", {'all_teachers': data, 'userid': request.session['userid'],
                                                  'username': request.session['username']})
    else:
        return redirect("loginPage")
def row_wise(request):
    if 'userid' in request.session:
        # all_teachers = register.objects.filter()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM directory_subject_detail inner join directory_register on directory_subject_detail.user_ID_id=directory_register.user_ID")
        row = cursor.fetchall()
        return render(request, "row_wise.html", {'all_teachers': row, 'userid': request.session['userid'],
                                                  'username': request.session['username']})
    else:
        return redirect("loginPage")

def loginPage(request):
    return render(request,"login.html")

def registerPage(request):
    return render(request,"register.html")

def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    employeeobj = registerAdmin.objects.filter(email=username, password=password)
    if (employeeobj):
        request.session['userid'] = employeeobj[0].user_id
        request.session['username'] = employeeobj[0].username
        return JsonResponse({'result': request.session['userid'], 'username': request.session['username']})
    else:
        return JsonResponse({'result': 'No such entry', })

def logout(request):
    del request.session['userid']
    del request.session['username']
    return redirect("loginPage")
def profile(request,pk):
    if 'userid' in request.session:
        teacher = register.objects.get(user_ID=pk)
        all_subjects = subject_detail.objects.filter(user_ID=pk)
        return render(request, "profile.html", {'teacher': teacher,'all_subjects':all_subjects, 'userid': request.session['userid'],
                                                  'username': request.session['username']})
    else:
        return redirect("loginPage")

def bulk_profile(request,pk):
    if 'userid' in request.session:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM directory_bulk_register where user_ID='{0}';".format(pk))
        row = cursor.fetchall()
        row = list(row)
        data = []
        for item in row:
            item = list(item)
            data.append(list(item))
        print(data)
        data = data[0]
        print(data)
        data[7] = list(data[7].split(","))
        print(data)
        return render(request, "bulk_profile.html", {'data': data, 'userid': request.session['userid'],
                                                  'username': request.session['username']})
    else:
        return redirect("loginPage")

def delete(request,pk):
    if 'userid' in request.session:
        item = register.objects.get(user_ID=pk)
        item.delete()
        all_teachers = register.objects.filter()
        return render(request, "home.html", {'all_teachers': all_teachers, 'userid': request.session['userid'],
                                                  'username': request.session['username']})
    else:
        return redirect("loginPage")

def bulk_delete(request,pk):
    if 'userid' in request.session:
        item = bulk_register.objects.get(user_ID=pk)
        item.delete()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM directory_bulk_register")
        row = cursor.fetchall()
        row = list(row)
        data = []
        for item in row:
            item = list(item)
            data.append(list(item))

        for item in data:
            item[7] = list(item[7].split(","))
        return render(request, "home.html", {'all_teachers': data, 'userid': request.session['userid'],
                                                  'username': request.session['username']})
    else:
        return redirect("loginPage")

def deleteSubject(request,pk):
    if 'userid' in request.session:
        item = subject_detail.objects.get(subject_ID=pk)
        temp = item.user_ID
        item.delete()
        teacher = register.objects.get(user_ID=temp)
        all_subjects = subject_detail.objects.filter(user_ID=temp)
        return render(request, "profile.html",
                      {'teacher': teacher, 'all_subjects': all_subjects, 'userid': request.session['userid'],
                       'username': request.session['username']})
    else:
        return redirect("loginPage")

def importFile(request):
    if 'userid' in request.session:
        return render(request, "upload.html")
    else:
        return redirect("loginPage")

def upload_csv(request):
    if 'userid' in request.session:
        data = {}
        # if "GET" == request.method:
        #     return render(request, "home.html", data)
        # if not GET, then proceed
        try:
            csv_file = request.FILES["csv_file"]
            if not csv_file.name.endswith('.csv'):
                # messages.error(request, 'File is not CSV type')
                # return HttpResponseRedirect(reverse("myapp:upload_csv"))
                return render(request, "home.html")
            # if file is too large, return
            if csv_file.multiple_chunks():
                # messages.error(request, "Uploaded file is too big (%.2f MB)." % (csv_file.size / (1000 * 1000),))
                # return HttpResponseRedirect(reverse("myapp:upload_csv"))
                return render(request, "home.html")

            file_data = csv_file.read().decode("utf-8")

            lines = file_data.split("\n")
            # loop over the lines and save them in db. If error , store as string and then display
            for line in lines:
                fields = line.split(",")
                print("length of fields",len(fields))
                data_dict = {}
                data_subjects=[]
                if (re.search(regex,fields[3])):
                    data_dict["first_name"] = fields[0]
                    data_dict["last_name"] = fields[1]
                    data_dict["profile_pic"] = fields[2]
                    data_dict["email"] = fields[3]
                    data_dict["phone"] = fields[4]
                    data_dict["room_number"] = fields[5]
                    for x in range(6,len(fields)):
                        data_subjects.append(fields[x])
                    print(data_subjects,"-----",data_dict)
                    try:
                        form = registerForm(data_dict)
                        if form.is_valid():
                            form.save()
                            print("here")
                            item = register.objects.get(email=data_dict["email"])

                            list_length = len(data_subjects)
                            result = 5 - list_length
                            print(item.user_ID, "ID",result)
                            if(result<=0):
                                print("greater")
                                for x in range(5):
                                    data_subjects[x]=data_subjects[x].strip('"')
                                    obj = subject_detail(subject_name=(data_subjects[x]), user_ID=register.objects.get(user_ID=item.user_ID))
                                    obj.save()
                                    print("greater",obj)
                            else:
                                print("lesser")
                                for x in range(list_length):
                                    data_subjects[x] = data_subjects[x].strip('"')
                                    print(x,data_subjects[x])
                                    obj = subject_detail(subject_name=(data_subjects[x]), user_ID=register.objects.get(user_ID=item.user_ID))
                                    obj.save()
                                    print("lesser",obj)

                        else:
                            logging.getLogger("error_logger").error(form.errors.as_json())
                    except Exception as e:
                        logging.getLogger("error_logger").error(form.errors.as_json())
                        pass
            return redirect("home")
        except Exception as e:
            logging.getLogger("error_logger").error("Unable to upload file. " + repr(e))
            # messages.error(request, "Unable to upload file. " + repr(e))
            return redirect("home")
        # return HttpResponseRedirect(reverse("myapp:upload_csv"))
    else:
        return redirect("loginPage")

def search(request):
    if 'userid' in request.session:
        return render(request,"search.html")
    else:
        return redirect("loginPage")

def bulk_upload(request):
    if 'userid' in request.session:
        return render(request,"bulk_upload.html")
    else:
        return redirect("loginPage")

def add(request):
    if 'userid' in request.session:
        return render(request,"addTeacher.html")
    else:
        return redirect("loginPage")
def search_re(request):

    lastName = request.POST.get('lastName')
    subjectName = request.POST.get('subjectName')
    if(lastName=='' and subjectName==''):
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM directory_subject_detail inner join directory_register on directory_subject_detail.user_ID_id=directory_register.user_ID")
        row = cursor.fetchall()
    elif(lastName==''):
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM directory_subject_detail inner join directory_register on directory_subject_detail.user_ID_id=directory_register.user_ID WHERE directory_subject_detail.subject_name LIKE '{0}%';".format(subjectName))
        row = cursor.fetchall()
    elif(subjectName==''):
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM directory_subject_detail inner join directory_register on directory_subject_detail.user_ID_id=directory_register.user_ID WHERE directory_register.last_name LIKE '{0}%';".format(lastName))
        row = cursor.fetchall()
    else:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM directory_subject_detail inner join directory_register on directory_subject_detail.user_ID_id=directory_register.user_ID WHERE directory_register.last_name LIKE '{0}%' and directory_subject_detail.subject_name LIKE '{1}%';".format(lastName,subjectName))
        row = cursor.fetchall()

    return render(request, "row_wise.html", {'all_teachers': row, 'userid': request.session['userid'],
                                         'username': request.session['username']})

# def bilk_search_re(request):
#
#     lastName = request.POST.get('lastName')
#     subjectName = request.POST.get('subjectName')
#     if(lastName=='' and subjectName==''):
#         cursor = connection.cursor()
#         cursor.execute("SELECT * FROM directory_subject_detail inner join directory_register on directory_subject_detail.user_ID_id=directory_register.user_ID")
#         row = cursor.fetchall()
#     elif(lastName==''):
#         cursor = connection.cursor()
#         cursor.execute("SELECT * FROM directory_subject_detail inner join directory_register on directory_subject_detail.user_ID_id=directory_register.user_ID WHERE directory_subject_detail.subject_name LIKE '{0}%';".format(subjectName))
#         row = cursor.fetchall()
#     elif(subjectName==''):
#         cursor = connection.cursor()
#         cursor.execute("SELECT * FROM directory_subject_detail inner join directory_register on directory_subject_detail.user_ID_id=directory_register.user_ID WHERE directory_register.last_name LIKE '{0}%';".format(lastName))
#         row = cursor.fetchall()
#     else:
#         cursor = connection.cursor()
#         cursor.execute("SELECT * FROM directory_subject_detail inner join directory_register on directory_subject_detail.user_ID_id=directory_register.user_ID WHERE directory_register.last_name LIKE '{0}%' and directory_subject_detail.subject_name LIKE '{1}%';".format(lastName,subjectName))
#         row = cursor.fetchall()
#
#     return render(request, "home.html", {'all_teachers': row, 'userid': request.session['userid'],
#                                          'username': request.session['username']})

def upload_csv_bulk(request):
    if 'userid' in request.session:
        data = {}
        try:
            csv_file = request.FILES["csv_file"]
            if not csv_file.name.endswith('.csv'):
                return render(request, "home.html")
            # if file is too large, return
            if csv_file.multiple_chunks():
                return render(request, "home.html")
            file_data = csv_file.read().decode("utf-8")
            lines = file_data.split("\n")
            total_rows=[]
            for line in lines:
                if(line):
                    fields = line.split(",")
                    data_subjects=[]
                    subject_count = 1
                    if (re.search(regex,fields[3])):
                        for x in range(6, len(fields)):
                            if(subject_count<=5):
                                clean_text = fields[x].strip('"')
                                data_subjects.append(clean_text)
                                subject_count = subject_count + 1
                        subject_string = ",".join(data_subjects)
                        total_rows.append(bulk_register(email=(fields[3]),first_name=(fields[0]),last_name=(fields[1]),profile_pic=(fields[2]),
                                            phone=(fields[4]), room_number=(fields[5]),subjects=(subject_string))
                                          )
            bulk_register.objects.bulk_create(total_rows)
            return redirect("home")
        except Exception as e:
            logging.getLogger("error_logger").error("Unable to upload file. " + repr(e))
            return redirect("home")
    else:
        return redirect("loginPage")

def registeradmin(request):
    if request.method == "POST":
        adminForm = admin_registerForm(request.POST)
        if adminForm.is_valid():
            crew_password = request.POST.get('password')
            form = adminForm.save(commit=False)
            form.password = make_password(crew_password)
            form.save()
        return redirect("loginPage")