import imp
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import is_valid_path
from .models import comm, Comment,  ReComment

from commapp.forms import CommentForm, commForm, ReCommentForm
# Create your views here.


def main(request):
    return render(request, 'main.html')

def test(request):
    return render(request, 'test.html')

def board_post(request):
    if request.method == 'POST' or request.method=='FILES': #POST요청 폼의 버튼을 눌렀다
        form  = commForm(request.POST, request.FILES) #form 유효성 확인
        if form.is_valid():
            c = form.save(commit=False) #db에 당장 저장x
            c.save()
            return redirect('board_detail', pk = c.pk)
    else: #GET요청 웹 브라우저에서 페이지 접속
        form = commForm()
    return render(request, 'board_post.html', {'form':form})

def board(request):
    c = comm.objects.all()
    return render(request, 'board.html',{'comm':c})

def board_detail(request, pk):
    # all = comm.objects.all()
    c = get_object_or_404(comm, pk=pk)
    form = CommentForm()
    reform = ReCommentForm()
    return render(request, 'board_detail.html',{'comm':c, 'comment_form':form,'recomment_form':reform})

def board_update(request, pk):
    c = get_object_or_404(comm,pk=pk)
    if(request.method == "POST" or request.method == 'FILES'):
        form = commForm(request.POST, request.FILES, instance=c)
        if(form.is_valid()):
            c = form.save(commit=False)
            c.save()
        return redirect('board_detail', pk=c.pk)
    else:
        form = commForm(instance=c)
        return render(request, 'board_post.html', {'form':form})

def board_delete(request,pk):
    c = get_object_or_404(comm,pk=pk)
    c.delete()
    return redirect('board')

def comment_create(request, pk):
    filled_form = CommentForm(request.POST)
    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.post = get_object_or_404(comm, pk=pk)
        finished_form.author = request.user
        finished_form.save()
    return redirect('board_detail', pk)

def comment_update(request, pk):
    c = get_object_or_404(Comment,pk=pk) # 모델로부터 객체를 받을 때 객체가 있으면 받고, 없을 시 404 에러 페이지를 보여줌
    p = get_object_or_404(comm,pk=c.post.pk)
    if(request.method == "POST"):
        form = CommentForm(request.POST, instance=c)
        if(form.is_valid()):
            c = form.save(commit=False)
            c.save()
        return redirect('board_detail', pk=p.pk) #댓글 모델의 포스트pk값을 받아서 디테일페이지/pk로 사요
    else:
        form = CommentForm(instance=c) #CommentForm에 정보 넣음
        return render(request, 'board_post.html', {'form':form}) #render함수를 통해 board_post에 form을 넣는다.
def comment_delete(request, pk):
    c = get_object_or_404(Comment,pk=pk)
    p = get_object_or_404(comm, pk=c.post.pk)
    c.delete()
    return redirect('board_detail', pk=p.pk)

def recomment_create(request,c_pk):
    filled_form = ReCommentForm(request.POST)
    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.post = get_object_or_404(Comment, pk=c_pk)
        finished_form.author = request.user
        finished_form.save()
    return redirect('board_detail', pk=finished_form.post.post.pk)

def recomment_delete(request, rc_pk):
    # c = get_object_or_404(Comment, pk=pk)
    rc = get_object_or_404(ReComment, pk=rc_pk)
    p = get_object_or_404(comm, pk=rc.post.post.pk)
    rc.delete()
    return redirect('board_detail', pk=p.pk)
