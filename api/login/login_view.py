from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib import messages


# View for login
def login_views(request):
    template_name = "auth-login-basic.html"

    # Verificar si el usuario ya está autenticado
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")

    return render(request, template_name)

def register_view(request):
    template_name = "register.html"
    
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password != confirm_password:
            messages.error(request, "The passwords do not match.")
            return render(request, template_name)

        if User.objects.filter(username=username).exists():
            messages.error(request, "The username is already in use.")
            return render(request, template_name)
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "The email is already in use")
            return render(request, template_name)

        user = User(
            username=username, 
            email=email, 
            password=make_password(password),
            is_active = 0
            )
        user.save()
        messages.success(request, "Account successfully created.")
    return render (request,template_name)




def forgot_view(request):
    if request.method == 'POST':
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            # Aquí puedes implementar la lógica para enviar un correo electrónico
            # para la recuperación de la contraseña, por ejemplo, generando un token.
            messages.success(request, 'Si el correo existe, hemos enviado un enlace para restablecer tu contraseña.')
            return redirect('login')  # Redirige a la página de inicio de sesión
    else:
        form = ForgotPasswordForm()

    return render(request, 'forgot_password.html', {'form': form})


def logout_view(request):
          logout(request)
          return redirect('login')
