from django.shortcuts import render,redirect
from social_app.models import post
from social_app.form import post_upload_form

# Create your views here.

def baseindex_view(request):
    return render(request,"baseindex.html")

def footer_view(request):
    return render(request,'footer.html')

def post_view(request):
    post_data = post.objects.all()
    context = {'post_data':post_data}
    return render(request, 'post.html',context)

def postdetail_view(request,id):
    data = post.objects.filter(id=id)
    context = {'data':data}
    return render(request,'postdetail.html',context)




def create_new_post(request):
    form = post_upload_form()
    
    if request.method == 'POST':
        form = post_upload_form(request.POST,request.FILES)
        
        if form.is_valid():
            form.save()
            print(" ! Successfully Saved !")
        else:
            print("Errors Occur")
            
        return redirect('post')
    
    else:
        return render(request,"form.html",{'form':form})
    
    
def delete_post(request,id):
    detele_data = post.objects.filter(id=id)
    detele_data.delete()
    
    return redirect('post')