from tortoise import Tortoise, run_async


async def init():
    # Here we create a SQLite DB using file "db.sqlite3"
    #  also specify the app name of "models"
    #  which contain models from "app.models"
    await Tortoise.init(
        # db_url=f'postgres://{settings.POSTGRESQL_USERNAME}:{settings.POSTGRESQL_PASSWORD}@{settings.POSTGRESQL_HOSTNAME}:5432/{settings.POSTGRESQL_DATABASE}"',
        db_url='sqlite://db.sqlite3',
        modules={'models': ['bot_app.models']}
    )
    # Generate the schema
    await Tortoise.generate_schemas()


run_async(init())
