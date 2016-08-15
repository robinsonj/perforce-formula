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

shared_examples_for :p4_cli_base do
  describe 'P4 CLI Base' do
    describe package('helix-cli') do
      it { should_not be_installed }
    end

    describe package('helix-cli-base') do
      it { should be_installed }
    end
  end
end

shared_examples_for :p4_broker do
  describe 'P4 Broker' do
    describe package('helix-broker') do
      it { should be_installed }
    end

    describe package('helix-broker-base') do
      it { should be_installed }
    end
  end
end

shared_examples_for :p4_broker_base do
  describe 'P4 Broker Base' do
    describe package('helix-broker') do
      it { should_not be_installed }
    end

    describe package('helix-broker-base') do
      it { should be_installed }
    end
  end
end

shared_examples_for :p4_server do
  describe 'P4 Server' do
    describe package('helix-p4d') do
      it { should be_installed }
    end

    describe package('helix-p4d-base') do
      it { should be_installed }
    end

    describe package('helix-p4dctl') do
      it { should be_installed }
    end
  end
end

shared_examples_for :p4_server_base do
  describe 'P4 Server' do
    describe package('helix-p4d') do
      it { should_not be_installed }
    end

    describe package('helix-p4d-base') do
      it { should be_installed }
    end

    describe package('helix-p4dctl') do
      it { should_not be_installed }
    end
  end
end
