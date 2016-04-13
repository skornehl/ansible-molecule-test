require 'serverspec'

set :backend, :exec

 describe package('httpd') do
    it { should be_installed }.with_version('2')
    it { should be_running }
    it { should be_enabled }
  end
end
