class Point	
	#attr_accessor :x #(x nesnesi okuma yazmak için hazır kod yazdı(setter/getter))
	#attr_reader :x
	#attr_writer :x
	#attr :x,true 
	attr_accessor :x,:y
	def initialize(x,y)
		@x=x
		@y=y
	end
	def merhaba	
		puts "merhaba,ben #{x},#{y}"
	end
end
p=Point.new 19,123
p.merhaba
p.x=17
p.y=34
p.merhaba
puts p.x
puts p.y
			
