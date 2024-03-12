from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Contact


# Create your views here.
@login_required(login_url='login')
def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        subject = request.POST.get("subject")
        message = request.POST.get("message")



        en = Contact(
            name=name,
            email=email,
            phone=phone,
            subject=subject,
            message=message,

        )
        en.save()
    return render(request, "contact.html")

# def contact_view(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             message = form.cleaned_data['message']
#             ContactMessage.objects.create(name=name, email=email, message=message)
#             return redirect('contact')  # Redirect to a success page
#     else:
#         user = request.user
#         form = ContactForm(initial={'name': user.username, 'email': user.email})
    
#     return render(request, 'contact.html', {'form': form})
