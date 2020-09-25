from django.shortcuts import render
def Homepage(request):
    return render(request, 'student/HoD_template/main_content.html')