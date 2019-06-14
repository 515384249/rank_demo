from django import forms
from django.core import validators
from apps.forms import FormMixin


class AddRankForm(forms.Form, FormMixin):
    nickname = forms.CharField(
        min_length=2,
        max_length=20,
        error_messages={
            'min_length': '玩家昵称长度不能少于2位',
            'max_length': '玩家昵称长度不能多于20位',
            'required': '未输入玩家昵称'
        }
    )
    game_name = forms.CharField(
        min_length=1,
        max_length=40,
        error_messages={
            'min_length': '游戏名称长度不能少于1位',
            'max_length': '游戏名称长度不能多于40位',
            'required': '未输入游戏名称'
        }
    )
    duration = forms.CharField(
        validators=[validators.RegexValidator(
            r'[0-9]{1,2}h[0-9]{1,2}m[0-9]{1,2}s[0-9]{1,3}ms',
            message='传入游戏时长有误'
        )],
        max_length=40,
        error_messages={
            'max_length': '游戏时长不能超过40个字符',
            'required': '必须传入游戏时长',
        }
    )
    platform = forms.IntegerField(
        error_messages={
            'required': '未选择游戏平台'
        }
    )
