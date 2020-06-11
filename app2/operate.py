# -*- coding: UTF-8 -*-
# @Summary : operate
# @Author  : rey
# @Time    : 2020/6/10 6:38 下午
# @Log     :
#            author datetime(DESC) summary
from tortoise import run_async

from app2.models import Tour
from app2.run import run


async def operate():
    await run()
    # tour = await Tour.create(name='tour_1')
    # event = await Event.create(name='event_1', tour=tour)
    # await Event.create(name='event_2', tour=tour)
    # team = Team(name='team_1')
    # await team.save()
    # await event.participants.add(team)

    print(await Tour.filter(name='tour_1'))


if __name__ == '__main__':
    run_async(operate())
