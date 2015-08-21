import maya.cmds as cmds
import maya.mel as mel
from functools import partial

def UI_Rig():
    
    #check if the window exists, if exists then delete
    if(cmds.window("RigInterface",ex = True)):
        cmds.deleteUI("RigInterface",window = True)
        
    #if(cmds.dockControl("RigInterface",ex = True)):
        #cmds.deleteUI("RigInterface")

    #create the window
    cmds.window("RigInterface",title="RigToolKit",s=True,mnb=True,mxb=True,w=700, h=300)
    
    #create a tab layout
    tabs = cmds.tabLayout(imw=5,imh=5)

    #SET 1 : set of basic commands for joints 
    #create column layout in each tab
    rc1 = cmds.rowColumnLayout(nc=2,cw=[(1,350),(2,350)],columnOffset=[(1,"both",5),(2,"both",5)])                                                                                     
    
    #creates spaces between lines
    cmds.separator(h=15,style="none")
    cmds.separator(h=15,style="none")

    #creates buttons
    cmds.button('Joint Tool',w=70,h=40,command="cmds.joint()",annotation="Creates Joints");
    cmds.button('Insert Joint',w=70, h=40,command="cmds.insertJoint()",annotation="Inserts Joints");
    
    cmds.separator(h=15,style="none")
    cmds.separator(h=15,style="none")

    cmds.button('Mirror Joint',w=70, h=40,command="cmds.mirrorJoint()",annotation="Mirror's Joints");
    cmds.text("  ")
    
    cmds.separator(h=15,style="none")
    cmds.separator(h=15,style="none")
    
    cmds.button('Remove Joint',w=70, h=40,command="cmds.removeJoint()",annotation="Removes Joints");
    cmds.button('IK handle',w=70, h=40,command="cmds.ikHandle()",annotation="Inserts Joints");
    
    #its a way to go the parent. In this case, the tab layout.
    cmds.setParent("..")

    #SET 2 : set of basic commands to perform different transformations on the joints. Also some basic editors used
    rc2 = cmds.rowColumnLayout(nc=4,cw=[(1,175),(2,175),(3,175),(4,175)],columnOffset=[(1,"both",5),(2,"both",5),(3,"both",5),(4,"both",5)])
    
    #creates line spaces
    cmds.separator(h=15,style="none")
    cmds.separator(h=15,style="none")
    cmds.separator(h=15,style="none")
    cmds.separator(h=15,style="none")
    
    #buttons                                                                                     
    cmds.button('CP',w=50,h=40,command="CP()",annotation="center's Pivot");
    cmds.button('FT',w=50, h=40,command="FT()",annotation="freezes Transforms");
    cmds.button('LocalAxis',w=50, h=40,command="LocalAxis()",annotation="Shows Local Rotation Axis for the object");
    cmds.button('ComponentEditor',w=50,h=40,command="Componenteditor()",annotation="Open's Component window")
    
    
    cmds.separator(h=15,style="none")
    cmds.separator(h=15,style="none")
    cmds.separator(h=15,style="none")
    cmds.separator(h=15,style="none")
    
    cmds.button('Add Attribute',w=50,h=40,command="Addattribute()",annotation="Open's Add Attribte window")
    cmds.button('ConnectionEditor',w=50,h=40,command="Connectioneditor()",annotation="Opens's Connection Editor")
    cmds.button('Node Editor',w=50,h=40,command="NodeEditor()",annotation="Open's node Editor")
    cmds.button('SetDrivenKey',w=50,h=40,command="SDK()",annotation="Open's Set Drivenkey Options")
    
    cmds.separator(h=15,style="none")
    cmds.separator(h=15,style="none")
    cmds.separator(h=15,style="none")
    cmds.separator(h=15,style="none")
    
    cmds.button('DeleteHistory',w=50,h=40,command="deleteHistory()",annotation="Delete's history")
    cmds.button('Prefixname',w=50,h=40,command="PrefixName()",annotation="PrefixHierarchyNames")
    cmds.button('ExpressionEditor',w=50,h=40,command="Expressioneditor()",annotation="Open's the expression Editor")
    
    cmds.setParent("..")
    
    #set3 : Contraint Tool : helps you to apply constraints on the objects selected
    rc3 = cmds.rowColumnLayout(nc=2,cw=[(1,350),(2,350)],columnOffset=[(1,"both",5),(2,"both",5)])
    
    cmds.separator(h=15,style="none")
    cmds.separator(h=15,style="none")
    
    cmds.button('Constraint Tool',w=350,h=40,command="ConstraintTool()",annotation="helps you give constraints to the joints")
    
    #since the number of columns is 2, this text leaves a empty space in column2
    cmds.text(" ")
    cmds.setParent("..")
    
    #set4 : Custom Joint Tools
    rc4 = cmds.rowColumnLayout(nc=2,cw=[(1,350),(2,350)],columnOffset=[(1,"both",5),(2,"both",5)])
    cmds.separator(h=15,style="none")
    cmds.separator(h=15,style="none")
    
    #this button segments the bone
    cmds.button("Joint Segment Tool",w=150,h=40,command="JointSegTool()",annotation="Divides joints into further joints")
    #fixes the rotation of the joints
    cmds.button("Zero JointOrient Tool",w=150,h=40,command="ZeroOrientTool()",annotation="Fixes the joint orientation")
    cmds.setParent("..")
    
    #set5 : Commands for Custom Control Tools and also basic control commands required
    rc5 = cmds.rowColumnLayout(nc=4,cw=[(1,175),(2,175),(3,175),(4,175)],columnOffset=[(1,"both",5),(2,"both",5),(3,"both",5),(4,"both",5)])
    
    cmds.separator(h=15,style="none")
    cmds.separator(h=15,style="none")
    cmds.separator(h=15,style="none")
    cmds.separator(h=15,style="none")
    
    cmds.button('CV Cube',w=50,h=40,command="CV_Cube()",annotation="Creates a CV cube")
    cmds.button('CV Curve',w=50,h=40,command="CV_Curve()",annotation="Creates a CV Curve")
    cmds.button('Mirror Control Objs',w=50,h=40,command="MirrorControlObjects()",annotation="Mirror Control Objects")
    cmds.text("")
    
    cmds.separator(h=15,style="none")
    cmds.separator(h=15,style="none")
    cmds.separator(h=15,style="none")
    cmds.separator(h=15,style="none")
    
    cmds.button('Color & Rename Right Controls',w=50,h=40,command="Color_Rnm_rightCtrls()",annotation="Colors and Renames Right Controls")
    cmds.button('Color & Rename left Controls',w=50,h=40,command="Color_Rnm_leftCtrls()",annotation="Colors and Renames Right Controls")
    cmds.button('Parent Shape Node',w=50,h=40,command="ParentShapeNode()",annotation="Parent Shape Node: select the child objects first and then the parent object")
    cmds.button('Locator Tool',w=50,h=40,command="LocatorAlign()",annotation="Creates a Locator at that position")
    
    cmds.separator(h=15,style="none")
    cmds.separator(h=15,style="none")
    cmds.separator(h=15,style="none")
    cmds.separator(h=15,style="none")
    
    cmds.button('Change the color of sel obj to Red',w=50,h=40,command="ChangeColorToRed()",annotation="Changes the color of sel obj to Red")
    cmds.button('Change the color of sel obj to Blue',w=50,h=40,command="ChangeColorToBlue()",annotation="Changes the color of sel obj to Blue")
    cmds.button('Change the color of sel obj to Yellow',w=50,h=40,command="ChangeColorToYellow()",annotation="Changes the color of sel obj to Yellow")
    cmds.button('Nurbs Circle',w=50,h=40,command="NurbsCircle()",annotation="Creates a nurb Circle")
    
    cmds.separator(h=15,style="none")
    cmds.separator(h=15,style="none")
    cmds.separator(h=15,style="none")
    cmds.separator(h=15,style="none")
    
    cmds.button('Grouping Tool',w=50,h=40,command="GroupObjects()",annotation="groups selected objects")
    cmds.button('Object Alignment Tool',w=50,h=40,command="ObjectAlignment()",annotation="Aligns the last selected object to the first two selected objects")
    cmds.button('Generate obj along Curve',w=50,h=40,command="ObjectAlongCurve()",annotation="Generate objects along the CV's of the Curve")
    cmds.text(" ")
    
    cmds.setParent("..")   
    
    #set6 : button for squash and stretch mechanism
    rc6 = cmds.rowColumnLayout(nc=2,cw=[(1,350),(2,350)],columnOffset=[(1,"both",5),(2,"both",5)])
    
    cmds.separator(h=15,style="none")
    cmds.separator(h=15,style="none")
    
    cmds.button('Squash and Stretch',w=300,h=40,annotation="Creates squash and Stretch Tool")
    cmds.setParent("..")
    
    #adds the tab layout and names all of them
    cmds.tabLayout(tabs,edit=True,tabLabel=((rc1,"Skeleton Rigs"),(rc2,"Helpful Tools"),(rc3,'Constraint Tool'),(rc4,'Custom Tools for Joints'),(rc5,'Tools for Controls'),(rc6,'Squash and Stretch')))
    
    #show Window
    cmds.showWindow()
    #cmds.dockControl("Rig_ToolKit",area='left',content= "Rig" ,allowedArea='left')

