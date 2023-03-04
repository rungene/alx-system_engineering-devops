#!/usr/bin/env ruby
# The regular expression only matching: capital letters
puts ARGV[0].scan(/[A-Z]/).join
