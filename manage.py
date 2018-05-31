from manager import Manager
from mpesa.authenticate import authenticate
from mpesa.credentials import encryptInitiatorPassword
from mpesa.b2c import b2c

manager = Manager()

@manager.command()
def mpesa(args):
    """print the given <name>"""

    if args == "authenticate":
        return authenticate()
    if args == "encrypt":
        return encryptInitiatorPassword()
    if args == "b2c":
        return b2c()


if __name__ == "__main__":
    manager.main()