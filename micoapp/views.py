
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth import login as auth_login
from.models import *

from micoapp.models import Doctor


# Create your views here.
def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def index(request):
    if not request.user.is_staff:
        return redirect('login')
    doctors = Doctor.objects.all()
    patients = Patient.objects.all()
    appointments = Appointment.objects.all()


    d = 0;
    p = 0;
    a = 0;
    for i in doctors:
        d+=1
    for i in patients:
        p +=1
    for i in appointments:
        a +=1
    d1 = {'d':d, 'p':p, 'a':a}
    return render(request, 'index.html')


def login_view(request):
    error = ""
    if request.method == "POST":
        U = request.POST['username']
        P = request.POST['password']



        # Authenticate the user
        user = authenticate(username=U, password=P)

        print("Authenticated user:", user)  # Debugging line

        if user is not None:
            # Check if the user is a staff member before logging them in
            if user.is_staff:
                auth_login(request, user)  # Correctly passing both arguments
                return redirect('index')  # Redirect to the index page if login is successful
            else:
                error = "You do not have admin privileges."
        else:
            error = "Invalid username or password."

    d = {'error': error}
    return render(request, 'login.html', d)




def logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return redirect('login')

def view_doctor(request):
    if not request.user.is_staff:
        return redirect('login')
    doc = Doctor.objects.all()
    d = {'doctor': doc}
    return render(request, 'view_doctor.html', d)


from django.shortcuts import render, redirect
from .models import Doctor


def add_doctor(request):
    error = ""

    # Check if the user is an admin (staff)
    if not request.user.is_staff:
        return redirect('login')

    # Check if the form is being submitted via POST
    if request.method == "POST":
        n = request.POST.get('name')
        m = request.POST.get('mobile')
        s = request.POST.get('specialization')

        # Try to find a doctor with the same username, contact, and specialization
        try:
            # If a doctor with the same details exists, set error message
            Doctor.objects.get(name=n, mobile=m, specialization=s)
            error = "Doctor with these details already exists."
        except Doctor.DoesNotExist:
            # No doctor found, proceed to save the new doctor (if needed)
            error = "Doctor added successfully."
            # You might want to add logic to save the new doctor here, like:
            # Doctor.objects.create(username=n, contact=c, specialization=s)

    # Pass the error message to the template for rendering
    return render(request, 'add_doctor.html', {'error': error})



def delete_doctor(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    doctor = Doctor.objects.get(id=pid)
    doctor.delete()
    return redirect('view_doctor')

def view_patient(request):
    if not request.user.is_staff:
        return redirect('login')
    pat = Patient.objects.all()
    d = {'pat':pat}
    return render(request, 'view_patient.html', d)

from django.shortcuts import render, redirect
from .models import Patient

def add_patient(request):
    error = ""

    # Check if the user is an admin (staff)
    if not request.user.is_staff:
        return redirect('login')

    # Check if the form is being submitted via POST
    if request.method == "POST":
        n = request.POST.get('username')
        g = request.POST.get('gender')
        m = request.POST.get('mobile')
        a = request.POST.get('address')

        # Check if a patient with the same mobile or username already exists
        if Patient.objects.filter(mobile=m).exists():
            error = "A patient with this mobile number already exists."
        elif Patient.objects.filter(username=n).exists():
            error = "A patient with this username already exists."
        else:
            # No duplicate found, proceed to save the new patient
            Patient.objects.create(username=n, gender=g, mobile=m, address=a)
            error = "Patient added successfully."
            return redirect('patient_list')

            # Pass the error message to the template for rendering
    return render(request, 'add_patient.html', {'error': error})





def delete_patient(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    pat = Patient.objects.get(id=pid)
    pat.delete()

    return redirect('view_patient')

def view_appointment(request):
    if not request.user.is_staff:
        return redirect('login')
    appoint = Appointment.objects.all()
    d = {'appoint':appoint}
    return render(request, 'view_appointment.html', d)


from django.shortcuts import render, redirect
from .models import Appointment, Doctor, Patient


def add_appointment(request):
    error = ""

    # Check if the user is an admin (staff)
    if not request.user.is_staff:
        return redirect('login')

    # Get all doctors and patients
    doctor1 = Doctor.objects.all()
    patient1 = Patient.objects.all()

    # Check if the form is being submitted via POST
    if request.method == "POST":
        d = request.POST.get('doctor')
        p = request.POST.get('patient')
        d1 = request.POST.get('date')  # Ensure this is the correct field
        t = request.POST.get('time')

        # Check if doctor and patient exist in the database
        doctor = Doctor.objects.filter(name=d).first()
        patient = Patient.objects.filter(name=p).first()

        # Handle case if doctor or patient is not found
        if not doctor:
            error = "Doctor not found."
        elif not patient:
            error = "Patient not found."
        else:
            # If doctor and patient exist, check if the appointment already exists
            try:
                # Ensure you're using 'date1' instead of 'date'
                Appointment.objects.get(doctor=doctor, patient=patient, date1=d1, time1=t)
                error = "Appointment with these details already exists."
            except Appointment.DoesNotExist:
                # Create a new appointment
                Appointment.objects.create(doctor=doctor, patient=patient, date1=d1, time1=t)
                error = "Appointment added successfully."

    # Prepare context data
    context = {'doctor': doctor1, 'patient': patient1, 'error': error}

    # Pass the context to the template
    return render(request, 'add_appointment.html', context)


# from django.shortcuts import render, redirect
# from .models import Doctor
# def add_appointment(request):
#     error = ""
#
#     # Check if the user is an admin (staff)
#     if not request.user.is_staff:
#         return redirect('login')
#     doctor1 = Doctor.objects.all()
#     patient1 = Patient.objects.all()
#
#     # Check if the form is being submitted via POST
#     if request.method == "POST":
#         d = request.POST.get('doctor')
#         p = request.POST.get('patient')
#
#         d1 = request.POST.get('date')
#         t = request.POST.get('time')
#         doctor = Doctor.objects.filter(name=d).first()
#         patient = Patient.objects.filter(name=p).first()
#
#         # Try to find a doctor with the same username, contact, and specialization
#         try:
#             # If a doctor with the same details exists, set error message
#             Appointment.objects.get(doctor=doctor, patient=patient, date=d1, time=t)
#             error = "Appointment with these details already exists."
#         except Appointment.DoesNotExist:
#             # No doctor found, proceed to save the new doctor (if needed)
#             error = "Appointment added successfully."
#             # You might want to add logic to save the new doctor here, like:
#             # Doctor.objects.create(username=n, contact=c, specialization=s)
#     d = {'doctor':doctor1,'patient':patient1,'error':error}
#     # Pass the error message to the template for rendering
#     return render(request, 'add_appointment.html', {'error': error})
#


def delete_appointment(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    appoint = Appointment.objects.get(id=pid)
    appoint.delete()
    return redirect('view_appointment')





