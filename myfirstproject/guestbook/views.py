from django.shortcuts import render,redirect
from .models import AboutME
from .forms import CommentForm
def index(request):
    aboutme= AboutME.objects.order_by('-date_added')
    context ={'aboutme':aboutme}
    return render(request,'guestbook/index.html',context)

def sign(request):

    if request.method=='POST':
        form= CommentForm(request.POST)

        if form. is_valid():
            new_commment=AboutME(topic=request.POST['name'],
                                 aboutme=request.POST['comment'])
            new_commment.save()
            return redirect("index")
    else:    
         form =CommentForm()

    context={'form': form}
    return render(request,'guestbook/sign.html', context)
