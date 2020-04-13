from django.shortcuts import render,redirect
from .models import Cususer,Department,Book,Issuedbooks,IssuedHistorys
from django.contrib import messages
from django.contrib.auth.models import User

from django.core.paginator import Paginator
# Create your views here.

import json


def index(request):

    book = Book.objects.all().order_by('id')
    paginator = Paginator(book, 8)
    page = request.GET.get('page')
    book_page = paginator.get_page(page)
    count = len(book)

    if request.method == 'POST' and 'delete_id' in request.POST:
        id = request.POST.get('delete_id')
        print(id)
        obj = Book.objects.get(id=id)
        obj.delete()
        
    return render(request, 'library/index.html',
                    {
                    'book': book_page,
                    'count': count
                    })



    # book = Book.objects.all()
    # return render(request,'library/index.html',{'book':book})
    
def book(request):
    if request.method   ==   'POST':
        book_name       =    request.POST.get("book_name")
        stock           =    request.POST.get("stock")
        add             =    Book()
        add.book_name   =    book_name
        add.stock       =    stock
        add.save()
        print("Book Added")
        messages.info(request,'Book added successful')
        return redirect('book')
    else:
        return render(request,'library/addbook.html')


def addstudent(request):
    departments = Department.objects.all()
    if request.method == 'POST':
        profile         = request.FILES.get("profile")
        first_name      = request.POST.get("first_name")
        last_name       = request.POST.get("last_name")
        email           = request.POST.get("email")
        username        = request.POST.get("username")
        password1       = request.POST.get("password1")
        password2       = request.POST.get("password2")
        address         = request.POST.get("address")
        department      = request.POST.get("department")
        phonenumber     = request.POST.get("phonenumber")
        dob             = request.POST.get("dob")
          
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'user taken')
                return redirect('addstudent')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect('addstudent')
            else:

                user = User.objects.create_user(username=username,password=password1,email=email)
                user.save()

                cus = Cususer()
                cus.profile         =   profile
                cus.first_name      =   first_name
                cus.last_name       =   last_name
                cus.address         =   address
                cus.department      =   Department.objects.get(id=department)
                cus.phonenumber     =   phonenumber
                cus.dob             =   dob   
                cus.username        =   user
                cus.save()
                messages.info(request,'Student Add Successful')
                return redirect('addstudent')  
        else:
            messages.info(request,'Password not match')
            return redirect('addstudent')
        return redirect('addstudent')
    else:

        return render(request,'library/addstudent.html',{'departments':departments})


def profile_view(request):
    p=Cususer.objects.get(username_id=request.user.id)
    print(p)
    return render(request,'library/profile.html',{'p':p})


def view_books(request):
    boos = Book.objects.all()
    print(boos,'--------------------------------------')
    return render(request,'library/books.html',{'boos':boos})


def issuebook(request):

    book                =   Book.objects.all()
    student             =   Cususer.objects.all()
    b = ''

    #selected book ID 
    book1            =   request.POST.get("book")

    if request.method == 'POST' and 'submit' in request.POST:
        
        student1         =   request.POST.get("student")
        datetime         =   request.POST.get("datetime")
        a                =   Issuedbooks.objects.filter(username=student1)
        b                =   len(a)

        # stock   =   Book.objects.get(id=book1.id)
        # print(stock,'+++++++++++++++++++++++++++++++++++++++++++')

        



        if  b >= 2:
            messages.info(request,'This user already issued more than two times Please return Book and Issue new ')
            return redirect('issuebook')
        
        else:
            

            # saving all history to database
            history             =   IssuedHistorys()
            # get selected book id 
            bookname            =   Book.objects.get(id=book1)
            username            =   Cususer.objects.get(id=student1)
            # save  book id correspounding book name 
            history.book_name   =   bookname.book_name
            history.username    =   username.username.username
            history.datetime    =   datetime
            history.save()  


                    # Stock updation
            add_stock   = Book.objects.get(id=book1)
            add_stock.stock = add_stock.stock - 1 # changing stock


            if add_stock.stock <= -1:

                messages.info(request,'No stock available')
                return redirect('issuebook')

            else:

                add_stock.save()
                print('stock count changed successful')

                # issue a book that will save to database
                booked          =   Issuedbooks()
                booked.datetime =   datetime
                booked.book_name=   Book.objects.get(id=book1)
                booked.username =   Cususer.objects.get(id=student1)
                booked.save()
            
            
                messages.info(request,'Book Issue Completed ')
                return redirect('issuebook')
    else:
        
        issues        =   Issuedbooks.objects.all()
        return render(request,'library/issuebook.html',{'book':book,'student':student,'issues':issues})

    
def allhistorys(request):

    allhistorys          = IssuedHistorys.objects.all()
    return render(request,'library/allhistorys.html',{'allhistorys':allhistorys})


def returnbook(request):
    add    =12
    if request.method   ==  'POST':   
        drop            =   request.POST.get("issuedusername")
        Issued          =   Issuedbooks.objects.get(id=drop)
    
        # Stock Updation
        change_stock    = Book.objects.get(id=Issued.book_name.id)
        change_stock.stock  = change_stock.stock + 1
        change_stock.save()
        print("stock updations successful")

        # drop database data
        Issued.delete()
        messages.info(request,'Book Return Successful') 

        return redirect('returnbook')
        

    else:

        issues        =   Issuedbooks.objects.all()
        return render(request,'library/returnbook.html',{'issues':issues})





def mybooks(request,):

    # find logined user database and id
    logined_user   =   Cususer.objects.get(username_id=request.user.id)

    #find issued books datas and  filtering user 
    mybooks =   Issuedbooks.objects.filter(username_id=logined_user.id)
    return render(request,'library/mybooks.html',{'mybooks':mybooks})



def myhistory(request):
    logined_user    =   Cususer.objects.get(username_id=request.user.id)
    print(logined_user,'------------------------333333')
    historys        =   IssuedHistorys.objects.filter(username=logined_user)
    print(historys,'+-+----+777777777-')
    return render(request,'library/myhistory.html',{'historys':historys,})
    book_name       = Book.objects.get(id=historys)


def updateprofile(request):

    if request.method == 'POST':

        last_name   =   request.POST.get("last_name")
        phonenumber =   request.POST.get("phonenumber")
        email       =   request.POST.get("email")
        # password1   =   request.POST.get("password1")
        # password2   =   request.POST.get("password2")
        # img       =   request.POST.get("file")
        
        profile_data    =   Cususer.objects.get(username_id=request.user.id)
        profile_data.last_name  =   last_name
        profile_data.phonenumber=   phonenumber
        # profile_data.profile    =   img

        user        =   User.objects.get(id=request.user.id)
        user.email  =   email
        
        user.save()
        profile_data.save()
        print('User Updated')

        messages.info(request,'Profile Update Successful')
        return redirect('profile_view')

    else:
        return render(request,'library/updateprofile.html')

    
from django.http import JsonResponse    

def answer_me(request):
    print('----------------------------------------------------------------')

    a   =   '10'
    field = request.GET.get('inputValue')

    answer = a
    this    =   'this'
    yahoo   =   'yahoo'
    data = {
        'respond': answer,
        'this':this,
        'yahoo':yahoo,
            }
    return JsonResponse(data)



def selected_book_stock(request):
    selected_data = request.GET.get('selected_data')
    book          = Book.objects.get(id=selected_data)
    book_stock     = book.stock

    answer        = book_stock
    data          = {
        'respond':answer
    }
    return JsonResponse(data)
