require 'serverspec'

set :backend, :exec

shared_examples_for :p4_cli do
  describe 'P4 CLI' do
    describe package('helix-cli') do
      it { should be_installed }
    end

    describe package('helix-cli-base') do
      it { should be_installed }
    end
  end
end
