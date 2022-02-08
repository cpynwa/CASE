from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import HttpResponse
from tablib import Dataset
from .models import JuniperCase
from .form import JuniperCaseForm
from .resources import JuniperCaseResource



@login_required
@permission_required('juniper.view_junipercase', raise_exception=True)
def data_list(request):
    # db 조회 생성 날짜 순으로 전체 조회
    item = JuniperCase.objects.order_by('-created_date')

    # url의 query string에서 'page'에 해당하는 값을 가져옵니다. 단, page값이 존재하지 않을 경우 1로 셋팅합니다.
    page = request.GET.get('page', '1')

    # 페이징처리
    paginator = Paginator(item, 20) # 페이지당 20개씩 보여주기
    page_obj = paginator.get_page(page)
    return render(request, 'juniper/data_list.html', {'item': page_obj})


@login_required
@permission_required('juniper.view_junipercase', raise_exception=True)
def data_new(request):
    case_id = timezone.now().strftime('%Y-%m%d-%H%M%S') # 2022-0111-043020
    form = JuniperCaseForm(request.POST)
    nowdate = timezone.now()
    if request.method == "POST":
        if form.is_valid():
            data = form.save(commit=False)
            data.manager = request.user
            data.created_date = timezone.now()
            data.case_num = case_id
            data.save()
            return redirect('juniper_detail', pk=data.pk)
    else:
        form = JuniperCaseForm()
        return render(request, 'juniper/data_edit.html', {'form': form, 'nowdate': nowdate})


@login_required
@permission_required('juniper.view_junipercase', raise_exception=True)
def data_detail(request, pk):
    item = get_object_or_404(JuniperCase, pk=pk)
    return render(request, 'juniper/data_detail.html', {'item': item})


@login_required
@permission_required('juniper.view_junipercase', raise_exception=True)
def data_edit(request, pk):
    item = get_object_or_404(JuniperCase, pk=pk)
    if request.method == "POST":
        form = JuniperCaseForm(request.POST, instance=item)
        if form.is_valid():
            data = form.save(commit=False)
            data.manager = request.user
            data.save()
            return redirect('juniper_detail', pk=data.pk)
    else:
        form = JuniperCaseForm(instance=item)
    return render(request, 'juniper/data_edit.html', {'form': form})


@login_required
@permission_required('juniper.view_junipercase', raise_exception=True)
def data_delete(request, pk):
    item = JuniperCase.objects.get(pk=pk)
    if request.user == item.manager:
        item.delete()
        return redirect('juniper_list')
    else:
        return redirect('juniper_detail', pk=item.pk)


@login_required
@permission_required('juniper.view_junipercase', raise_exception=True)
def search(request):
    item = JuniperCase.objects.all().order_by('-id')
    q = request.POST.get('q', "")
    if q:
        item = item.filter(
            Q(manager__username=q) |
            Q(case_num__icontains=q) |
            Q(site__icontains=q) |
            Q(part__icontains=q) |
            Q(serial__icontains=q) |
            Q(os_ver__icontains=q) |
            Q(title__icontains=q) |
            Q(symptom__icontains=q) |
            Q(conclusion__icontains=q) |
            Q(progress__icontains=q)
        )
        return render(request, 'juniper/search.html', {'item': item, 'q': q})
    else:
        return render(request, 'juniper/search.html')


@login_required
@permission_required('juniper.view_junipercase', raise_exception=True)
def data_export(request):
    person_resource = JuniperCaseResource()
    dataset = person_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="{}_data.xls"'.format(timezone.now())
    return response


@login_required
@permission_required('juniper.view_junipercase', raise_exception=True)
def data_import(request):
    if request.method == 'POST':
        person_resource = JuniperCaseResource()
        dataset = Dataset()
        new_persons = request.FILES['myfile']
        imported_data = dataset.load(new_persons.read())
        result = person_resource.import_data(dataset, dry_run=True)  # Test the data import
        if not result.has_errors():
            person_resource.import_data(dataset, dry_run=False)  # Actually import now
    return render(request, 'juniper/data_list.html')
