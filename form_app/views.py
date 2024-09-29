from django.shortcuts import render
from .forms import QuestionForm
from .models import Question

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'thank_you.html')
    else:
        form = QuestionForm()
        return render(request, 'home.html', {'form': form})

def question_list(request):
    questions = Question.objects.all()
    return render(request, 'question_list.html', {'questions': questions})
