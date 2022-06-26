from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import VVPictureBook, VVPicture, VVPictureQuestion


class VVPictureBookIndexView(PermissionRequiredMixin, ListView):
    permission_required = 'vv_pictures.view_vv_pictures'
    template_name = "vv_pictures/index.html"
    model = VVPictureBook
    context_object_name = 'books'
    queryset = VVPictureBook.objects.all()
    # print("vv_pictures List View Book Trying")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ref_tab'] = True
        return context


class VVPictureIndexView(PermissionRequiredMixin, ListView):
    permission_required = 'vv_pictures.view_vv_pictures'
    template_name = "vv_pictures/pictureindex.html"
    model = VVPicture
    context_object_name = 'pictures'

    def get_queryset(self, *args, **kwargs):
        print("Ok: Let's See...")
        print(self.kwargs.get("book"))
        print(VVPicture.objects.filter(book_id=self.kwargs.get("book")))
        return VVPicture.objects.filter(book_id=self.kwargs.get('book'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ref_tab'] = True
        return context


class PictureDetailView(PermissionRequiredMixin, DetailView):
    permission_required = 'vv_pictures.view_vv_pictures'
    template_name = "vv_pictures/picturedetail.html"
    context_object_name = 'picture'
    model = VVPicture
    print("hmm...")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(self.object.image)
        # Note: personalizing the context data allows you to get more organized context and other object data.? \()/
        context['questions'] = VVPictureQuestion.objects.filter(story=self.kwargs.get("pk"))
        context['ref_tab'] = True
        return context
