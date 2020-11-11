function generatePattern()
  n = tonumber(io.read())
  for i=n,1,-1 do
	  for k=1,i,1 do
		  if (k%5==0)
		then
    	io.write('#')
		else
		  io.write('*')
		end 
	  end
	  io.write('\n')
	end
    
end
 
-- read the test cases input
tc = tonumber(io.read())

-- for each case, call the generatePattern function to print the pattern
for i=1,tc
do
    generatePattern()
end