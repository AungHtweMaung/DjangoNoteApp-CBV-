from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Notes
from .forms import NotesForm
from django.views.generic import CreateView,ListView, DetailView, UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class NotesDeleteView(LoginRequiredMixin, DeleteView):
    model = Notes 
    template_name = "notes/delete_note.html"
    context_object_name = "note"
    success_url = "/smart/notes/"

    login_url = "/login"

    def get_queryset(self):
        return self.request.user.notes.all()

class NotesUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "notes/create_note.html"
    success_url = '/smart/notes/'
    form_class = NotesForm      

    login_url = "/login"

    def get_queryset(self):
        return self.request.user.notes.all()

class NotesCreateView(LoginRequiredMixin, CreateView):
    model = Notes
    template_name = "notes/create_note.html"
    success_url = '/smart/notes/'
    form_class = NotesForm

    login_url = "/login"

    def form_valid(self, form): 
        self.object = form.save(commit=False)
        self.object.user = self.request.user

        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


# model => Notes ပေးထားတာ Notes က table object list တစ်ခုလုံးပါလို့ ListView သုံးလိုက်တာ
class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    template_name = "notes/note_list.html"
    context_object_name = 'notes'
    login_url = "/login"

    # def get_queryset(self):
    #     return self.request.user.notes.all()


class NotesDetailView(LoginRequiredMixin, DetailView):
    model = Notes
    context_object_name = "note"
    template_name = "notes/detail_note.html"
    
    login_url = "/login"

    # def get_queryset(self):
    #     return self.request.user.notes.all()
# def note_list(request):
#     all_notes = Notes.objects.all()
#     context = {
#         "notes": all_notes
#     }
    
#     return render(request, "notes/note_list.html", context)

# def detail_note(request, id):
#     note = get_object_or_404(Notes, pk=id)

#     return render(request, "notes/detail_note.html", {"note": note})
    