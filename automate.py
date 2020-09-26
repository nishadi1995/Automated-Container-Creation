import os
import re
import xml_parser


def need_to_combine():
   val = raw_input("Do you need to combine these two services? : ") 
   if (val == "yes"):return 1 
  
#implement - generate effective pom automatically
def can_combine(pom_1,pom_2):
   tree_1= xml_parser.input_xml(pom_1)
   tree_2= xml_parser.input_xml(pom_2)

   dependencyInfo_1 = xml_parser.derive_dependencies(tree_1)
   dependencyInfo_2 = xml_parser.derive_dependencies(tree_2)

   dependencyInfoSet_1 = xml_parser.list_to_set(dependencyInfo_1)
   dependencyInfoSet_2 = xml_parser.list_to_set(dependencyInfo_2)

   print("parser checks dependency conflicts")
   return xml_parser.compare_dependencies(dependencyInfoSet_1,dependencyInfoSet_2)


#derive jar file location from 'ARG JAR_FILE' and append that to given dockerfile location
#return absolute path to jar file
def jarFile_location(dockerfile_1,dockerfile_2):
   f1 = open(dockerfile_1+"Dockerfile", "r")
   f2 = open(dockerfile_2+"Dockerfile", "r")
   list_of_lines1 = f1.readlines()
   list_of_lines2 = f2.readlines()

   #print(re.split("=",list_of_lines1[1]))

   JAR_FILE_1 = list_of_lines1[1][13:]
   JAR_FILE_2 = list_of_lines2[1][13:]

   return (dockerfile_1+JAR_FILE_1).rstrip("\n") , (dockerfile_2+JAR_FILE_2).rstrip("\n")



def copy_to_current_directory(jar_path1,jar_path2):
   os.system('cp -R {} .'.format(jar_path1))
   os.system('cp -R {} .'.format(jar_path2))


#"/home/nishadi/Desktop/spring-performance-test-master/server/target/server-0.0.1.jar"
#create the DockerFile (and run)

#implement - get jar name and input
def combine():

   f = open("Dockerfile", "r")
   list_of_lines = f.readlines()

   list_of_lines[1] = "ARG SERVER_JAR_FILE={}\n".format("server-0.0.1.jar")
   list_of_lines[2] = "ARG CLIENT_JAR_FILE={}\n".format("client-0.0.1.jar")

   f = open("Dockerfile", "w")
   f.writelines(list_of_lines)
   f.close()

   return 1

#building .sh file
#get copied names and write it in start.sh

def run_DockerFile():
   os.system('sudo docker build --tag "single_container_auto" .')
   os.system('sudo docker run --name client_server single_container_auto')


#---------------------------------main------------------------------------------------#

print("DO IT GIRL!!")
dockerfile_1 = raw_input("Enter Dockerfile 1 location : ") 
dockerfile_2 = raw_input("Enter Dockerfile 2 location : ")

xml_1 = raw_input("Enter effective pom file 1 location : ") 
xml_2 = raw_input("Enter effective pom file 2 location : ")


if (need_to_combine()):
   if (can_combine(xml_1,xml_2)):
       jar_path1,jar_path2 = jarFile_location(dockerfile_1,dockerfile_2)
       copy_to_current_directory(jar_path1,jar_path2)
       combine()
       run_DockerFile()


#update dockerfile, start.sh
#final - derive different services from yml and complete all these

