#!/usr/bin/env ruby
# The regular expression must match School
puts ARGV[0].scan(/hbn|hbt+n/).join
