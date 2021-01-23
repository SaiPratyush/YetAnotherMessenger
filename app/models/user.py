"""User Model."""

from app import bcrypt, myclient

clients = myclient["Clients"]
users = clients["users"]


class User:
    """User class."""

    def __init__(self, email, password, username=None, phone=None,
                 devices=None, location=None, authenticated=False,
                 active=False):
        """Intialize user.

        Args:
            email (str): Email id of the user
            password (str): User's password
            username (str, optional): Username. Defaults to None.
            phone (str, optional): Phone number of user. Defaults to None.
            devices (list, optional): List of devices signed in by user.\
                Defaults to None.
            location (str, optional): Current location of user.\
                Defaults to None.
            authenticated (bool, optional): Flag for whether the user \
                is authenticated. Defaults to False.
            active (bool, optional): Flag for whether the user is active. \
                Defaults to False.
        """
        self.username = username.strip().lower()
        self.email = email.strip().lower()
        self.password = bcrypt.generate_password_hash(password)
        self.phone = phone
        self.devices = devices
        self.location = location
        self.authenticated = authenticated
        self.active = active

    def check_password(self, password):
        """Validate password during sign in.

        Args:
            password (str): Password.

        Returns:
            bool: Returns True if password matches.
        """
        query = {"email": self.email}
        doc = users.find_one(query)
        return bcrypt.check_password_hash(doc['password'], password)

    def register_user(self):
        """Register user."""
        query = {"email": self.email}
        doc = users.find_one(query)
        if doc is not None:
            return False
        users.insert_one(self.__dict__)
        return True

    def logout(self):
        """Logout user by setting the authenticated flag False."""
        self.authenticated = False

    def is_active(self):
        """Return the active/inactive status of user.

        Returns:
            bool: Returns True if active
        """
        return self.active

    def get_username(self):
        """Return username.

        Returns:
            str: Username.
        """
        return self.email

    def get_email(self):
        """Return user email id.

        Returns:
            str: User email id.
        """
        return self.email

    def get_phone(self):
        """Return user number.

        Returns:
            str: User phone number
        """
        return self.phone

    def get_devices(self):
        """Return devices user is signed in on.

        Returns:
            list: list of devices user is signed in on
        """
        return self.devices

    def is_authenticated(self):
        """Return whether user is authenticated.

        Returns:
            bool: Returns True if user is authenticated.
        """
        return self.authenticated