#SET2 functions for HELPFUL-TOOLS uses mel commands in python
def CP():
    cmds.xform(cp=True)
    
def FT():
    cmds.makeIdentity(apply=True)
    
def LocalAxis():
    cmds.toggle(localAxis=True)
    
def Componenteditor():
    mel.eval('ComponentEditor;')
    
def Addattribute():
    mel.eval('AddAttribute;')
    
def Connectioneditor():
    mel.eval('ConnectionEditor;')
    
def NodeEditor():
    mel.eval('NodeEditorWindow')
    
def SDK():
    mel.eval('setDrivenKeyWindow \"\" {};')
    
def deleteHistory():
    cmds.delete(ch=True)
    
def PrefixName():
    mel.eval('PrefixHierarchyNames;')

def Expressioneditor():
    mel.eval('ExpressionEditor;')
    
#SET 5 : CONTROL TOOLS
def CV_Cube():
    cmds.nurbsCube();
    
def CV_Curve():
    mel.eval('CVCurveToolOptions')
    
def Color_Rnm_rightCtrls():                                     #renames the group of the controls and color codes them
    right_controls = cmds.ls(sl=True)    						#select/lists all the objects selected
    for all in right_controls:                                  #for all the controls selected:
        cmds.select(all)
        cmds.pickWalk(d='Up')                                   #tranverses up in the hierarchy
        sel_grpSDK = cmds.ls(sl=True)
        cmds.rename(sel_grpSDK[0],'grpSDK_'+all)                #renames the group
        
        cmds.pickWalk(d='Up')
        sel_grpOri = cmds.ls(sl=True)
        cmds.rename(sel_grpOri[0],'grp_Ori'+all)
        
        all_shape = cmds.listRelatives(type= 'shape all')       #selects all the objects of type shape 
        cmds.setAttr(all_shape[0]+".overrideEnabled",1)         
        cmds.setAttr(all_shape[0]+".overrideColor",18)          # changes the color

