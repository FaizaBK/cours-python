class VeloMobile:
    def __init__(self, model, description, weight, photo):
        if not all((model, description, weight, photo)):
            raise ValueError('Model, description, weight, and photo are required')
        self._model = model
        self._description = description
        self._weight = weight
        self._photo = photo

    def __setattr__(self, name, value):
        if name.startswith('_') or hasattr(self, name):
            super().__setattr__(name, value)
        else:
            raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'")

    def __getattr__(self, name):
        if name.startswith('_') or hasattr(self, name):
            return super().__getattribute__(name)
        else:
            raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'")


# Creating a VeloMobile instance
try:
    velo_mobile = VeloMobile("Model A", "Description A", 100, "photo.jpg")
    print("VeloMobile instance created successfully.")

    # Setting the wheel attribute
    velo_mobile._wheel = 3
    print("VeloMobile wheel attribute set successfully:", velo_mobile._wheel)

except ValueError as e:
    print("Error:", e)
except AttributeError as e:
    print("Error:", e)
