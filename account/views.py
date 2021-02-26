from django.shortcuts import render, redirect
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import login, logout
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from .forms import RegistrationForm, UserEditForm
from .models import Account
from .token import account_activation_token
from django.contrib.auth.decorators import login_required
# Create your views here.
'''class UserDetailView(DetailView):
    model = Account
    template_name = "account/profile2.html"
    queryset = Account.objects.all()
    context = {'qs.username' : queryset}'''
@login_required
def edit_details(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)

        if user_form.is_valid():
            user_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
        
    return render(request, 'account/user/edit_details.html', {'user_form':user_form})

def account(request):
    return render(request, "account/profile.html")

def dashboard(request):
    return render(request, "account/dashboard.html")

'''def registration_view(request):
    context = {}
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            #email = form.cleaned_data.get('email')
            #raw_password = form.cleaned_data.get('password1')
            #account = authenticate(email=email, password=raw_password)
            #login(request, account)
            form.save()
            return redirect('home')
        else: #if not valid
            context['registration_form'] = form
    else:#if request.method == 'GET'
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'account/register.html', context)'''

def account_register(request):
    #if request.user.is_authenticated:
        #return redirect('account:dashboard')
    
    if request.method == 'POST':
        registerForm = RegistrationForm(request.POST)
        if registerForm.is_valid():
            user = registerForm.save(commit=False)
            user.email = registerForm.cleaned_data['email']
            user.set_password(registerForm.cleaned_data['password'])
            user.is_active = False
            user.save()
            #setup email
            current_site = get_current_site(request)
            subject = 'Activate your Account'
            message = render_to_string('account/registration/account_activation_email.html',{
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            
            user.email_user(subject=subject, message=message)
            return HttpResponse('registered successfully and activation sent')
    else:
        registerForm = RegistrationForm()
    return render(request, 'account/registration/register.html',{'form': registerForm})

def account_activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = Account.objects.get(pk = uid)
    except(TypeError, ValueError, OverflowError, user.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('account:dashboard')
    else:
        return render(request, 'account/registration/activation_invalid.html')
#def login_view(request):
    #form = LoginForm(request.post or None)
    #if form.is_valid():
    #    email = form.cleaned_data.get("email")
    #    password = form.cleaned_data.get("password")
    #    user = authenticate(request, email = email, password = password)
#
    #    if user != None:
     #       login(request, user)
    #        return redirect("/")
    #        # attempt = request.session.get("attempt") or 0
    #        # request.session['attempt'] = attempt + 1
            #return redirect("/invalid-password")
    #    else:
    #        request.session['invalid_user'] = 1
    #        return render(request, "dashboard.html", {"form": form, "invalid_user": True})
        
    #return render(request, "forms.html", {"form": form})

#def logout_view(request):
    #logout(request)
    #return redirect('/login')
