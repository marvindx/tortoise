# -*- coding: UTF-8 -*-
# @Summary : 
# @Author  : marvin
# @Time    : 2020/6/10 2:42 下午
# @Log     :
#            author datetime(DESC) summary
from app.models import Tournament, Event, Team

# tournamet = Tournament(name='new tournament')
# print('sdadas')
# print(tournamet.name)
# await tournamet.save()
#
# await Event.create(tournamet=tournamet, name='new event')
#
# event = await Event.create(name='test', tournamet=tournamet)
#
# participants = []
# for i in range(2):
#     team = await Team(name=f'team{i + 1}')
#     participants.append(team)
#
# await event.participants.add(**participants)  # 多对多添加数据
#
# print(event.participants)
# async for team in event.participants:
#     print(team.name)
