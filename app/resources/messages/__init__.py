from mako.template import Template

HELLO = "Hello, i'm Viki"
HELP = "you can say me: \nhello \njoke"
JOKE = "joke"

SOFTWARE_TEMPLATE = Template(
    """
                % for programme in software:
                    name: {programme.name}
                    vendor: {programme.vendor}
                    version: {programme.version}
                % endfor
                             """
)
