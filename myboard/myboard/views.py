from django.shortcuts import render, redirect
from .models import MyBoard
from django.utils import timezone


def index(request):
    return render(request, 'index.html', {'list': MyBoard.objects.all().order_by('-id')}) # -id는 내림차순 id는 오름차순


def insert_form(request):
    return render(request, 'insert.html')


def insert_res(request):
    myname = request.POST['myname']
    mytitle = request.POST['mytitle']
    mycontent = request.POST['mycontent']
    # create를 하면 데이터베이스에 값을 넣어줌
    result = MyBoard.objects.create(myname=myname, mytitle=mytitle, mycontent=mycontent, mydate=timezone.now())

    if result:
        return redirect('index')
    else:
        return redirect('insertform')

def detail(request, id):
    return render(request, 'detail.html', {'dto': MyBoard.objects.get(id=id)})

def update_form(request, id):
    return render(request, 'update.html', {'dto': MyBoard.objects.get(id=id)})

def update_res(request):
    id = request.POST['id']
    mytitle = request.POST['mytitle']
    mycontent = request.POST['mycontent']

    myboard = MyBoard.objects.filter(id=id)

    result_title = myboard.update(mytitle=mytitle)
    result_content = myboard.update(mycontent=mycontent)
    # 확인해보기
    # print(result_content)
    # print(result_title)

    if result_title + result_content == 2:
        return redirect('/detail/'+id)
    else:
        return redirect('/updateform/'+id)


def delete(request, id):
    result_delete = MyBoard.objects.filter(id=id).delete()
    # print(result_delete)

    if result_delete[0]:
        return redirect('index')
    else:
        return redirect('/detail/'+id)