class Token:
    def __init__(self, _type, _value = None) -> None:
        self.type = _type
        self.value = _value
        
    def __repr__(self) -> str:
        if self.value:
            return f'{self.type}:{self.value}'
        else:
            return f'{self.type}'