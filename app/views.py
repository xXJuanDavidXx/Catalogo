from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Profile
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, FormView
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from .forms import SignUpForm, ProfileForm
from django.template.loader import render_to_string
from django.core.mail import EmailMessage, send_mail
from django.conf import settings



#Copiar

def copiar(request):
    return render(request, 'copiar.html')



# Create your views here.

def list_products(request, user_id=None):
    producto = Product.objects.all()
    profile = None    
    if user_id:
        profile = get_object_or_404(Profile, user_id=user_id)
    else:
        profile = None
    
    return render(request, 'index.html', {'product': producto, 'profile': profile,'current_page':'catalogo'})



class SignUpView(CreateView):
    """
    Vista para el registro de usuarios.

    Esta vista maneja la visualización y el procesamiento del formulario de registro de usuarios.
    Al enviar el formulario correctamente, guarda el usuario, lo autentica y lo inicia sesión.

    Atributos:
        form_class (SignUpForm): La clase de formulario utilizada para el registro de usuarios.
        template_name (str): La ruta a la plantilla utilizada para renderizar el formulario.
        success_url (str): La URL a la que redirigir tras un registro exitoso.
    """

    form_class = SignUpForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('lista_lociones')


    def get_context_data(self, **kwargs):
        """
logout        Agrega `current_page` al contexto para usar en las plantillas.
        """
        context = super().get_context_data(**kwargs)
        context['current_page'] = 'signup'
        return context



    def form_valid(self, form):
        """
        Procesa una validación exitosa del formulario.

        Guarda el nuevo usuario, lo autentica y lo inicia sesión.
        """
        response = super().form_valid(form)
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        login(self.request, user)
        return response

class CustomLoginView(LoginView):
    """
    Vista para el inicio de sesión de usuarios.

    Esta vista maneja la visualización y el procesamiento del formulario de inicio de sesión.
    Al enviar el formulario correctamente, inicia sesión al usuario.

    Atributos:
        template_name (str): La ruta a la plantilla utilizada para renderizar el formulario.
        form_class (AuthenticationForm): La clase de formulario utilizada para el inicio de sesión.
    """

    template_name = 'registration/login.html'
    form_class = AuthenticationForm
    
    def get_context_data(self, **kwargs):
        """
        Agrega `current_page` al contexto para usar en las plantillas.
        """
        context = super().get_context_data(**kwargs)
        context['current_page'] = 'login'
        return context



    def form_valid(self, form):
        """
        Procesa una validación exitosa del formulario.

        Inicia sesión al usuario y redirige a la página de inicio.
        """
        user = form.get_user()
        login(self.request, user)
        return redirect('lista_lociones')



class index(TemplateView):
    template_name = 'index.html'







@login_required
def profile_edit(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = Profile(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('lista_lociones')  # O la vista a la que quieras redirigir después de guardar
    else:
        form = ProfileForm(instance=profile)

    # Genera el enlace al catálogo
    catalogo_url = request.build_absolute_uri(reverse('catalogo', args=[request.user.id]))

    return render(request, 'profile_edit.html', {'form': form, 'catalogo_url': catalogo_url})








#Eliminar
def profile_view(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'profile.html', {'profile': profile})

#---cerrar sesión
def singout(request):
    logout(request)
    return redirect('login')

# RECUPERAR CONTRASEÑA

# def passwordReset():
#     if request.method == "POST":
#        name = requets.POST["name"]
#        email = request.POST["email"]
#        subject = request.POST["subject"]
#        message = request.POST["message"]












