import sys
from os.path import abspath, dirname

sys.path.append(dirname(dirname(abspath(__file__))))

from app.core.config import settings
from app.core.database import Base
from app.models import User, Technician, ServiceOrder

target_metadata = Base.metadata

def get_url():
    return settings.DATABASE_URL

def run_migrations_offline():
    url = get_url()

    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={'paramstyle': 'named'},
    )
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online(): 
    configuration = config.get_section(config.config_ini_section)
    configuration['sqlalchemy.url'] = get_url()
    connectable = engine_from_config(
        configuration,
        prefix='sqlalchemy.'
    )
    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )
        with context.begin_transaction():
            context.run_migrations()
            