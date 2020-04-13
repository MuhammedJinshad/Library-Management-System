# from django.shortcuts import render,redirect
# from django.contrib.auth import login, authenticate
# from baseuser.froms import RegistrationFrom



# def home(request):
#     return render(request,'baseuser/home.html')



# def Registration_view(request):
#     context =   {}
#     if request.POST:
#         form    =   RegistrationFrom(request.POST)
#         if form.is_valid():
#             form.save()
#             email   =   form.cleaned_data.get('email')
#             raw_password   =   form.cleaned_data.get('password1')
#             baseuser       =   form.cleaned_data.get('email')
#             baseuser       =   authenticate(email=email,password=password1)
#             login(request,account)
#             return redirect('home')

#         else:
#             context['registration_form']    =   form
#     else:
        
#         form = RegistrationFrom()
#         context['registration_form']    =   form
#     return render(request,'baseuser/baseuser.html',context)



