require 'package_helper'

describe 'p4dctl-config' do
  it_behaves_like :p4_p4dctl
  it_behaves_like :p4_server

  describe process('p4d [p4d-example/1666]') do
    it { should be_running }

    its(:count) { should eq 1 }
    its(:user)  { should eq 'nobody' }
  end

  describe file('/etc/perforce/p4dctl.conf.d/example.conf') do
    it { should be_file }
    it { should be_mode 644 }
    it { should be_owned_by 'root' }
    it { should be_grouped_into 'root' }
  end
end
