print("Python first program")
print("sanskriti dutta")
import matplotlib.pyplot as plt # type: ignore
#Graph ___Sanskriti_dutta___
print("\n******************************************************")
graph=input("\nWould you like to get some additional information about our site and know about its progress in different countries? (Yes/No)--- ")
if graph.lower() == "yes":
  print("\n1. List of features:")
  features=["clear product images","product reviews","product descriptions","easy checkout process","easy search","simple navigation","easy to use on mobile devices","payment options","shop remembers me","product videos"]
  percentage=[87.6,78.1,77.3,75.6,69.3,55.8,48.4,39.5,30.8,20.9] # GRAPH 1
  plt.barh(features,percentage)
  plt.xlabel("features")
  plt.ylabel("percentage")
  plt.show()
  print("\n2. Our p_r_o_g_r_e_s_s in different countries")
  countries=["brazil","china","france","germany","india","japan","russia","spain","sweden","united kingdom","united states"]
  money_stats=[350,626,1228,1064,928,1083,396,849,1146,1629,1804]
  plt.barh(countries,money_stats , color=['brown','blue','green','black','yellow','pink','gold','purple','grey','orange','red'])
  plt.xlabel("Counteries")
  plt.ylabel("Monetorial Statistics")
  plt.show()
  print("\n3. ONLINE SHOPPING % BY AGE GROUP")
  print("-Millenials continue to be the largest age group to shop online")
  age_group=[11,21,31,12,12,27,24,53,4,5,32,32,43,1,35,15,35,12,12,32,6,36,8,98,87,65,44,33,22,27,42,67,86,56,15]
  plt.hist(age_group,bins=5)
  plt.show()
  print("\n*PROGRAM ENDED*\nThankyou for visiting ^_^")
 
else:
    print("*PROGRAM ENDED*\nThankyou for visiting ^-^")

