def test_httpd_is_installed(Package, Ansible):
    httpd = Package("httpd")
    assert httpd.is_installed
    assert httpd.version.startswith("2")

def test_httpd_running_and_enabled(Service):
    httpd = Service("httpd")
    assert httpd.is_running
    assert httpd.is_enabled
