from tortoise import Tortoise, run_async

from app.models import Team, Event, Tournament


async def init():
    await Tortoise.init(
        # DB_TYPE: // USERNAME: PASSWORD @ HOST:PORT / DB_NAME?PARAM1 = value & PARAM2 = value
        # db_url='sqlite://db.sqlite3',
        db_url='postgres://postgres:password@localhost:5432/tortoise',  # 连接PostgreSQL
        modules={'models': ['app.models']}  # models文件的路径
    )

    await Tortoise.generate_schemas()
    tournamet = Tournament(name='new tournament')
    print('sdadas')
    print(tournamet.name)
    await tournamet.save()

    await Event.create(tournamet=tournamet, name='new event')

    event = await Event.create(name='test', tournamet=tournamet)

    participants = []
    for i in range(2):
        team = await Team.create(name=f'team{i + 1}')

        participants.append(team)

    await event.participants.add(*participants)  # 多对多添加数据

    async for team in event.participants:
        print(team.name)

    a = await Event.all()

    print(a[0].name)

    await Tortoise.close_connections()


if __name__ == '__main__':
    run_async(init())