def Color_Rnm_leftCtrls():                                      #works similar to Color_rnm_rightControls
    left_controls = cmds.ls(sl=True)
    for all in left_controls:
        cmds.select(all)
        cmds.pickWalk(d='Up')
        sel_grpSDK = cmds.ls(sl=True)
        cmds.rename(sel_grpSDK[0],'grpSDK_'+all)
        
        cmds.pickWalk(d='Up')
        sel_grpOri = cmds.ls(sl=True)
        cmds.rename(sel_grpOri[0],'grp_Ori'+all)
        
        all_shape = cmds.listRelatives(type='shape_all')
        cmds.setAttr(all_shape[0]+".overrideEnabled",1)
        cmds.setAttr(all_shape[0]+".overrideColor",17)
	print "Colored renamed on left circle"
	
def ChangeColorToYellow():                                #changes colors of the objects to Yellow
    selObj = cmds.ls(sl=True)
    for all in selObj:
        cmds.setAttr(all+".overrideEnabled",1)
        cmds.setAttr(all+".overrideColor",17)
        
def ChangeColorToRed():                                   #changes colors of the objects to Red
    selObj = cmds.ls(sl=True)
    for all in selObj:
        cmds.setAttr(all+".overrideEnabled",1)
        cmds.setAttr(all+".overrideColor",13)

