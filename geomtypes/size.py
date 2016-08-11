import sys
import inspect

class _Size(object): 

    def __init__(self, width, height): 
        assert 'width'  in self._types
        assert 'height' in self._types

        try: 
            self.width  = self._types['width'](width)
            self.height = self._types['height'](height)
        except:
            ClassParamsConvertError(self)

        self.validate()

    def __new__(cls, *args, **kw):
        obj = super().__new__(cls)

        cls._types = inspect.getfullargspec(cls.__init__).annotations

        return obj

    def __str__(self): 
        return '<Size {}x{}>'.format(self.width, self.height)

    def __norm_types(self): 
        self.width  = self._types['width'] (self.width)
        self.height = self._types['height'](self.height)

    def validate(self): 
        self.__norm_types()

        assert self.width  >= self._types['width'] (0)
        assert self.height >= self._types['height'](0) 

    @classmethod
    def zero(cls): 
        return cls(width =cls._types['width'] (0), 
                   height=cls._types['height'](0))


class Size(_Size): 

    def __init__(self, width: int, height: int):
        super().__init__(width, height)

    @classmethod
    def ever_biggest(cls): 
        return cls(width =sys.maxsize, height=sys.maxsize)


class SizeF(_Size): 

    def __init__(self, width: float, height: float):
        super().__init__(width, height)

    @classmethod
    def ever_biggest(cls): 
        return cls(width =sys.float_info.max, 
                   height=sys.float_info.max)