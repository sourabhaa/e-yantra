--[[
*****************************************************************************************
*
*
*  This script is code stub for CodeChef problem code WLEN_LUA
*  under contest PYLT20TS in Task 0 of Nirikshak Bot (NB) Theme (eYRC 2020-21).
*
*  Filename:			WLEN_LUA.lua
*  Created:				07/10/2020
*  Last Modified:		07/10/2020
*  Author:				e-Yantra Team
*
*****************************************************************************************
]]--

function countChar(str)
  s= string.find(str,"@")
  if(s==1) then 
  str = str:gsub("@","")
  printres=''
  for token in string.gmatch(str, "[^%s]+") do
    printres= printres..tostring(string.len(token))..','

  end
  printres = printres:sub(1, -2)
  print(printres)
  end  
end

tc = tonumber(io.read())
if (( tc >= 1) and (tc <= 25 )) then
for i=1,tc
do
    str=io.read();
    countChar(str)
end
end
