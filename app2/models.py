# -*- coding: UTF-8 -*-
# @Summary : app_2
# @Author  : rey
# @Time    : 2020/6/10 6:03 下午
# @Log     :
#            author datetime(DESC) summary
from tortoise import models, fields


class Tour(models.Model):
    """
    Tour model class
    """
    id = fields.IntField(pk=True)
    name = fields.TextField()

    events: fields.ReverseRelation["Event"]

    class Meta:
        table = 'tour'
        ordering = ['id']

    def __str__(self):
        return str(id) + self.name


class Event(models.Model):
    """
    Event model class
    """
    id = fields.IntField(pk=True)
    name = fields.TextField()

    tour: fields.ForeignKeyRelation[Tour] = fields.ForeignKeyField(
        "models.Tour", related_name="events"
    )
    participants: fields.ManyToManyRelation["Team"] = fields.ManyToManyField(
        "models.Team", related_name="events"
    )

    class Meta:
        table = 'event'
        ordering = ['id']

    def __str__(self):
        return str(id) + self.name


class Team(models.Model):
    id = fields.IntField(pk=True)
    name = fields.TextField()

    events: fields.ManyToManyRelation[Event]

    def __str__(self):
        return str(id) + self.name

