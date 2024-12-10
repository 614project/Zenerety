from typing import List
from .BaseObject import BaseObject;

class ObjectList:
    """객체 리스트"""
    def Add(object:BaseObject):
        """객체를 추가합니다."""
    def AddRange(objects:List[BaseObject]):
        """객체를 여러개 추가합니다."""
    def Insert(index:int, object:BaseObject):
        """객체를 원하는 위치에 삽입합니다."""
    # def Switch(object:BaseObject, index:int) -> bool:
    #     """원하는 위치와 자리를 바꿉니다."""
    def Remove(object:BaseObject) -> bool:
        """객체를 제거합니다."""

from JyunrcaeaFramework import ObjectList;