from django.shortcuts import render, redirect, get_object_or_404
from .models import Medicine, Comment
from .forms import MedicineForm
from django.contrib.auth.decorators import login_required

def medicine_list(request):
    medicines = Medicine.objects.all().order_by('name')
    return render(request, 'medicine_list.html', {'medicines':medicines})

def medicine_detail(request, pk):
    medicine = get_object_or_404(Medicine, pk=pk)
    comments = medicine.comments.all()

    if request.method == 'POST':
        text = request.POST.get('text')
        if text and request.user.is_authenticated:
            Comment.objects.create(medicine=medicine, user=request.user, text=text)
            return redirect('medicine_detail', pk=pk)

    return render(request, 'medicine_detail.html', {'medicine': medicine, 'comments': comments})

def medicine_add(request):
    if request.method == 'POST':
        form = MedicineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medicine_list')
    else:
        form = MedicineForm()
    return render(request, 'medicine_form.html', {'form': form})

def medicine_edit(request,pk):
    medicine = get_object_or_404(Medicine, pk=pk)
    if request.method == 'POST':
        medicine.name = request.POST['name']
        medicine.description = request.POST['description']
        medicine.save()
        return redirect('medicine_list')
    return render(request,'medicine_form.html', {'medicine': medicine})

def medicine_delete(request, pk):
    medicine = get_object_or_404(Medicine, pk=pk)
    if request.method == 'POST':
        medicine.delete()
        return redirect('medicine_list')
    return render(request, 'medicine_confirm_delete.html', {'medicine': medicine})



