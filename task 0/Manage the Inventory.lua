--[[
*****************************************************************************************
*
*
*  This script is code stub for CodeChef problem code INV_LUA
*  under contest PYLT20TS in Task 0 of Nirikshak Bot (NB) Theme (eYRC 2020-21).
*
*  Filename:            INV_LUA.lua
*  Created:             07/10/2020
*  Last Modified:       07/10/2020
*  Author:              e-Yantra Team
*
*****************************************************************************************
]]--
 
-- manageInventory function to add, update / delete items to / from the Inventory
function manageInventory()
  Inventory={}
  N = tonumber(io.read())
  if (N>=1 and N <= 100) then
    for i=1,N do
         Inventory[i]={}
        itemlist_raw=io.read()
        n_of_item=tonumber(string.match(itemlist_raw, '%f[%d]%d[,.%d]*%f[%D]'))
        items_name=itemlist_raw:gsub("%s+%f[%d]%d[,.%d]*%f[%D]","")
          if(n_of_item>=1 and n_of_item<= 100) then
            for j=1, 2 do        
              if j==1 then
              Inventory[i][j]=items_name
              end
              if j==2 then
              Inventory[i][j]=n_of_item
              end
            end
          end  
  
    end
  end  
 
  t=N
   
  M = tonumber(io.read())
  if ((M>=1 and M <= 100) or (M>=1 and M<= 10)) then
      editIvent={}
      for i=1,M do
          editIvent[i]={}
          command_raw=io.read()
          command=((string.match(command_raw, 'ADD')) or (string.match(command_raw, 'DELETE')))
          
          editing_value=tonumber(string.match(command_raw,'%f[%d]%d[,.%d]*%f[%D]'))
          itemX=command_raw:gsub(command,"")
          editing_items_name=itemX:gsub("%s+%f[%d]%d[,.%d]*%f[%D]","")
          editing_items_name=editing_items_name:gsub('%s',"")
        if (command == 'ADD') or (command == 'DELETE')  then 
          if (editing_value >= 0 and editing_value <= 100) then
            for j=1, 3 do  
              if j==1 then
              editIvent[i][j]=command 
              end        
              if j==2 then
              editIvent[i][j]=editing_items_name
              end
              if j==3 then
              editIvent[i][j]=editing_value
              end
              
            end          
          end  
        end  
      end
  end         
        in2={}       
        for i=1, N+M do
          in2[i]={}
          for j=1,2 do
            if i<N+1 then       
              if j==1 then
              in2[i][j]=Inventory[i][j]
              end
              if j==2 then
              in2[i][j]=Inventory[i][j]
              end
            else
              in2[i][j]=0
            end
          end
        end    

      for k = 1,M do 
        if editIvent[k][1] == "ADD" then             
          acount=0        
          for i =1 , t do      
            if editIvent[k][2]== in2[i][1] then
              in2[i][2]=((in2[i][2])+(editIvent[k][3])) 
              io.write("UPDATED Item "..editIvent[k][2].."\n")              
            else  
              acount=acount+1             
            end            
          end         
            if acount==t then
             t=t+1                                        
              in2[t][2]=editIvent[k][3]
              in2[t][1]=editIvent[k][2]              
              io.write("ADDED Item "..editIvent[k][2].."\n")
            end
        end

        if editIvent[k][1] == "DELETE" then 
          dcount=0
          for i = 1,t do             
            if editIvent[k][2]== in2[i][1] then
              if editIvent[k][3]> in2[i][2] then
                io.write("Item "..editIvent[k][2].." could not be DELETED\n")               
              else
                in2[i][2]= in2[i][2]-editIvent[k][3] 
                io.write("DELETED Item "..editIvent[k][2].."\n")               
              end
            else
              dcount=dcount+1
            end
          end  
          if(dcount== t) then
            io.write("Item "..editIvent[k][2].." does not exist\n")
          end
        end  
      end
  sum=0
  for i=1,N+M do
    sum = sum+in2[i][2]
  end
  io.write(sum.."\n")
end
 
-- for each case, call the manageInventory function to add, update / delete items to / from the Inventory
tc = tonumber(io.read())
i = 0
if ((tc>=1 and tc<=25) or (tc>=0 and tc<=5)) then
  while i < tc do
    manageInventory()
      i = i + 1
  end
end 