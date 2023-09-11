def get_db_url(database_credentials: dict[str, str], is_async: bool = False) -> str:
    if is_async:
        database_credentials['connector'] = 'postgresql+asyncpg'
    db_url = '{connector}://{user}:{password}@{host}:{port}/{database}'.format(**database_credentials)

    return db_url
