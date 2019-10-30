from mako.lookup import TemplateLookup

HELLO = "Hello, i'm Viki"
HELP = "you can say me: \nhello \njoke"
JOKE = "joke"

_TEMPLATE_LOOKUP = TemplateLookup(
    directories=["app/resources/messages"], input_encoding="utf-8"
)

SOFTWARE_TEMPLATE = _TEMPLATE_LOOKUP.get_template("programs.txt")

INFO_TEMPLATE = _TEMPLATE_LOOKUP.get_template("./computers.txt")
