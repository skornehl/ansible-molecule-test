def test_ntp_is_installed(Package):
    ntp = Package("ntp")
    assert ntp.is_installed

def test_ntp_running_and_enabled(Service):
    ntp = Service("ntpd")
    assert ntp.is_running
    assert ntp.is_enabled

def test_ntp_is_configured(File, Command):
    ntp_config = File("/etc/ntp.conf")
    assert ntp_config.contains("0.de.pool.ntp.org")

def test_ntp_is_synchronous(Command):
    assert Command.run_test("ntpstat")
