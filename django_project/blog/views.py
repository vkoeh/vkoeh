
from django.shortcuts import render, get_object_or_404, redirect
from django_project.forms import ContactForm
from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.conf import settings

#added beginning: 

def home(request):
    return render(request, 'blog/home.html')

"""
def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts': posts})
"""
def about(request):
    return render(request, 'blog/about.html')



def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data
            return redirect('blog-success')
    else:
        form = ContactForm()
    return render(request, 'blog/contact.html', {'form': form})

#contact form to send email
"""
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']


            EmailMessage(
               'Contact Form Submission from {}'.format(name),
               message,
               'form-response@example.com', # Send from (your website)
               ['v.koeh@yahoo.de'], # Send to (your admin email)
               [],
               reply_to=[email] # Email from the form to get back to
           ).send()

            return redirect('blog-success')
    else:
        form = ContactForm()
    return render(request, 'blog/contact.html', {'form': form})
    """

def success(request):
    return render(request, 'blog/success.html')