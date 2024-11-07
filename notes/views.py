from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from django.contrib import messages
from .models import Note

class SignUpView(FormView):
    template_name = 'notes/signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('notes:note_list')

    def form_valid(self, form):
        user = form.save()
        messages.success(self.request, "Your account was created successfully.")
        return super().form_valid(form)

class NoteListView(LoginRequiredMixin, ListView):
    model = Note
    paginate_by = 10
    template_name = 'notes/note_list.html'

    def get_queryset(self):
        # Ensure only notes created by the logged-in user are displayed
        return Note.objects.filter(user=self.request.user)

class NoteDetailView(LoginRequiredMixin, DetailView):
    model = Note
    template_name = 'notes/note_detail.html'

class NoteCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Note
    fields = ['title', 'body']
    template_name = 'notes/note_form.html'
    success_url = reverse_lazy('notes:note_list')
    success_message = "Note created successfully."

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class NoteUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Note
    fields = ['title', 'body']
    template_name = 'notes/note_form.html'
    success_url = reverse_lazy('notes:note_list')
    success_message = "Note updated successfully."

    def get_queryset(self):
        # Ensure users can only update their own notes
        return Note.objects.filter(user=self.request.user)

class NoteDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Note
    template_name = 'notes/note_confirm_delete.html'
    success_url = reverse_lazy('notes:note_list')
    success_message = "Note deleted successfully."

    def get_queryset(self):
        # Ensure users can only delete their own notes
        return Note.objects.filter(user=self.request.user)

