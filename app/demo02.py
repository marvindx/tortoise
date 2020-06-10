# -*- coding: UTF-8 -*-
# @Summary : demo02
# @Author  : rey
# @Time    : 2020/6/10 5:27 下午
# @Log     : demo02
#            author datetime(DESC) summary
from tortoise import Tortoise, run_async

from app.models import Event, Tournament


async def run():
    """
    简单例子的入口程序 run（）方法
    :return:
    """
    await Tortoise.init(
        db_url="postgres://postgres:password@localhost:5432/tortoise",
        modules={'models': ['app.models']}
    )
    await Tortoise.generate_schemas()

    event = await Event.all()
    for i in event:
        print(i.__dict__)
    first_event = await Event.first()
    first_event.name = 'first_event'
    await first_event.save()

    tournamet = await Tournament.create(name='marvin')

    for i in range(2):
        await Event.create(name=f'event_{i + 2}', tournamet=tournamet)

    event = await Event.first()
    await Event.filter(id=event.id).update(name='marvin_z')

    print(await Event.all().values_list('name', flat=True))  # flat 只保留value不保留key

if __name__ == '__main__':
    run_async(run())
