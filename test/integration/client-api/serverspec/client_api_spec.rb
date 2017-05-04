require 'serverspec'

set :backend, :exec

describe 'client-api' do
  describe file('/opt/perforce/p4api') do
    it { should be_symlink }
    it { should be_mode 777 }
    it { should be_owned_by 'root' }
    it { should be_grouped_into 'root' }
  end

  describe file('/opt/perforce/p4api/lib') do
    it { should be_directory }
    it { should be_mode 755 }
    it { should be_owned_by 'root' }
    it { should be_grouped_into 'root' }
  end

  describe file('/opt/perforce/p4api/include') do
    it { should be_directory }
    it { should be_mode 755 }
    it { should be_owned_by 'root' }
    it { should be_grouped_into 'root' }
  end

  describe file('/opt/perforce/p4api/lib/libclient.a') do
    it { should be_file }
    it { should be_mode 644 }
    it { should be_owned_by 'root' }
    it { should be_grouped_into 'root' }
    its(:sha256sum) { should eq '90f4f6380c7253be058fcc38e54659d9c5004174504797d454a483f0e4ded2ef' }
  end

  describe file('/opt/perforce/p4api/lib/libp4sslstub.a') do
    it { should be_file }
    it { should be_mode 644 }
    it { should be_owned_by 'root' }
    it { should be_grouped_into 'root' }
    its(:sha256sum) { should eq '50395594a6990fefeced25d5694700ec55b0f8cc784fe627141b23697d75f7ae' }
  end

  describe file('/opt/perforce/p4api/lib/librpc.a') do
    it { should be_file }
    it { should be_mode 644 }
    it { should be_owned_by 'root' }
    it { should be_grouped_into 'root' }
    its(:sha256sum) { should eq '49ebbd18adb3b0be40a98d884a7361313053f4ee3ff8af00fb761b1a5169a7e8' }
  end

  describe file('/opt/perforce/p4api/lib/libsupp.a') do
    it { should be_file }
    it { should be_mode 644 }
    it { should be_owned_by 'root' }
    it { should be_grouped_into 'root' }
    its(:sha256sum) { should eq '31229a0c535cad6154f68841106ef8a2731a6960df04a68fafd90df762e93e16' }
  end
end
