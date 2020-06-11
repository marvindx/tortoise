# -*- coding: UTF-8 -*-
# @Summary : run.py
# @Author  : rey
# @Time    : 2020/6/10 6:27 下午
# @Log     :
#            author datetime(DESC) summary
from tortoise import Tortoise, run_async


async def run():
    await Tortoise.init(
        db_url="postgres://postgres:password@localhost:5432/tortoise",
        modules={'models': ['app2.models']}
    )
    await Tortoise.generate_schemas()


if __name__ == '__main__':
    run_async(run())
