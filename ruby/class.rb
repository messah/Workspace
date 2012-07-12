class Point
	def initialize(x,y)
		@x,@y = x,y
	end
	
	def to_s
		"{#@x,#@y}"
	end
end

p = Point.new(1,2)
puts p
