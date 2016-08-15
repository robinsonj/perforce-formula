require 'package_helper'

describe 'Server Base' do
  it_behaves_like :p4_server_base

  describe package('helix-cli') do
    it { should_not be_installed }
  end
end
