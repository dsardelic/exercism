class InputCell:
    def __init__(self, initial_value):
        self._value = initial_value
        self._observers = set()

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value
        for observer in self._observers:
            observer.compute()

    def register_observer(self, observer):
        self._observers.add(observer)

    def compute(self):
        pass


class ComputeCell:
    def __init__(self, inputs, compute_function):
        self.inputs = inputs
        self.compute_function = compute_function
        self.callbacks = set()
        self._value = None
        self._start_observing_ultimate_observables()
        self.compute()

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, computed_value):
        self._value = computed_value
        for callback in self.callbacks:
            callback(self.value)

    def add_callback(self, callback):
        self.callbacks.add(callback)

    def remove_callback(self, callback):
        self.callbacks.discard(callback)

    def _start_observing_ultimate_observables(self):
        def ultimate_observables(inputs):
            for input_ in inputs:
                if isinstance(input_, ComputeCell):
                    yield from ultimate_observables(input_.inputs)
                else:  # InputCell
                    yield input_

        for ultimate_observable in ultimate_observables(self.inputs):
            ultimate_observable.register_observer(self)

    def compute(self):
        for input_ in self.inputs:
            input_.compute()
        computed_value = self.compute_function([input_.value for input_ in self.inputs])
        if computed_value != self.value:
            self.value = computed_value
