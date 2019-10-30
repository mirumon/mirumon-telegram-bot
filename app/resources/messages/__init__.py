from mako.lookup import TemplateLookup

HELP = "\n".join(
    [
        "\\computers for show all computers",
        "\\software {mac_address} for get csv file with all software",
    ]
)
HELLO = f"Hello, i'm mirumon bot.\n {HELP}"
JOKE = "joke"

_TEMPLATE_LOOKUP = TemplateLookup(
    directories=["app/resources/messages"], input_encoding="utf-8"
)

SOFTWARE_TEMPLATE = _TEMPLATE_LOOKUP.get_template("programs.txt")

INFO_TEMPLATE = _TEMPLATE_LOOKUP.get_template("./computers.txt")
