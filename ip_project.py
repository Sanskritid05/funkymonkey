
# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""
#___Naina_Mishra___
from IPython.display import Image,display
import matplotlib.pyplot as plt
import pandas as pd
import random
print("*****WELCOME TO OUR SHOPPING SITE*****")
print("The funkiest style your money could ever buy!!!")
print("*Sanskriti*Naina*Arina*")
print("p r e s e n t s")
print("WE FUNKY MONKEY'S\nWear your heart on your sleeve and humor on your clothes.")
print("Namaste!!!  Welcome to our newly launched online shopping site...")
usr_name=(input("\nWhat would you like us to call you???:--"))
print("\nHey,", usr_name, "let's make our connection more easy and secure.\nPlease fill out some information.")
print("Inform@tion booklet-")
f_name=(str(input("FIRSTNAME:")))
l_name=(str(input("LASTNAME:")))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
cntct=(int(input("CONTACT:")))
Adrs=(input("ADDRESS:"))
print("\nNow let's explore our site---")
print("For whom would you like to shop??")
print("1.Men")
print("2.Women")
print("3.Kids")
cat=int(input("Enter your choice : "))

while cat > 3:
    print("That is not in the list")
    cat=int(input("Enter your choice: "))

checkout = {}

if cat==1:
    print("\nYou selected men's wear ")
    print("Categories")
    print("1.Topwear\n2.Bottomwear\n3.Sportswear\n4.Ethnicwear\n5.Winter wear")
    men_wear=(int(input("Select category:")))
   
    while men_wear > 5:
        print("That option is not in the category")
        men_wear=(int(input("Select category:")))

    if men_wear==1:
        print("\nTOPWEARS-")
        print("1.Tshirts")
        print("2.Shirts")
        print("3.Sweatshirts")
        print("4.Blazers & Suits")
        print("5.Coats")
        topwear = {1: "Tshirts", 2:"Shirts", 3:"Sweatshirts", 4:"Blazers & Suits", 5:"Coats"}
       
        #all avaible options with color in topwear
        tshirts = {"Red":[],
                   "Blue": [],
                   "Yellow": [],
                   "Pink": [],
                   "Black": []}
        shirts = {"Blue": ["mb1", "mb2", "mb3", "mb4", "mb5"],
                  "Red":[],
                  "Yellow": [],
                  "Pink": [],
                  "Black": []}
        sweatshirts = {"Red":[],
                       "Blue": [],
                       "Yellow": [],
                       "Pink": [],
                       "Black": []}
        blazers = {"Red":[],
                   "Blue": [],
                   "Yellow": [],
                   "Pink": [],
                   "Black": []}
        coats = {"Red":[],
                 "Blue": [],
                 "Yellow": [],
                 "Pink": [],
                 "Black": []}
       
        top=int(input("Please select your desired topwear type:"))
        while top > 5:
            print("Topwear not found")
            top=int(input("Please select your desired topwear type:"))
        print("You selected", topwear[top], "--")
       
        #Filters
        print("\n*FILTERS*")
       
        #size filter
        print("Size:-")
        print("1.XS\n2.S\n3.M\n4.L\n5.XL")
        sizeList = {1: "XS", 2: "S", 3: "M", 4: "L", 5: "Xl"}
        size = int(input("Select Size:-"))
        while size > 5:
            print("Size not available")
            size = int(input("Select Size:-"))
        print("\nYou selected", sizeList[size] ,"size--")
       
        #price range filter
        print("\nPrice range")
        print("1.0-499\n2.500-999\n3.1000-1499")
        priceRange = {1: "0-499", 2:"500-999", 3:"1000-1499"}
        pri_rng=int(input("Select price range:-"))
        while pri_rng > 3:
            print("Price not in range")
            pri_rng=input("Select price range:-")    
        print("\nPrice range:", priceRange[pri_rng], "--")
       
        #Fabric filter
        print("\nFabric")
        print("1.Cotton\n2.Polyster\n3.Rayon\n4.Silk")
        fabricList = {1: "Cotton", 2:"Polyster", 3:"Rayon", 4:"Silk"}
        fabric=int(input("Select fabric:-"))
        while fabric > 4:
            print("Fabric not in list")
            fabric=input("Select fabric:-")            
        print("\n"+fabricList[fabric], "--")
       
        #Color filter
        print("\nColor")
        print("1.Red\n2.Blue\n3.Yellow\n4.Pink\n5.Black")
        clrList = {1: "Red", 2:"Blue", 3:"Yellow", 4:"Pink", 5:"Black"}            
        clr=int(input("Select color:-"))
        while clr > 5:
            print("Color not in list")
            clr=input("Select color:-")
        selectedColor = clrList[clr]
        print("\nYou selected", clrList[clr], "--")
       
        #results of all filters
        result = {}
        print("Results:")
        if top == 1:
            tshirtColors = tshirts[selectedColor]
            if len(tshirtColors) == 0:
                checkout["stock"] = 0
            else:
                checkout["stock"] = 1
                for colorOption in tshirtColors:
                    numbering = tshirtColors.index(colorOption) + 1
                    print(str(numbering) + ")")
                    display(Image(filename="men/topwear/tshirts/"+colorOption+".jpeg", width=150, height=200))
                    result[tshirtColors.index(colorOption) + 1] = [colorOption, "men/topwear/tshirts/"+colorOption]
                    #for table
                    print(pd.read_csv("men/topwear/tshirts/"+selectedColor+".csv"), "\n")
           
        elif top == 2:
            shirtColor = shirts[selectedColor]
               
            if len(shirtColor) == 0:
                checkout["stock"] = 0
            else:
                checkout["stock"] = 1
                for colorOption in shirtColor:
                    numbering = shirtColor.index(colorOption) + 1
                    print(str(numbering) + ")")
                    display(Image(filename="men/topwear/shirts/"+colorOption+".jpeg", width=150, height=200))
                    result[shirtColor.index(colorOption) + 1] = [colorOption, "men/topwear/shirts/"+colorOption]
                    #for table
                    print(pd.read_csv("men/topwear/shirts/"+selectedColor+".csv"), "\n")
               
        elif top == 3:
            sweatshirtColor = sweatshirts[selectedColor]

            if len(sweatshirtColor) == 0:
                checkout["stock"] = 0
            else:
                checkout["stock"] = 1
                for colorOption in sweatshirtColor:
                    numbering = sweatshirtColor.index(colorOption) + 1
                    print(str(numbering) + ")")
                    display(Image(filename="men/topwear/sweatshirts/"+colorOption+".jpeg", width=150, height=200))
                    result[sweatshirtColor.index(colorOption) + 1] = [colorOption, "men/topwear/sweatshirts/"+colorOption]
                    #for table
                    print(pd.read_csv("men/topwear/sweatshirts/"+selectedColor+".csv"), "\n")
       
        elif top == 4:
            blazerColor = blazers[selectedColor]
           
            if len(blazerColor) == 0:
                checkout["stock"] = 0
            else:
                checkout["stock"] = 1
                for colorOption in blazerColor:
                    nambering = blazerColor.index(colorOption) + 1
                    print(numbering)
                    display(Image(filename="men/topwear/blazers/"+colorOption+".jpeg", width=150, height=200))
                    result[blazerColor.index(colorOption) + 1] = [colorOption, "men/topwear/blazers/"+colorOption]
                    #for table
                    print(pd.read_csv("men/topwear/blazers/"+selectedColor+".csv"), "\n")    
           
        elif top == 5:
            coatColor = coats[selectedColor]
           
            if len(coatColor) == 0:
                checkout["stock"] == 0
            else:
                checkout["stock"] = 1
                for colorOption in coatColor:
                    name = coatColor.index(colorOption) + 1
                    print(name)
                    display(Image(filename="men/topwear/coats/"+colorOption+".jpeg", width=150, height=200))
                    result[coatColor.index(colorOption) + 1] = [colorOption, "men/topwear/coats/"+colorOption]
                    #for table
                    print(pd.read_csv("men/topwear/coats/"+selectedColor+".csv"), "\n")
       
        stock = checkout["stock"]
        if stock != 0:
            final = int(input("Select an option to checkout:-"))
            checkout["product"] = result[final][0]
            checkout["productImage"] = result[final][1]
            checkout["filters"] = {
                "size":sizeList[size],
                "fabric":fabricList[fabric],
                "price":pri_rng}
           
    elif men_wear==2:
        print("\nBOTTOMWEARS-")
        print("1.Jeans")
        print("2.Casual trousers")
        print("3.Formal trousers")
        print("4.Trackpants")
        print("5.Joggers")
        bottomwear = {1: "Jeans", 2:"Casual trousers", 3:"Formal trousers", 4:"Trackpants", 5:"Joggers"}

        #all avaible options with color in topwear
        jeans = {"Red":[],
                 "Blue": [],
                 "Yellow": [],
                 "Pink": [],
                 "Black": []}
        ctrousers = {"Red":[],
                     "Blue": [],
                     "Yellow": [],
                     "Pink": [],
                     "Black": []}
        ftrousers = {"Red":[],
                     "Blue": [],
                     "Yellow": [],
                     "Pink": [],
                     "Black": []}
        trackpants = {"Red":[],
                      "Blue": [],
                      "Yellow": [],
                      "Pink": [],
                      "Black": []}
        joggers = {"Red":[],
                   "Blue": [],
                   "Yellow": [],
                   "Pink": [],
                   "Black": []}
       
        bottom=int(input("Please select your desired bottomwear type:"))
        while bottom > 5:
            print("bottomwear not found")
            bottom=int(input("Please select your desired bottomwear type:"))
        print("You selected", bottomwear[bottom], "--")
       
        #Filters
        print("\n*FILTERS*")
       
        #size filter
        print("Size:-")
        print("1.XS\n2.S\n3.M\n4.L\n5.XL")
        sizeList = {1: "XS", 2: "S", 3: "M", 4: "L", 5: "Xl"}
        size = int(input("Select Size:-"))
        while size > 5:
            print("Size not available")
            size = int(input("Select Size:-"))
        print("\nYou selected", sizeList[size] ,"size--")
       
        #price range filter
        print("\nPrice range")
        print("1.0-499\n2.500-999\n3.1000-1499")
        priceRange = {1: "0-499", 2:"500-999", 3:"1000-1499"}
        pri_rng=int(input("Select price range:-"))
        while pri_rng > 3:
            print("Price not in range")
            pri_rng=input("Select price range:-")    
        print("\nPrice range:", priceRange[pri_rng], "--")
       
        #Fabric filter
        print("\nFabric")
        print("1.Cotton\n2.Polyster\n3.Rayon\n4.Silk")
        fabricList = {1: "Cotton", 2:"Polyster", 3:"Rayon", 4:"Silk"}
        fabric=int(input("Select fabric:-"))
        while fabric > 4:
            print("Fabric not in list")
            fabric=input("Select fabric:-")            
        print("\n"+fabricList[fabric], "--")
       
        #Color filter
        print("\nColor")
        print("1.Red\n2.Blue\n3.Yellow\n4.Pink\n5.Black")
        clrList = {1: "Red", 2:"Blue", 3:"Yellow", 4:"Pink", 5:"Black"}            
        clr=int(input("Select color:-"))
        while clr > 5:
            print("Color not in list")
            clr=input("Select color:-")
        selectedColor = clrList[clr]
        print("\nYou selected", clrList[clr], "--")
       
        #results of all filters
        result = {}
        print("Results:")
        if bottom == 1:
            jeansColor = jeans[selectedColor]
           
            if len(jeansColor) == 0:
                checkout["stock"] = 0
            else:
                for colorOption in jeansColor:
                    print(jeansColor.index(colorOption) + 1)
                    display(Image(filename="men/bottomwear/jeans/"+colorOption+".jpeg", width=150, height=200))
                    result[jeansColor.index(colorOption) + 1] = [colorOption, "men/bottomwear/jeans/"+colorOption]
                    #for table
                    print(pd.read_csv("men/bottomwear/jeans/"+selectedColor+".csv"), "\n")
           
        elif bottom == 2:
            ctrousersColor = ctrousers[selectedColor]
           
            if len(ctrousersColor) == 0:
                checkout["stock"] = 0
            else:
                checkout["stock"] = 1
                for colorOption in ctrousersColor:
                    print(ctrousersColor.index(colorOption) + 1)
                    display(Image(filename="men/bottomwear/ctrousers/"+colorOption+".jpeg", width=150, height=200))
                    result[ctrousersColor.index(colorOption) + 1] = [colorOption, "men/bottomwear/ctrousers/"+colorOption]
                    #for table
                    print(pd.read_csv("men/bottomwear/ctrousers/"+selectedColor+".csv"), "\n")
               
        elif bottom == 3:
            ftrousersColor = ftrousers[selectedColor]
           
            if len(ftrousersColor) == 0:
                checkout["stock"] = 0
            else:
                checkout["stock"] = 1
                for colorOption in ftrousersColor:
                    print(ftrousersColor.index(colorOption) + 1)
                    display(Image(filename="men/bottomwear/ftrousers/"+colorOption+".jpeg", width=150, height=200))
                    result[ftrousersColor.index(colorOption) + 1] = [colorOption, "men/bottomwear/ftrousers/"+colorOption]
                    #for table
                    print(pd.read_csv("men/bottomwear/ftousers/"+selectedColor+".csv"), "\n")

        elif bottom == 4:
            trackpantsColor = trackpants[selectedColor]
           
            if len(trackpantsColor) == 0:
                checkout["stock"] = 0
            else:
                checkout["stock"] = 1
                for colorOption in trackpantsColor:
                    print(trackpantsColor.index(colorOption) + 1)
                    display(Image(filename="men/bottomwear/trackpants/"+colorOption+".jpeg", width=150, height=200))
                    result[trackpantsColor.index(colorOption) + 1] = [colorOption, "men/bottomwear/trackpants/"+colorOption]
                    #for table
                    print(pd.read_csv("men/bottomwear/trackpants/"+selectedColor+".csv"), "\n")

       
        elif bottom == 5:
            joggersColor = joggers[selectedColor]
           
            if len(joggersColor) == 0:
                checkout["stock"] = 0
            else:
                checkout["stock"] = 1
                for colorOption in joggersColor:
                    print(joggersColor.index(colorOption) + 1)
                    display(Image(filename="men/bottomwear/joggers/"+colorOption+".jpeg", width=150, height=200))
                    result[joggersColor.index(colorOption) + 1] = [colorOption, "men/bottomwear/joggers/"+colorOption]
                    #for table
                    print(pd.read_csv("men/bottomwear/joggers/"+selectedColor+".csv"), "\n")

       
        stock = checkout["stock"]
        if stock != 0:
            final = int(input("Select an option to checkout:-"))
            checkout["product"] = result[final][0]
            checkout["productImage"] = result[final][1]
            checkout["filters"] = {
                "size":sizeList[size],
                "fabric":fabricList[fabric],
                "price":pri_rng}
       
    elif men_wear==3:
        print("\nSPORTSWEAR-")
        print("1.Headband")
        print("2.Fingerless gloves")
        print("3.Polo Tshirts")
        print("4.Waist Pouches")
        sportswear = {1: "Headband", 2:"Fingerless gloves", 3:"Polo Tshirts", 4:"Waist Pouces"}
       
        #all avaible options with color in topwear
        headband = {"Red":[],
                    "Blue": [],
                    "Yellow": [],
                    "Pink": [],
                    "Black": []}
        gloves = {"Red":[],
                  "Blue": [],
                  "Yellow": [],
                  "Pink": [],
                  "Black": []}
        tshirts = {"Red":[],
                   "Blue": [],
                   "Yellow": [],
                   "Pink": [],
                   "Black": []}
        pouches = {"Red":[],
                   "Blue": [],
                   "Yellow": [],
                   "Pink": [],
                   "Black": []}
       
        sports=int(input("Please select your desired sportswear type:"))
        while sports > 4:
            print("Sportswear not found")
            sports=int(input("Please select your desired sportswear type:"))
        print("You selected", sportswear[sports], "--")
       
        #Filters
        print("\n*FILTERS*")
       
        #size filter
        print("Size:-")
        print("1.XS\n2.S\n3.M\n4.L\n5.XL")
        sizeList = {1: "XS", 2: "S", 3: "M", 4: "L", 5: "Xl"}
        size = int(input("Select Size:-"))
        while size > 5:
            print("Size not available")
            size = int(input("Select Size:-"))
        print("\nYou selected", sizeList[size] ,"size--")
       
        #price range filter
        print("\nPrice range")
        print("1.0-499\n2.500-999\n3.1000-1499")
        priceRange = {1: "0-499", 2:"500-999", 3:"1000-1499"}
        pri_rng=int(input("Select price range:-"))
        while pri_rng > 3:
            print("Price not in range")
            pri_rng=input("Select price range:-")    
        print("\nPrice range:", priceRange[pri_rng], "--")
       
        #Fabric filter
        print("\nFabric")
        print("1.Cotton\n2.Polyster\n3.Rayon\n4.Silk")
        fabricList = {1: "Cotton", 2:"Polyster", 3:"Rayon", 4:"Silk"}
        fabric=int(input("Select fabric:-"))
        while fabric > 4:
            print("Fabric not in list")
            fabric=input("Select fabric:-")            
        print("\n"+fabricList[fabric], "--")
       
        #Color filter
        print("\nColor")
        print("1.Red\n2.Blue\n3.Yellow\n4.Pink\n5.Black")
        clrList = {1: "Red", 2:"Blue", 3:"Yellow", 4:"Pink", 5:"Black"}            
        clr=int(input("Select color:-"))
        while clr > 5:
            print("Color not in list")
            clr=input("Select color:-")
        selectedColor = clrList[clr]
        print("\nYou selected", clrList[clr], "--")
       
        #results of all filters
        result = {}
        print("Results:")
        if sports == 1:
            headbandColor = headband[selectedColor]
           
            if len(headbandColor) == 0:
                checkout["stock"] = 0
            else:
                checkout["stock"] = 1
                for colorOption in headbandColor:
                    print(headbandColor.index(colorOption) + 1)
                    display(Image(filename="men/sportswear/headbands/"+colorOption+".jpeg", width=150, height=200))
                    result[headbandColor.index(colorOption) + 1] = [colorOption, "men/sportswear/headband/"+colorOption]
                    #for table
                    print(pd.read_csv("men/sportswear/headbands/"+selectedColor+".csv"), "\n")
           
        elif sports == 2:
            glovesColor = gloves[selectedColor]
           
            if len(glovesColor) == 0:
                checkout["stock"] = 0
            else:
                checkout["stock"] = 1
                for colorOption in glovesColor:
                    print(glovesColor.index(colorOption) + 1)
                    display(Image(filename="men/sportswear/gloves/"+colorOption+".jpeg", width=150, height=200))
                    result[glovesColor.index(colorOption) + 1] = [colorOption, "men/sportswear/gloves/"+colorOption]
                    #for table
                    print(pd.read_csv("men/sportswear/gloves/"+selectedColor+".csv"), "\n")
               
        elif sports == 3:
            tshirtColor = tshirts[selectedColor]
           
            if len(tshirtColor) == 0:
                checkout["stock"] = 0
            else:
                checkout["stock"] = 1
                for colorOption in tshirtColor:
                    print(tshirtColor.index(colorOption) + 1)
                    display(Image(filename="men/sportswear/tshirts/"+colorOption+".jpeg", width=150, height=200))
                    result[tshirtColor.index(colorOption) + 1] = [colorOption, "men/sportswear/tshirts/"+colorOption]
                    #for table
                    print(pd.read_csv("men/sportswear/tshirts/"+selectedColor+".csv"), "\n")
       
        elif sports == 4:
            pouchColor = pouches[selectedColor]
           
            if len(pouchColor) == 0:
                checkout["stock"] = 0
            else:
                checkout["stock"] = 1
                for colorOption in pouchColor:
                    print(pouchColor.index(colorOption) + 1)
                    display(Image(filename="men/spotswear/pouches/"+colorOption+".jpeg", width=150, height=200))
                    result[pouchColor.index(colorOption) + 1] = [colorOption, "men/sportswear/pouches/"+colorOption]
                    #for table
                    print(pd.read_csv("men/sportswear/pouches/"+selectedColor+".csv"), "\n")
       
        stock = checkout["stock"]
        if stock != 0:
            final = int(input("Select an option to checkout:-"))
            checkout["product"] = result[final][0]
            checkout["productImage"] = result[final][1]
            checkout["filters"] = {
                "size":sizeList[size],
                "fabric":fabricList[fabric],
                "price":pri_rng}
       
    elif men_wear==4:
        print("\nETHNICWEAR-")
        print("1.Kurtas & Kurtasets")
        print("2.Nehru jackets")
        print("3.Sherwanis")
        print("4.Ethnic blazers")
        ethnicwear = {1: "Kurtas & Kurtasets", 2:"Nehru jackets", 3:"Sherwanis", 4:"Ethnic blazers"}
       
        #all avaible options with color in topwear
        kurtas = {"Red":[],
                  "Blue": [],
                  "Yellow": [],
                  "Pink": [],
                  "Black": []}
        jackets = {"Red":[],
                   "Blue": [],
                   "Yellow": [],
                   "Pink": [],
                   "Black": []}
        sherwanis = {"Red":[],
                     "Blue": [],
                     "Yellow": [],
                     "Pink": [],
                     "Black": []}
        blazers = {"Red":[],
                   "Blue": [],
                   "Yellow": [],
                   "Pink": [],
                   "Black": []}
       
        ethnic=int(input("Please select your desired ethnicwear type:"))
        while ethnic > 4:
            print("Ethnicwear not found")
            sports=int(input("Please select your desired ethnicwear type:"))
        print("You selected", ethnicwear[ethnic], "--")
       
        #Filters
        print("\n*FILTERS*")
       
        #size filter
        print("Size:-")
        print("1.XS\n2.S\n3.M\n4.L\n5.XL")
        sizeList = {1: "XS", 2: "S", 3: "M", 4: "L", 5: "Xl"}
        size = int(input("Select Size:-"))
        while size > 5:
            print("Size not available")
            size = int(input("Select Size:-"))
        print("\nYou selected", sizeList[size] ,"size--")
       
        #price range filter
        print("\nPrice range")
        print("1.0-499\n2.500-999\n3.1000-1499")
        priceRange = {1: "0-499", 2:"500-999", 3:"1000-1499"}
        pri_rng=int(input("Select price range:-"))
        while pri_rng > 3:
            print("Price not in range")
            pri_rng=input("Select price range:-")    
        print("\nPrice range:", priceRange[pri_rng], "--")
       
        #Fabric filter
        print("\nFabric")
        print("1.Cotton\n2.Polyster\n3.Rayon\n4.Silk")
        fabricList = {1: "Cotton", 2:"Polyster", 3:"Rayon", 4:"Silk"}
        fabric=int(input("Select fabric:-"))
        while fabric > 4:
            print("Fabric not in list")
            fabric=input("Select fabric:-")            
        print("\n"+fabricList[fabric], "--")
       
        #Color filter
        print("\nColor")
        print("1.Red\n2.Blue\n3.Yellow\n4.Pink\n5.Black")
        clrList = {1: "Red", 2:"Blue", 3:"Yellow", 4:"Pink", 5:"Black"}            
        clr=int(input("Select color:-"))
        while clr > 5:
            print("Color not in list")
            clr=input("Select color:-")
        selectedColor = clrList[clr]
        print("\nYou selected", clrList[clr], "--")
       
        #results of all filters
        result = {}
        print("Results:")
        if ethnic == 1:
            kurtaColor = kurtas[selectedColor]
           
            if len(kurtaColor) == 0:
                checkout["stock"] = 0
            else:
                checkout["stock"] = 1
                for colorOption in kurtaColor:
                    print(kurtaColor.index(colorOption) + 1)
                    display(Image(filename="men/ethnicwear/kurtas/"+colorOption+".jpeg", width=150, height=200))
                    result[headbandColor.index(colorOption) + 1] = [colorOption, "men/ethnicwear/kurtas/"+colorOption]
                    #for table
                    print(pd.read_csv("men/ethnicwear/kurtas/"+selectedColor+".csv"), "\n")
           
        elif ethnic == 2:
            jacketColor = jackets[selectedColor]
           
            if len(jacketColor) == 0:
                checkout["stock"] = 0
            else:
                checkout["stock"] = 1
                for colorOption in jacketColor:
                    print(jacketColor.index(colorOption) + 1)
                    display(Image(filename="men/ethnicwear/jacket/"+colorOption+".jpeg", width=150, height=200))
                    result[jacketColor.index(colorOption) + 1] = [colorOption, "men/ethnicwear/jacket/"+colorOption]
                    #for table
                    print(pd.read_csv("men/ethnicwear/jacket/"+selectedColor+".csv"), "\n")
               
        elif ethnic == 3:
            sherwaniColor = sherwanis[selectedColor]
           
            if len(sherwaniColor) == 0:
                checkout["stock"] = 0
            else:
                checkout["stock"] = 1
                for colorOption in sherwaniColor:
                    print(sherwaniColor.index(colorOption) + 1)
                    display(Image(filename="men/ethnicwear/sherwanis/"+colorOption+".jpeg", width=150, height=200))
                    result[tshirtColor.index(colorOption) + 1] = [colorOption, "men/ethnicwear/sherwanis/"+colorOption]
                    #for table
                    print(pd.read_csv("men/ethnicwear/sherwanis/"+selectedColor+".csv"), "\n")
       
        elif ethnic == 4:
            blazerColor = blazers[selectedColor]
           
            if len(blazerColor) == 0:
                checkout["stock"] = 0
            else:
                checkout["stock"] = 1
                for colorOption in blazerColor:
                    print(blazerColor.index(colorOption) + 1)
                    display(Image(filename="men/ethnicwear/blazers/"+colorOption+".jpeg", width=150, height=200))
                    result[blazerColor.index(colorOption) + 1] = [colorOption, "men/ethnicwear/blazers/"+colorOption]
                    #for table
                    print(pd.read_csv("men/ethnicwear/blazers/"+selectedColor+".csv"), "\n")
       
        stock = checkout["stock"]
        if stock != 0:
            final = int(input("Select an option to checkout:-"))
            checkout["product"] = result[final][0]
            checkout["productImage"] = result[final][1]
            checkout["filters"] = {
                "size":sizeList[size],
                "fabric":fabricList[fabric],
                "price":pri_rng}
       
    elif men_wear==5:
        print("\nWINTER WEAR-")
        print("1.Sweaters")
        print("2.Hoodies")
        print("3.Mufflers")
        print("4.Gloves")
        winterwear = {1: "Sweaters", 2:"Hoodies", 3:"Mufflers", 4:"Gloves"}
       
        #all avaible options with color in topwear
        sweaters = {"Red":[],
                    "Blue": [],
                    "Yellow": [],
                    "Pink": [],
                    "Black": []}
        hoodies = {"Red":[],
                   "Blue": [],
                   "Yellow": [],
                   "Pink": [],
                   "Black": []}
        mufflers = {"Red":[],
                    "Blue": [],
                    "Yellow": [],
                    "Pink": [],
                    "Black": []}
        gloves = {"Red":[],
                  "Blue": [],
                  "Yellow": [],
                  "Pink": [],
                  "Black": []}
       
        winter=int(input("Please select your desired winterwear type:"))
        while winter > 4:
            print("Winterwear not found")
            sports=int(input("Please select your desired winterwear type:"))
        print("You selected", winterwear[winter], "--")
       
        #Filters
        print("\n*FILTERS*")
       
        #size filter
        print("Size:-")
        print("1.XS\n2.S\n3.M\n4.L\n5.XL")
        sizeList = {1: "XS", 2: "S", 3: "M", 4: "L", 5: "Xl"}
        size = int(input("Select Size:-"))
        while size > 5:
            print("Size not available")
            size = int(input("Select Size:-"))
        print("\nYou selected", sizeList[size] ,"size--")
       
        #price range filter
        print("\nPrice range")
        print("1.0-499\n2.500-999\n3.1000-1499")
        priceRange = {1: "0-499", 2:"500-999", 3:"1000-1499"}
        pri_rng=int(input("Select price range:-"))
        while pri_rng > 3:
            print("Price not in range")
            pri_rng=input("Select price range:-")    
        print("\nPrice range:", priceRange[pri_rng], "--")
       
        #Fabric filter
        print("\nFabric")
        print("1.Cotton\n2.Polyster\n3.Rayon\n4.Silk")
        fabricList = {1: "Cotton", 2:"Polyster", 3:"Rayon", 4:"Silk"}
        fabric=int(input("Select fabric:-"))
        while fabric > 4:
            print("Fabric not in list")
            fabric=input("Select fabric:-")            
        print("\n"+fabricList[fabric], "--")
       
        #Color filter
        print("\nColor")
        print("1.Red\n2.Blue\n3.Yellow\n4.Pink\n5.Black")
        clrList = {1: "Red", 2:"Blue", 3:"Yellow", 4:"Pink", 5:"Black"}            
        clr=int(input("Select color:-"))
        while clr > 5:
            print("Color not in list")
            clr=input("Select color:-")
        selectedColor = clrList[clr]
        print("\nYou selected", clrList[clr], "--")
       
        #results of all filters
        result = {}
        print("Results:")
        if winter == 1:
            sweaterColor = sweaters[selectedColor]
           
            if len(sweaterColor) == 0:
                checkout["stock"] = 0
            else:
                checkout["stock"] = 1
                for colorOption in sweaterColor:
                    print(sweaterColor.index(colorOption) + 1)
                    display(Image(filename="men/winterwear/sweaters/"+colorOption+".jpeg", width=150, height=200))
                    result[sweaterColor.index(colorOption) + 1] = [colorOption, "men/winterwear/sweaters/"+colorOption]
                    #for table
                    print(pd.read_csv("men/winterwear/sweaters/"+selectedColor+".csv"), "\n")
           
        elif winter == 2:
            hoodieColor = hoodies[selectedColor]
           
            if len(hoodieColor) == 0:
                checkout["stock"] = 0
            else:
                checkout["stock"] = 1
                for colorOption in hoodieColor:
                    print(hoodieColor.index(colorOption) + 1)
                    display(Image(filename="men/winterwear/hoodies/"+colorOption+".jpeg", width=150, height=200))
                    result[hoodieColor.index(colorOption) + 1] = [colorOption, "men/winterwear/hoodies/"+colorOption]
                    #for table
                    print(pd.read_csv("men/winterwear/hoodies/"+selectedColor+".csv"), "\n")
               
        elif winter == 3:
            mufflerColor = mufflers[selectedColor]
           
            if len(mufflerColor) == 0:
                checkout["stock"] = 0
            else:
                checkout["stock"] = 1
                for colorOption in mufflerColor:
                    print(mufflerColor.index(colorOption) + 1)
                    display(Image(filename="men/winterwear/mufflers/"+colorOption+".jpeg", width=150, height=200))
                    result[mufflerColor.index(colorOption) + 1] = [colorOption, "men/winterwear/mufflers/"+colorOption]
                    #for table
                    print(pd.read_csv("men/winterwear/mufflers/"+selectedColor+".csv"), "\n")
       
        elif winter == 4:
            gloveColor = gloves[selectedColor]
           
            if len(gloveColor) == 0:
                checkout["stock"] = 0
            else:
                checkout["stock"] = 1
                for colorOption in gloveColor:
                    print(gloveColor.index(colorOption) + 1)
                    display(Image(filename="men/winterwear/gloves/"+colorOption+".jpeg", width=150, height=200))
                    result[gloveColor.index(colorOption) + 1] = [colorOption, "men/winterwear/gloves/"+colorOption]
                    #for table
                    print(pd.read_csv("men/winterwear/gloves/"+selectedColor+".csv"), "\n")
       
       
        stock = checkout["stock"]
        if stock != 0:
            final = int(input("Select an option to checkout:-"))
            checkout["product"] = result[final][0]
            checkout["productImage"] = result[final][1]
            checkout["filters"] = {
                "size":sizeList[size],
                "fabric":fabricList[fabric],
                "price":pri_rng}
       
    else:
        print("Sorry product-type not available!!")
   
