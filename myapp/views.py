from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Device, BorrowRecord

# หน้าแรก (Home Page)
@login_required
def home(request):
    if request.user.is_authenticated:
        # สมมติว่ามี BorrowRecord และต้องการดึงข้อมูลที่เกี่ยวข้องกับผู้ใช้
        borrow_records = BorrowRecord.objects.filter(user=request.user)
        return render(request, 'home.html', {'borrow_records': borrow_records})
    return render(request, 'home.html')

# การลงทะเบียนผู้ใช้
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # สมมติว่าชื่อ URL สำหรับหน้า login คือ 'login'
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# การเข้าสู่ระบบ
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # สมมติว่าชื่อ URL สำหรับหน้า home คือ 'home'
        else:
            error_message = "ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง"
            return render(request, 'login.html', {'error_message': error_message})
    return render(request, 'login.html')

# การออกจากระบบ
def user_logout(request):
    logout(request)
    return redirect('home')  # สมมติว่าชื่อ URL สำหรับหน้าแรกคือ 'index'
