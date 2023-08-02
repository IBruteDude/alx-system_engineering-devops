#!/usr/bin/env ruby
regex = /.*\[from:(\+?\w*)\] \[to:(\+?\w*)\] \[flags:(\-?\d*:\-?\d*:\-?\d*:\-?\d*:\-?\d*)\].*/
puts ARGV[0].gsub(regex, '\1,\2,\3')