def ChangeColorToBlue():                                  #changes colors of the objects to Blue
    selObj = cmds.ls(sl=True)
    for all in selObj:
        cmds.setAttr(all+".overrideEnabled",1)
        cmds.setAttr(all+".overrideColor",18)

def NurbsCircle():                                        #creates a nurbs circle
    cmds.circle()
    
#Mirrors control objects
def MirrorControlObjects():
    sel_Obj = cmds.ls(sl=True)        					  #stores all the selected objects
    if len(sel_Obj)==0:                                   #if no object is selected : Throws a warning
        cmds.warning("select object")
    else:
        cmds.duplicate(rr=True)    						 #duplicates the object
        grp_sel_Obj = cmds.group()                       #groups the object
        cmds.xform(os=True,piv=[0,0,0])                  #centers the pivot point
        cmds.setAttr(grp_sel_Obj+".sx",-1)               #mirrors it across by setting scale.X to -1
        cmds.select(grp_sel_Obj)
        cmds.ungroup()                                   #ungroups the object
        cmds.makeIdentity(apply=True)    				 #freezes the transform
        
#Creates a locator for a object that matches the orientation of the object
def LocatorAlign():
    selObj = cmds.ls(sl=True)
    for allObj in selObj:                                                #all the selected objects
        loc = cmds.spaceLocator()                                        #creates a locator
        locPar = cmds.parentConstraint(allObj,loc[0])                    #parent constraints the locator so that it matches the orientation and position of the object
        find_locPar = cmds.listRelatives(loc[0],type='parentConstraint') #find the parentConstraint
        cmds.delete(find_locPar[0])                                      #when found deletes it
        cmds.rename(loc[0],"LocAlign_"+allObj)                           #renames the locator

#select the child objects and then the parent object: Parents the shape nodes of the objects        
def ParentShapeNode():
    selObjs = cmds.ls(sl=True)    							#store all the selected objs     
    if len(selObjs)==0:                                
        cmds.warning("Select atleast 2 objects")
    elif len(selObjs)>=2 :
        last_selObj = cmds.ls(sl=True,tail=1)               #if there are 2 or more objects, select the last selected the object and store it
        cmds.select(selObjs)                                #select all the objects
        cmds.select(last_selObj,toggle=True)    			#deselect the last one
        sel_children = cmds.ls(sl=True)						#store the renaming selected objects
        cmds.parent(sel_children,last_selObj)               #parent all the children to the last selected objects
        for allObjs in sel_children:
            cmds.select(allObjs)                            #select all the child objects
            cmds.makeIdentity(apply=True)    				#freeze transform on them
            find_shapeNode = cmds.listRelatives(allObjs,shapes=True)    #find the shape Nodes of those objects
            cmds.parent(find_shapeNode[0],last_selObj,r=True,s=True)    #parent the shapeNode to the last selected object
            cmds.delete(allObjs)                                        #delete the transform node of the selected child objects
            cmds.select(last_selObj)                        #select the last selected obj that is the parent obj

#group selected object or makes groups for all selected objects
def GroupObjects():
    selObjects = cmds.ls(sl=True)    								#store all the selected objects
    for all in selObjects:                                            
        grp = cmds.group(empty=True)    							#creates an empty group
        rnm_grp = cmds.rename(grp,"grp_"+all)                       #renames the group
        cmds.parent(rnm_grp,all)                                    #parents the grp with the object
        cmds.setAttr(rnm_grp + ".tx",0)                             #set attributes to 0
        cmds.setAttr(rnm_grp + ".ty",0)
        cmds.setAttr(rnm_grp + ".tz",0)
        cmds.setAttr(rnm_grp + ".rx",0)
        cmds.setAttr(rnm_grp + ".ry",0)
        cmds.setAttr(rnm_grp + ".rz",0)
        cmds.delete(cmds.pointConstraint(all,rnm_grp))
        cmds.parent(rnm_grp,world=True)
        cmds.parent(all,rnm_grp)
        cmds.makeIdentity(all,apply=True,t=True,r=True,s=True)
        
