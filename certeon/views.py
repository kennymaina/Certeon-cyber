from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect

from .forms import ContactForm
from django import template
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.views.generic import View
from .utils import render_to_pdf
from .forms import  NewsLetterForm
from django.core.mail import send_mail
from . models import NewsLetterRecipients
from django.contrib.auth.decorators import login_required
from .forms import NewsLetterForm


# Create your views here.
# @login_required(login_url='/accounts/login/')
def home(request):
    return render(request, 'home.html')



def contact(request):
    # current_user = request.user
    # w= Profile.objects.all()
    # return render(request, 'home.html',locals())
    return render(request, 'contact.html')


def about(request):
    # current_user = request.user
    # w= Profile.objects.all()
    # return render(request, 'home.html',locals())
    return render(request, 'about.html')

def great(request):
    # current_user = request.user
    # w= Profile.objects.all()
    # return render(request, 'home.html',locals())
    return render(request, 'great.html')


def download(request):
    # current_user = request.user
    # w= Profile.objects.all()
    # return render(request, 'home.html',locals())
    return render(request, 'download.html')


def offer(request):
    # current_user = request.user
    # w= Profile.objects.all()
    # return render(request, 'home.html',locals())
    return render(request, 'offer.html')





def contact(request):
    form = ContactForm()

    # new logic!
    if request.method == 'POST':
        form = ContactForm(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
            , '')
            contact_email = request.POST.get(
                'contact_email'
            , '')
            form_content = request.POST.get('content', '')

            # Email the profile with the
            # contact information
            template = get_template('contact_template.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            }
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" +'',
                ['kemaina2022@gmail.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            return redirect('contact')

    return render(request, 'contact.html', {
        'form': form,
    })





def generate_view(request, *args, **kwargs):
    template = get_template('download.html')
    context = {
            'invoice_id': 123,
            'today': 'Today', 
            'amount': 9939.99,
        'customer_name': 'kenny',
    }
    html = template.render(context)
    return HttpResponse(html)


def newsletter(request):
    if request.method == 'POST':
        form = NewsUserForm(request.POST)
        if form.is_valid():
            instance = form.save()
        else:
                print('your email is already added to our database')
                send_mail('this is certeon technologies', 'welcome', 'mail@achiengcindy.com',[instance.email], fail_silently=False) 
    return render(request, 'subscribe.html', {})






def news(request):
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            instance = form.save()
            recipient = NewsLetterRecipients(name = name,email =email)
            recipient.save()
            HttpResponseRedirect('news')
    else:
        form = NewsLetterForm()
    return render(request, 'subscription.html',{"letterForm":form})

