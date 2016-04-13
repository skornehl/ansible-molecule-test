def test_deployed_app(Socket, Ansible, Command):
    # Get Hostname
    hostname = Ansible("setup")["ansible_facts"]["ansible_hostname"]

    if(hostname.startswith("webserver")):
        # If webserver, test for port 80
        check_for_net_tools(Socket, Command)
        assert Socket("tcp://:::80").is_listening

        # Check if local app contains given String
        returnValue = Command("curl -s localhost")
        assert u"<b>Host:</b> %s" % hostname in returnValue.stdout

def check_for_net_tools(Socket, Command):
    try:
        Socket.get_listening_sockets()
    except:
        Command("yum install -y net-tools")
