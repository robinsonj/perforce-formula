require 'serverspec'

set :backend, :exec

describe 'P4 CLI' do
  describe package('helix-cli') do
    it { should be_installed }
  end

  describe package('helix-cli-base') do
    it { should be_installed }
  end
end
