#!/usr/bin/env ruby
# The regular expression must match School
# A word character: [a-zA-Z_0-9] \w
puts ARGV[0].scan(/^h\wn$/).join
