"""User Model."""

from app import bcrypt


class User:
    """User class."""

    def __init__(self, email, password, phone=None,
                 devices=None, location=None, authenticated=False,
                 active=False):
        """Intialize user.

        Args:
            email (str): Email id of the user
            password (str): User's password
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
        self.email = email
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
        return bcrypt.check_password_hash(self.password, password)

    def logout(self):
        """Logout user by setting the authenticated flag False."""
        self.authenticated = False

    def is_active(self):
        """Return the active/inactive status of user.

        Returns:
            bool: Returns True if active
        """
        return self.active

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
