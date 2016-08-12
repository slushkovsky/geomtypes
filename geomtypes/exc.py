class ClassParamsConvertError(Exception): 

    def __init__(self, raiser): 
        self.raiser = raiser

    def __str__(self): 
        argspec = inspect.getfullargspec(self.raiser.__init__)

        for arg in argspec.args: 
            val  = getattr(self.raiser, arg)
            anno = argspec.annotations[arg]

            params_str += '{name} = {val} ({anno})\n'.format(name=arg, 
                                                             val =val,
                                                             anno=anno)

        classname = self.raiser.__class__.__name__ 

        return 'Couldn\'t convert {} params: \n'.format(classname) + params_str
