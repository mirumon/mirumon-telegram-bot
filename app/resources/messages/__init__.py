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

INFO_TEMPLATE = Template(
    """
    % for computer in computers:
            <% tmp domain = "" %>
            % if computer.domain != tmp_domain:
                \n In domain {computer.domain}\n\n
            % endif
            {computer.name} [{computer.username}] <{computer.mac_address}>\n
    % endfor
    """
)
