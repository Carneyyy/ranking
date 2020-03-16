# -*- coding: utf-8 -*-
# __auth__   ：崔老表
# createtime ：2020/3/16  13:34
# _filename_ ：utils.PY
# __IDE__    ：PyCharm
class StatusResponse(object):
    @classmethod
    def success(cls, data):
        return {
                "message": "ok",
                "code": "200",
                "data": data or {},
            }

    @classmethod
    def error(cls, code, msg):
        return {
                "message": msg,
                "code": str(code),
                "data": {},
            }
