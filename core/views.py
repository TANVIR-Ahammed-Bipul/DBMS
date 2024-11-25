from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import File
from .forms import FileUploadForm
import logging

logger = logging.getLogger(__name__)

@login_required
def dashboard(request):
    """
    Displays the dashboard with a list of files uploaded by the logged-in user.
    """
    logger.debug(f"User: {request.user}, Authenticated: {request.user.is_authenticated}")
    # Fetch files uploaded by the logged-in user
    files = File.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'files': files})


@login_required
def upload_file(request):
    """
    Handles file uploads. Requires the user to be logged in.
    """
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.save(commit=False)
            file.user = request.user  # Associate the file with the current user
            file.save()
            messages.success(request, "File uploaded successfully!")
            return redirect('dashboard')  # Redirect to dashboard after upload
        else:
            messages.error(request, "Error uploading file. Please check the form.")
    else:
        form = FileUploadForm()  # Display an empty form for GET requests
    return render(request, 'upload.html', {'form': form})


def home(request):
    """
    Displays the home page. Accessible to everyone.
    """
    return render(request, 'home.html')
