# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 17:02:41 2024

@author: Sanskriti Dutta
"""

##beerfactory##

import pandas as pd   
print("\n")                                          #INTRODUCTION
print("hello user!! welcome to my BEER SHOP, \nI'm your BREWER GIRl, Nice to meet you  ")
print("\n")
print("lets know more about you ;> ProVide some more details/n")
username=input("whatzzza NAME??--> ")  
print("\n",username,"!!! that's a nice name to for me to flatter...\nNOW tell me shall I SIR you or MAM you???")
print("\nGENDER")                                        #name
print("\n1. MALE""\n""2.FEMALE")

gender=int(input("\nyour GENDER??? (click 1 or 2) :  "))                                       #gender
if gender==1:
    print("\nhey!!!Brother; PROCEED")
if gender==2:
    print("\nheY!!!Sissy, there you go...PROCEED")
else:
    print()
print("\n")
print("almost there...")
age=int(input("don't mind me...but I need to know your AGE : "))
if age<18:
  print("\nage restricted")                                              #age
elif age>17:
    print("\nYou must look so FLY!!! \nlets proceed..")
    print("\n")                                          # BOTTLES
    print("^^^ BOTTLE MEASUREMENT {in litres} :: 1^^^ \n[Fixed]")
    print("\n")
    print("we shall notify you in ???")
    print("\n")
    mob_no= int(input("Enter your mobile no.(10 digits ; else no verification of info.) ::  "))
    if 999999999<mob_no<9999999999:
        print(username,"\nyou will get the notification on the number given above")
        print("\nverify your details--->>\n1.USERNAME: ",username,"\n2.GENDER: ",gender,"\nAGE: ",age,"\nMOBILE NUMBER: ",mob_no)
    else:
        print("NO NOTIFICATION AND VERIFICATION OF DEATILS :-/ ")
    print('\n')
    print("done with the info...YOU here...")
    print("\n",username,"Now,mostly you'll be given options; make sure your hands lie on the NUMBER KEYS :)")
    print("\nNO. OF BOTTLES #not more than 4 ;else set to 1#")
    ch0= int(input("\nchoose no.of BOTTLES:  "))
    if ch0==1:
        print("\nno. of bottles chosen = 1 \nthat's HEALTHY")
        print("\n")
        print("\n*** BEER MAKING PROCESS ***")
        print("\n")
        print("*** INGREDIENT COLUMN ***")
        ing=pd.Series(data=["WHEAT","MAIZE","RICE","OATS","BARLEY"],index=["1","2","3","4","5"])    ##ingredients 
        print(ing)
        print("\n")
        ch1=int(input("CHOOSE YOUR CORE INGREDIENT:  "))
        if ch1==1:
            print("\nYou chose your CORE INGREDIENT as WHEAT")
        elif ch1==2:
            print("\nYou chose your CORE INGREDIENT as MAIZE")
        elif ch1==3:
            print("\nYou chose your CORE INGREDIENT as RICE")
        elif ch1==4:
            print("\nYou chose your CORE INGREDIENT as OATS")
        elif ch1==5:
            print("\nYou chose your CORE INGREDIENT as BARLEY")
        elif ch1>5:  
            print("default value set to 1\nYou chose your CORE INGREDIENT as WHEAT")
        print("\n")
        print("lets commence with BREWING your BEER")                       #PROCESS
        print("*** STEPS TO FOLLOW ***")
        steps=pd.Series(["MALTING","KINLING","MILLING","MASHING","LAUTERING","WORT BOILING","CLARIFICATION","FERMENTATION","CONDITIONING","FILTERATION","PASTEURISATION","FILLING BOTTLING"],index=["1","2","3","4","5","6","7","8","9","10","11","12",])
        print(steps)
        print("\n")
        ch2= int(input("press 1 to BEGIN the PROCESS : "))
        if ch2==1:
            print("\n")
            print("\nMODE MALTING ON!!")                    ####MALTING__
            print("*")
            print("\n")
            print("MALTING--->> THE PROCESS OF SOAKING GRAIN IN WATER (NORNAL TEMPERATURE) AND ALLOW IT TO GERMINATE ")
            print("GRAIN MEASUREMENT RANGE")
            print("\n")
            print("1. 500 gms - 1 kgs""\n""2. 1 kgs - 2 kgs ")
            print("\n")
            grainbeer=int(input("ENTER GRAIN AMOUNT: "))
            if grainbeer==1:
                print("\nGrain amount selected:: 500gms-1kgs")
            if grainbeer==2:
                 print("\nGrain amount selected:: 1kgs-2kgs")
            elif grainbeer>2:
                print("Your choice not found ;\n Grain amount selected:: 500gms-1kgs")
            print("\nSOAKING DAYS")
            days_beer= int(input("ENTER THE NO. OF DAYS FOR SOAKING PERIOD  ## not more than 4 days :  "))
            if days_beer==1:
                print("\nSOAKING MODE SET TO DAYS=1")
            if days_beer==2:
                print("\nSOAKING MODE SET TO DAYS=2")
            if days_beer==3:
                print("\nSOAKING MODE SET TO DAYS=3")
            if days_beer==4:
                print("\nSOAKING MODE SET TO DAYS=4")
            elif days_beer>4:
                print("Your choice not found;\nSOKING MODE SET TO DAYS=1")
            print("\nDo you wish to continue?")
            print("\n1.yes""\n""2.no")
            print("\n")
            continue2=int(input("enter your preference: "))
            if continue2==1:
                print("\n")
                print("\nMODE KINLING ON!!")                         ###KINLING__
                print("*")
                print("\n")
                print("KINLING--->> IT IS THE PROCESS IN WHICH A PARTICULAR TEMPERATURE IS SET IN ORDER TO PROHIBIT GERMINATION AFTER RESPECTIVE PERIOD")
                print("\n")
                print("TEMPERETURE PREFERENCE (in degrees)")
                print("\n")
                print("1. 30-35")
                print("2. 35-40")
                print("3. 40-45")
                print("4. 45-50")
                print("5. 50-55")
                print("6. 55-60")
                print("\n")
                days_kinling=int(input("ENTER KILNING TEMPERATURE PREFERENCE:  "))
                if days_kinling==1:
                    print("\nTEMPERATURE RANGE PREFERENCE: 30-35")
                if days_kinling==2:
                    print("\nTEMPERATURE RANGE PREFERENCE: 35-40")
                if days_kinling==3:
                    print("\nTEMPERATURE RANGE PREFERENCE: 40-45")
                if days_kinling==4:
                    print("\nTEMPERATURE RANGE PREFERENCE: 45-50")
                if days_kinling==5:
                    print("\nTEMPERATURE RANGE PREFERENCE: 50-55")
                if days_kinling==6:
                   print("\nTEMPERATURE RANGE PREFERENCE: 55-60") 
                elif days_kinling>6:
                    print("Your choice not found ;\nTEMPERATURE RANGE PREFERNCE: 30-35")
                print("\n")
                print("Do you wish to continue?")
                print("\n1.yes""\n""2.no")
                continue3=int(input("enter your preference: "))
                if continue3==1: 
                   print("\n")                              ###MILLING__
                   print("\nMODE MILLING ON!!")
                   print("*")
                   print("\n")
                   print("MILLING-->> IN THIS PROCESS THE DRIED GRAINS WILL NOW BE GRINDED INTO COARSE POWDER KNOWN AS Grist")
                   print("\nGRINDING TEXTURE OF GRIST")
                   print("\n")
                   print("1 coarse""\n""2 medium coarse""\n""3 medium""\n""4 medium fine""\n""5 fine""\n""6 extra fine")
                   grind_texture=int(input("SELECT GRINDING TEXTURE: "))
                   if grind_texture==1:
                      print("\nGRIST TEXTURE SELECTED = COARSE ")
                   if grind_texture==2:
                      print("\nGRIST TEXTURE SELECTED = MEDIUM COARSE ")
                   if grind_texture==3:
                      print("\nGRIST TEXTURE SELECTED = MEDIUM ")
                   if grind_texture==4:
                      print("\nGRIST TEXTURE SELECTED = MEDIUM FINE ")
                   if grind_texture==5:
                      print("\nGRIST TEXTURE SELECTED = FINE ")
                   if grind_texture==6:
                      print("\nGRIST TEXTURE SELECTED = EXTRA FINE ")
                   elif grind_texture>6:
                       print("Your choice not found ;\nGRIST TEXTURE SELECTED = COARES")
                   print("\n")
                   print("Do you wish to continue?")
                   print("\n1.yes""\n""2.no")
                   continue4=int(input("enter your preference: "))
                   if continue4==1:                              ###MASHING__
                       print("\n")
                       print("\nMODE MASHING ON!!")
                       print("*")
                       print("\n")
                       print("MASHING--->> THE GRIST OR THE COARSE POEDER WILL BE MIXED WITH WARM WATER AND THE RESULTING MATERIAL (GRIST+ WATER) IS MIXED WELL AND MAINTAINED AT A CERTAIN TEMPERATURE FOR ABOUT AN HOUR OR QUATER ")
                       print("\n")
                       print("WATER AMOUNT RANGE # between 500-1000 ml")
                       print("\n1.400 ml-500 ml""\n""2. 500 ml-1 litr")
                       print("\n")
                       water_measure=int(input("ENTER THE WATER LEVEL: "))
                       if water_measure==1:
                           print("\nwater level set: LEVEL 1")
                           print("\nwater level= 400 ml-500 ml")
                       if water_measure==2:
                           print("\nwater level set: LEVEL 2")
                           print("\nwater level= 500 ml-1 litr")
                       elif water_measure>2:
                           print("Your choice not found ;\nwater level set: LEVEL1\nwater level=400 ml - 500ml")
                       print("\n")
                       print("Enter no. of preferred mixing days # not more than 3")
                       mix_days=int(input("\nSELECT NO. OF MIXING DAYS: "))
                       if mix_days<3:
                           print("\nNo. of days for MASHING(process_name)::",mix_days)
                       else:
                           print("Your choice not found ;\nNo. of days for MASHING:: 1")
                       print("\n")
                       print("MASHING TEMPERATURE (in celcius)")
                       print("\n1. 40-50""\n""2. 50-60""\n""3. 60-65")
                       print("\n")
                       mash_temp= int(input("SELECT MASHING TEMP. : "))
                       if mash_temp==1:
                           print("\nMASH TEMPERATURE= ",mash_temp)
                       if mash_temp==2:
                           print("\nMASH TEMPERATURE= ",mash_temp)       
                       if mash_temp==3:
                           print("\nMASH TEMPERATURE= ",mash_temp)
                       elif mash_temp>3:
                           print("Your choice not found ;\nMASH TEMPERATURE= 1.40-50")
                       print("Do you wish to continue?")
                       print("\n1.yes""\n""2.no")
                       continue5=int(input("enter your preference: "))
                       if continue5==1:                              ###LAUTERING__
                          print("\n")
                          print("\nMODE LAUTERING ON!!")
                          print("*")
                          print("\nLAUTERING--->> THE MASH LIQUID WILL NOW BE FILTERED AND SEPERATED FROM THE SOLID SUBSTANCES SUCH AS HUSK, OTHER GRAIN REIDUE ETC. AND THEN TRANSFERRED TO ANOTHER VESSEL.")
                          print("\n==>NOW THIS FILTERED AND SEPERATED LIQUID WHICH IS TRANSFERRED TO ANOTHER VESSEL IS CALLED ::-->'Wort ")
                          print("\n==>SOLID LEFT AFTER FILTERATION IS CALLED ::-->> Brewer Spent Grain [BSG]")
                          print("\n==>BSG can be used as cattle feed")
                          print("\n")
                          print("SPARGING")
                          print(" NOW WE NEED THIS WORT FOR FERMENTATION.THEREFORE WE ADD WATER DURING LAUTERING PROCESS WITHOUT DISTURBING THE GRAIN BED")
                          print("\n")
                          print("sparge water")
                          print("1. 250-300")
                          print("2. 300-350")
                          print("3. 350-400")
                          print("4. 400-450")
                          print("5. 450-550")
                          print("\n")
                          sparge_water_amt=int(input("Sparge water amount(in ml) :  "))
                          if sparge_water_amt==1:
                             print("\nsparge water amount selected: 250-300")
                          if sparge_water_amt==2:
                             print("\nsparge water amount selected: 300-350")
                          if sparge_water_amt==3:
                             print("\nsparge water amount selected: 350-400")
                          if sparge_water_amt==4:
                             print("\nsparge water amount selected: 400-450")
                          if sparge_water_amt==5:
                             print("\nsparge water amount selected: 450-500")
                          elif sparge_water_amt>5:
                              print("Your choice not found ;\nsparge water amount selected: 250-300")
                          print("\nDo you wish to continue?")
                          print("\n1.yes""\n""2.no")
                          continue6=int(input("enter your preference: "))
                          if continue6==1:                                      ###WORT_BOILING__
                              print("\n")
                              print("\nMODE WORT BOILING ON!")
                              print("*")
                              print("\nWORT BOILING--->> THE PROCESS IN WHICH THE WORT IS NOW BOILED IN THE COPPER OR STAINLESS STEEL KETTLES FOR A PARTICULAR TIME AND CONTINUOUSLY STIRRED.")
                              print("\n")
                              print("HOPS AND SUGARS ARE ADDED AT DIFFERENT STAGES. {THE TASTE OF THE BEER DEPENDS ON THE T Y P E AND A M O U N T OF HOPS AND SUGAR ADDED")
                              print("\nNOTE--->> HOP:::--->HOP IS A TYPE OF FLOWER FROM HOP PLANT WHICH ADD FLAVOR AND AROMA TO THE BEER")
                              print("\nwort boiling time limit")
                              print("\n")
                              print("\n1. 30 min.- 1hr.""\n""2. 1hr. - 2hr.""\n")
                              wort_boiling_time_period=int(input("enter the wort boil time limit:  "))
                              if wort_boiling_time_period==1:
                                 print("\nWORT BOIL TIME LIMIT SET::: 30 min.- 1 hr.")
                              if wort_boiling_time_period==2:
                                 print("\nWORT BOIL TIME LIMIT SET::: 1 hr. - 2hr.")
                              elif wort_boiling_time_period>2:
                                  print("Your choice not found ;\nWORT BOIL TIME LIMIT SET:::30 min. - 1 hr. ")       
                              print("\nDo you wish to continue?") 
                              print("\n1.yes\n2.no")
                              continue7=int(input("enter your preference: "))
                              if continue7==1:
                                 print("\nMODE CLARIFICATION ON!")                                ###CLARIFICATION__
                                 print("*")
                                 print("\nCLARIFICATION--->> THE PROCESS IN WHICH HOP PARTICLES ARE ACCUMULATED IN THE MIDDLE BY THE TURBULANCE AND IS REMOVED LATER.\nTHE FILTERED WORT IS NOW TRANSFERED TO WORT COOLER FOR CHILLING PERIOD\nTHE CHILLED WORT IS NOW SET FOR FERMENTATION AND THEREFORE TRANSFERED TO FERMENTATION TANK")
                                 print("\nclarification turbulance period:: AUTOSET")
                                 print("clarification chilling temperature:: AUTOSET")
                                 print("\n")
                                 print("select chilling period:")
                                 print("\n1. 3 hrs.\n2. 4 hrs.\n3. 5 hrs\n4. 6 hrs.")
                                 chill=int(input("enter chilling period: "))
                                 if chill==1:
                                     print("\nchilling period set to::1")
                                 elif chill==2:   
                                     print("\nchilling period set to::2")
                                 elif chill==3:
                                     print("\nchilling period set to::3")
                                 elif chill==4:
                                     print("\nchilling period set to::4")
                                 elif chill>4:
                                     print("Your choice not found ;\nchilling period set to::1")
                                 print("\nDo you wish to continue?")
                                 print("\n1. yes\n2. no")
                                 continue8= int(input("enter your preference: "))        ###FERMENTATION__          
                              if continue8==1:
                                 print("\nMODE FERMENTATION ON!")
                                 print("*")
                                 print("\nFERMENTATION--->> THE PROCESS IN WHICH SUGAR + BREWING_YEAST IS ADDED TO PRODUCE ALCOHOL + CARBON DIOXIDE[ for natural fizz]")
                                 print("\nBREWING YEAST COULD LEAD TO TWO VARIETIES OF FERMENTATION--->>\n1.top fermentation \n2.bottom fermentation")
                                 print("\nas the name suggest, in top fermentation, the yeast is collected at the top while in bottom fermentation the yeast settles down at the bottom")
                                 print("\nfermentation type:\n1. top fermentation\n2. bottom fermentation\n")
                                 fermentation= int(input("input your prefered fermentation type: "))
                                 if fermentation==1:
                                    print("\nfermentation type chosen::",fermentation)
                                    print("\ntop fermented beer type\n1.ALES\n2. PORTER\n3.STOUTS")
                                    ferm_top= int(input("Enter your choice:: "))
                                    if ferm_top==1:
                                       print("\nyou chose ALES")
                                    elif ferm_top==2:
                                       print("\nyou chose PORTER")
                                    elif ferm_top==3:
                                       print("\nyou chose STOUTS")
                                    elif ferm_top>3:
                                        print("Your choice not found ; you chose ALES")
                                 if fermentation==2:
                                     print("\nfermentation type chosen::",fermentation)
                                     print("\nbottom fermented beer type(no choice)")
                                     print("\nyour chose lagers")
                              else:
                                  print()
                              print("\nDo you wish to continue?")
                              print("1. yes\n2. no")
                              continue9= int(input("enter your preference: "))
                              if continue9==1:
                                  print("\nMODE CONDITIONING ON!")              ###CONDITIONING__
                                  print('*')
                                  print("\nCONDITIONING / MATURING--->> THE STORAGE PROCESS WHICH LEADS TO SECONDARY FERMENTATION.\nIN THIS PROCESS THE ADDITION OF STILL FERMENTED WORT ALSO TAKES PLACE (KRAUSENING)\nTHE REMAINING YEAST SETTLES AT THE BOTTOM THEN FILTERED BY USING FILTERING AGENTS.")
                                  print("\nSET THE MODE OF CONDITIONING\n1. ON\n2.OFF")
                                  cond_ingmode= int(input("enter your choice: "))
                                  if cond_ingmode==1:
                                      print("\nCONDITION MODE: ON")
                                  elif cond_ingmode==2:    
                                      print("\nCONDITION MODE: OFF")
                                  elif cond_ingmode>2:
                                      print("Your choice not found ;\nCONDITIONING MODE: ON")
                              else:
                                  print()
                              print("\nDo you wish to continue?")
                              print("\n1.yes\n2. no")
                              continue10=int(input("enter your preference: "))
                              if continue10==1:
                                 print("\nMODE FILTERATION ON!")
                                 print("\nFILTERATION--->> NOW THE BEER WILL BE FILTERED AND THE{ADDITIONAL WORT} ADDED DURING CONDITIONING WILL NOW BE REMOVED")
                              else:
                                  print()
                              print("\nDo you wish to continue?")
                              print("\n1. yes\n2. no")
                              continue11= int(input("enter your prefernece: "))
                              if continue11==1:
                                  print("\nMODE PASTEAURIZATION ON!")            ###PASTURIZATION__
                                  print("*")
                                  print("\nPASTEAURIZATION--->> THE CONFINED LIQUID IS PASSED THROUGH HIGH TEMPERATURES FOR SHORET TIME AND THEN COOLED RAPIDLY\n THIS PORCESS MAKES SURE OF KILLING OF MICROORGANISMS AND ALSO EXTENDS THE LIFE OF BEER")
                                  print("\npasturization temperature(in degrees)\n 1. 50-60\n2. 60-70\n3. 70-80\n4. 80-90\n5. 90-100")
                                  past_temp=int(input("Select the pasturization temperature: "))
                                  if past_temp==1:
                                      print("\npasteaurization temp:50-60 ")
                                  elif past_temp==2:
                                      print("\npasteaurization temp:60-70 ")
                                  elif past_temp==3:     
                                      print("\npasteaurization temp:70-80 ")
                                  elif past_temp==4:     
                                      print("\npasteaurization temp:80-90 ")
                                  elif past_temp==5:     
                                      print("\npasteaurization temp:90-100 ")
                                  elif past_temp>5:
                                      print("Your choice not found ; \npasteaurisation temp:50-60")
                              else:
                                  print()
                              print("\nDo you wish to continue?")
                              print("\n1.yes\n2.no")
                              continue12= int(input("enter your preference: "))
                              if continue12==1:
                                  print("\nMODE CARBONATION AND FILLING BOTTLE ON!")           ###CARBONATION__
                                  print("*")
                                  print("\nCARBONATION--->> THE CARBONATION IS THE PROCES TO INJECT (CARBON DIOXIDE) TO MAKE THE BEER FIZZY")
                                  print("\nDO you prefer \n1. injecting CO2 \n2. natural fizz(zero CO2; addition of [YEAST+SUGAR+WORT])")
                                  fizz_ch= int(input("enter your preference: "))
                                  if fizz_ch==1:
                                      injections= int(input("enter no. of inejections (#not more than 2 per bottle):  "))
                                      if injections==1:
                                          print("\nnumber of injections: 1")
                                      elif injections==2:
                                          print("\nnumber of injections: 2")
                                      elif injections>2:
                                          print("Your choice not found ;\nnumber of injections: 1") 
                                  else:
                                      print("\nYour choice not found ;you are set to natural fizz")
                              else:
                                  print()
                              print(username,"here we end up... \nNOW PATIENTLY WAIT FOR YOUR ORDER \nLet's meet soon...")
        else:
            print()
    elif ch0==2:
        print("\nno. of bottles chosen = 2 \nthat's LITTLE TOO MUCH...")
        print("\n")
        print("\n*** BEER MAKING PROCESS ***")
        print("\n")
        print("*** INGREDIENT COLUMN ***")
        ing=pd.Series(data=["WHEAT","MAIZE","RICE","OATS","BARLEY"],index=["1","2","3","4","5"])    ##ingredients 
        print(ing)
        print("\n")
        ch1=int(input("CHOOSE YOUR CORE INGREDIENT:  "))
        if ch1==1:
            print("\nYou chose your CORE INGREDIENT as WHEAT")
        elif ch1==2:
            print("\nYou chose your CORE INGREDIENT as MAIZE")
        elif ch1==3:
            print("\nYou chose your CORE INGREDIENT as RICE")
        elif ch1==4:
            print("\nYou chose your CORE INGREDIENT as OATS")
        elif ch1==5:
            print("\nYou chose your CORE INGREDIENT as BARLEY")
        elif ch1>5:  
            print("default value set to 1\nYou chose your CORE INGREDIENT as WHEAT")
        print("\n")
        print("lets commence with BREWING your BEER")                       #PROCESS
        print("*** STEPS TO FOLLOW ***")
        steps=pd.Series(["MALTING","KINLING","MILLING","MASHING","LAUTERING","WORT BOILING","CLARIFICATION","FERMENTATION","CONDITIONING","FILTERATION","PASTEURISATION","FILLING BOTTLING"],index=["1","2","3","4","5","6","7","8","9","10","11","12",])
        print(steps)
        print("\n")
        ch2= int(input("press 1 to BEGIN the PROCESS : "))
        if ch2==1:
            print("\n")
            print("\nMODE MALTING ON!!")                    ####MALTING__
            print("*")
            print("\n")
            print("MALTING--->> THE PROCESS OF SOAKING GRAIN IN WATER (NORNAL TEMPERATURE) AND ALLOW IT TO GERMINATE ")
            print("GRAIN MEASUREMENT RANGE")
            print("\n")
            print("1. 500 gms - 1 kgs""\n""2. 1 kgs - 2 kgs ")
            print("\n")
            grainbeer=int(input("ENTER GRAIN AMOUNT: "))
            if grainbeer==1:
                print("\nGrain amount selected:: 500gms-1kgs")
            if grainbeer==2:
                 print("\nGrain amount selected:: 1kgs-2kgs")
            elif grainbeer>2:
                print("Your choice not found ;\n Grain amount selected:: 500gms-1kgs")
            print("\nSOAKING DAYS")
            days_beer= int(input("ENTER THE NO. OF DAYS FOR SOAKING PERIOD  ## not more than 4 days :  "))
            if days_beer==1:
                print("\nSOAKING MODE SET TO DAYS=1")
            if days_beer==2:
                print("\nSOAKING MODE SET TO DAYS=2")
            if days_beer==3:
                print("\nSOAKING MODE SET TO DAYS=3")
            if days_beer==4:
                print("\nSOAKING MODE SET TO DAYS=4")
            elif days_beer>4:
                print("Your choice not found;\nSOKING MODE SET TO DAYS=1")
            print("\nDo you wish to continue?")
            print("\n1.yes""\n""2.no")
            print("\n")
            continue2=int(input("enter your preference: "))
            if continue2==1:
                print("\n")
                print("\nMODE KINLING ON!!")                         ###KINLING__
                print("*")
                print("\n")
                print("KINLING--->> IT IS THE PROCESS IN WHICH A PARTICULAR TEMPERATURE IS SET IN ORDER TO PROHIBIT GERMINATION AFTER RESPECTIVE PERIOD")
                print("\n")
                print("TEMPERETURE PREFERENCE (in degrees)")
                print("\n")
                print("1. 30-35")
                print("2. 35-40")
                print("3. 40-45")
                print("4. 45-50")
                print("5. 50-55")
                print("6. 55-60")
                print("\n")
                days_kinling=int(input("ENTER KILNING TEMPERATURE PREFERENCE:  "))
                if days_kinling==1:
                    print("\nTEMPERATURE RANGE PREFERENCE: 30-35")
                if days_kinling==2:
                    print("\nTEMPERATURE RANGE PREFERENCE: 35-40")
                if days_kinling==3:
                    print("\nTEMPERATURE RANGE PREFERENCE: 40-45")
                if days_kinling==4:
                    print("\nTEMPERATURE RANGE PREFERENCE: 45-50")
                if days_kinling==5:
                    print("\nTEMPERATURE RANGE PREFERENCE: 50-55")
                if days_kinling==6:
                   print("\nTEMPERATURE RANGE PREFERENCE: 55-60") 
                elif days_kinling>6:
                    print("Your choice not found ;\nTEMPERATURE RANGE PREFERNCE: 30-35")
                print("\n")
                print("Do you wish to continue?")
                print("\n1.yes""\n""2.no")
                continue3=int(input("enter your preference: "))
                if continue3==1: 
                   print("\n")                              ###MILLING__
                   print("\nMODE MILLING ON!!")
                   print("*")
                   print("\n")
                   print("MILLING-->> IN THIS PROCESS THE DRIED GRAINS WILL NOW BE GRINDED INTO COARSE POWDER KNOWN AS Grist")
                   print("\nGRINDING TEXTURE OF GRIST")
                   print("\n")
                   print("1 coarse""\n""2 medium coarse""\n""3 medium""\n""4 medium fine""\n""5 fine""\n""6 extra fine")
                   grind_texture=int(input("SELECT GRINDING TEXTURE: "))
                   if grind_texture==1:
                      print("\nGRIST TEXTURE SELECTED = COARSE ")
                   if grind_texture==2:
                      print("\nGRIST TEXTURE SELECTED = MEDIUM COARSE ")
                   if grind_texture==3:
                      print("\nGRIST TEXTURE SELECTED = MEDIUM ")
                   if grind_texture==4:
                      print("\nGRIST TEXTURE SELECTED = MEDIUM FINE ")
                   if grind_texture==5:
                      print("\nGRIST TEXTURE SELECTED = FINE ")
                   if grind_texture==6:
                      print("\nGRIST TEXTURE SELECTED = EXTRA FINE ")
                   elif grind_texture>6:
                       print("Your choice not found ;\nGRIST TEXTURE SELECTED = COARES")
                   print("\n")
                   print("Do you wish to continue?")
                   print("\n1.yes""\n""2.no")
                   continue4=int(input("enter your preference: "))
                   if continue4==1:                              ###MASHING__
                       print("\n")
                       print("\nMODE MASHING ON!!")
                       print("*")
                       print("\n")
                       print("MASHING--->> THE GRIST OR THE COARSE POEDER WILL BE MIXED WITH WARM WATER AND THE RESULTING MATERIAL (GRIST+ WATER) IS MIXED WELL AND MAINTAINED AT A CERTAIN TEMPERATURE FOR ABOUT AN HOUR OR QUATER ")
                       print("\n")
                       print("WATER AMOUNT RANGE # between 500-1000 ml")
                       print("\n1.400 ml-500 ml""\n""2. 500 ml-1 litr")
                       print("\n")
                       water_measure=int(input("ENTER THE WATER LEVEL: "))
                       if water_measure==1:
                           print("\nwater level set: LEVEL 1")
                           print("\nwater level= 400 ml-500 ml")
                       if water_measure==2:
                           print("\nwater level set: LEVEL 2")
                           print("\nwater level= 500 ml-1 litr")
                       elif water_measure>2:
                           print("Your choice not found ;\nwater level set: LEVEL1\nwater level=400 ml - 500ml")
                       print("\n")
                       print("Enter no. of preferred mixing days # not more than 3")
                       mix_days=int(input("\nSELECT NO. OF MIXING DAYS: "))
                       if mix_days<3:
                           print("\nNo. of days for MASHING(process_name)::",mix_days)
                       else:
                           print("Your choice not found ;\nNo. of days for MASHING:: 1")
                       print("\n")
                       print("MASHING TEMPERATURE (in celcius)")
                       print("\n1. 40-50""\n""2. 50-60""\n""3. 60-65")
                       print("\n")
                       mash_temp= int(input("SELECT MASHING TEMP. : "))
                       if mash_temp==1:
                           print("\nMASH TEMPERATURE= ",mash_temp)
                       if mash_temp==2:
                           print("\nMASH TEMPERATURE= ",mash_temp)       
                       if mash_temp==3:
                           print("\nMASH TEMPERATURE= ",mash_temp)
                       elif mash_temp>3:
                           print("Your choice not found ;\nMASH TEMPERATURE= 1.40-50")
                       print("Do you wish to continue?")
                       print("\n1.yes""\n""2.no")
                       continue5=int(input("enter your preference: "))
                       if continue5==1:                              ###LAUTERING__
                          print("\n")
                          print("\nMODE LAUTERING ON!!")
                          print("*")
                          print("\nLAUTERING--->> THE MASH LIQUID WILL NOW BE FILTERED AND SEPERATED FROM THE SOLID SUBSTANCES SUCH AS HUSK, OTHER GRAIN REIDUE ETC. AND THEN TRANSFERRED TO ANOTHER VESSEL.")
                          print("\n==>NOW THIS FILTERED AND SEPERATED LIQUID WHICH IS TRANSFERRED TO ANOTHER VESSEL IS CALLED ::-->'Wort ")
                          print("\n==>SOLID LEFT AFTER FILTERATION IS CALLED ::-->> Brewer Spent Grain [BSG]")
                          print("\n==>BSG can be used as cattle feed")
                          print("\n")
                          print("SPARGING")
                          print(" NOW WE NEED THIS WORT FOR FERMENTATION.THEREFORE WE ADD WATER DURING LAUTERING PROCESS WITHOUT DISTURBING THE GRAIN BED")
                          print("\n")
                          print("sparge water")
                          print("1. 250-300")
                          print("2. 300-350")
                          print("3. 350-400")
                          print("4. 400-450")
                          print("5. 450-550")
                          print("\n")
                          sparge_water_amt=int(input("Sparge water amount(in ml) :  "))
                          if sparge_water_amt==1:
                             print("\nsparge water amount selected: 250-300")
                          if sparge_water_amt==2:
                             print("\nsparge water amount selected: 300-350")
                          if sparge_water_amt==3:
                             print("\nsparge water amount selected: 350-400")
                          if sparge_water_amt==4:
                             print("\nsparge water amount selected: 400-450")
                          if sparge_water_amt==5:
                             print("\nsparge water amount selected: 450-500")
                          elif sparge_water_amt>5:
                              print("Your choice not found ;\nsparge water amount selected: 250-300")
                          print("\nDo you wish to continue?")
                          print("\n1.yes""\n""2.no")
                          continue6=int(input("enter your preference: "))
                          if continue6==1:                                      ###WORT_BOILING__
                              print("\n")
                              print("\nMODE WORT BOILING ON!")
                              print("*")
                              print("\nWORT BOILING--->> THE PROCESS IN WHICH THE WORT IS NOW BOILED IN THE COPPER OR STAINLESS STEEL KETTLES FOR A PARTICULAR TIME AND CONTINUOUSLY STIRRED.")
                              print("\n")
                              print("HOPS AND SUGARS ARE ADDED AT DIFFERENT STAGES. {THE TASTE OF THE BEER DEPENDS ON THE T Y P E AND A M O U N T OF HOPS AND SUGAR ADDED")
                              print("\nNOTE--->> HOP:::--->HOP IS A TYPE OF FLOWER FROM HOP PLANT WHICH ADD FLAVOR AND AROMA TO THE BEER")
                              print("\nwort boiling time limit")
                              print("\n")
                              print("\n1. 30 min.- 1hr.""\n""2. 1hr. - 2hr.""\n")
                              wort_boiling_time_period=int(input("enter the wort boil time limit:  "))
                              if wort_boiling_time_period==1:
                                 print("\nWORT BOIL TIME LIMIT SET::: 30 min.- 1 hr.")
                              if wort_boiling_time_period==2:
                                 print("\nWORT BOIL TIME LIMIT SET::: 1 hr. - 2hr.")
                              elif wort_boiling_time_period>2:
                                  print("Your choice not found ;\nWORT BOIL TIME LIMIT SET:::30 min. - 1 hr. ")       
                              print("\nDo you wish to continue?") 
                              print("\n1.yes\n2.no")
                              continue7=int(input("enter your preference: "))
                              if continue7==1:
                                 print("\nMODE CLARIFICATION ON!")                                ###CLARIFICATION__
                                 print("*")
                                 print("\nCLARIFICATION--->> THE PROCESS IN WHICH HOP PARTICLES ARE ACCUMULATED IN THE MIDDLE BY THE TURBULANCE AND IS REMOVED LATER.\nTHE FILTERED WORT IS NOW TRANSFERED TO WORT COOLER FOR CHILLING PERIOD\nTHE CHILLED WORT IS NOW SET FOR FERMENTATION AND THEREFORE TRANSFERED TO FERMENTATION TANK")
                                 print("\nclarification turbulance period:: AUTOSET")
                                 print("clarification chilling temperature:: AUTOSET")
                                 print("\n")
                                 print("select chilling period:")
                                 print("\n1. 3 hrs.\n2. 4 hrs.\n3. 5 hrs\n4. 6 hrs.")
                                 chill=int(input("enter chilling period: "))
                                 if chill==1:
                                     print("\nchilling period set to::1")
                                 elif chill==2:   
                                     print("\nchilling period set to::2")
                                 elif chill==3:
                                     print("\nchilling period set to::3")
                                 elif chill==4:
                                     print("\nchilling period set to::4")
                                 elif chill>4:
                                     print("Your choice not found ;\nchilling period set to::1")
                                 print("\nDo you wish to continue?")
                                 print("\n1. yes\n2. no")
                                 continue8= int(input("enter your preference: "))        ###FERMENTATION__          
                              if continue8==1:
                                 print("\nMODE FERMENTATION ON!")
                                 print("*")
                                 print("\nFERMENTATION--->> THE PROCESS IN WHICH SUGAR + BREWING_YEAST IS ADDED TO PRODUCE ALCOHOL + CARBON DIOXIDE[ for natural fizz]")
                                 print("\nBREWING YEAST COULD LEAD TO TWO VARIETIES OF FERMENTATION--->>\n1.top fermentation \n2.bottom fermentation")
                                 print("\nas the name suggest, in top fermentation, the yeast is collected at the top while in bottom fermentation the yeast settles down at the bottom")
                                 print("\nfermentation type:\n1. top fermentation\n2. bottom fermentation\n")
                                 fermentation= int(input("input your prefered fermentation type: "))
                                 if fermentation==1:
                                    print("\nfermentation type chosen::",fermentation)
                                    print("\ntop fermented beer type\n1.ALES\n2. PORTER\n3.STOUTS")
                                    ferm_top= int(input("Enter your choice:: "))
                                    if ferm_top==1:
                                       print("\nyou chose ALES")
                                    elif ferm_top==2:
                                       print("\nyou chose PORTER")
                                    elif ferm_top==3:
                                       print("\nyou chose STOUTS")
                                    elif ferm_top>3:
                                        print("Your choice not found ; you chose ALES")
                                 if fermentation==2:
                                     print("\nfermentation type chosen::",fermentation)
                                     print("\nbottom fermented beer type(no choice)")
                                     print("\nyour chose lagers")
                              else:
                                  print()
                              print("\nDo you wish to continue?")
                              print("1. yes\n2. no")
                              continue9= int(input("enter your preference: "))
                              if continue9==1:
                                  print("\nMODE CONDITIONING ON!")              ###CONDITIONING__
                                  print('*')
                                  print("\nCONDITIONING / MATURING--->> THE STORAGE PROCESS WHICH LEADS TO SECONDARY FERMENTATION.\nIN THIS PROCESS THE ADDITION OF STILL FERMENTED WORT ALSO TAKES PLACE (KRAUSENING)\nTHE REMAINING YEAST SETTLES AT THE BOTTOM THEN FILTERED BY USING FILTERING AGENTS.")
                                  print("\nSET THE MODE OF CONDITIONING\n1. ON\n2.OFF")
                                  cond_ingmode= int(input("enter your choice: "))
                                  if cond_ingmode==1:
                                      print("\nCONDITION MODE: ON")
                                  elif cond_ingmode==2:    
                                      print("\nCONDITION MODE: OFF")
                                  elif cond_ingmode>2:
                                      print("Your choice not found ;\nCONDITIONING MODE: ON")
                              else:
                                  print()
                              print("\nDo you wish to continue?")
                              print("\n1.yes\n2. no")
                              continue10=int(input("enter your preference: "))
                              if continue10==1:
                                 print("\nMODE FILTERATION ON!")
                                 print("\nFILTERATION--->> NOW THE BEER WILL BE FILTERED AND THE{ADDITIONAL WORT} ADDED DURING CONDITIONING WILL NOW BE REMOVED")
                              else:
                                  print()
                              print("\nDo you wish to continue?")
                              print("\n1. yes\n2. no")
                              continue11= int(input("enter your prefernece: "))
                              if continue11==1:
                                  print("\nMODE PASTEAURIZATION ON!")            ###PASTURIZATION__
                                  print("*")
                                  print("\nPASTEAURIZATION--->> THE CONFINED LIQUID IS PASSED THROUGH HIGH TEMPERATURES FOR SHORET TIME AND THEN COOLED RAPIDLY\n THIS PORCESS MAKES SURE OF KILLING OF MICROORGANISMS AND ALSO EXTENDS THE LIFE OF BEER")
                                  print("\npasturization temperature(in degrees)\n 1. 50-60\n2. 60-70\n3. 70-80\n4. 80-90\n5. 90-100")
                                  past_temp=int(input("Select the pasturization temperature: "))
                                  if past_temp==1:
                                      print("\npasteaurization temp:50-60 ")
                                  elif past_temp==2:
                                      print("\npasteaurization temp:60-70 ")
                                  elif past_temp==3:     
                                      print("\npasteaurization temp:70-80 ")
                                  elif past_temp==4:     
                                      print("\npasteaurization temp:80-90 ")
                                  elif past_temp==5:     
                                      print("\npasteaurization temp:90-100 ")
                                  elif past_temp>5:
                                      print("Your choice not found ; \npasteaurisation temp:50-60")
                              else:
                                  print()
                              print("\nDo you wish to continue?")
                              print("\n1.yes\n2.no")
                              continue12= int(input("enter your preference: "))
                              if continue12==1:
                                  print("\nMODE CARBONATION AND FILLING BOTTLE ON!")           ###CARBONATION__
                                  print("*")
                                  print("\nCARBONATION--->> THE CARBONATION IS THE PROCES TO INJECT (CARBON DIOXIDE) TO MAKE THE BEER FIZZY")
                                  print("\nDO you prefer \n1. injecting CO2 \n2. natural fizz(zero CO2; addition of [YEAST+SUGAR+WORT])")
                                  fizz_ch= int(input("enter your preference: "))
                                  if fizz_ch==1:
                                      injections= int(input("enter no. of inejections (#not more than 2 per bottle):  "))
                                      if injections==1:
                                          print("\nnumber of injections: 1")
                                      elif injections==2:
                                          print("\nnumber of injections: 2")
                                      elif injections>2:
                                          print("Your choice not found ;\nnumber of injections: 1") 
                                  else:
                                      print("\nYour choice not found ;you are set to natural fizz")
                              else:
                                  print()
                              print(username,"here we end up... \nNOW PATIENTLY WAIT FOR YOUR ORDER \nLet's meet soon...")
        else:
            print()
    elif ch0==3:
        print("\nno. of bottles chosen = 3 \nDarling don't drink too much, I'm worried :-(")
        print("\n")
        print("\n*** BEER MAKING PROCESS ***")
        print("\n")
        print("*** INGREDIENT COLUMN ***")
        ing=pd.Series(data=["WHEAT","MAIZE","RICE","OATS","BARLEY"],index=["1","2","3","4","5"])    ##ingredients 
        print(ing)
        print("\n")
        ch1=int(input("CHOOSE YOUR CORE INGREDIENT:  "))
        if ch1==1:
            print("\nYou chose your CORE INGREDIENT as WHEAT")
        elif ch1==2:
            print("\nYou chose your CORE INGREDIENT as MAIZE")
        elif ch1==3:
            print("\nYou chose your CORE INGREDIENT as RICE")
        elif ch1==4:
            print("\nYou chose your CORE INGREDIENT as OATS")
        elif ch1==5:
            print("\nYou chose your CORE INGREDIENT as BARLEY")
        elif ch1>5:  
            print("default value set to 1\nYou chose your CORE INGREDIENT as WHEAT")
        print("\n")
        print("lets commence with BREWING your BEER")                       #PROCESS
        print("*** STEPS TO FOLLOW ***")
        steps=pd.Series(["MALTING","KINLING","MILLING","MASHING","LAUTERING","WORT BOILING","CLARIFICATION","FERMENTATION","CONDITIONING","FILTERATION","PASTEURISATION","FILLING BOTTLING"],index=["1","2","3","4","5","6","7","8","9","10","11","12",])
        print(steps)
        print("\n")
        ch2= int(input("press 1 to BEGIN the PROCESS : "))
        if ch2==1:
            print("\n")
            print("\nMODE MALTING ON!!")                    ####MALTING__
            print("*")
            print("\n")
            print("MALTING--->> THE PROCESS OF SOAKING GRAIN IN WATER (NORNAL TEMPERATURE) AND ALLOW IT TO GERMINATE ")
            print("GRAIN MEASUREMENT RANGE")
            print("\n")
            print("1. 500 gms - 1 kgs""\n""2. 1 kgs - 2 kgs ")
            print("\n")
            grainbeer=int(input("ENTER GRAIN AMOUNT: "))
            if grainbeer==1:
                print("\nGrain amount selected:: 500gms-1kgs")
            if grainbeer==2:
                 print("\nGrain amount selected:: 1kgs-2kgs")
            elif grainbeer>2:
                print("Your choice not found ;\n Grain amount selected:: 500gms-1kgs")
            print("\nSOAKING DAYS")
            days_beer= int(input("ENTER THE NO. OF DAYS FOR SOAKING PERIOD  ## not more than 4 days :  "))
            if days_beer==1:
                print("\nSOAKING MODE SET TO DAYS=1")
            if days_beer==2:
                print("\nSOAKING MODE SET TO DAYS=2")
            if days_beer==3:
                print("\nSOAKING MODE SET TO DAYS=3")
            if days_beer==4:
                print("\nSOAKING MODE SET TO DAYS=4")
            elif days_beer>4:
                print("Your choice not found;\nSOKING MODE SET TO DAYS=1")
            print("\nDo you wish to continue?")
            print("\n1.yes""\n""2.no")
            print("\n")
            continue2=int(input("enter your preference: "))
            if continue2==1:
                print("\n")
                print("\nMODE KINLING ON!!")                         ###KINLING__
                print("*")
                print("\n")
                print("KINLING--->> IT IS THE PROCESS IN WHICH A PARTICULAR TEMPERATURE IS SET IN ORDER TO PROHIBIT GERMINATION AFTER RESPECTIVE PERIOD")
                print("\n")
                print("TEMPERETURE PREFERENCE (in degrees)")
                print("\n")
                print("1. 30-35")
                print("2. 35-40")
                print("3. 40-45")
                print("4. 45-50")
                print("5. 50-55")
                print("6. 55-60")
                print("\n")
                days_kinling=int(input("ENTER KILNING TEMPERATURE PREFERENCE:  "))
                if days_kinling==1:
                    print("\nTEMPERATURE RANGE PREFERENCE: 30-35")
                if days_kinling==2:
                    print("\nTEMPERATURE RANGE PREFERENCE: 35-40")
                if days_kinling==3:
                    print("\nTEMPERATURE RANGE PREFERENCE: 40-45")
                if days_kinling==4:
                    print("\nTEMPERATURE RANGE PREFERENCE: 45-50")
                if days_kinling==5:
                    print("\nTEMPERATURE RANGE PREFERENCE: 50-55")
                if days_kinling==6:
                   print("\nTEMPERATURE RANGE PREFERENCE: 55-60") 
                elif days_kinling>6:
                    print("Your choice not found ;\nTEMPERATURE RANGE PREFERNCE: 30-35")
                print("\n")
                print("Do you wish to continue?")
                print("\n1.yes""\n""2.no")
                continue3=int(input("enter your preference: "))
                if continue3==1: 
                   print("\n")                              ###MILLING__
                   print("\nMODE MILLING ON!!")
                   print("*")
                   print("\n")
                   print("MILLING-->> IN THIS PROCESS THE DRIED GRAINS WILL NOW BE GRINDED INTO COARSE POWDER KNOWN AS Grist")
                   print("\nGRINDING TEXTURE OF GRIST")
                   print("\n")
                   print("1 coarse""\n""2 medium coarse""\n""3 medium""\n""4 medium fine""\n""5 fine""\n""6 extra fine")
                   grind_texture=int(input("SELECT GRINDING TEXTURE: "))
                   if grind_texture==1:
                      print("\nGRIST TEXTURE SELECTED = COARSE ")
                   if grind_texture==2:
                      print("\nGRIST TEXTURE SELECTED = MEDIUM COARSE ")
                   if grind_texture==3:
                      print("\nGRIST TEXTURE SELECTED = MEDIUM ")
                   if grind_texture==4:
                      print("\nGRIST TEXTURE SELECTED = MEDIUM FINE ")
                   if grind_texture==5:
                      print("\nGRIST TEXTURE SELECTED = FINE ")
                   if grind_texture==6:
                      print("\nGRIST TEXTURE SELECTED = EXTRA FINE ")
                   elif grind_texture>6:
                       print("Your choice not found ;\nGRIST TEXTURE SELECTED = COARES")
                   print("\n")
                   print("Do you wish to continue?")
                   print("\n1.yes""\n""2.no")
                   continue4=int(input("enter your preference: "))
                   if continue4==1:                              ###MASHING__
                       print("\n")
                       print("\nMODE MASHING ON!!")
                       print("*")
                       print("\n")
                       print("MASHING--->> THE GRIST OR THE COARSE POEDER WILL BE MIXED WITH WARM WATER AND THE RESULTING MATERIAL (GRIST+ WATER) IS MIXED WELL AND MAINTAINED AT A CERTAIN TEMPERATURE FOR ABOUT AN HOUR OR QUATER ")
                       print("\n")
                       print("WATER AMOUNT RANGE # between 500-1000 ml")
                       print("\n1.400 ml-500 ml""\n""2. 500 ml-1 litr")
                       print("\n")
                       water_measure=int(input("ENTER THE WATER LEVEL: "))
                       if water_measure==1:
                           print("\nwater level set: LEVEL 1")
                           print("\nwater level= 400 ml-500 ml")
                       if water_measure==2:
                           print("\nwater level set: LEVEL 2")
                           print("\nwater level= 500 ml-1 litr")
                       elif water_measure>2:
                           print("Your choice not found ;\nwater level set: LEVEL1\nwater level=400 ml - 500ml")
                       print("\n")
                       print("Enter no. of preferred mixing days # not more than 3")
                       mix_days=int(input("\nSELECT NO. OF MIXING DAYS: "))
                       if mix_days<3:
                           print("\nNo. of days for MASHING(process_name)::",mix_days)
                       else:
                           print("Your choice not found ;\nNo. of days for MASHING:: 1")
                       print("\n")
                       print("MASHING TEMPERATURE (in celcius)")
                       print("\n1. 40-50""\n""2. 50-60""\n""3. 60-65")
                       print("\n")
                       mash_temp= int(input("SELECT MASHING TEMP. : "))
                       if mash_temp==1:
                           print("\nMASH TEMPERATURE= ",mash_temp)
                       if mash_temp==2:
                           print("\nMASH TEMPERATURE= ",mash_temp)       
                       if mash_temp==3:
                           print("\nMASH TEMPERATURE= ",mash_temp)
                       elif mash_temp>3:
                           print("Your choice not found ;\nMASH TEMPERATURE= 1.40-50")
                       print("Do you wish to continue?")
                       print("\n1.yes""\n""2.no")
                       continue5=int(input("enter your preference: "))
                       if continue5==1:                              ###LAUTERING__
                          print("\n")
                          print("\nMODE LAUTERING ON!!")
                          print("*")
                          print("\nLAUTERING--->> THE MASH LIQUID WILL NOW BE FILTERED AND SEPERATED FROM THE SOLID SUBSTANCES SUCH AS HUSK, OTHER GRAIN REIDUE ETC. AND THEN TRANSFERRED TO ANOTHER VESSEL.")
                          print("\n==>NOW THIS FILTERED AND SEPERATED LIQUID WHICH IS TRANSFERRED TO ANOTHER VESSEL IS CALLED ::-->'Wort ")
                          print("\n==>SOLID LEFT AFTER FILTERATION IS CALLED ::-->> Brewer Spent Grain [BSG]")
                          print("\n==>BSG can be used as cattle feed")
                          print("\n")
                          print("SPARGING")
                          print(" NOW WE NEED THIS WORT FOR FERMENTATION.THEREFORE WE ADD WATER DURING LAUTERING PROCESS WITHOUT DISTURBING THE GRAIN BED")
                          print("\n")
                          print("sparge water")
                          print("1. 250-300")
                          print("2. 300-350")
                          print("3. 350-400")
                          print("4. 400-450")
                          print("5. 450-550")
                          print("\n")
                          sparge_water_amt=int(input("Sparge water amount(in ml) :  "))
                          if sparge_water_amt==1:
                             print("\nsparge water amount selected: 250-300")
                          if sparge_water_amt==2:
                             print("\nsparge water amount selected: 300-350")
                          if sparge_water_amt==3:
                             print("\nsparge water amount selected: 350-400")
                          if sparge_water_amt==4:
                             print("\nsparge water amount selected: 400-450")
                          if sparge_water_amt==5:
                             print("\nsparge water amount selected: 450-500")
                          elif sparge_water_amt>5:
                              print("Your choice not found ;\nsparge water amount selected: 250-300")
                          print("\nDo you wish to continue?")
                          print("\n1.yes""\n""2.no")
                          continue6=int(input("enter your preference: "))
                          if continue6==1:                                      ###WORT_BOILING__
                              print("\n")
                              print("\nMODE WORT BOILING ON!")
                              print("*")
                              print("\nWORT BOILING--->> THE PROCESS IN WHICH THE WORT IS NOW BOILED IN THE COPPER OR STAINLESS STEEL KETTLES FOR A PARTICULAR TIME AND CONTINUOUSLY STIRRED.")
                              print("\n")
                              print("HOPS AND SUGARS ARE ADDED AT DIFFERENT STAGES. {THE TASTE OF THE BEER DEPENDS ON THE T Y P E AND A M O U N T OF HOPS AND SUGAR ADDED")
                              print("\nNOTE--->> HOP:::--->HOP IS A TYPE OF FLOWER FROM HOP PLANT WHICH ADD FLAVOR AND AROMA TO THE BEER")
                              print("\nwort boiling time limit")
                              print("\n")
                              print("\n1. 30 min.- 1hr.""\n""2. 1hr. - 2hr.""\n")
                              wort_boiling_time_period=int(input("enter the wort boil time limit:  "))
                              if wort_boiling_time_period==1:
                                 print("\nWORT BOIL TIME LIMIT SET::: 30 min.- 1 hr.")
                              if wort_boiling_time_period==2:
                                 print("\nWORT BOIL TIME LIMIT SET::: 1 hr. - 2hr.")
                              elif wort_boiling_time_period>2:
                                  print("Your choice not found ;\nWORT BOIL TIME LIMIT SET:::30 min. - 1 hr. ")       
                              print("\nDo you wish to continue?") 
                              print("\n1.yes\n2.no")
                              continue7=int(input("enter your preference: "))
                              if continue7==1:
                                 print("\nMODE CLARIFICATION ON!")                                ###CLARIFICATION__
                                 print("*")
                                 print("\nCLARIFICATION--->> THE PROCESS IN WHICH HOP PARTICLES ARE ACCUMULATED IN THE MIDDLE BY THE TURBULANCE AND IS REMOVED LATER.\nTHE FILTERED WORT IS NOW TRANSFERED TO WORT COOLER FOR CHILLING PERIOD\nTHE CHILLED WORT IS NOW SET FOR FERMENTATION AND THEREFORE TRANSFERED TO FERMENTATION TANK")
                                 print("\nclarification turbulance period:: AUTOSET")
                                 print("clarification chilling temperature:: AUTOSET")
                                 print("\n")
                                 print("select chilling period:")
                                 print("\n1. 3 hrs.\n2. 4 hrs.\n3. 5 hrs\n4. 6 hrs.")
                                 chill=int(input("enter chilling period: "))
                                 if chill==1:
                                     print("\nchilling period set to::1")
                                 elif chill==2:   
                                     print("\nchilling period set to::2")
                                 elif chill==3:
                                     print("\nchilling period set to::3")
                                 elif chill==4:
                                     print("\nchilling period set to::4")
                                 elif chill>4:
                                     print("Your choice not found ;\nchilling period set to::1")
                                 print("\nDo you wish to continue?")
                                 print("\n1. yes\n2. no")
                                 continue8= int(input("enter your preference: "))        ###FERMENTATION__          
                              if continue8==1:
                                 print("\nMODE FERMENTATION ON!")
                                 print("*")
                                 print("\nFERMENTATION--->> THE PROCESS IN WHICH SUGAR + BREWING_YEAST IS ADDED TO PRODUCE ALCOHOL + CARBON DIOXIDE[ for natural fizz]")
                                 print("\nBREWING YEAST COULD LEAD TO TWO VARIETIES OF FERMENTATION--->>\n1.top fermentation \n2.bottom fermentation")
                                 print("\nas the name suggest, in top fermentation, the yeast is collected at the top while in bottom fermentation the yeast settles down at the bottom")
                                 print("\nfermentation type:\n1. top fermentation\n2. bottom fermentation\n")
                                 fermentation= int(input("input your prefered fermentation type: "))
                                 if fermentation==1:
                                    print("\nfermentation type chosen::",fermentation)
                                    print("\ntop fermented beer type\n1.ALES\n2. PORTER\n3.STOUTS")
                                    ferm_top= int(input("Enter your choice:: "))
                                    if ferm_top==1:
                                       print("\nyou chose ALES")
                                    elif ferm_top==2:
                                       print("\nyou chose PORTER")
                                    elif ferm_top==3:
                                       print("\nyou chose STOUTS")
                                    elif ferm_top>3:
                                        print("Your choice not found ; you chose ALES")
                                 if fermentation==2:
                                     print("\nfermentation type chosen::",fermentation)
                                     print("\nbottom fermented beer type(no choice)")
                                     print("\nyour chose lagers")
                              else:
                                  print()
                              print("\nDo you wish to continue?")
                              print("1. yes\n2. no")
                              continue9= int(input("enter your preference: "))
                              if continue9==1:
                                  print("\nMODE CONDITIONING ON!")              ###CONDITIONING__
                                  print('*')
                                  print("\nCONDITIONING / MATURING--->> THE STORAGE PROCESS WHICH LEADS TO SECONDARY FERMENTATION.\nIN THIS PROCESS THE ADDITION OF STILL FERMENTED WORT ALSO TAKES PLACE (KRAUSENING)\nTHE REMAINING YEAST SETTLES AT THE BOTTOM THEN FILTERED BY USING FILTERING AGENTS.")
                                  print("\nSET THE MODE OF CONDITIONING\n1. ON\n2.OFF")
                                  cond_ingmode= int(input("enter your choice: "))
                                  if cond_ingmode==1:
                                      print("\nCONDITION MODE: ON")
                                  elif cond_ingmode==2:    
                                      print("\nCONDITION MODE: OFF")
                                  elif cond_ingmode>2:
                                      print("Your choice not found ;\nCONDITIONING MODE: ON")
                              else:
                                  print()
                              print("\nDo you wish to continue?")
                              print("\n1.yes\n2. no")
                              continue10=int(input("enter your preference: "))
                              if continue10==1:
                                 print("\nMODE FILTERATION ON!")
                                 print("\nFILTERATION--->> NOW THE BEER WILL BE FILTERED AND THE{ADDITIONAL WORT} ADDED DURING CONDITIONING WILL NOW BE REMOVED")
                              else:
                                  print()
                              print("\nDo you wish to continue?")
                              print("\n1. yes\n2. no")
                              continue11= int(input("enter your prefernece: "))
                              if continue11==1:
                                  print("\nMODE PASTEAURIZATION ON!")            ###PASTURIZATION__
                                  print("*")
                                  print("\nPASTEAURIZATION--->> THE CONFINED LIQUID IS PASSED THROUGH HIGH TEMPERATURES FOR SHORET TIME AND THEN COOLED RAPIDLY\n THIS PORCESS MAKES SURE OF KILLING OF MICROORGANISMS AND ALSO EXTENDS THE LIFE OF BEER")
                                  print("\npasturization temperature(in degrees)\n 1. 50-60\n2. 60-70\n3. 70-80\n4. 80-90\n5. 90-100")
                                  past_temp=int(input("Select the pasturization temperature: "))
                                  if past_temp==1:
                                      print("\npasteaurization temp:50-60 ")
                                  elif past_temp==2:
                                      print("\npasteaurization temp:60-70 ")
                                  elif past_temp==3:     
                                      print("\npasteaurization temp:70-80 ")
                                  elif past_temp==4:     
                                      print("\npasteaurization temp:80-90 ")
                                  elif past_temp==5:     
                                      print("\npasteaurization temp:90-100 ")
                                  elif past_temp>5:
                                      print("Your choice not found ; \npasteaurisation temp:50-60")
                              else:
                                  print()
                              print("\nDo you wish to continue?")
                              print("\n1.yes\n2.no")
                              continue12= int(input("enter your preference: "))
                              if continue12==1:
                                  print("\nMODE CARBONATION AND FILLING BOTTLE ON!")           ###CARBONATION__
                                  print("*")
                                  print("\nCARBONATION--->> THE CARBONATION IS THE PROCES TO INJECT (CARBON DIOXIDE) TO MAKE THE BEER FIZZY")
                                  print("\nDO you prefer \n1. injecting CO2 \n2. natural fizz(zero CO2; addition of [YEAST+SUGAR+WORT])")
                                  fizz_ch= int(input("enter your preference: "))
                                  if fizz_ch==1:
                                      injections= int(input("enter no. of inejections (#not more than 2 per bottle):  "))
                                      if injections==1:
                                          print("\nnumber of injections: 1")
                                      elif injections==2:
                                          print("\nnumber of injections: 2")
                                      elif injections>2:
                                          print("Your choice not found ;\nnumber of injections: 1") 
                                  else:
                                      print("\nYour choice not found ;you are set to natural fizz")
                              else:
                                  print()
                              print(username,"here we end up... \nNOW PATIENTLY WAIT FOR YOUR ORDER \nLet's meet soon...")
        else:
            print()
    elif ch0==4:
        print("\nno. of bottles chosen = 4 \nTOO SAD...OR TOO HAPPY...? Anyway ")
        print("\n")
        print("\n*** BEER MAKING PROCESS ***")
        print("\n")
        print("*** INGREDIENT COLUMN ***")
        ing=pd.Series(data=["WHEAT","MAIZE","RICE","OATS","BARLEY"],index=["1","2","3","4","5"])    ##ingredients 
        print(ing)
        print("\n")
        ch1=int(input("CHOOSE YOUR CORE INGREDIENT:  "))
        if ch1==1:
            print("\nYou chose your CORE INGREDIENT as WHEAT")
        elif ch1==2:
            print("\nYou chose your CORE INGREDIENT as MAIZE")
        elif ch1==3:
            print("\nYou chose your CORE INGREDIENT as RICE")
        elif ch1==4:
            print("\nYou chose your CORE INGREDIENT as OATS")
        elif ch1==5:
            print("\nYou chose your CORE INGREDIENT as BARLEY")
        elif ch1>5:  
            print("default value set to 1\nYou chose your CORE INGREDIENT as WHEAT")
        print("\n")
        print("lets commence with BREWING your BEER")                       #PROCESS
        print("*** STEPS TO FOLLOW ***")
        steps=pd.Series(["MALTING","KINLING","MILLING","MASHING","LAUTERING","WORT BOILING","CLARIFICATION","FERMENTATION","CONDITIONING","FILTERATION","PASTEURISATION","FILLING BOTTLING"],index=["1","2","3","4","5","6","7","8","9","10","11","12",])
        print(steps)
        print("\n")
        ch2= int(input("press 1 to BEGIN the PROCESS : "))
        if ch2==1:
            print("\n")
            print("\nMODE MALTING ON!!")                    ####MALTING__
            print("*")
            print("\n")
            print("MALTING--->> THE PROCESS OF SOAKING GRAIN IN WATER (NORNAL TEMPERATURE) AND ALLOW IT TO GERMINATE ")
            print("GRAIN MEASUREMENT RANGE")
            print("\n")
            print("1. 500 gms - 1 kgs""\n""2. 1 kgs - 2 kgs ")
            print("\n")
            grainbeer=int(input("ENTER GRAIN AMOUNT: "))
            if grainbeer==1:
                print("\nGrain amount selected:: 500gms-1kgs")
            if grainbeer==2:
                 print("\nGrain amount selected:: 1kgs-2kgs")
            elif grainbeer>2:
                print("Your choice not found ;\n Grain amount selected:: 500gms-1kgs")
            print("\nSOAKING DAYS")
            days_beer= int(input("ENTER THE NO. OF DAYS FOR SOAKING PERIOD  ## not more than 4 days :  "))
            if days_beer==1:
                print("\nSOAKING MODE SET TO DAYS=1")
            if days_beer==2:
                print("\nSOAKING MODE SET TO DAYS=2")
            if days_beer==3:
                print("\nSOAKING MODE SET TO DAYS=3")
            if days_beer==4:
                print("\nSOAKING MODE SET TO DAYS=4")
            elif days_beer>4:
                print("Your choice not found;\nSOKING MODE SET TO DAYS=1")
            print("\nDo you wish to continue?")
            print("\n1.yes""\n""2.no")
            print("\n")
            continue2=int(input("enter your preference: "))
            if continue2==1:
                print("\n")
                print("\nMODE KINLING ON!!")                         ###KINLING__
                print("*")
                print("\n")
                print("KINLING--->> IT IS THE PROCESS IN WHICH A PARTICULAR TEMPERATURE IS SET IN ORDER TO PROHIBIT GERMINATION AFTER RESPECTIVE PERIOD")
                print("\n")
                print("TEMPERETURE PREFERENCE (in degrees)")
                print("\n")
                print("1. 30-35")
                print("2. 35-40")
                print("3. 40-45")
                print("4. 45-50")
                print("5. 50-55")
                print("6. 55-60")
                print("\n")
                days_kinling=int(input("ENTER KILNING TEMPERATURE PREFERENCE:  "))
                if days_kinling==1:
                    print("\nTEMPERATURE RANGE PREFERENCE: 30-35")
                if days_kinling==2:
                    print("\nTEMPERATURE RANGE PREFERENCE: 35-40")
                if days_kinling==3:
                    print("\nTEMPERATURE RANGE PREFERENCE: 40-45")
                if days_kinling==4:
                    print("\nTEMPERATURE RANGE PREFERENCE: 45-50")
                if days_kinling==5:
                    print("\nTEMPERATURE RANGE PREFERENCE: 50-55")
                if days_kinling==6:
                   print("\nTEMPERATURE RANGE PREFERENCE: 55-60") 
                elif days_kinling>6:
                    print("Your choice not found ;\nTEMPERATURE RANGE PREFERNCE: 30-35")
                print("\n")
                print("Do you wish to continue?")
                print("\n1.yes""\n""2.no")
                continue3=int(input("enter your preference: "))
                if continue3==1: 
                   print("\n")                              ###MILLING__
                   print("\nMODE MILLING ON!!")
                   print("*")
                   print("\n")
                   print("MILLING-->> IN THIS PROCESS THE DRIED GRAINS WILL NOW BE GRINDED INTO COARSE POWDER KNOWN AS Grist")
                   print("\nGRINDING TEXTURE OF GRIST")
                   print("\n")
                   print("1 coarse""\n""2 medium coarse""\n""3 medium""\n""4 medium fine""\n""5 fine""\n""6 extra fine")
                   grind_texture=int(input("SELECT GRINDING TEXTURE: "))
                   if grind_texture==1:
                      print("\nGRIST TEXTURE SELECTED = COARSE ")
                   if grind_texture==2:
                      print("\nGRIST TEXTURE SELECTED = MEDIUM COARSE ")
                   if grind_texture==3:
                      print("\nGRIST TEXTURE SELECTED = MEDIUM ")
                   if grind_texture==4:
                      print("\nGRIST TEXTURE SELECTED = MEDIUM FINE ")
                   if grind_texture==5:
                      print("\nGRIST TEXTURE SELECTED = FINE ")
                   if grind_texture==6:
                      print("\nGRIST TEXTURE SELECTED = EXTRA FINE ")
                   elif grind_texture>6:
                       print("Your choice not found ;\nGRIST TEXTURE SELECTED = COARES")
                   print("\n")
                   print("Do you wish to continue?")
                   print("\n1.yes""\n""2.no")
                   continue4=int(input("enter your preference: "))
                   if continue4==1:                              ###MASHING__
                       print("\n")
                       print("\nMODE MASHING ON!!")
                       print("*")
                       print("\n")
                       print("MASHING--->> THE GRIST OR THE COARSE POEDER WILL BE MIXED WITH WARM WATER AND THE RESULTING MATERIAL (GRIST+ WATER) IS MIXED WELL AND MAINTAINED AT A CERTAIN TEMPERATURE FOR ABOUT AN HOUR OR QUATER ")
                       print("\n")
                       print("WATER AMOUNT RANGE # between 500-1000 ml")
                       print("\n1.400 ml-500 ml""\n""2. 500 ml-1 litr")
                       print("\n")
                       water_measure=int(input("ENTER THE WATER LEVEL: "))
                       if water_measure==1:
                           print("\nwater level set: LEVEL 1")
                           print("\nwater level= 400 ml-500 ml")
                       if water_measure==2:
                           print("\nwater level set: LEVEL 2")
                           print("\nwater level= 500 ml-1 litr")
                       elif water_measure>2:
                           print("Your choice not found ;\nwater level set: LEVEL1\nwater level=400 ml - 500ml")
                       print("\n")
                       print("Enter no. of preferred mixing days # not more than 3")
                       mix_days=int(input("\nSELECT NO. OF MIXING DAYS: "))
                       if mix_days<3:
                           print("\nNo. of days for MASHING(process_name)::",mix_days)
                       else:
                           print("Your choice not found ;\nNo. of days for MASHING:: 1")
                       print("\n")
                       print("MASHING TEMPERATURE (in celcius)")
                       print("\n1. 40-50""\n""2. 50-60""\n""3. 60-65")
                       print("\n")
                       mash_temp= int(input("SELECT MASHING TEMP. : "))
                       if mash_temp==1:
                           print("\nMASH TEMPERATURE= ",mash_temp)
                       if mash_temp==2:
                           print("\nMASH TEMPERATURE= ",mash_temp)       
                       if mash_temp==3:
                           print("\nMASH TEMPERATURE= ",mash_temp)
                       elif mash_temp>3:
                           print("Your choice not found ;\nMASH TEMPERATURE= 1.40-50")
                       print("Do you wish to continue?")
                       print("\n1.yes""\n""2.no")
                       continue5=int(input("enter your preference: "))
                       if continue5==1:                              ###LAUTERING__
                          print("\n")
                          print("\nMODE LAUTERING ON!!")
                          print("*")
                          print("\nLAUTERING--->> THE MASH LIQUID WILL NOW BE FILTERED AND SEPERATED FROM THE SOLID SUBSTANCES SUCH AS HUSK, OTHER GRAIN REIDUE ETC. AND THEN TRANSFERRED TO ANOTHER VESSEL.")
                          print("\n==>NOW THIS FILTERED AND SEPERATED LIQUID WHICH IS TRANSFERRED TO ANOTHER VESSEL IS CALLED ::-->'Wort ")
                          print("\n==>SOLID LEFT AFTER FILTERATION IS CALLED ::-->> Brewer Spent Grain [BSG]")
                          print("\n==>BSG can be used as cattle feed")
                          print("\n")
                          print("SPARGING")
                          print(" NOW WE NEED THIS WORT FOR FERMENTATION.THEREFORE WE ADD WATER DURING LAUTERING PROCESS WITHOUT DISTURBING THE GRAIN BED")
                          print("\n")
                          print("sparge water")
                          print("1. 250-300")
                          print("2. 300-350")
                          print("3. 350-400")
                          print("4. 400-450")
                          print("5. 450-550")
                          print("\n")
                          sparge_water_amt=int(input("Sparge water amount(in ml) :  "))
                          if sparge_water_amt==1:
                             print("\nsparge water amount selected: 250-300")
                          if sparge_water_amt==2:
                             print("\nsparge water amount selected: 300-350")
                          if sparge_water_amt==3:
                             print("\nsparge water amount selected: 350-400")
                          if sparge_water_amt==4:
                             print("\nsparge water amount selected: 400-450")
                          if sparge_water_amt==5:
                             print("\nsparge water amount selected: 450-500")
                          elif sparge_water_amt>5:
                              print("Your choice not found ;\nsparge water amount selected: 250-300")
                          print("\nDo you wish to continue?")
                          print("\n1.yes""\n""2.no")
                          continue6=int(input("enter your preference: "))
                          if continue6==1:                                      ###WORT_BOILING__
                              print("\n")
                              print("\nMODE WORT BOILING ON!")
                              print("*")
                              print("\nWORT BOILING--->> THE PROCESS IN WHICH THE WORT IS NOW BOILED IN THE COPPER OR STAINLESS STEEL KETTLES FOR A PARTICULAR TIME AND CONTINUOUSLY STIRRED.")
                              print("\n")
                              print("HOPS AND SUGARS ARE ADDED AT DIFFERENT STAGES. {THE TASTE OF THE BEER DEPENDS ON THE T Y P E AND A M O U N T OF HOPS AND SUGAR ADDED")
                              print("\nNOTE--->> HOP:::--->HOP IS A TYPE OF FLOWER FROM HOP PLANT WHICH ADD FLAVOR AND AROMA TO THE BEER")
                              print("\nwort boiling time limit")
                              print("\n")
                              print("\n1. 30 min.- 1hr.""\n""2. 1hr. - 2hr.""\n")
                              wort_boiling_time_period=int(input("enter the wort boil time limit:  "))
                              if wort_boiling_time_period==1:
                                 print("\nWORT BOIL TIME LIMIT SET::: 30 min.- 1 hr.")
                              if wort_boiling_time_period==2:
                                 print("\nWORT BOIL TIME LIMIT SET::: 1 hr. - 2hr.")
                              elif wort_boiling_time_period>2:
                                  print("Your choice not found ;\nWORT BOIL TIME LIMIT SET:::30 min. - 1 hr. ")       
                              print("\nDo you wish to continue?") 
                              print("\n1.yes\n2.no")
                              continue7=int(input("enter your preference: "))
                              if continue7==1:
                                 print("\nMODE CLARIFICATION ON!")                                ###CLARIFICATION__
                                 print("*")
                                 print("\nCLARIFICATION--->> THE PROCESS IN WHICH HOP PARTICLES ARE ACCUMULATED IN THE MIDDLE BY THE TURBULANCE AND IS REMOVED LATER.\nTHE FILTERED WORT IS NOW TRANSFERED TO WORT COOLER FOR CHILLING PERIOD\nTHE CHILLED WORT IS NOW SET FOR FERMENTATION AND THEREFORE TRANSFERED TO FERMENTATION TANK")
                                 print("\nclarification turbulance period:: AUTOSET")
                                 print("clarification chilling temperature:: AUTOSET")
                                 print("\n")
                                 print("select chilling period:")
                                 print("\n1. 3 hrs.\n2. 4 hrs.\n3. 5 hrs\n4. 6 hrs.")
                                 chill=int(input("enter chilling period: "))
                                 if chill==1:
                                     print("\nchilling period set to::1")
                                 elif chill==2:   
                                     print("\nchilling period set to::2")
                                 elif chill==3:
                                     print("\nchilling period set to::3")
                                 elif chill==4:
                                     print("\nchilling period set to::4")
                                 elif chill>4:
                                     print("Your choice not found ;\nchilling period set to::1")
                                 print("\nDo you wish to continue?")
                                 print("\n1. yes\n2. no")
                                 continue8= int(input("enter your preference: "))        ###FERMENTATION__          
                              if continue8==1:
                                 print("\nMODE FERMENTATION ON!")
                                 print("*")
                                 print("\nFERMENTATION--->> THE PROCESS IN WHICH SUGAR + BREWING_YEAST IS ADDED TO PRODUCE ALCOHOL + CARBON DIOXIDE[ for natural fizz]")
                                 print("\nBREWING YEAST COULD LEAD TO TWO VARIETIES OF FERMENTATION--->>\n1.top fermentation \n2.bottom fermentation")
                                 print("\nas the name suggest, in top fermentation, the yeast is collected at the top while in bottom fermentation the yeast settles down at the bottom")
                                 print("\nfermentation type:\n1. top fermentation\n2. bottom fermentation\n")
                                 fermentation= int(input("input your prefered fermentation type: "))
                                 if fermentation==1:
                                    print("\nfermentation type chosen::",fermentation)
                                    print("\ntop fermented beer type\n1.ALES\n2. PORTER\n3.STOUTS")
                                    ferm_top= int(input("Enter your choice:: "))
                                    if ferm_top==1:
                                       print("\nyou chose ALES")
                                    elif ferm_top==2:
                                       print("\nyou chose PORTER")
                                    elif ferm_top==3:
                                       print("\nyou chose STOUTS")
                                    elif ferm_top>3:
                                        print("Your choice not found ; you chose ALES")
                                 if fermentation==2:
                                     print("\nfermentation type chosen::",fermentation)
                                     print("\nbottom fermented beer type(no choice)")
                                     print("\nyour chose lagers")
                              else:
                                  print()
                              print("\nDo you wish to continue?")
                              print("1. yes\n2. no")
                              continue9= int(input("enter your preference: "))
                              if continue9==1:
                                  print("\nMODE CONDITIONING ON!")              ###CONDITIONING__
                                  print('*')
                                  print("\nCONDITIONING / MATURING--->> THE STORAGE PROCESS WHICH LEADS TO SECONDARY FERMENTATION.\nIN THIS PROCESS THE ADDITION OF STILL FERMENTED WORT ALSO TAKES PLACE (KRAUSENING)\nTHE REMAINING YEAST SETTLES AT THE BOTTOM THEN FILTERED BY USING FILTERING AGENTS.")
                                  print("\nSET THE MODE OF CONDITIONING\n1. ON\n2.OFF")
                                  cond_ingmode= int(input("enter your choice: "))
                                  if cond_ingmode==1:
                                      print("\nCONDITION MODE: ON")
                                  elif cond_ingmode==2:    
                                      print("\nCONDITION MODE: OFF")
                                  elif cond_ingmode>2:
                                      print("Your choice not found ;\nCONDITIONING MODE: ON")
                              else:
                                  print()
                              print("\nDo you wish to continue?")
                              print("\n1.yes\n2. no")
                              continue10=int(input("enter your preference: "))
                              if continue10==1:
                                 print("\nMODE FILTERATION ON!")
                                 print("\nFILTERATION--->> NOW THE BEER WILL BE FILTERED AND THE{ADDITIONAL WORT} ADDED DURING CONDITIONING WILL NOW BE REMOVED")
                              else:
                                  print()
                              print("\nDo you wish to continue?")
                              print("\n1. yes\n2. no")
                              continue11= int(input("enter your prefernece: "))
                              if continue11==1:
                                  print("\nMODE PASTEAURIZATION ON!")            ###PASTURIZATION__
                                  print("*")
                                  print("\nPASTEAURIZATION--->> THE CONFINED LIQUID IS PASSED THROUGH HIGH TEMPERATURES FOR SHORET TIME AND THEN COOLED RAPIDLY\n THIS PORCESS MAKES SURE OF KILLING OF MICROORGANISMS AND ALSO EXTENDS THE LIFE OF BEER")
                                  print("\npasturization temperature(in degrees)\n 1. 50-60\n2. 60-70\n3. 70-80\n4. 80-90\n5. 90-100")
                                  past_temp=int(input("Select the pasturization temperature: "))
                                  if past_temp==1:
                                      print("\npasteaurization temp:50-60 ")
                                  elif past_temp==2:
                                      print("\npasteaurization temp:60-70 ")
                                  elif past_temp==3:     
                                      print("\npasteaurization temp:70-80 ")
                                  elif past_temp==4:     
                                      print("\npasteaurization temp:80-90 ")
                                  elif past_temp==5:     
                                      print("\npasteaurization temp:90-100 ")
                                  elif past_temp>5:
                                      print("Your choice not found ; \npasteaurisation temp:50-60")
                              else:
                                  print()
                              print("\nDo you wish to continue?")
                              print("\n1.yes\n2.no")
                              continue12= int(input("enter your preference: "))
                              if continue12==1:
                                  print("\nMODE CARBONATION AND FILLING BOTTLE ON!")           ###CARBONATION__
                                  print("*")
                                  print("\nCARBONATION--->> THE CARBONATION IS THE PROCES TO INJECT (CARBON DIOXIDE) TO MAKE THE BEER FIZZY")
                                  print("\nDO you prefer \n1. injecting CO2 \n2. natural fizz(zero CO2; addition of [YEAST+SUGAR+WORT])")
                                  fizz_ch= int(input("enter your preference: "))
                                  if fizz_ch==1:
                                      injections= int(input("enter no. of inejections (#not more than 2 per bottle):  "))
                                      if injections==1:
                                          print("\nnumber of injections: 1")
                                      elif injections==2:
                                          print("\nnumber of injections: 2")
                                      elif injections>2:
                                          print("Your choice not found ;\nnumber of injections: 1") 
                                  else:
                                      print("\nYour choice not found ;you are set to natural fizz")
                              else:
                                  print()
                              print(username,"here we end up... \nNOW PATIENTLY WAIT FOR YOUR ORDER \nLet's meet soon...")
        else:
            print()
    else:
        print("\ndefault value set to 1")
        print("\n")
        print("\n*** BEER MAKING PROCESS ***")
        print("\n")
        print("*** INGREDIENT COLUMN ***")
        ing=pd.Series(data=["WHEAT","MAIZE","RICE","OATS","BARLEY"],index=["1","2","3","4","5"])    ##ingredients 
        print(ing)
        print("\n")
        ch1=int(input("CHOOSE YOUR CORE INGREDIENT:  "))
        if ch1==1:
            print("\nYou chose your CORE INGREDIENT as WHEAT")
        elif ch1==2:
            print("\nYou chose your CORE INGREDIENT as MAIZE")
        elif ch1==3:
            print("\nYou chose your CORE INGREDIENT as RICE")
        elif ch1==4:
            print("\nYou chose your CORE INGREDIENT as OATS")
        elif ch1==5:
            print("\nYou chose your CORE INGREDIENT as BARLEY")
        elif ch1>5:  
            print("default value set to 1\nYou chose your CORE INGREDIENT as WHEAT")
        print("\n")
        print("lets commence with BREWING your BEER")                       #PROCESS
        print("*** STEPS TO FOLLOW ***")
        steps=pd.Series(["MALTING","KINLING","MILLING","MASHING","LAUTERING","WORT BOILING","CLARIFICATION","FERMENTATION","CONDITIONING","FILTERATION","PASTEURISATION","FILLING BOTTLING"],index=["1","2","3","4","5","6","7","8","9","10","11","12",])
        print(steps)
        print("\n")
        ch2= int(input("press 1 to BEGIN the PROCESS : "))
        if ch2==1:
            print("\n")
            print("\nMODE MALTING ON!!")                    ####MALTING__
            print("*")
            print("\n")
            print("MALTING--->> THE PROCESS OF SOAKING GRAIN IN WATER (NORNAL TEMPERATURE) AND ALLOW IT TO GERMINATE ")
            print("GRAIN MEASUREMENT RANGE")
            print("\n")
            print("1. 500 gms - 1 kgs""\n""2. 1 kgs - 2 kgs ")
            print("\n")
            grainbeer=int(input("ENTER GRAIN AMOUNT: "))
            if grainbeer==1:
                print("\nGrain amount selected:: 500gms-1kgs")
            if grainbeer==2:
                 print("\nGrain amount selected:: 1kgs-2kgs")
            elif grainbeer>2:
                print("Your choice not found ;\n Grain amount selected:: 500gms-1kgs")
            print("\nSOAKING DAYS")
            days_beer= int(input("ENTER THE NO. OF DAYS FOR SOAKING PERIOD  ## not more than 4 days :  "))
            if days_beer==1:
                print("\nSOAKING MODE SET TO DAYS=1")
            if days_beer==2:
                print("\nSOAKING MODE SET TO DAYS=2")
            if days_beer==3:
                print("\nSOAKING MODE SET TO DAYS=3")
            if days_beer==4:
                print("\nSOAKING MODE SET TO DAYS=4")
            elif days_beer>4:
                print("Your choice not found;\nSOKING MODE SET TO DAYS=1")
            print("\nDo you wish to continue?")
            print("\n1.yes""\n""2.no")
            print("\n")
            continue2=int(input("enter your preference: "))
            if continue2==1:
                print("\n")
                print("\nMODE KINLING ON!!")                         ###KINLING__
                print("*")
                print("\n")
                print("KINLING--->> IT IS THE PROCESS IN WHICH A PARTICULAR TEMPERATURE IS SET IN ORDER TO PROHIBIT GERMINATION AFTER RESPECTIVE PERIOD")
                print("\n")
                print("TEMPERETURE PREFERENCE (in degrees)")
                print("\n")
                print("1. 30-35")
                print("2. 35-40")
                print("3. 40-45")
                print("4. 45-50")
                print("5. 50-55")
                print("6. 55-60")
                print("\n")
                days_kinling=int(input("ENTER KILNING TEMPERATURE PREFERENCE:  "))
                if days_kinling==1:
                    print("\nTEMPERATURE RANGE PREFERENCE: 30-35")
                if days_kinling==2:
                    print("\nTEMPERATURE RANGE PREFERENCE: 35-40")
                if days_kinling==3:
                    print("\nTEMPERATURE RANGE PREFERENCE: 40-45")
                if days_kinling==4:
                    print("\nTEMPERATURE RANGE PREFERENCE: 45-50")
                if days_kinling==5:
                    print("\nTEMPERATURE RANGE PREFERENCE: 50-55")
                if days_kinling==6:
                   print("\nTEMPERATURE RANGE PREFERENCE: 55-60") 
                elif days_kinling>6:
                    print("Your choice not found ;\nTEMPERATURE RANGE PREFERNCE: 30-35")
                print("\n")
                print("Do you wish to continue?")
                print("\n1.yes""\n""2.no")
                continue3=int(input("enter your preference: "))
                if continue3==1: 
                   print("\n")                              ###MILLING__
                   print("\nMODE MILLING ON!!")
                   print("*")
                   print("\n")
                   print("MILLING-->> IN THIS PROCESS THE DRIED GRAINS WILL NOW BE GRINDED INTO COARSE POWDER KNOWN AS Grist")
                   print("\nGRINDING TEXTURE OF GRIST")
                   print("\n")
                   print("1 coarse""\n""2 medium coarse""\n""3 medium""\n""4 medium fine""\n""5 fine""\n""6 extra fine")
                   grind_texture=int(input("SELECT GRINDING TEXTURE: "))
                   if grind_texture==1:
                      print("\nGRIST TEXTURE SELECTED = COARSE ")
                   if grind_texture==2:
                      print("\nGRIST TEXTURE SELECTED = MEDIUM COARSE ")
                   if grind_texture==3:
                      print("\nGRIST TEXTURE SELECTED = MEDIUM ")
                   if grind_texture==4:
                      print("\nGRIST TEXTURE SELECTED = MEDIUM FINE ")
                   if grind_texture==5:
                      print("\nGRIST TEXTURE SELECTED = FINE ")
                   if grind_texture==6:
                      print("\nGRIST TEXTURE SELECTED = EXTRA FINE ")
                   elif grind_texture>6:
                       print("Your choice not found ;\nGRIST TEXTURE SELECTED = COARES")
                   print("\n")
                   print("Do you wish to continue?")
                   print("\n1.yes""\n""2.no")
                   continue4=int(input("enter your preference: "))
                   if continue4==1:                              ###MASHING__
                       print("\n")
                       print("\nMODE MASHING ON!!")
                       print("*")
                       print("\n")
                       print("MASHING--->> THE GRIST OR THE COARSE POEDER WILL BE MIXED WITH WARM WATER AND THE RESULTING MATERIAL (GRIST+ WATER) IS MIXED WELL AND MAINTAINED AT A CERTAIN TEMPERATURE FOR ABOUT AN HOUR OR QUATER ")
                       print("\n")
                       print("WATER AMOUNT RANGE # between 500-1000 ml")
                       print("\n1.400 ml-500 ml""\n""2. 500 ml-1 litr")
                       print("\n")
                       water_measure=int(input("ENTER THE WATER LEVEL: "))
                       if water_measure==1:
                           print("\nwater level set: LEVEL 1")
                           print("\nwater level= 400 ml-500 ml")
                       if water_measure==2:
                           print("\nwater level set: LEVEL 2")
                           print("\nwater level= 500 ml-1 litr")
                       elif water_measure>2:
                           print("Your choice not found ;\nwater level set: LEVEL1\nwater level=400 ml - 500ml")
                       print("\n")
                       print("Enter no. of preferred mixing days # not more than 3")
                       mix_days=int(input("\nSELECT NO. OF MIXING DAYS: "))
                       if mix_days<3:
                           print("\nNo. of days for MASHING(process_name)::",mix_days)
                       else:
                           print("Your choice not found ;\nNo. of days for MASHING:: 1")
                       print("\n")
                       print("MASHING TEMPERATURE (in celcius)")
                       print("\n1. 40-50""\n""2. 50-60""\n""3. 60-65")
                       print("\n")
                       mash_temp= int(input("SELECT MASHING TEMP. : "))
                       if mash_temp==1:
                           print("\nMASH TEMPERATURE= ",mash_temp)
                       if mash_temp==2:
                           print("\nMASH TEMPERATURE= ",mash_temp)       
                       if mash_temp==3:
                           print("\nMASH TEMPERATURE= ",mash_temp)
                       elif mash_temp>3:
                           print("Your choice not found ;\nMASH TEMPERATURE= 1.40-50")
                       print("Do you wish to continue?")
                       print("\n1.yes""\n""2.no")
                       continue5=int(input("enter your preference: "))
                       if continue5==1:                              ###LAUTERING__
                          print("\n")
                          print("\nMODE LAUTERING ON!!")
                          print("*")
                          print("\nLAUTERING--->> THE MASH LIQUID WILL NOW BE FILTERED AND SEPERATED FROM THE SOLID SUBSTANCES SUCH AS HUSK, OTHER GRAIN REIDUE ETC. AND THEN TRANSFERRED TO ANOTHER VESSEL.")
                          print("\n==>NOW THIS FILTERED AND SEPERATED LIQUID WHICH IS TRANSFERRED TO ANOTHER VESSEL IS CALLED ::-->'Wort ")
                          print("\n==>SOLID LEFT AFTER FILTERATION IS CALLED ::-->> Brewer Spent Grain [BSG]")
                          print("\n==>BSG can be used as cattle feed")
                          print("\n")
                          print("SPARGING")
                          print(" NOW WE NEED THIS WORT FOR FERMENTATION.THEREFORE WE ADD WATER DURING LAUTERING PROCESS WITHOUT DISTURBING THE GRAIN BED")
                          print("\n")
                          print("sparge water")
                          print("1. 250-300")
                          print("2. 300-350")
                          print("3. 350-400")
                          print("4. 400-450")
                          print("5. 450-550")
                          print("\n")
                          sparge_water_amt=int(input("Sparge water amount(in ml) :  "))
                          if sparge_water_amt==1:
                             print("\nsparge water amount selected: 250-300")
                          if sparge_water_amt==2:
                             print("\nsparge water amount selected: 300-350")
                          if sparge_water_amt==3:
                             print("\nsparge water amount selected: 350-400")
                          if sparge_water_amt==4:
                             print("\nsparge water amount selected: 400-450")
                          if sparge_water_amt==5:
                             print("\nsparge water amount selected: 450-500")
                          elif sparge_water_amt>5:
                              print("Your choice not found ;\nsparge water amount selected: 250-300")
                          print("\nDo you wish to continue?")
                          print("\n1.yes""\n""2.no")
                          continue6=int(input("enter your preference: "))
                          if continue6==1:                                      ###WORT_BOILING__
                              print("\n")
                              print("\nMODE WORT BOILING ON!")
                              print("*")
                              print("\nWORT BOILING--->> THE PROCESS IN WHICH THE WORT IS NOW BOILED IN THE COPPER OR STAINLESS STEEL KETTLES FOR A PARTICULAR TIME AND CONTINUOUSLY STIRRED.")
                              print("\n")
                              print("HOPS AND SUGARS ARE ADDED AT DIFFERENT STAGES. {THE TASTE OF THE BEER DEPENDS ON THE T Y P E AND A M O U N T OF HOPS AND SUGAR ADDED")
                              print("\nNOTE--->> HOP:::--->HOP IS A TYPE OF FLOWER FROM HOP PLANT WHICH ADD FLAVOR AND AROMA TO THE BEER")
                              print("\nwort boiling time limit")
                              print("\n")
                              print("\n1. 30 min.- 1hr.""\n""2. 1hr. - 2hr.""\n")
                              wort_boiling_time_period=int(input("enter the wort boil time limit:  "))
                              if wort_boiling_time_period==1:
                                 print("\nWORT BOIL TIME LIMIT SET::: 30 min.- 1 hr.")
                              if wort_boiling_time_period==2:
                                 print("\nWORT BOIL TIME LIMIT SET::: 1 hr. - 2hr.")
                              elif wort_boiling_time_period>2:
                                  print("Your choice not found ;\nWORT BOIL TIME LIMIT SET:::30 min. - 1 hr. ")       
                              print("\nDo you wish to continue?") 
                              print("\n1.yes\n2.no")
                              continue7=int(input("enter your preference: "))
                              if continue7==1:
                                 print("\nMODE CLARIFICATION ON!")                                ###CLARIFICATION__
                                 print("*")
                                 print("\nCLARIFICATION--->> THE PROCESS IN WHICH HOP PARTICLES ARE ACCUMULATED IN THE MIDDLE BY THE TURBULANCE AND IS REMOVED LATER.\nTHE FILTERED WORT IS NOW TRANSFERED TO WORT COOLER FOR CHILLING PERIOD\nTHE CHILLED WORT IS NOW SET FOR FERMENTATION AND THEREFORE TRANSFERED TO FERMENTATION TANK")
                                 print("\nclarification turbulance period:: AUTOSET")
                                 print("clarification chilling temperature:: AUTOSET")
                                 print("\n")
                                 print("select chilling period:")
                                 print("\n1. 3 hrs.\n2. 4 hrs.\n3. 5 hrs\n4. 6 hrs.")
                                 chill=int(input("enter chilling period: "))
                                 if chill==1:
                                     print("\nchilling period set to::1")
                                 elif chill==2:   
                                     print("\nchilling period set to::2")
                                 elif chill==3:
                                     print("\nchilling period set to::3")
                                 elif chill==4:
                                     print("\nchilling period set to::4")
                                 elif chill>4:
                                     print("Your choice not found ;\nchilling period set to::1")
                                 print("\nDo you wish to continue?")
                                 print("\n1. yes\n2. no")
                                 continue8= int(input("enter your preference: "))        ###FERMENTATION__          
                              if continue8==1:
                                 print("\nMODE FERMENTATION ON!")
                                 print("*")
                                 print("\nFERMENTATION--->> THE PROCESS IN WHICH SUGAR + BREWING_YEAST IS ADDED TO PRODUCE ALCOHOL + CARBON DIOXIDE[ for natural fizz]")
                                 print("\nBREWING YEAST COULD LEAD TO TWO VARIETIES OF FERMENTATION--->>\n1.top fermentation \n2.bottom fermentation")
                                 print("\nas the name suggest, in top fermentation, the yeast is collected at the top while in bottom fermentation the yeast settles down at the bottom")
                                 print("\nfermentation type:\n1. top fermentation\n2. bottom fermentation\n")
                                 fermentation= int(input("input your prefered fermentation type: "))
                                 if fermentation==1:
                                    print("\nfermentation type chosen::",fermentation)
                                    print("\ntop fermented beer type\n1.ALES\n2. PORTER\n3.STOUTS")
                                    ferm_top= int(input("Enter your choice:: "))
                                    if ferm_top==1:
                                       print("\nyou chose ALES")
                                    elif ferm_top==2:
                                       print("\nyou chose PORTER")
                                    elif ferm_top==3:
                                       print("\nyou chose STOUTS")
                                    elif ferm_top>3:
                                        print("Your choice not found ; you chose ALES")
                                 if fermentation==2:
                                     print("\nfermentation type chosen::",fermentation)
                                     print("\nbottom fermented beer type(no choice)")
                                     print("\nyour chose lagers")
                              else:
                                  print()
                              print("\nDo you wish to continue?")
                              print("1. yes\n2. no")
                              continue9= int(input("enter your preference: "))
                              if continue9==1:
                                  print("\nMODE CONDITIONING ON!")              ###CONDITIONING__
                                  print('*')
                                  print("\nCONDITIONING / MATURING--->> THE STORAGE PROCESS WHICH LEADS TO SECONDARY FERMENTATION.\nIN THIS PROCESS THE ADDITION OF STILL FERMENTED WORT ALSO TAKES PLACE (KRAUSENING)\nTHE REMAINING YEAST SETTLES AT THE BOTTOM THEN FILTERED BY USING FILTERING AGENTS.")
                                  print("\nSET THE MODE OF CONDITIONING\n1. ON\n2.OFF")
                                  cond_ingmode= int(input("enter your choice: "))
                                  if cond_ingmode==1:
                                      print("\nCONDITION MODE: ON")
                                  elif cond_ingmode==2:    
                                      print("\nCONDITION MODE: OFF")
                                  elif cond_ingmode>2:
                                      print("Your choice not found ;\nCONDITIONING MODE: ON")
                              else:
                                  print()
                              print("\nDo you wish to continue?")
                              print("\n1.yes\n2. no")
                              continue10=int(input("enter your preference: "))
                              if continue10==1:
                                 print("\nMODE FILTERATION ON!")
                                 print("\nFILTERATION--->> NOW THE BEER WILL BE FILTERED AND THE{ADDITIONAL WORT} ADDED DURING CONDITIONING WILL NOW BE REMOVED")
                              else:
                                  print()
                              print("\nDo you wish to continue?")
                              print("\n1. yes\n2. no")
                              continue11= int(input("enter your prefernece: "))
                              if continue11==1:
                                  print("\nMODE PASTEAURIZATION ON!")            ###PASTURIZATION__
                                  print("*")
                                  print("\nPASTEAURIZATION--->> THE CONFINED LIQUID IS PASSED THROUGH HIGH TEMPERATURES FOR SHORET TIME AND THEN COOLED RAPIDLY\n THIS PORCESS MAKES SURE OF KILLING OF MICROORGANISMS AND ALSO EXTENDS THE LIFE OF BEER")
                                  print("\npasturization temperature(in degrees)\n 1. 50-60\n2. 60-70\n3. 70-80\n4. 80-90\n5. 90-100")
                                  past_temp=int(input("Select the pasturization temperature: "))
                                  if past_temp==1:
                                      print("\npasteaurization temp:50-60 ")
                                  elif past_temp==2:
                                      print("\npasteaurization temp:60-70 ")
                                  elif past_temp==3:     
                                      print("\npasteaurization temp:70-80 ")
                                  elif past_temp==4:     
                                      print("\npasteaurization temp:80-90 ")
                                  elif past_temp==5:     
                                      print("\npasteaurization temp:90-100 ")
                                  elif past_temp>5:
                                      print("Your choice not found ; \npasteaurisation temp:50-60")
                              else:
                                  print()
                              print("\nDo you wish to continue?")
                              print("\n1.yes\n2.no")
                              continue12= int(input("enter your preference: "))
                              if continue12==1:
                                  print("\nMODE CARBONATION AND FILLING BOTTLE ON!")           ###CARBONATION__
                                  print("*")
                                  print("\nCARBONATION--->> THE CARBONATION IS THE PROCES TO INJECT (CARBON DIOXIDE) TO MAKE THE BEER FIZZY")
                                  print("\nDO you prefer \n1. injecting CO2 \n2. natural fizz(zero CO2; addition of [YEAST+SUGAR+WORT])")
                                  fizz_ch= int(input("enter your preference: "))
                                  if fizz_ch==1:
                                      injections= int(input("enter no. of inejections (#not more than 2 per bottle):  "))
                                      if injections==1:
                                          print("\nnumber of injections: 1")
                                      elif injections==2:
                                          print("\nnumber of injections: 2")
                                      elif injections>2:
                                          print("Your choice not found ;\nnumber of injections: 1") 
                                  else:
                                      print("\nYour choice not found ;you are set to natural fizz")
                              else:
                                  print()
                              print(username,"here we end up... \nNOW PATIENTLY WAIT FOR YOUR ORDER \nLet's meet soon...")
        else:
            print()