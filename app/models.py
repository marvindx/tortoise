from tortoise.models import Model
from tortoise import fields, Tortoise


class Tournament(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)

    def __str__(self):
        return 'Tournament--' + str(self.id) + self.name


class Event(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)

    tournamet = fields.ForeignKeyField('models.Tournament', related_name='events')
    participants = fields.ManyToManyField('models.Team', related_name='events', through='event_team')
    """
        tournamet = fields.ForeignKeyField('models.Tournament', related_name='events')
        
    """
    def __str__(self):
        return 'Event--' + str(self.id) + self.name


class Team(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)

    def __str__(self):
        return "Team--" + str(self.id) + self.name

    class Meta:
        table = 'team_table'
        abstract = False  # 指定是否为抽象model类，是则不创建model 否则创建model
        table_description = '表格的相关描述'
        # unique_together = None  # 为表格设置复合唯一索引 元组或者列表的形式
        # unique_together = ('id','name')
        # indexes = None  # 为表格设置非唯一索引 元组的形式
        # indexes = ('id','name')
        # ordering = None  # 设置表格的默认排序方式
        # ordering = ["name", "-score"] 和Django类似

