from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect


# Create your views here.
def review(request):
    if request.method == 'POST':
        entered_username = request.POST['username']
        print(entered_username)
        # return HttpResponseRedirect('/reviews/thank-you')
        return HttpResponseRedirect(reverse(viewname='thank-you'))
    else:
        print('WTF')
        return render(request, template_name='reviews/review.html')


def thank_you(request):
    return render(request, template_name='reviews/thank_you.html')
