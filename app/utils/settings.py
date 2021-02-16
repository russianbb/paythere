# @TODO: desacoplar config de banco de dados
DATABASE = {
    "host": "mysql",
    "name": "paythere",
    "user": "root",
    "password": "1234",
    "port": 3306,
}

# @TODO: desacoplar config de JWT
JWT = {
    "SECRET_KEY": "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7",  # noqa E501
    "ALGORITHM": "HS256",
    "ACCESS_TOKEN_EXPIRE_MINUTES": 21600,
}
