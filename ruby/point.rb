class Point 
	attr_accessor :x,:y,:z
	@@z=122
	def initialize(x,y)
		@x,@y=x,y
	end
	def goruntule
		puts x,y,z
	end
end
p=Point.new 123,12
p.goruntule
p.z = 15			
puts p.z
