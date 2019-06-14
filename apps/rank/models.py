from django.db import models


class Rank(models.Model):
    nickname = models.CharField(max_length=20, help_text='玩家昵称')
    game_name = models.CharField(max_length=40, help_text='游戏名称')
    duration = models.CharField(max_length=40, help_text='游戏时长')
    platform = models.IntegerField(
        choices=((0, '其他'), (1, '游聚游戏平台'), (2, 'Nestopia模拟器'), (3, '小霸王游戏机')),
        default=1, help_text='游戏平台')
    create_time = models.DateTimeField(auto_now_add=True, help_text='创建时间')

    class Meta:
        ordering = ['duration', 'create_time']
