from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from extreme.models import ExtremeCase
from juniper.models import JuniperCase

# Create your views here.
@login_required
def my_page(request):
    current_user = request.user.id
    jitem = JuniperCase.objects.filter(manager=current_user).order_by('-created_date')
    eitem = ExtremeCase.objects.filter(manager=current_user).order_by('-created_date')

    # url의 query string에서 'page'에 해당하는 값을 가져옵니다. 단, page값이 존재하지 않을 경우 1로 셋팅합니다.
    page = request.GET.get('page', '1')

    # 페이징처리
    j_paginator = Paginator(jitem, 20)  # 페이지당 20개씩 보여주기
    j_page_obj = j_paginator.get_page(page)
    e_paginator = Paginator(eitem, 20)  # 페이지당 20개씩 보여주기
    e_page_obj = e_paginator.get_page(page)
    return render(request, 'common/my_page.html', {'jitem': j_page_obj, 'eitem': e_page_obj})
    # return render(request, 'common/my_page.html', {'jitem': jitem, 'eitem': eitem})

