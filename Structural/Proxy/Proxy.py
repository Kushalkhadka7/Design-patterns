from __future__ import annotations

from abc import ABC, abstractmethod


class IDatabase(ABC):
    @abstractmethod
    def get_users(self):
        pass

    @abstractmethod
    def get_user_info(self):
        pass


class DatabaseAccessor(IDatabase):

    def get_users(self):
        return ['kushal', 'nischal', 'ram', 'shyam']

    def get_user_info(self):
        return f"User info"


class CacheDbData(IDatabase):
    _cache = {}

    def get_users(self):
        if self._cache.get("users"):
            return f"Users found on cache"
        self._cache["users"] = "new Users"

        return self._cache

    def get_user_info(self):
        if self._cache.get("user_info"):
            return f"User info found in cache"

        self._cache['user_info'] = "user info"

        return self._cache


class DBManager(IDatabase):

    def __init__(self):
        self.service = CacheDbData()

    def get_users(self):
        return self.service.get_users()

    def get_user_info(self):
        return self.service.get_user_info()


data = DBManager()
print(data.get_users())
print(data.get_users())
