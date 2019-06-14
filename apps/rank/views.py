from django.shortcuts import render, Http404
from django.conf import settings
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import View
from .forms import AddRankForm
from .models import Rank
from utils import restful, time_format
from utils.pagination import get_pagination_data


class RankView(View):
    def get(self, request):
        ranks = Rank.objects.all()
        count = settings.ONE_PAGE_NEWS_COUNT
        try:
            page = int(request.GET.get('p', 1))
        except:
            page = 1
        paginator = Paginator(ranks, count)
        try:
            page_obj = paginator.page(page)
        except PageNotAnInteger:
            page_obj = paginator.page(1)
        except EmptyPage:
            page_obj = paginator.page(1)
        context_data = get_pagination_data(paginator, page_obj, count=count)
        context = {
            'ranks': page_obj.object_list,
            'page_obj': page_obj,
            'paginator': paginator,
            'total': ranks.count()
        }
        context.update(context_data)
        return render(request, 'rank.html', context=context)

    def http_method_not_allowed(self, request, *args, **kwargs):
        return Http404


@require_POST
def add_rank(request):
    form = AddRankForm(request.POST)
    if form.is_valid():
        nickname = request.POST.get('nickname')
        game_name = request.POST.get('game_name')
        duration = request.POST.get('duration')
        duration = time_format.split_time(duration)
        platform = request.POST.get('platform')
        # if platform.isdigit():
        #     platform = int(platform)  # 这么写太low了
        platform = int(platform) if platform.isdigit() else 0
        try:
            Rank.objects.create(nickname=nickname, game_name=game_name, duration=duration, platform=platform)
            return restful.ok()
        except:
            return restful.server_error(message='添加排行失败，服务器内部错误')
    else:
        return restful.params_error(message=form.get_errors())


@require_POST
def edit_rank(request):  # 这里本来应该使用EditRankForm验证。但是我没写
    pk = request.POST.get('pk')
    nickname = request.POST.get('nickname')
    game_name = request.POST.get('game_name')
    duration = request.POST.get('duration')
    duration = time_format.split_time(duration)
    platform = request.POST.get('platform')
    try:
        Rank.objects.filter(pk=pk).update(
            nickname=nickname, game_name=game_name, duration=duration, platform=platform
        )
        return restful.result(message='编辑成功')
    except:
        return restful.params_error(message='编辑排行失败，排行不存在')


@require_POST
def delete_rank(request):
    pk = request.POST.get('pk')
    try:
        Rank.objects.filter(pk=pk).delete()
        return restful.result(message='删除成功')
    except:
        return restful.params_error(message='删除排行失败，排行不存在')
