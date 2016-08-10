require 'package_helper'

describe 'Server' do
  it_behaves_like :p4_server
  it_behaves_like :p4_cli # Package 'helix-p4d' has a dependency to install the
                          # client packages.
end
