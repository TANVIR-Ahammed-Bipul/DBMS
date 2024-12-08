from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum
from .models import File, DataItem
from .forms import FileUploadForm, DataItemForm
import logging
from django.forms import ModelForm

logger = logging.getLogger(__name__)

# Dashboard View with file list and aggregate sum of file sizes
@login_required
def dashboard(request):
    """
    Displays the dashboard with a list of files uploaded by the logged-in user
    and the total file size of the uploaded files.
    """
    logger.debug(f"User: {request.user}, Authenticated: {request.user.is_authenticated}")
    
    # Fetch files uploaded by the logged-in user
    files = File.objects.filter(user=request.user)
    
    # Calculate the total file size using aggregate Sum
    total_size = files.aggregate(Sum('file_size'))['file_size__sum'] or 0
    
    return render(request, 'dashboard.html', {'files': files, 'total_size': total_size})

# File Upload View
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

# Home Page View
def home(request):
    """
    Displays the home page. Accessible to everyone.
    """
    return render(request, 'home.html')

# DataItem CRUD operations
class DataItemForm(ModelForm):
    class Meta:
        model = DataItem
        fields = ['title', 'description']

@login_required
def item_list(request):
    items = DataItem.objects.filter(user=request.user)  
    return render(request, 'list_items.html', {'items': items})

@login_required
def create_item(request):
    if request.method == 'POST':
        form = DataItemForm(request.POST)
        if form.is_valid():
            data_item = form.save(commit=False)
            data_item.user = request.user
            data_item.save()
            return redirect('item_list')
    else:
        form = DataItemForm()
    return render(request, 'create_item.html', {'form': form})

@login_required
def update_item(request, pk):
    item = get_object_or_404(DataItem, pk=pk, user=request.user)
    if request.method == 'POST':
        form = DataItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = DataItemForm(instance=item)
    return render(request, 'update_item.html', {'form': form})

@login_required
def delete_item(request, pk):
    item = get_object_or_404(DataItem, pk=pk, user=request.user)
    if request.method == 'POST':
        item.delete()
        return redirect('item_list')
    return render(request, 'delete_item.html', {'item': item})

# Joined View (for related models)
@login_required
def joined_view(request):
    """
    Example: Join File with DataItem (or any related model)
    """
    # Fetch related data using select_related or prefetch_related if applicable
    items = File.objects.select_related('data_item').filter(user=request.user)  # Adjust 'data_item' to your actual related field
    return render(request, 'joined_template.html', {'items': items})
