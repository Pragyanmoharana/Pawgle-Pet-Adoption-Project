from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Pet, DonatePet  # ✅ make sure this line includes both
from .forms import DonatePetForm, CustomerRegistrationForm


def about(request):
    return render(request, 'adoption/about_us.html')
@login_required(login_url='login')
def donate_pet(request):
    if request.method == 'POST':
        form = DonatePetForm(request.POST, request.FILES)
        if form.is_valid():
            donation = form.save(commit=False)
            donation.user = request.user
            donation.save()
            messages.success(request, "Your donation request has been submitted. You’ll be notified once it's approved.")
            return redirect('my_donations')
    else:
        form = DonatePetForm()
    return render(request, 'adoption/donate_pet.html', {'form': form})

@login_required
def my_donations(request):
    donations = DonatePet.objects.filter(user=request.user)
    if donations.filter(is_converted=True).exists():
        messages.info(request, "Some of your pets have been approved and listed for adoption!")
    return render(request, 'adoption/my_donations.html', {'donations': donations})

def donate_success(request):
    return render(request, 'adoption/donate_success.html')

def home(request):
    species = request.GET.get('species', '')
    gender = request.GET.get('gender', '')

    pets = Pet.objects.filter(is_approved=True)

    if species:
        pets = pets.filter(species__iexact=species)
    if gender:
        pets = pets.filter(gender__iexact=gender)

    if not species and not gender:
        pets = []  # empty queryset

    return render(request, 'adoption/home.html', {
        'pets': pets,
    })


def pet_list(request):
    pets = Pet.objects.filter(is_approved=True)
    return render(request, 'adoption/pet_list.html', {
        'pets': pets,
    })
def pet_detail(request, pk):
    pet = get_object_or_404(Pet, pk=pk, is_approved=True)
    return render(request, 'adoption/pet_detail.html', {'pet': pet})

def adopt_pet(request, pk):
    pet = get_object_or_404(Pet, pk=pk, is_approved=True)

    if request.method == 'POST':
        messages.success(request, f'Adoption request sent for {pet.name}!')
        return redirect('home')

    return render(request, 'adoption/adopt_confirm.html', {'pet': pet})    

class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'adoption/customerregistration.html', {'form': form})
  
    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulations!! Registered Successfully.')
            form.save()
        return render(request, 'adoption/customerregistration.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'adoption/profile.html', {'user': request.user})


from .models import Pet, AdoptionRequest
from .forms import AdoptionRequestForm
@login_required
def adopt_pet(request, pk):
    pet = get_object_or_404(Pet, pk=pk, is_approved=True)

    if request.method == 'POST':
        form = AdoptionRequestForm(request.POST)
        if form.is_valid():
            adoption = form.save(commit=False)
            adoption.pet = pet
            adoption.user = request.user
            adoption.save()
            return redirect('adoption_submitted')
    else:
        form = AdoptionRequestForm()

    return render(request, 'adoption/adopt_confirm.html', {'pet': pet, 'form': form})

@login_required
def adoption_submitted(request):
    return render(request, 'adoption/adoption_submitted.html')

@login_required
def my_adoptions(request):
    requests = AdoptionRequest.objects.filter(user=request.user).order_by('-submitted_at')
    return render(request, 'adoption/my_adoptions.html', {'requests': requests})

@login_required
def cancel_adoption(request, pk):
    adoption = get_object_or_404(AdoptionRequest, pk=pk, user=request.user)
    if adoption.status == "Pending":
        adoption.status = "Cancelled"
        adoption.save()
        messages.success(request, "Your adoption request was cancelled.")
    return redirect('my_adoptions')
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def all_adoption_requests(request):
    from .models import AdoptionRequest
    requests = AdoptionRequest.objects.all().order_by('-submitted_at')
    return render(request, 'adoption/all_adoption_requests.html', {'requests': requests})

@staff_member_required
def update_adoption_status(request, pk):
    from .models import AdoptionRequest
    adoption = get_object_or_404(AdoptionRequest, pk=pk)
    if request.method == 'POST':
        new_status = request.POST.get('status')
        if new_status in dict(AdoptionRequest.STATUS_CHOICES):
            adoption.status = new_status
            adoption.save()
    return redirect('all_adoption_requests')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # You can also send mail here or store in database
        # send_mail(subject, message, from_email, [to_email], fail_silently=False)
        messages.success(request, "Thanks for reaching out! We’ll get back to you soon.")
        
    return render(request, 'adoption/contact.html')


