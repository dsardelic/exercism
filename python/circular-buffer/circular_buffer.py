class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full.

    message: explanation of the error.

    """

    def __init__(self, message):
        super().__init__(message)


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty.

    message: explanation of the error.

    """

    def __init__(self, message):
        super().__init__(message)


class CircularBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self._buffer = [None] * capacity
        self._read_pos = 0
        self._write_pos = 0

    def read(self):
        if self._is_empty:
            raise BufferEmptyException("Circular buffer is empty")
        item = self._buffer[self._read_pos]
        if self._is_full:
            self._write_pos = self._read_pos
        self._buffer[self._read_pos] = None
        self._read_pos = (self._read_pos + 1) % self.capacity
        return item

    def write(self, data):
        if self._is_full:
            raise BufferFullException("Circular buffer is full")
        self._buffer[self._write_pos] = data
        self._write_pos = (self._write_pos + 1) % self.capacity

    def overwrite(self, data):
        if self._is_full:
            self._buffer[self._write_pos] = data
            self._write_pos = (self._write_pos + 1) % self.capacity
            self._read_pos = (self._read_pos + 1) % self.capacity
        else:
            self.write(data)

    def clear(self):
        self._buffer[:] = [None] * self.capacity
        self._read_pos = 0
        self._write_pos = 0

    @property
    def _is_empty(self):
        return all(item is None for item in self._buffer)

    @property
    def _is_full(self):
        return all(item is not None for item in self._buffer)
