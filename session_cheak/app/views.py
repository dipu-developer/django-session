from django.shortcuts import render

def settestcookie(request):
    # its cheak the user brower that the All cookie is is enable or not if enale it return the True otherwise False  
    request.session.set_test_cookie()
    return render(request,'settestsession.html')

def cheaktestcookie(request):
    # if the user allow the cookie in browser  and its run after set test cookies
    print(request.session.test_cookie_work())       #it return the true or false 
    # we can see in the terminal True or False 
    return render(request,'cheaktestsession.html')

def deltestcookie(request):
    request.session.set_test_cookie()
    return render(request,'settestsession.html')   