def ObjectAlignment():	                                            #aligns the third object to the first two selected accoridng to position
    if cmds.window("ObjectAligner",ex=True):    					#find window : if found, delete it
        cmds.deleteUI("ObjectAligner",window=True)    			
    cmds.window("ObjectAligner",title = "Object Alginment Tool", s = False, tb = True, mnb = True, mxb = True, mb = True,wh= (400,200))    #create a new window
    cmds.columnLayout(adj=True)    									#create a column layout
    cmds.text(l= "Instructions : select source then target")        #displays the instruction
    cmds.button(l = "Align the object and delete Aligner", w=300, h=100, c="aligner()")    #creates a button to align object
    cmds.showWindow("ObjectAligner")

#function for ObjectAlignment()    
def aligner():
    prtCns = cmds.parentConstraint()                    #creates a parent constraint and then deletes it
    cmds.delete(prtCns)

#Constraint tool
def ConstraintTool():                                   #helps to give constraints
    cmds.window("cnsWin",w=200,h=50,t="Constraining Tool",s=False)
    cmds.columnLayout(adj=True)
    cmds.textScrollList("List",h=50,a=["Parent Constraint","Orient Constraint","Point Constraint"])        #creates a list to select an option
    cmds.checkBox("CheckBox",label="Maintain Offset")
    cmds.button(label="Click to Constraint",c="Constraint()")
    cmds.button(label="Remove Constraint",c="rmvConstraint()")
    cmds.showWindow("cnsWin")
    
def Constraint():                                            #uses maya commands to give constraints to the selected objects
    sel_item = cmds.textScrollList("List",q=True,si=True)
    if(cmds.checkBox("CheckBox",query=True,value=True) == 1):
        if(sel_item[0] == "Parent Constraint"):
            cmds.parentConstraint(mo=True)
        if(sel_item[0] == "Orient Constraint"):
            cmds.orientConstraint(mo=True)
        if(sel_item[0] == "Point Constraint"):
            cmds.pointConstraint(mo=True)
    else:
        if(sel_item[0] == "Parent Constraint"):
            cmds.parentConstraint()
        if(sel_item[0] == "Orient Constraint"):
            cmds.orientConstraint()
        if(sel_item[0] == "Point Constraint"):
            cmds.pointConstraint()

def rmvConstraint():                                        #remove the constraint
    sel_item = cmds.textScrollList("List",q=True,si=True)   #depending on what constraint is selected in the list, find that type of constraint in an object and delete it
    if (sel_item[0] == "Parent Constraint"):
        selObj = cmds.ls(sl=True)
        Cns = cmds.listRelatives(selObj,type="parentConstraint")
        cmds.delete(Cns)
    if (sel_item[0] == "Orient Constraint"):
        selObj = cmds.ls(sl=True)
        Cns = cmds.listRelatives(selObj,type="orientConstraint")
        cmds.delete(Cns)
    if (sel_item[0] == "Point Constraint"):
        selObj = cmds.ls(sl=True)
        Cns = cmds.listRelatives(selObj,type="pointConstraint")
        cmds.delete(Cns)

def ObjectAlongCurve():                                        #creates an object along the cv's of the curve
    window_1 = cmds.window("Create Object Along Curve")
    cmds.columnLayout()
    objectlist = cmds.optionMenu("objects",label="Select object")
    cmds.menuItem("Cube", parent="objects")
    cmds.menuItem("Circle",parent="objects")
    cmds.menuItem("Joint",parent="objects")
    cmds.button(label = "Create Selected option", command = partial(CreateObjects,objectlist))            #sends in the list in the object list Menu
    cmds.showWindow(window_1)
    
