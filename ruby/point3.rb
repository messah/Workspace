class Point	
	attr_accessor :x,:y
	def initialize (*args)
	@x,@y=*args
	end
end
class Point3D < Point
	attr_accessor :z	
	def initialize (*args)
		super 
		@z= args.last
		
	end
end
				
p=Point3D.new 12,13,15
puts p.z
puts p.y
puts p.x


