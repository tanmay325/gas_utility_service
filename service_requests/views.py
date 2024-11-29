from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import ServiceRequest
from .forms import ServiceRequestForm

@login_required
def create_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user
            service_request.save()
            print("Service request saved to database")
            messages.success(request, 'Service request submitted successfully!')
            return redirect('track_request', request_id=service_request.id)
    else:
        form = ServiceRequestForm()
    return render(request, 'service_requests/create_request.html', {'form': form})
@login_required
def track_request(request, request_id):
    service_request = ServiceRequest.objects.get(id=request_id)
    track_request_url = reverse('track_request', args=[service_request.id])
    return redirect(track_request_url)

@login_required
def request_list(request):
    requests = ServiceRequest.objects.all().order_by('-created_at')
    return render(request, 'service_requests/request_list.html', {'requests': requests})
