from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import File

@receiver(post_save, sender=File)  # Replace YourModel with the actual model name
def update_file_size(sender, instance, created, **kwargs):
    """
    Update the file size after saving the instance.
    This method prevents recursive save calls by checking if the instance is already saved.
    """
    if created:  # Only run if the instance was just created
        return
    
    # Logic to update file size
    instance.size = instance.file.size  # Example: Update the 'size' field with file's size
    
    # Save the instance without triggering the signal again
    instance.save(update_fields=['size'])  # Use update_fields to save only the specific field