if cat==2:
    print("\nYou selected women's wear")
    print("Categories")        
    print("1.Western wear\n2.Ethnic wear\n3.Sports wear\n4.Winter wear")
    wmn_wear=(int(input("Select category:")))
    if wmn_wear==1:
        print("\nWESTERN WEARS-")
        print("1.Tops & tshirts")
        print("2.Shirts")
        print("3.Jeans")
        print("4.Trousers")
        print("5.Co-ords")
        westernwear = {1: "Tops & Tshirts", 2:"Shirts", 3:"Jeans", 4:"Trousers", 5:"Co-ords"}
       
        #all available options with color
        tops = {"Red":[],
                "Blue": [],
                "Yellow": [],
                "Pink": [],
                "Black": []}
        shirts = {"Red":[],
                 "Blue": [],
                 "Yellow": [],
                 "Pink": [],
                 "Black": []}
        jeans = {"Red":[],
                 "Blue": [],
                 "Yellow": [],
                 "Pink": [],
                 "Black": []}
        trousers = {"Red":[],
                 "Blue": [],
                 "Yellow": [],
                 "Pink": [],
                 "Black": []}
        ords = {"Red":[],
                 "Blue": [],
                 "Yellow": [],
                 "Pink": [],
                 "Black": []}
       
        western = int(input("Please select your desired westernwear type:"))
        while western > 5:
            print("Westernwear not found")
            western = int(input("Please select your desired westernwear type:"))
        print("You selected", westernwear[western], "--")
       
       
        #Filters
        print("\n*FILTERS*")
       
        #size filter
        print("Size:-")
        print("1.XS\n2.S\n3.M\n4.L\n5.XL")
        sizeList = {1: "XS", 2: "S", 3: "M", 4: "L", 5: "Xl"}
        size = int(input("Select Size:-"))
        while size > 5:
            print("Size not available")
            size = int(input("Select Size:-"))
        print("\nYou selected", sizeList[size] ,"size--")
       
        #price range filter
        print("\nPrice range")
        print("1.0-499\n2.500-999\n3.1000-1499")
        priceRange = {1: "0-499", 2:"500-999", 3:"1000-1499"}
        pri_rng=int(input("Select price range:-"))
        while pri_rng > 3:
            print("Price not in range")
            pri_rng=input("Select price range:-")    
        print("\nPrice range:", priceRange[pri_rng], "--")
       
        #Fabric filter
        print("\nFabric")
        print("1.Cotton\n2.Polyster\n3.Rayon\n4.Silk")
        fabricList = {1: "Cotton", 2:"Polyster", 3:"Rayon", 4:"Silk"}
        fabric=int(input("Select fabric:-"))
        while fabric > 4:
            print("Fabric not in list")
            fabric=input("Select fabric:-")            
        print("\n"+fabricList[fabric], "--")
       
        #Color filter
        print("\nColor")
        print("1.Red\n2.Blue\n3.Yellow\n4.Pink\n5.Black")
        clrList = {1: "Red", 2:"Blue", 3:"Yellow", 4:"Pink", 5:"Black"}            
        clr=int(input("Select color:-"))
        while clr > 5:
            print("Color not in list")
            clr=input("Select color:-")
        selectedColor = clrList[clr]
        print("\nYou selected", clrList[clr], "--")
       
        #results of all filters
        result = {}
        print("Results:")
        if top == 1:
            topColors = top[selectedColor]
           
            if len(topColors) == 0:
                checkout["stock"] = 0
            else:
                checkout["stock"] = 1
                for colorOption in topColors:
                    print(topColors.index(colorOption) + 1)
                    display(Image(filename="women/westernwear/tops/"+colorOption+".jpeg", width=150, height=200))
                    result[topColors.index(colorOption) + 1] = [colorOption, "women/westernwear/tops/"+colorOption]
                    #for table
                    print(pd.read_csv("women/westernwear/tops/"+selectedColor+".csv"), "\n")
           
        elif top == 2:
            shirtColor = shirts[selectedColor]
           
            if len(shirtColor) == 0:
                checkout["stock"] = 0
            else:
                checkout["stock"] = 1
                for colorOption in shirtColor:
                    print(shirtColor.index(colorOption) + 1)
                    display(Image(filename="women/westernwear/shirts/"+colorOption+".jpeg", width=150, height=200))
                    result[shirtColor.index(colorOption) + 1] = [colorOption, "women/westernwear/shirts/"+colorOption]
                    #for table
                    print(pd.read_csv("women/westernwear/shirts/"+selectedColor+".csv"), "\n")
               
        elif top == 3:
            jeansColor = jeans[selectedColor]
           
            if len(jeansColor) == 0:
                checkout["stock"] = 0
            else:
                checkout["stock"] = 1
                for colorOption in jeansColor:
                    print(jeansColor.index(colorOption) + 1)
                    display(Image(filename="men/westernwear/jeans/"+colorOption+".jpeg", width=150, height=200))
                    result[jeansColor.index(colorOption) + 1] = [colorOption, "women/westernwear/jeans/"+colorOption]
                    #for table
                    print(pd.read_csv("women/westernwear/jeans/"+selectedColor+".csv"), "\n")
       
        elif top == 4:
            trouserColor = trousers[selectedColor]
           
            if len(trouserColor) == 0:
                checkout["stock"] = 0
            else:
                checkout["stock"] = 1
                for colorOption in trouserColor:
                    print(trouserColor.index(colorOption) + 1)
                    display(Image(filename="women/westernwear/tousers/"+colorOption+".jpeg", width=150, height=200))
                    result[trouserColor.index(colorOption) + 1] = [colorOption, "women/westernwear/trousers/"+colorOption]
                    #for table
                    print(pd.read_csv("women/westernwear/trousers/"+selectedColor+".csv"), "\n")
       
        elif top == 5:
            ordColor = ords[selectedColor]
           
            if len(ordColor) == 0:
                checkout["stock"] = 0
            else:
                checkout["stock"] = 1
                for colorOption in ordColor:
                    print(ordColor.index(colorOption) + 1)
                    display(Image(filename="women/westernwear/coords/"+colorOption+".jpeg", width=150, height=200))
                    result[ordColor.index(colorOption) + 1] = [colorOption, "women/westernwear/coords/"+colorOption]
                    #for table
                    print(pd.read_csv("women/westernwear/coords/"+selectedColor+".csv"), "\n")
       
        stock = checkout["stock"]
        if stock != 0:
            final = int(input("Select an option to checkout:-"))
            checkout["product"] = result[final][0]
            checkout["productImage"] = result[final][1]
            checkout["filters"] = {
                "size":sizeList[size],
                "fabric":fabricList[fabric],
                "price":pri_rng}
       
    elif wmn_wear==2:
        print("\nETHNIC WEAR-")
        print("1.Kurta")
        print("2.Kurta sets")
        print("3.Ethnic dresses")
        print("4.Sarees")
        print("5.Lehenga choli")
        ethnicwear = {1: "Kurta", 2:"Kurta Sets", 3:"Ethnic dresses", 4:"Sarees", 5:"Lahenga Choli"}
       
        #all available options with color
        kurta = {"Red":[],
                 "Blue": [],
                 "Yellow": [],
                 "Pink": [],
                 "Black": []}
        kurtaset = {"Pink":["wp1", "wp2", "wp3", "wp4", "wp5"],
                    "Red":[],
                    "Blue": [],
                    "Yellow": [],
                    "Black": []}
        edress = {"Red":[],
                 "Blue": [],
                 "Yellow": [],
                 "Pink": [],
                 "Black": []}
        sarees = {"Red":[],
                 "Blue": [],
                 "Yellow": [],
                 "Pink": [],
                 "Black": []}
        lahenga = {"Red":[],
                 "Blue": [],
                 "Yellow": [],
                 "Pink": [],
                 "Black": []}
       
        ethnic = int(input("Please select your desired Ethnicwear type:"))
        while ethnic > 5:
            print("Ethnicwear not found")
            western = int(input("Please select your desired ethnicwear type:"))
        print("You selected", ethnicwear[ethnic], "--")
       
       
        #Filters
        print("\n*FILTERS*")
       
        #size filter
        print("Size:-")
        print("1.XS\n2.S\n3.M\n4.L\n5.XL")
        sizeList = {1: "XS", 2: "S", 3: "M", 4: "L", 5: "Xl"}
        size = int(input("Select Size:-"))
        while size > 5:
            print("Size not available")
            size = int(input("Select Size:-"))
        print("\nYou selected", sizeList[size] ,"size--")
       
        #price range filter
        print("\nPrice range")
        print("1.0-499\n2.500-999\n3.1000-1499")
        priceRange = {1: "0-499", 2:"500-999", 3:"1000-1499"}
        pri_rng=int(input("Select price range:-"))
        while pri_rng > 3:
            print("Price not in range")
            pri_rng=input("Select price range:-")    
        print("\nPrice range:", priceRange[pri_rng], "--")
       
        #Fabric filter
        print("\nFabric")
        print("1.Cotton\n2.Polyster\n3.Rayon\n4.Silk")
        fabricList = {1: "Cotton", 2:"Polyster", 3:"Rayon", 4:"Silk"}
        fabric=int(input("Select fabric:-"))
        while fabric > 4:
            print("Fabric not in list")
            fabric=input("Select fabric:-")            
        print("\n"+fabricList[fabric], "--")
       
        #Color filter
        print("\nColor")
        print("1.Red\n2.Blue\n3.Yellow\n4.Pink\n5.Black")
        clrList = {1: "Red", 2:"Blue", 3:"Yellow", 4:"Pink", 5:"Black"}            
        clr=int(input("Select color:-"))
        while clr > 5:
            print("Color not in list")
            clr=input("Select color:-")
        selectedColor = clrList[clr]
        print("\nYou selected", clrList[clr], "--")
       
        #results of all filters
        result = {}
        print("Results:")
        if ethnic == 1:
            kurtaColors = kurta[selectedColor]
           
            if len(kurtaColors) == 0:
                checkout["stock"] = 0
            else:
                checkout["stock"] = 1
                for colorOption in kurtaColors:
                    print(kurtaColors.index(colorOption) + 1)
                    display(Image(filename="women/ethnicwear/kurtas/"+colorOption+".jpeg", width=150, height=200))
                    result[kurtaColors.index(colorOption) + 1] = [colorOption, "women/ethnicwear/kurtas/"+colorOption]
                    #for table
                    print(pd.read_csv("women/ethnicwear/kurtas/"+selectedColor+".csv"), "\n")
           
        elif ethnic == 2:
            kurtasetColor = kurtaset[selectedColor]
           
            if len(kurtasetColor) == 0:
                checkout["stock"] = 0
            else:
                checkout["stock"] = 1
                for colorOption in kurtasetColor:
                    print(kurtasetColor.index(colorOption) + 1)
                    display(Image(filename="women/ethnicwear/kurtaset/"+colorOption+".jpeg", width=150, height=200))
                    result[kurtasetColor.index(colorOption) + 1] = [colorOption, "women/ethnicwear/kurtaset/"+colorOption]
                    #for table
                    print(pd.read_csv("women/ethnicwear/kurtaset/"+selectedColor+".csv"), "\n")
               
        elif ethnic == 3:
            edressColor = edress[selectedColor]
           
            if len(edressColor) == 0:
                checkout["stock"] = 0
            else:
                checkout["stock"] = 1
                for colorOption in edressColor:
                    print(edressColor.index(colorOption) + 1)
                    display(Image(filename="women/ethnicwear/edress/"+colorOption+".jpeg", width=150, height=200))
                    result[edressColor.index(colorOption) + 1] = [colorOption, "women/ethnicwear/edress/"+colorOption]
                    #for table
                    print(pd.read_csv("women/ethnicwear/edress/"+selectedColor+".csv"), "\n")
       
        elif ethnic == 4:
            sareeColor = sarees[selectedColor]
           
            if len(sareeColor) == 0:
                checkout["stock"] = 0
            else:
                checkout["stock"] = 1
                for colorOption in sareeColor:
                    print(sareeColor.index(colorOption) + 1)
                    display(Image(filename="women/ethnicwear/sarees/"+colorOption+".jpeg", width=150, height=200))
                    result[sareeColor.index(colorOption) + 1] = [colorOption, "women/ethnicwear/sarees/"+colorOption]
                    #for table
                    print(pd.read_csv("women/ethnicwear/sarees/"+selectedColor+".csv"), "\n")
       
        elif ethnic == 5:
            lahengaColor = lahenga[selectedColor]
           
            if len(lahengaColor) == 0:
                checkout["stock"] = 0
            else:
                checkout["stock"] = 1
                for colorOption in lahengaColor:
                    print(lahengaColor.index(colorOption) + 1)
                    display(Image(filename="women/ethnicwear/lahenga/"+colorOption+".jpeg", width=150, height=200))
                    result[lahengaColor.index(colorOption) + 1] = [colorOption, "women/ethnicwear/lahenga/"+colorOption]
                    #for table
                    print(pd.read_csv("women/ethnicwear/lahenga/"+selectedColor+".csv"), "\n")
       
        stock = checkout["stock"]
        if stock != 0 :
           final = int(input("Select an option to checkout:-"))
           checkout["product"] = result[final][0]
           checkout["productImage"] = result[final][1]
           checkout["filters"] = {
              "size":sizeList[size],
              "fabric":fabricList[fabric],
              "price":pri_rng}
   
    elif wmn_wear==3:
        print("\nSPORTSWEARS-")
        print("1.Crew neck tshirts")
        print("2.Polo tshirts")
        print("3.Trackpants & joggers")
        print("4.Tracksuits")
        sportswear = {1: "Crew neck tshirts", 2:"Polo tshirts", 3:"Trackpants & Joggers", 4:"Tracksuits"}
       
        #all available options with color
        tshirt = {"Red":[],
                 "Blue": [],
                 "Yellow": [],
                 "Pink": [],
                 "Black": []}
        polo = {"Red":[],
                 "Blue": [],
                 "Yellow": [],
                 "Pink": [],
                 "Black": []}
        trackpants = {"Red":[],
                 "Blue": [],
                 "Yellow": [],
                 "Pink": [],
                 "Black": []}
        tracksuits = {"Red":[],
                 "Blue": [],
                 "Yellow": [],
                 "Pink": [],
                 "Black": []}
       
        sports = int(input("Please select your desired sportswear type:"))
        while sports > 5:
            print("Sportswear not found")
            western = int(input("Please select your desired sportswear type:"))
        print("You selected", sportswear[sports], "--")
       
       
        #Filters
        print("\n*FILTERS*")
       
        #size filter
        print("Size:-")
        print("1.XS\n2.S\n3.M\n4.L\n5.XL")
        sizeList = {1: "XS", 2: "S", 3: "M", 4: "L", 5: "Xl"}
        size = int(input("Select Size:-"))
        while size > 5:
            print("Size not available")
            size = int(input("Select Size:-"))
        print("\nYou selected", sizeList[size] ,"size--")
       
        #price range filter
        print("\nPrice range")
        print("1.0-499\n2.500-999\n3.1000-1499")
        priceRange = {1: "0-499", 2:"500-999", 3:"1000-1499"}
        pri_rng=int(input("Select price range:-"))
        while pri_rng > 3:
            print("Price not in range")
            pri_rng=input("Select price range:-")    
        print("\nPrice range:", priceRange[pri_rng], "--")
       
        #Fabric filter
        print("\nFabric")
        print("1.Cotton\n2.Polyster\n3.Rayon\n4.Silk")
        fabricList = {1: "Cotton", 2:"Polyster", 3:"Rayon", 4:"Silk"}
        fabric=int(input("Select fabric:-"))
        while fabric > 4:
            print("Fabric not in list")
            fabric=input("Select fabric:-")            
        print("\n"+fabricList[fabric], "--")
       
        #Color filter
        print("\nColor")
        print("1.Red\n2.Blue\n3.Yellow\n4.Pink\n5.Black")
        clrList = {1: "Red", 2:"Blue", 3:"Yellow", 4:"Pink", 5:"Black"}            
        clr=int(input("Select color:-"))
        while clr > 5:
            print("Color not in list")
            clr=input("Select color:-")
        selectedColor = clrList[clr]
        print("\nYou selected", clrList[clr], "--")
       
        #results of all filters
        result = {}
        print("Results:")
        if sports == 1:
            tshirtColors = tshirt[selectedColor]
           
            if len(tshirtColors) == 0:
                checkout["stock"] = 0
            else:
                checkout["stock"] = 1
                for colorOption in tshirtColors:
                    print(tshirtColors.index(colorOption) + 1)
                    display(Image(filename="women/sportswear/tshirt/"+colorOption+".jpeg", width=150, height=200))
                    result[tshirtColors.index(colorOption) + 1] = [colorOption, "women/sportswear/tshirt/"+colorOption]
                    #for table
                    print(pd.read_csv("women/sportswear/tshirt/"+selectedColor+".csv"), "\n")
           
        elif ethnic == 2:
            poloColor = polo[selectedColor]
           
            if len(poloColor) == 0:
                checkout["stock"] = 0
            else:
                checkout["stock"] = 1
                for colorOption in poloColor:
                    print(poloColor.index(colorOption) + 1)
                    display(Image(filename="women/sportswear/polo/"+colorOption+".jpeg", width=150, height=200))
                    result[poloColor.index(colorOption) + 1] = [colorOption, "women/sportswear/polo/"+colorOption]
                    #for table
                    print(pd.read_csv("women/sportswear/polo/"+selectedColor+".csv"), "\n")
               
        elif ethnic == 3:
            trackpantsColor = trackpants[selectedColor]
           
            if len(trackpantsColor) == 0:
                checkout["stock"] = 0
            else:
                checkout["stock"] = 1
                for colorOption in trackpantsColor:
                    print(trackpantsColor.index(colorOption) + 1)
                    display(Image(filename="women/sportswear/trackpants/"+colorOption+".jpeg", width=150, height=200))
                    result[trackpantsColor.index(colorOption) + 1] = [colorOption, "women/sportswear/trackpants/"+colorOption]
                    #for table
                    print(pd.read_csv("women/sportswear/trackpants/"+selectedColor+".csv"), "\n")
       
        elif ethnic == 4:
            tracksuitsColor = tracksuits[selectedColor]
           
            if len(tracksuitsColor) == 0:
                checkout["stock"] = 0
            else:
                checkout["stock"] = 1
                for colorOption in tracksuitsColor:
                    print(tracksuitsColor.index(colorOption) + 1)
                    display(Image(filename="women/sportswear/tracksuits/"+colorOption+".jpeg", width=150, height=200))
                    result[tracksuitsColor.index(colorOption) + 1] = [colorOption, "women/sportswear/tracksuits/"+colorOption]
                    #for table
                    print(pd.read_csv("women/sportswear/tracksuits/"+selectedColor+".csv"), "\n")
       
        stock = checkout["stock"]
        if stock != 0:
            final = int(input("Select an option to checkout:-"))
            checkout["product"] = result[final][0]
            checkout["productImage"] = result[final][1]
            checkout["filters"] = {
                "size":sizeList[size],
                "fabric":fabricList[fabric],
                "price":pri_rng}
       
    elif wmn_wear==4:
        print("\nWINTERWEARS-")
        print("1.Sweatshirts")
        print("2.Jackets")
        print("3.Mufflers")
        print("4.Shawls")
        print("5.Winter gloves")
        winterwear = {1: "Sweatshirts", 2:"Jackets", 3:"Mufflers", 4:"Shawls", 5:"Winter gloves"}
       
        #all available options with color
        sweatshirts = {"Red":[],
                 "Blue": [],
                 "Yellow": [],
                 "Pink": [],
                 "Black": []}
        jackets = {"Red":[],
                 "Blue": [],
                 "Yellow": [],
                 "Pink": [],
                 "Black": []}
        mufflers = {"Red":[],
                 "Blue": [],
                 "Yellow": [],
                 "Pink": [],
                 "Black": []}
        shawls = {"Red":[],
                 "Blue": [],
                 "Yellow": [],
                 "Pink": [],
                 "Black": []}
        gloves = {"Red":[],
                 "Blue": [],
                 "Yellow": [],
                 "Pink": [],
                 "Black": []}
       
        winter = int(input("Please select your desired winterwear type:"))
        while winter > 5:
            print("winterwear not found")
            winter = int(input("Please select your desired winterwear type:"))
        print("You selected", winterwear[winter], "--")
       
       
        #Filters
        print("\n*FILTERS*")
       
        #size filter
        print("Size:-")
        print("1.XS\n2.S\n3.M\n4.L\n5.XL")
        sizeList = {1: "XS", 2: "S", 3: "M", 4: "L", 5: "Xl"}
        size = int(input("Select Size:-"))
        while size > 5:
            print("Size not available")
            size = int(input("Select Size:-"))
        print("\nYou selected", sizeList[size] ,"size--")
       
        #price range filter
        print("\nPrice range")
        print("1.0-499\n2.500-999\n3.1000-1499")
        priceRange = {1: "0-499", 2:"500-999", 3:"1000-1499"}
        pri_rng=int(input("Select price range:-"))
        while pri_rng > 3:
            print("Price not in range")
            pri_rng=input("Select price range:-")    
        print("\nPrice range:", priceRange[pri_rng], "--")
       
        #Fabric filter
        print("\nFabric")
        print("1.Cotton\n2.Polyster\n3.Rayon\n4.Silk")
        fabricList = {1: "Cotton", 2:"Polyster", 3:"Rayon", 4:"Silk"}
        fabric=int(input("Select fabric:-"))
        while fabric > 4:
            print("Fabric not in list")
            fabric=input("Select fabric:-")            
        print("\n"+fabricList[fabric], "--")
       
        #Color filter
        print("\nColor")
        print("1.Red\n2.Blue\n3.Yellow\n4.Pink\n5.Black")
        clrList = {1: "Red", 2:"Blue", 3:"Yellow", 4:"Pink", 5:"Black"}            
        clr=int(input("Select color:-"))
        while clr > 5:
            print("Color not in list")
            clr=input("Select color:-")
        selectedColor = clrList[clr]
        print("\nYou selected", clrList[clr], "--")
       
        #results of all filters
        result = {}
        print("Results:")
        if winter == 1:
            sweatshirtColors = sweatshirts[selectedColor]
           
            if len(sweatshirtColors) == 0:
                checkout["stock"] = 0
            else:
                checkout["stock"] = 1
                for colorOption in sweatshirtColors:
                    print(sweatshirtColors.index(colorOption) + 1)
                    display(Image(filename="women/winterwear/sweatshirt/"+colorOption+".jpeg", width=150, height=200))
                    result[sweatshirtColors.index(colorOption) + 1] = [colorOption, "women/winterwear/sweatshirt/"+colorOption]
                    #for table
                    print(pd.read_csv("women/winterwear/sweatshirt/"+selectedColor+".csv"), "\n")
           
        elif winter == 2:
            jacketColor = jackets[selectedColor]
           
            if len(jacketColor) == 0:
                checkout["stock"] = 0
            else:
                checkout["stock"] = 1
                for colorOption in jacketColor:
                    print(jacketColor.index(colorOption) + 1)
                    display(Image(filename="women/winterwear/jackets/"+colorOption+".jpeg", width=150, height=200))
                    result[jacketColor.index(colorOption) + 1] = [colorOption, "women/winterwear/jackets/"+colorOption]
                    #for table
                    print(pd.read_csv("women/winterwear/jackets/"+selectedColor+".csv"), "\n")
               
        elif winter == 3:
            mufflerColor = mufflers[selectedColor]
           
            if len(mufflerColor) == 0:
                checkout["stock"] = 0
            else:
                checkout["stock"] = 1
                for colorOption in mufflerColor:
                    print(mufflerColor.index(colorOption) + 1)
                    display(Image(filename="women/winterwear/mufflers/"+colorOption+".jpeg", width=150, height=200))
                    result[mufflerColor.index(colorOption) + 1] = [colorOption, "women/winterwear/mufflers/"+colorOption]
                    #for table
                    print(pd.read_csv("women/winterwear/mufflers/"+selectedColor+".csv"), "\n")
       
        elif winter == 4:
            shawlColor = shawls[selectedColor]
           
            if len(shawlColor) == 0:
                checkout["stock"] = 0
            else:
                checkout["stock"] = 1
                for colorOption in shawlColor:
                    print(shawlColor.index(colorOption) + 1)
                    display(Image(filename="women/winterwear/shawls/"+colorOption+".jpeg", width=150, height=200))
                    result[shawlColor.index(colorOption) + 1] = [colorOption, "women/winterwear/shawls/"+colorOption]
                    #for table
                    print(pd.read_csv("women/winterwear/shawls/"+selectedColor+".csv"), "\n")
       
        elif winter == 5:
            gloveColor = gloves[selectedColor]
           
            if len(gloveColor) == 0:
                checkout["stock"] = 0
            else:
                checkout["stock"] = 1
                for colorOption in glovesColor:
                    print(gloveColor.index(colorOption) + 1)
                    display(Image(filename="women/winterwear/gloves/"+colorOption+".jpeg", width=150, height=200))
                    result[gloveColor.index(colorOption) + 1] = [colorOption, "women/winterwear/gloves/"+colorOption]
                    #for table
                    print(pd.read_csv("women/winterwear/gloves/"+selectedColor+".csv"), "\n")
       
        stock = checkout["stock"]
        if stock != 0:
            final = int(input("Select an option to checkout:-"))
            checkout["product"] = result[final][0]
            checkout["productImage"] = result[final][1]
            checkout["filters"] = {
                "size":sizeList[size],
                "fabric":fabricList[fabric],
                "price":pri_rng}
       
