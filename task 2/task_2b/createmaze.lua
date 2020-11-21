 maze = {
 {7, 3, 10, 10, 6, 3, 10, 6, 3, 6}, {1, 12, 3, 10, 12, 5, 7, 9, 12, 5},
 {1, 14, 9, 6, 7, 5, 9, 10, 6, 5}, {5, 3, 6, 5, 5, 9, 6, 3, 12, 5},
 {5, 5, 9, 12, 1, 14, 9, 4, 3, 4}, {5, 9, 6, 7, 1, 10, 10, 12, 5, 13},
 {9, 6, 5, 1, 8, 10, 10, 14, 9, 6}, {7, 5, 5, 9, 6, 3, 6, 3, 6, 5},
 {5, 5, 9, 14, 13, 5, 9, 12, 5, 5}, {9, 8, 10, 10, 10, 12, 11, 10, 8, 12}
 }


function sysCall_init()
dummy= sim.getObjectHandle("Dummy") 
createmaze()
end


function createWall()
    wallObjectHandle = sim.createPureShape(0, 26, {0.09, 0.01, 0.1}, 0, nil)
    sim.setShapeColor(wallObjectHandle, nil, sim.colorcomponent_ambient_diffuse, {0, 0, 0})
    sim.setObjectSpecialProperty(wallObjectHandle, sim.objectspecialproperty_collidable)
    sim.setObjectSpecialProperty(wallObjectHandle, sim.objectspecialproperty_measurable)
    sim.setObjectSpecialProperty(wallObjectHandle, sim.objectspecialproperty_detectable_all)
    sim.setObjectSpecialProperty(wallObjectHandle, sim.objectspecialproperty_renderable)
    return wallObjectHandle
end

function createmaze()

X=-4.5000e-01
Y=-5.0000e-01
z=6.5000e-02

function top_down(x,y,z)

    wallObjectHandle = createWall()
    sim.setObjectPosition(wallObjectHandle,dummy,{x,y,z})
   
end


function left_right(x,y,z)

    wallObjectHandle = createWall()
    sim.setObjectPosition(wallObjectHandle,dummy,{x,y,z})
    sim.setObjectOrientation(wallObjectHandle,-1,{0,0,1.5708})
end

x1=X
y1=Y

for i=1,10,1
        do
    for j=1,10,1
        do
        print(maze[i][j].."= maze number")
        print("x=".. x1.."y="..y1.."z="..z)
        if maze[i][j] == 2 or maze[i][j] == 2+8 or maze[i][j] == 2+1 or maze[i][j] == 2+4 or maze[i][j] == 2+8+4 or maze[i][j] == 2+8+1 or maze[i][j] == 2+4+1 then 
            print("2 if lop")
            top_down(x1,y1,z)
        
            end 
        if maze[i][j] == 8 or maze[i][j] == 2+8 or maze[i][j] == 4+8 or maze[i][j] == 1+8 or maze[i][j] == 2+8+4 or maze[i][j] == 2+8+1 or maze[i][j] == 4+8+1 then 
            print("8 if lop")
            top_down((x1+0.1000e-01),y1,z)
            end
        if maze[i][j] == 1 or maze[i][j] == 2+1 or maze[i][j] == 1+8 or maze[i][j] == 1+4 or maze[i][j] == 2+8+1 or maze[i][j] == 2+4+1 or maze[i][j] == 8+4+1 then
            print("1 if lop")
            left_right((x1+(-0.5000e-01)),(y1+(0.5000e-01)),z) 
            end
        if maze[i][j] == 4 or  maze[i][j] == 2+4 or maze[i][j] == 4+8 or maze[i][j] == 1+4 or maze[i][j] == 2+8+4 or maze[i][j] == 2+4+1 or maze[i][j] == 8+4+1  then 
            print("4 if lop")
            left_right((x1+(-0.5000e-01)),(y1+(0.5000e-01)+0.1000e-01),z)
            end 
        
        y1=y1+1.0000e-01
        end
        x1=x1+1.0000e-01
        y1=Y
      end
  

end
