from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect

from .models import Transaction
from .forms import TransactionForm


# Create your views here.

def login(request):
    pass

#READ
def list(request):
    if request.user.is_authenticated:
        data = {}
        data ['transaction'] = Transaction.objects.all()
        return render(request,'contas/listagem.html', data)
    else:
        return HttpResponseRedirect('/accounts/login')


#CREATE
def create(request): 
    if request.user.is_authenticated:                                     
        data = {}
        form = TransactionForm(request.POST or None)

       
        if form.is_valid():
            form.save()
            print('foi')
            return redirect('url_list')

                         

        data['form'] = form
    else:
        return HttpResponseRedirect('/accounts/login')
        

    return render(request, 'contas/form.html', data)

#UPDATE
def update(request, id):
    if request.user.is_authenticated:
        data = {}
        transaction = Transaction.objects.get(id=id)
        form = TransactionForm(request.POST or None, instance=transaction)

    
     
        if form.is_valid():
            form.save()
            return redirect('url_list')

        data['form'] = form
        data['transaction'] = transaction
    return render(request, 'contas/form.html', data)



# DELETE
def delete(request, id):
    transaction = Transaction.objects.get(id=id)
    transaction.delete()
        
    return redirect('url_list') 


def charts(request):
    if request.user.is_authenticated:
        data = {'transaction': Transaction.objects.all().count(),
                'transaction_d': Transaction.objects.filter(category_id = 1).count(),
                'transaction_a': Transaction.objects.filter(category_id = 3).count(),
                'transaction_t' : Transaction.objects.filter(category_id = 2).count()}
        
        return render(request, 'contas/charts.html', data)
    else:
        return HttpResponseRedirect('/accounts/login')