from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView
from .models import Review
from .forms import ReviewForm
from django.views import View


class ReviewView(CreateView):
    model = Review
    # fields = "__all__"
    form_class = ReviewForm
    template_name = 'reviews/review.html'

    success_url = reverse_lazy('thank-you')


    # def get(self, request):
    #     form = ReviewForm()
    #
    #     return render(request, 'reviews/review.html',
    #                   {'form': form})
    #
    # def post(self, request):
    #     if request.method == 'POST':
    #         form = ReviewForm(request.POST)
    #
    #         if form.is_valid():
    #             form.save()
    #             return HttpResponseRedirect(reverse(viewname='thank-you'))


def review(request):
    if request.method == 'POST':
        # existing_model = Review.objects.get(pk=1)  to update existing DV
        # entry
        # form = ReviewForm(request.POST, instance=existing_model)
        form = ReviewForm(request.POST)

        if form.is_valid():
            # review = Review(user_name=form.cleaned_data['user_name'],
            #                 review_text=form.cleaned_data['review_text'],
            #                 rating=form.cleaned_data['rating'])
            # review.save()
            form.save()
            return HttpResponseRedirect(reverse(viewname='thank-you'))

    else:
        form = ReviewForm()

    return render(request, 'reviews/review.html',
                  {'form': form})


class ThankYouView(TemplateView):
    template_name = 'reviews/thank_you.html'

    def get_context_data(self, **kwargs: object) -> dict[str, object]:
        context = super().get_context_data(**kwargs)
        context['message'] = 'This works!'
        return context


class ReviewsListView(ListView):
    template_name = 'reviews/review_list.html'
    model = Review
    context_object_name = 'reviews'

    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query.filter(rating__gt=4)
        return data


class ReviewDetailView(DetailView):
    template_name = 'reviews/review_detail.html'
    model = Review

