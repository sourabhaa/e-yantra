
X=-5.0000e-01
Y=-5.0000e-01
z=8.0000e-02
X1=-5.500e-01
Y1=-4.500e-01
function sysCall_init()

    dummy=sim.getObjectHandle("Dummy")
    print("dummy "..dummy)
    hwall()
    vwall()
    -- do some initialization here
end
--macha x and y varies from -0.5 to 0.5 wt is each block's range? 0.1 wait ill show uh
 function createWall()   
    wallObjectHandle = sim.createPureShape(0, 26, {0.09, 0.01, 0.1}, 0, nil)
    sim.setShapeColor(wallObjectHandle, nil, sim.colorcomponent_ambient_diffuse, {0, 0,0})
    sim.setObjectSpecialProperty(wallObjectHandle, sim.objectspecialproperty_collidable)
    sim.setObjectSpecialProperty(wallObjectHandle, sim.objectspecialproperty_measurable)
    sim.setObjectSpecialProperty(wallObjectHandle, sim.objectspecialproperty_detectable_all)
    sim.setObjectSpecialProperty(wallObjectHandle, sim.objectspecialproperty_renderable)
    return wallObjectHandle
    end
 function hwall()
y=Y 
x=X
 for i=1,10,1
    do
        for j=1,11,1
        do
           wallObjectHandle = createWall()
           -- y=Y
           sim.setObjectPosition(wallObjectHandle,dummy,{x,y,z})
           
            y = y+1.0000e-01
            print("Y "..y ..'i='.. j)
        end
    x=x+1.0000e-01
    y=Y 
    print("X "..x..i)
    
    end
    
 end
  function vwall()
y1=Y1 
x1=X1
 for i=1,10,1
    do
        for j=1,11,1
        do
           wallObjectHandle = createWall()
           -- y=Y
           sim.setObjectPosition(wallObjectHandle,dummy,{x1,y1,z})
           sim.setObjectOrientation(wallObjectHandle,-1,{0,0,1.5708})
    
            x1 = x1+1.0000e-01
            print("Y "..y ..'i='.. j)
        end
    y1=y1+1.0000e-01
    x1=X1 
    print("X "..x..i)
    
    end
 end
 