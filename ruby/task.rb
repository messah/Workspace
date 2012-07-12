puts "", "--- Sınıf değişkeni"

class Poligon
  @@kenarlar = 10
  def self.kenarlar
    @@kenarlar
  end
end

puts Poligon.kenarlar # => 10

class Ucgen < Poligon
  @@kenarlar = 3
end

puts Ucgen.kenarlar # => 3

class Dortgen < Poligon
  @@kenarlar = 4
end

puts Poligon.kenarlar # => 4

%w(Poligon Ucgen Dortgen).each { |c| Object.send(:remove_const, c.to_sym) }

puts "", "--- Sınıf kopyası değişkeni"

class Poligon
  attr_accessor :kenarlar
  @kenarlar = 10
end

begin
  puts Poligon.kenarlar # => NoMethodError: undefined method ‘kenarlar’ for Poligon:Class
rescue => e
  puts e
end

puts Poligon.new.kenarlar # => nil

class Poligon
  class << self; attr_accessor :kenarlar end
  @kenarlar = 8
end

puts Poligon.kenarlar # => 8

class Ucgen < Poligon
  @kenarlar = 3
end

puts Ucgen.kenarlar # => 3
puts Poligon.kenarlar # => 8
