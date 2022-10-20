from tkinter import *
import webbrowser
import os

#Declare root object

root = Tk()
root.title("Factal Quick Launch")
root.geometry('450x375')
root.config(background="dark grey")

#declare empty array to pass to launch, this array replaces the command line arguments

reg_arr = []

#declear header label

infoLabel = Label(root, text="It's another day at Factal", fg="black", bg="#F1AAA4" ).grid(row= 0, column = 1)

#define click function for the regions

def regionClick(region):
    reg_arr.append(region)
    print_me = ",".join(reg_arr)
    launchLabel = Label(root, text= "{"+print_me+"}", fg="black", bg="#F1AAA4", padx=10, pady=10).grid(row=6,column=1)
    
#this code is pulled from my previous project
    
def launch(arguments):
    
    crucial_links = ["https://www.factal.com/", "https://www.google.ca/maps", "https://www.factal.com/tools/radar/", "https://docs.google.com/document/d/1jVFn408nJur3oSkP4nxKs2iIzmXcmbTpVzJ9WNOezzw/edit", "https://docs.google.com/spreadsheets/d/1B6D7sxfu8XC4uS5oGhnR6bpOdB4YEA7v2m670-GWiNY/edit#gid=0", "https://docs.google.com/spreadsheets/d/1BB9AnLtcIaWzSDUZ8QCCQrehq-a6O2daF0pePYjEQYs/edit#gid=0", "gmail.com"    ]

    ukr_links = ["https://ria.ru/", "https://twitter.com/i/lists/1033474498656272384", "https://twitter.com/i/lists/1045724714599993345", "https://liveuamap.com/", "https://apps.crowdtangle.com/factalfacebook/lists/1660922"]

    euro_links = ["https://twitter.com/FactalMembers/lists/europe", "https://twitter.com/i/lists/1511991793893654528", "https://twitter.com/i/lists/1511999402176659456", "https://twitter.com/FactalMembers/lists/united-kingdom", "https://twitter.com/i/lists/1512052556830232576", "https://twitter.com/FactalMembers/lists/eastern-europe"]

    apac_links =  ["https://twitter.com/FactalMembers/lists/asia", "https://twitter.com/FactalMembers/lists/central-asia", "https://twitter.com/i/lists/1072990194666622977", "https://twitter.com/i/lists/1354871811616296962", "https://twitter.com/i/lists/1318708414168485889", "https://twitter.com/i/lists/1354887811346829313"]

    latam_links = ["https://twitter.com/FactalMembers/lists/latin-america", "https://twitter.com/i/lists/1362397817357168640", "https://twitter.com/i/lists/1364522787000483840", "https://twitter.com/i/lists/1364520809386115080", "https://twitter.com/FactalMembers/lists/caribbean", "https://twitter.com/FactalMembers/lists/mexico", "https://twitter.com/FactalMembers/lists/brazil", "https://twitter.com/search?q=tiroteo%20OR%20tiros%20OR%20balacera%20OR%20balazos%20OR%20pistolero%20OR%20pistoleros%20OR%20%22armas%20de%20fuego%22%20(min_retweets%3A3%20OR%20filter%3Averified)&src=typed_query&f=live"]

    afr_links = ["https://www.rfi.fr/fr/afrique/en-bref/", "https://twitter.com/search?q=list%3Afactalmembers%2Fafrica&src=typed_query", "https://apps.crowdtangle.com/factalfacebook/lists/1672211#", "https://twitter.com/search?q=min_retweets%3A1%20lang%3Afr%20(attentat%20OR%20tu%C3%A9es%20OR%20miliciens%20OR%20assaillants%20OR%20incursion%20OR%20%22coups%20de%20feu%22%20OR%20d%C3%A9placement%20OR%20bless%C3%A9es%20OR%20enlev%C3%A9s)%20AND%20(CODECO%20OR%20ADF%20OR%20RDC%20OR%20Congo%20OR%20Mali%20OR%20Burkina%20OR%20Burkinab%C3%A9%20OR%20Malien%20OR%20Congolais)&src=typed_query&f=live", "https://twitter.com/i/lists/1435544502136082433", "https://twitter.com/FactalMembers/lists/southern-africa", "https://twitter.com/FactalMembers/lists/east-africa", "https://twitter.com/FactalMembers/lists/east-africa", "https://twitter.com/FactalMembers/lists/west-africa"]

    mena_links = ["https://twitter.com/search?q=(%22%D8%B9%D8%A8%D9%88%D8%A9%20%D9%86%D8%A7%D8%B3%D9%81%D8%A9%22%20OR%20%D9%82%D9%86%D8%A8%D9%84%D8%A9%20OR%20%D8%AA%D9%81%D8%AC%D9%8A%D8%B1%20OR%20%D8%A5%D9%86%D9%81%D8%AC%D8%A7%D8%B1%20OR%20%D8%A5%D9%86%D9%81%D8%AC%D8%A7%D8%B1%D8%A7%D8%AA%20OR%20%D8%A8%D9%85%D8%A8%20OR%20%20%D8%A7%D9%86%D9%81%D8%AC%D8%A7%D8%B1%DB%8C%20%20patlama%20OR%20bomba%20OR)&src=typed_query&f=live", "https://twitter.com/search?q=(%D8%AD%D8%B1%D9%8A%D9%82%20OR%20%D8%AD%D8%B1%D9%82%20OR%20%22%D8%A5%D8%B6%D8%B1%D8%A7%D9%85%20%D8%A7%D9%84%D9%86%D8%A7%D8%B1%22%20OR%20%22%D8%A5%D8%B6%D8%B1%D8%A7%D9%85%20%D8%A7%D9%84%D9%86%D9%8A%D8%B1%D8%A7%D9%86%22%20OR%20%D8%A5%D8%B4%D8%AA%D8%B9%D8%A7%D9%84%20OR%20%22%D9%86%D8%B4%D9%88%D8%A8%20%D8%AD%D8%B1%D9%8A%D9%82%22%20OR%20%22%D8%A5%D8%B4%D8%B9%D8%A7%D9%84%20%D8%A7%D9%84%D9%86%D8%A7%D8%B1%22%20OR%20%D8%A2%D8%AA%D8%B4%20OR%20Ate%C5%9F)&src=typed_query&f=live", "https://twitter.com/FactalMembers/lists/middle-east", "https://twitter.com/FactalMembers/lists/syria", "https://twitter.com/FactalMembers/lists/israel", "https://asharq.com/latest-news/"]

    noram_links = ["https://twitter.com/i/lists/1072990561420759041", "https://twitter.com/FactalMembers/lists/canada", "https://abcnews.go.com/US", "https://twitter.com/i/lists/1407827406589632512", "https://twitter.com/search?q=((elmo%20OR%20moose%20OR%20%22east%20gap%22%20OR%20nohomin%20OR%20chalk%20OR%20sugarloaf%20OR%20fly%20creek)%20AND%20(fire))%20OR%20(OR%20elmofire%20OR%20moosefire%20OR%20eastgapfire%20OR%20nohominfire%20OR%20chalkfire%20OR%20sugarloaffire%20OR%20flycreekfire)%20filter%3Averified&src=typed_query&f=live"]

    valid_links = {"africa": afr_links, "europe": euro_links, "ukraine": ukr_links, "apac": apac_links, "mena": mena_links, "noram": noram_links, "latam": latam_links}
    
    if "start" in arguments:
        for i in range (len(crucial_links)):
            webbrowser.open_new(crucial_links[i])
    
    for i in range (len(arguments)):
        region = arguments[i].lower()
        if region == "ukraine":
            os.system("open /Applications/Telegram.app")
        if region in valid_links.keys():
            open_me = valid_links.get(region)
            for i in range (len(open_me)):
                webbrowser.open_new(open_me[i])
    
    
    
    
    
