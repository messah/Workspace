require 'benchmark'

Example = Struct.new("Example", :value)

struct = Example.new
hash = {}
value = "The value"

n = 5000000
Benchmark.bm do |m|
  # test assignment and access for Hash and Struct
  m.report { n.times do; hash[:value] = value; end }
  m.report { n.times do; struct.value = value; end }
end
