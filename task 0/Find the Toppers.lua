--[[
*****************************************************************************************
*
*
*  This script is code stub for CodeChef problem code SCOR_LUA
*  under contest PYLT20TS in Task 0 of Nirikshak Bot (NB) Theme (eYRC 2020-21).
*
*  Filename:			SCOR_LUA.lua
*  Created:				07/10/2020
*  Last Modified:		07/10/2020
*  Author:				e-Yantra Team
*
*****************************************************************************************
]]--

function readScoreList(N)

    local scorelist={}
    local marks={}
    if (( N >= 2) and (N <= 100 )) then
        for i=1,N
        do
        name=io.read()
        mark=tonumber(string.match(name, '%f[%d]%d[,.%d]*%f[%D]'))
        if (( mark >= 0) and (100 >= mark )) then
          names=name:gsub("%s+%f[%d]%d[,.%d]*%f[%D]","")
          table.insert(scorelist,i,names)
          table.insert(marks,i,mark)
          end

          function spairs(t, order)

              local keys = {}
              for k in pairs(t) do keys[#keys+1] = k end

              if order then
                  table.sort(keys, function(a,b) return order(t, a, b) end)
              else
                  table.sort(keys)
              end

              local i = 0
              return function()
                  i = i + 1
                  if keys[i] then
                      return keys[i], t[keys[i]]
                  end
              end
          end
     end
end
        for k,v in spairs(marks, function(t,a,b) return t[b] > t[a] end) do

            topper=marks[k]
            top=scorelist[k]
        end
        -- print("topm:"..topper)
        -- print("tops:"..top)
        topperlist ={}
        c=0
        for k,v in spairs(marks, function(t,a,b) return t[b] > t[a] end) do
            -- print(marks[k])
            if topper == marks[k]
            then 
            c=c+1
            table.insert(topperlist,scorelist[k])
           
            end
            -- print("c: "..c)
        end     
                for k,v in spairs(topperlist, function(t,a,b) return t[b] > t[a] end) do
                if c>1 then
                print(topperlist[k])
                else
                print(top)
               
          end
        end

        

       

        
end


tc = tonumber(io.read())
if (( tc >= 1) and (tc <= 25 )) then
for i=1,tc
do
    local N=tonumber(io.read())
    score_list=readScoreList(N);
  
end
end
