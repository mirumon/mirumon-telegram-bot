from mako.lookup import TemplateLookup

_TEMPLATE_LOOKUP = TemplateLookup(
    directories=["app/resources/messages"], input_encoding="utf-8"
)

HELP = _TEMPLATE_LOOKUP.get_template("help.txt")

SOFTWARE_TEMPLATE = _TEMPLATE_LOOKUP.get_template("programs.txt")

INFO_TEMPLATE = _TEMPLATE_LOOKUP.get_template("computers.txt")


WRONG_ARGUMENTS = "wrong arguments, please enter /software {mac_address}"

NOT_RESPONDING = "the service is not responding"

NO_ONE = "no one"
