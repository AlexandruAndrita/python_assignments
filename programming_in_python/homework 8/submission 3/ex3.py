class Aggregator:
    def __init__(self, agg_type: type, ignore_errors: bool=True):
        self.agg_type=agg_type
        self.ignore_errors=ignore_errors
        self.result=None

    def __call__(self, *args):
        if len(args)==0:
            return self.result
        elif len(args)!=0:
            if not isinstance(args[0],self.agg_type) and self.ignore_errors==False:
                raise TypeError(f"aggregation only works on type '{self.agg_type.__name__}', not '{type(args[0]).__name__}'")
            elif not isinstance(args[0],self.agg_type) and self.ignore_errors==True:
                pass
            else:
                if self.result is None:
                    self.result=args[0]
                elif self.result is not None:
                    self.result+=args[0]

        for value in args[1:]:
            if not isinstance(value,self.agg_type) and self.ignore_errors==True:
                continue
            elif not isinstance(value,self.agg_type) and self.ignore_errors==False:
                raise TypeError(f"aggregation only works on type '{self.agg_type.__name__}', not '{type(value).__name__}'")
            elif isinstance(value,self.agg_type):
                self.result=self.result+value

        return self.result

