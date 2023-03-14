l_o_C = ["aws","gcp"]
l_o_env = ["dev","test","prod"]
#list iteration
for  C in l_o_C:
    print(C)
if C =="aws":
    print("AWS is best")
#dictonary
dict_o_C = {
    "aws":'Amazom',
    "gcp":'Google'
    
}
print(dict_o_C["gcp"])
#rint(dict_o_C["aws"])
#rint(dict_o_C.get("gcp","not found"))