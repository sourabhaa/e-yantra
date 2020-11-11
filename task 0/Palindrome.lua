--[[
*****************************************************************************************
*
*
*  This script is code stub for CodeChef problem code PAL_LUA
*  under contest PYLT20TS in Task 0 of Nirikshak Bot (NB) Theme (eYRC 2020-21).
*
*  Filename:			PAL_LUA.lua
*  Created:				07/10/2020
*  Last Modified:		07/10/2020
*  Author:				e-Yantra Team
*
*****************************************************************************************
]]--

function palindrome(str)
  if (( string.len(str) >= 2) and (string.len(str) <= 100 ))
    then
      rstr=string.reverse(str)
      if (str == rstr) then 
        print("It is a palindrome" )
      else 
        print("It is not a palindrome")
      end

 
    end
end

tc = tonumber(io.read())
if (( tc >= 1) and (tc <= 25 ))
then
  for i=1,tc
  do
      str= string.lower(io.read())
      palindrome(str)
  end

  end
