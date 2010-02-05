

class Key(object):
    
    '''Key combines binding type and annotation into one object. Two different
    keys, constructed from the same objects always have the same hash.
    
    Example::
    
        >>> class A(object): pass
        >>> key = Key(A, 'annotation')
        >>> key2 = Key(A, 'annotation')
        
        >>> key is key2
        False
        >>> key == key2
        True
        
        >>> d = {}
        >>> d[key] = 'value'
        >>> d[key2]
        'value'
    
    '''
    
    __slots__ = ('type', 'annotation', '_hash')
    
    def __init__(self, type, annotation):
        self.type = type
        self.annotation = annotation
        self._hash = None
    
    def __hash__(self):
        _hash = self._hash
        if _hash is None:
            _hash = hash(self.type) ^ hash(self.annotation)
            self._hash = _hash
        return _hash
    
    def __eq__(self, other):
        return hash(self) == hash(other)
    
    def __ne__(self, other):
        return hash(self) != hash(other)
    
    def __repr__(self):
        return '<%s for "%s" annotated with "%s" at %s>' % \
            (self.__class__.__name__, self.type, self.annotation,
             hex(id(self)))