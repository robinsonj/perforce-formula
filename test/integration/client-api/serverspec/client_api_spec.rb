require 'serverspec'

set :backend, :exec

describe 'client-api' do
  describe file('/opt/perforce/p4api') do
    it { should be_symlink }
    it { should be_mode 777 }
    it { should be_owned_by 'root' }
    it { should be_grouped_into 'root' }
  end
end