def CreateObjects(objectlist,*args):
    selCVs = cmds.ls(sl=True)
    selCVs_pos = cmds.filterExpand(ex=True,sm=28)
    cmds.select(cl=True)
    ObjName = cmds.optionMenu(objectlist,query=True,value=True)
    for num in selCVs_pos:
        position = cmds.pointPosition(num,w=True)
        pos_x = position[0]
        pos_y = position[1]
        pos_z = position[2]
        if(ObjName == "Cube"):
            make_obj = cmds.nurbsCube();
            cmds.setAttr(make_obj[0] + ".tx",pos_x)
            cmds.setAttr(make_obj[0] + ".ty",pos_y)
            cmds.setAttr(make_obj[0] + ".tz",pos_z)
        if(ObjName == "Circle"):
            make_obj = cmds.circle();
            cmds.setAttr(make_obj[0] + ".tx",pos_x)
            cmds.setAttr(make_obj[0] + ".ty",pos_y)
            cmds.setAttr(make_obj[0] + ".tz",pos_z)
        if(ObjName == "Joint"):
            make_obj = cmds.joint()
            cmds.setAttr(make_obj + ".tx",pos_x)
            cmds.setAttr(make_obj + ".ty",pos_y)
            cmds.setAttr(make_obj + ".tz",pos_z)
            
def JointSegTool():
    cmds.window("Joints",w=200,h=100,s=True,t="Joint Segment Tool")
    cmds.columnLayout("Column1",adj=True)
    cmds.text(label="Select a bone to segment")
    cmds.separator(style="none")
    cmds.separator(style="none")
    cmds.text(label="Number of Joints?")
    cmds.textField("Number")
    cmds.separator(style="none")
    cmds.separator(style="none")
    cmds.button(label="Create Joints",c="create_Joints()")
    cmds.showWindow("Joints")
    
def create_Joints():
    src_joint = cmds.ls(sl=True)
    cmds.select(hi=True)
    findselAmt = cmds.ls(sl=True)
    if (len(findselAmt)<2):
        cmds.warning("select atleast 2 joints")
    else:
        noOfjoints = cmds.textField("Number",query=True,text=True)
        num_jnts = float(noOfjoints)
        cmds.pickWalk(d="down")
        childjnt = cmds.ls(sl=True)
        cmds.select(childjnt)
        pos_child = cmds.xform(childjnt[0],query=True,translation=True,ws=True)
        pos_start = cmds.xform(src_joint[0],query=True,translation=True,ws=True)
        splitPos_x = pos_child[0] - pos_start[0]
        splitPos_y = pos_child[1] - pos_start[1]
        splitPos_z = pos_child[2] - pos_start[2]
        splitPos = [(splitPos_x/num_jnts),(splitPos_y/num_jnts),(splitPos_z/num_jnts)]
        num_joints = int(num_jnts)
        cmds.pickWalk(d="up")
        if(noOfjoints<2):
            cmds.warning("Must create atleast 1 segment")
        else:
            for jnt in range(1,num_joints):
                newJoint = cmds.insertJoint(src_joint)
                newJoint = cmds.rename(newJoint, "tempName"+ str(jnt))
                cmds.move(splitPos[0],splitPos[1],splitPos[2],newJoint+".scalePivot",newJoint+".rotatePivot",ws=True,r=True)
                src_joint = newJoint
                cmds. select(newJoint)

def ZeroOrientTool():
    all_jnts = cmds.ls(sl=True)
    for all in all_jnts:
        if cmds.objExists(all + "_aimConstraint*"):
            cmds.delete(all + "_aimConstraint*")
        ori_x = cmds.getAttr(all+".rx")
        ori_y = cmds.getAttr(all+".ry")
        ori_z = cmds.getAttr(all+".rz")
        cmds.setAttr(all + ".jointOrientX",ori_x)
        cmds.setAttr(all+ ".jointOrientY",ori_y)
        cmds.setAttr(all + ".jointOrientZ",ori_z)
        cmds.setAttr(all + ".rx",0)
        cmds.setAttr(all + ".ry",0)
        cmds.setAttr(all + ".rz",0)
            

        

    