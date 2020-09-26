from lxml import etree

def input_xml(xml_file):
    tree = etree.parse(xml_file) #ElementTree object
    root = tree.getroot()   #value of the first tag and address

    return etree.ElementTree(root)  #ElementTree object

def derive_dependencies(tree):
    depend = tree.xpath("//*[local-name()='dependency']")   #address of the dependency tag
    dependencyInfo = [[]]
    for dep in depend:
        infoList = []
        for child in dep.getchildren():
            infoList.append(child.tag.split('}')[1])
            infoList.append(child.text)

        dependencyInfo.append([infoList[1],infoList[3],infoList[5]])

    #outF = open("myOutFile.txt", "w")
    #for ele in dependencyInfo:
    #   for e in ele:
    #        outF.write(e+'\n')
    #print(dependencyInfo)
        
    return dependencyInfo

#def checkDependencyManagement(tree):
#    dependency_Management = tree.xpath("//*[local-name()='dependencyManagement']")   #address of the dependencyManagement tag
#    print(dependency_Management)

def list_to_set(dependencyInfo):
    return set(tuple(x) for x in dependencyInfo)

def compare_dependencies(dependencyInfoSet1,dependencyInfoSet2):

    result= all(elem in dependencyInfoSet1  for elem in dependencyInfoSet2) and all(elem in dependencyInfoSet2  for elem in dependencyInfoSet1)
    if (result):
        print("Both containers can run on each other")
        return 1
    elif (dependencyInfoSet1.issubset(dependencyInfoSet2)):
        print("Container one can run on container two")
        return 1
    elif (dependencyInfoSet2.issubset(dependencyInfoSet1)):
        print("Container two can run on container one")
        return 1
    else :
        print("May contain conflicting dependencies")
        return 0

#***********************************************************************************************#
        
#xml_1 = raw_input("Input xml file one: ")
#xml_2 = raw_input("Input xml file two: ")

#tree_1 = input_xml(xml_1)
#tree_2 = input_xml(xml_2)

#dependencyInfo_1 = derive_dependencies(tree_1)
#dependencyInfo_2 = derive_dependencies(tree_2)

#dependencyInfoSet_1 = list_to_set(dependencyInfo_1)
#dependencyInfoSet_2 = list_to_set(dependencyInfo_2)

#compare_dependencies(dependencyInfoSet_1,dependencyInfoSet_2)

