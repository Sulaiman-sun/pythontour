POOL_SETTINGS = {
    "maxcached": 10,  # the maximum number of idle connections in the pool
    # (the default value of 0 or None means unlimited pool size)
    "maxconnections": 20,  # maximum number of connections generally allowed
    "maxshared": 0,  # maximum number of shared connections allowed 0 for NOT SHARE

}

MYSQL_SETTINGS = {
    "charset": "utf8mb4",
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "passwd": "",
}
