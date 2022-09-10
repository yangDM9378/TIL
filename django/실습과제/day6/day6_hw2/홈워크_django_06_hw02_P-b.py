from django.views.decorators.http import require_safe,require_POST,require_http_methods

@require_safe
def detail(request,pk):
    chatting = get_object_or_404(Chat,pk=pk)
    context = {
        'chatting':chatting,
    }
    return render(request,'chattings/detail.html',context)