if cat==3:  
    print("You selected kid's wear--")
   
    kids = {"Red":["kr1", "kr2", "kr3", "kr4", "kr5"],
            "Blue": ["kb1", "kb2", "kb3", "kb4", "kb5"],
            "Yellow": ["ky1", "ky2", "ky3", "ky4", "ky5"],
            "Pink": ["kp1", "kp2", "kp3", "kp4", "kp5"],
            "Black": ["kk1", "kk2", "kk3", "kk4", "kk5"]}
   
    #Filters
    print("\n*FILTERS*")
   
    #size filter
    print("Age:-")
    print("1. 0-2\n2. 3-5\n3. 6-8\n4.9-11\n5.12-14")
    ageList = {1: "0-2", 2: "3-5", 3: "6-8", 4: "9-11", 5: "12-14"}
    age = int(input("Select Age:-"))
    while age > 5:
        print("Age not available")
        age = int(input("Select age:-"))
    print("\nYou selected", ageList[age] ,"age--")
   
    #price range filter
    print("\nPrice range")
    print("1.0-499\n2.500-999\n3.1000-1499")
    priceRange = {1: "0-499", 2:"500-999", 3:"1000-1499"}
    pri_rng=int(input("Select price range:-"))
    while pri_rng > 3:
        print("Price not in range")
        pri_rng=input("Select price range:-")    
    print("\nPrice range:", priceRange[pri_rng], "--")
   
    #Fabric filter
    print("\nFabric")
    print("1.Cotton\n2.Polyster\n3.Rayon\n4.Silk")
    fabricList = {1: "Cotton", 2:"Polyster", 3:"Rayon", 4:"Silk"}
    fabric=int(input("Select fabric:-"))
    while fabric > 4:
        print("Fabric not in list")
        fabric=input("Select fabric:-")            
    print("\n"+fabricList[fabric], "--")
   
    #Color filter
    print("\nColor")
    print("1.Red\n2.Blue\n3.Yellow\n4.Pink\n5.Black")
    clrList = {1: "Red", 2:"Blue", 3:"Yellow", 4:"Pink", 5:"Black"}            
    clr=int(input("Select color:-"))
    while clr > 5:
        print("Color not in list")
        clr=input("Select color:-")
    selectedColor = clrList[clr]
    print("\nYou selected", clrList[clr], "--")
   
    #results of all filters
    result = {}
    print("Results:")
   
    kidsColor = kids[selectedColor]
   
    if len(kidsColor) == 0:
        checkout["stock"] = 0
    else:
        checkout["stock"] = 1
        for colorOption in kidsColor:
            print(kidsColor.index(colorOption) + 1)
            display(Image(filename="kids/"+colorOption+".jpeg", width=150, height=200))
            result[kidsColor.index(colorOption) + 1] = [colorOption, "kids/"+colorOption]
            #for table
            print(pd.read_csv("kids/"+selectedColor+".csv"), "\n")
   
    stock = checkout["stock"]
    if stock != 0:
        final = int(input("Select an option to checkout:-"))
        checkout["product"] = result[final][0]
        checkout["productImage"] = result[final][1]
        checkout["filters"] = {
            "size":ageList[age],
            "fabric":fabricList[fabric],
            "price":pri_rng}
       
#if item not in stock
stock = checkout["stock"]
if stock == 0:
    print("Item not in stock")
else:
    #checkout
    print("\n")
    print("**************************")
    print("\nReview your order")
    display(Image(filename=checkout["productImage"]+".jpeg", width=150, height=200))
    #order summary
    print("<Order Summary>")
    priceRange = checkout["filters"]["price"]
    fabric = checkout["filters"]["fabric"]
    size = checkout["filters"]["size"]

    print("> Fabric:", fabric)
    print("> size:", size)

    if priceRange == 1:
        priceStart = 100
        priceLast = 500
        price = random.randint(priceStart, priceLast)
        print("> Price:", float(price))
    elif priceRange == 2:
        priceStart = 500
        priceLast = 1000
        price = random.randint(priceStart, priceLast)
        print("> Price:", float(price))
    elif priceRange == 3:
        priceStart = 1000
        priceLast = 1500
        price = random.randint(priceStart, priceLast)
        print("> Price:", float(price))

    confirm = input("\nPress yes to proceed or press any button to cancel:-")
    if confirm.lower() == "yes":
        print("Your order has been placed")
    else:
        print("Order cancelled")
       
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

