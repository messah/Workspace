class Mutablepoint
	def initialize(x,y);@x,@y = x,y; end

	def x 
		@x 
	end
	def y 
		@y
	end

	def x=(value)
		@x = value
	end

	def y=(value)
		@y = value
	end
end

p=Mutablepoint.new 1,1
puts p.x
puts p.y
