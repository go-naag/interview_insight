# views.py

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
import random
from email.message import EmailMessage
import ssl
import smtplib
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse

def login(request):
    return render(request, 'login.html')


def send_otp(email):
    otp = str(random.randint(100000,999999))  # Generate a 6-digit OTP
    body = f'Your OTP is: {otp}'
    subject = 'Your OTP for Interview Insights'
    try:
        email_sender = 'interviewinsights37@gmail.com'
        email_password = 'ctxz seub ascd tcje'
        email_receiver = email
        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['Subject'] = subject
        em.set_content(body)
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())
    except Exception:
        return HttpResponse('''<h1 style='text-align:center'>Something went wrong. Please try again<h1>''')
    return otp


def verify_email(request):
    email = request.POST.get('emailid','')
    if request.method == 'POST' and email.endswith('@anurag.edu.in'):
        #email = request.POST.get('emailid', '')
        otp = send_otp(email)
        request.session['otp'] = otp
        request.session['email'] = email
        return render(request, 'verifylogin.html', {'otp_sent': True})
    else:
        messages.error(request, 'Please enter a valid email ending with @anurag.edu.in')
        return render(request,'login.html',{'invalid_email':True})


def verify_otp(request):
    if request.method == 'POST':
        otp_entered = request.POST.get('otp', '')
        if 'otp' in request.session:
            otp_generated = request.session['otp']
            if otp_entered == otp_generated:
                del request.session['otp']  # Clear OTP from session
                # If OTP is correct, redirect to a blank page or any desired page
                return render(request, 'home.html')
            else:
                messages.error(request, 'Invalid OTP. Please try again.')
                #return HttpResponseRedirect(request.path_info)  # Redirect back to the same page if OTP is invalid
                return render(request,'verifylogin.html',{'otp_sent':True,'invalid_otp':True})
        else:
            messages.error(request, 'OTP expired. Please request a new OTP.')
            return render(request, 'login.html', {'otp_sent':True, 'otp_expired':True})  # Redirect to enter OTP page if OTP is expired
            
    else:
        return HttpResponse('Method Not Allowed')


def logout_view(request):
    logout(request)
    # Redirect to a specific page after logout
    return redirect(reverse('login'))


def form_html(request):
    return render(request, 'form.html')

def home_html(request):
    companies = Company.objects.all()
    return render(request, 'home.html', {'companies': companies})


# views.py

# views.py

from django.shortcuts import render, redirect
from .models import Userdetails, Interview, Company

def add_interview(request):
    if request.method == 'POST':
        # Get form data
        name = request.POST.get('name')
        linkedin_url = request.POST.get('lp')
        branch = request.POST.get('branch')
        rollno = request.POST.get('rollno')
        year_of_passout = request.POST.get('year_of_passout')
        company_name = request.POST.get('cname')
        year_of_interview = request.POST.get('year_of_interview')
        role = request.POST.get('role')
        brief_description = request.POST.get('brief')
        selection_procedure = request.POST.get('selection')
        online_test_desc = request.POST.get('online')
        tech_interview_desc = request.POST.get('tr')
        hr_interview_desc = request.POST.get('hr')
        prep_resources = request.POST.get('resources')
        contact_no = request.POST.get('contact')
        
        # Get email from session
        email = request.session.get('email')

        # Create or get Interviewee object
        userdetails, created = Userdetails.objects.get_or_create(
            email=email,
            name = name,
            linkedin_url = linkedin_url,
            branch = branch,
            rollno = rollno,
            year_of_passout = year_of_passout,
            contact_no = contact_no
            
        )

        # Get or create Company object
        company, created = Company.objects.get_or_create(
            cname__iexact=company_name,
            defaults={'cname': company_name}
        )

        # Create Interview object
        interview = Interview.objects.create(
            user=userdetails,
            company=company,
            year_of_interview=year_of_interview,
            role=role,
            brief_description=brief_description,
            selection_procedure=selection_procedure,
            online_test_desc=online_test_desc,
            tech_interview_desc=tech_interview_desc,
            hr_interview_desc=hr_interview_desc,
            prep_resources=prep_resources
        )

        # Redirect to a success page or any other page
        return render(request,'form.html',{'submit':True})  # Change 'success_page' to your actual success page URL or name
    else:
        return render(request, 'your_template_name.html')  # Change 'your_template_name.html' to your actual template name





def companies(request):
    comp = Company.objects.all()
    return render(request, 'companies.html', {'comp':comp})



def company_detail(request, company_name):
    # Perform the query
    stusers = Userdetails.objects.filter(interview__company__cname__iexact=company_name).values('name', 'rollno', 'branch','id')

    # Pass the data to the template or process it further
    #context = {'users_under_company': users_under_company}
    return render(request, 'students.html', {'stusers':stusers})



from django.shortcuts import get_object_or_404


def user_detail(request, user_id):
    # Fetch the user details from the database
    user = get_object_or_404(Userdetails, pk=user_id)

    # Pass the user object to the template
    return render(request, 'user_details.html', {'user': user})
def search_companies(request):
    if 'company' in request.GET:
        company_name = request.GET['company']
        companies = Company.objects.filter(cname__istartswith=company_name)
    else:
        companies = Company.objects.all()
    return render(request, 'home.html', {'companies': companies})

def search_company_students_home(request):
    if 'company' in request.GET:
        company_name = request.GET['company']
        return company_detail(request, company_name)
from .models import * 
from .forms import * 

def community(request):
    forums=forum.objects.all()
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())
 
    context={'forums':forums,
              'count':count,
              'discussions':discussions}
    return render(request,'community.html',context)
 
from django.shortcuts import render, redirect
from .models import Userdetails, Interview, Company, forum
from .forms import CreateInForum, CreateInDiscussion

def addInForum(request):
    form = CreateInForum()
    if request.method == 'POST':
        form = CreateInForum(request.POST)
        if form.is_valid():
            # Create an instance of the forum object but exclude email field
            forum_instance = form.save(commit=False)
            # Set the email field from session data
            forum_instance.email = request.session.get('email')
            forum_instance.save()
            return redirect('community')
    context = {'form': form}
    return render(request, 'addInForum.html', context)

 
def addInDiscussion(request):
    form = CreateInDiscussion()
    if request.method == 'POST':
        form = CreateInDiscussion(request.POST)
        if form.is_valid():
            discussion_instance = form.save(commit=False)
            # Set the email field from session data
            discussion_instance.email = request.session.get('email')
            discussion_instance.save()
            
            return redirect('community')
    context ={'form':form}
    return render(request,'addInDiscussion.html',context)