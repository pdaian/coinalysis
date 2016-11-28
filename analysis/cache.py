import collections

class TxCache(collections.MutableMapping):
  def __init__(self, maxlen, *a, **k):
    self.maxlen = maxlen
    self.d = dict(*a, **k)
    while len(self) > maxlen:
      self.popitem()
  def __iter__(self):
    return iter(self.d)
  def __len__(self):
    return len(self.d)
  def __getitem__(self, k):
    return self.d[k]
  def __delitem__(self, k):
    del self.d[k]
  def __setitem__(self, k, v):
    if k not in self and len(self) == self.maxlen:
      self.popitem()
    self.d[k] = v

