#!/usr/bin/env ruby
# The regular expression must match 10 digit phone number
puts ARGV[0].scan(/^4155049898$/).join
