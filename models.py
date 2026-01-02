class user:
    def __init__(self, id, name, email, birthdate, address):
        self._id = id
        self._name = name
        self._email = email
        self._birthdate = birthdate
        self._address = address

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def email(self):
        return self._email

    @property
    def birthdate(self):
        return self._birthdate

    @property
    def address(self):
        return self._address

    def __str__(self):
        return (
            f"Id: {self.id}\n"
            f"Name: {self.name}\n"
            f"Email: {self.email}\n"
            f"Birthdate: {self.birthdate}\n"
            f"Address: {self.address}"
        )


class destino:
    def __init__(self, id, name, description):
        self._id = int(id)
        self._name = name
        self._description = description

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    def __str__(self):
        return (
            f"Id: {self.id}\n"
            f"Name: {self.name}\n"
            f"Description: {self.description}"
        )


class reserva:
    def __init__(self, id, idUsuario, idDestino, data, Status):
        self._id = int(id)
        self._idUsuario = idUsuario
        self._idDestino = idDestino
        self._data = data
        self._Status = Status

    @property
    def id(self):
        return self._id

    @property
    def idUsuario(self):
        return self._idUsuario

    @property
    def idDestino(self):
        return self._idDestino
    @idDestino.setter
    def idDestino(self, value):
        self._idDestino = value

    @property
    def data(self):
        return self._data

    @property
    def Status(self):
        return self._Status
    @Status.setter
    def Status(self, value):
        self._Status = value.strip()
    
    def __str__(self):
        return (
            f"Id: {self.id}\n"
            f"IdUsuario: {self.idUsuario}\n"
            f"IdDestino: {self.idDestino}\n"
            f"Data: {self.data}\n"
            f"Status: {self.Status}"
        )