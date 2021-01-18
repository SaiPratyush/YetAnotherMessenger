"""Flask App Configuration."""


class Config(object):
    """Configuration base."""

    DEBUG = False
    TESTING = False
    DATABASE_URI = ''


class ProductionConfig(Config):
    """Production Configuration."""

    DATABASE_URI = ''


class DevelopmentConfig(Config):
    """Development Configuration."""

    DEBUG = True


class TestingConfig(Config):
    """Testing Configuration."""

    TESTING = True
