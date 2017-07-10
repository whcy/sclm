from django.shortcuts import render

# Create your views here.
def updatePicture(request):
    if request.method == 'post':
        picture = request.FILES['picture']

    if picture:
        picturetime= request.user.username+str(time.time()).split('.')[0]
        picture_last=str(picture).split('.')[-1]
        picturename='photos/%s.%s'%(picturetime,picture_last)
        img=Image.open(picture)
        img.save('media/'+picturename)