#define start button
    
startButton = Button(root, text="Click if your shift is just beginning", command = lambda:regionClick("start"), padx=20, pady=10, fg="red", borderwidth=5).grid (row=1, column = 1)
    

#Label and frame for the regions
regionLabel = Label(root, text ="Choose your regions",fg="black",bg="#F1AAA4").grid(row=2, column=1)
regionFrame = Frame(root, borderwidth=8, bg="red").grid(row=3, column=1)


#define region buttons
afrbutton = Button(regionFrame, text="Africa", command = lambda:regionClick("Africa"),fg="red", padx=20, pady=20).grid(row=3,column=0)
apacbutton = Button(regionFrame, text="APAC", command = lambda:regionClick("APAC"),fg="red", padx=20, pady=20).grid(row=3, column=1)
eurobutton = Button(regionFrame, text="Europe", command = lambda:regionClick("Europe"), fg="red",padx=20, pady=20).grid(row=3,column=2)
ukrbutton = Button(regionFrame, text="Ukraine", command = lambda:regionClick("Ukraine"), fg="red",padx=20, pady=20).grid(row=4,column=0)
latambutton = Button(regionFrame, text="LATAM", command = lambda:regionClick("LATAM"), fg="red",padx=20, pady=20).grid(row=4,column=1)
norambutton = Button(regionFrame, text="NORAM", command = lambda:regionClick("NORAM"), fg="red",padx=20, pady=20).grid(row=4,column=2)
menabutton = Button(regionFrame, text="MENA", command = lambda:regionClick("MENA"), fg="red",padx=20, pady=20).grid(row=5,column=1)

#this button triggers the launch function
launchButton = Button(root, text="Launch", fg="red", command=lambda:launch(reg_arr), padx=10, pady=10).grid(row=7,column=1)