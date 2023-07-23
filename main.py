import tkinter as tk
import Wishlistopener as wlo

palette = ["#16697A","#489FB5","#82C0CC","#EDE7E3","#FFA62B"]

def main():
    global palette, listeWishlist

    root = tk.Tk()  
    root.geometry("800x450+{}+{}".format(int(root.winfo_screenwidth()/2 - 400), int(root.winfo_screenheight()/2 - 225)))

    root.focus_set()
    root.resizable(False,False)
    root.title("Kaiwinta's Wishlist")
    root.bind('<Escape>',lambda e: root.destroy())
    root.configure(bg=palette[2])

    def TopFrame():
        topframe = tk.Frame(root, bg= palette[0])
        topframe.place(relheight=0.15 , relwidth=1 , relx=0, rely=0.1)

        topline  = tk.Frame(topframe, bg=palette[4])
        topline.place(relheight=0.05 , relwidth=1 , relx=0, rely=0)

        botline  = tk.Frame(topframe, bg=palette[4])
        botline.place(relheight=0.05 , relwidth=1 , relx=0, rely=0.95)


    def LeftFrame():
        global listeWishlist
        leftframe =tk.Frame(root, bg=palette[1])
        leftframe.place(relheight=0.5 , relwidth=0.35 ,relx=0.1 , rely=0.4)

        topline  = tk.Frame(leftframe, bg=palette[0])
        topline.place(relheight=0.03 , relwidth=1 , relx=0, rely=0)

        botline  = tk.Frame(leftframe, bg=palette[0])
        botline.place(relheight=0.03 , relwidth=1 , relx=0, rely=0.97)

        titleLabel = tk.Label(leftframe, bg= palette[4], text= "Your Wishlist")
        titleLabel.place(relheight=0.2 , relwidth=0.9 , relx=0.05 , rely=0.09)
        
        listeWishlist = tk.Listbox(leftframe, bg= palette[3],justify='center')
        listeWishlist.place(relheight=0.6 , relwidth=0.8 , relx=0.1 , rely=0.35)

        def searchlist(event=None):
            liste_item = tk.Variable(value= wlo.getwishlistname())
            listeWishlist.config(listvariable=liste_item)

        def openWishlist(event=None):
            nomliste = listeWishlist.get(listeWishlist.curselection())
            if nomliste:
                UpdateWishlist(nomliste)
                
        listeWishlist.bind("<Configure>", searchlist)
        listeWishlist.bind('<Double-1>', openWishlist)

    def RightFrame():
        global listeWishlist
        def creerWishlist():
            nom = entreeNom.get()
            if nom :
                wlo.Savewishlist(nom,[])
                listeWishlist.insert(tk.END,f'{nom}.txt')


        rightframe =tk.Frame(root, bg=palette[1])
        rightframe.place(relheight=0.5 , relwidth=0.35 ,relx=0.55, rely=0.4)

        topline  = tk.Frame(rightframe, bg=palette[0])
        topline.place(relheight=0.03 , relwidth=1 , relx=0, rely=0)

        botline  = tk.Frame(rightframe, bg=palette[0])
        botline.place(relheight=0.03 , relwidth=1 , relx=0, rely=0.97)

        titleLabel = tk.Label(rightframe, bg= palette[4], text= "New Wishlist")
        titleLabel.place(relheight=0.2 , relwidth=0.9 , relx=0.05 , rely=0.09)

        labelnom = tk.Label(rightframe,bg = palette[2], text='Nom de la wishlist')
        labelnom.place(relheight=0.13, relwidth=0.4, relx=0.3, rely=0.35)

        entreeNom = tk.Entry(rightframe, bg=palette[0])
        entreeNom.place(relheight=0.13 , relwidth=0.4, relx=0.3, rely=0.53)

        boutonValider = tk.Button(rightframe, bg= palette[2], activebackground=palette[1],text="Valider",command= creerWishlist)
        boutonValider.place(relheight=0.1, relwidth=0.3, relx=0.35, rely=0.7)

    TopFrame()
    LeftFrame()
    RightFrame()
    root.mainloop()

def UpdateWishlist(nom):
    global palette
    root = tk.Toplevel()  
    root.geometry("800x450+{}+{}".format(int(root.winfo_screenwidth()/2 - 400), int(root.winfo_screenheight()/2 - 225)))

    root.focus_set()
    root.resizable(False,False)
    root.title("Updatewishlist")
    root.bind('<Escape>',lambda e: root.destroy())
    root.configure(bg=palette[2])


    topframe = tk.Frame(root, bg= palette[0])
    topframe.place(relheight=0.1 , relwidth=1 , relx=0, rely=0.07)

    midline = tk.Frame(topframe, bg=palette[1])
    midline.place(relheight=0.1 , relwidth=1 , relx=0, rely=0.45)

    levelFrame = tk.Frame(topframe,bg=palette[0],height=10)
    levelFrame.pack(side="bottom" , fill='x')

    LabelTitre = tk.Label(topframe, bg=palette[0],text= f'Affichage et modification de {nom}',font=('actual',14),foreground=palette[3])
    LabelTitre.pack(side='bottom')
    
    topline  = tk.Frame(topframe, bg=palette[4])
    topline.place(relheight=0.1 , relwidth=1 , relx=0, rely=0)

    botline  = tk.Frame(topframe, bg=palette[4])
    botline.place(relheight=0.1 , relwidth=1 , relx=0, rely=0.9)

    def afficherliste(nom):
        try:
            t = wlo.openWishlist(nom)
            
            for i in range (0,len(t)):
                listUrl.insert(tk.END, t[i][0])
                listNom.insert(tk.END, t[i][1])
                listPrix.insert(tk.END, t[i][2])
        except:
            return 0
        
    def saving():
        """
            Objective:
                Turning the data from the 3 listbox into a list that can be used 
                this list will be read by the function in Wishlistopener that will save all correctly
        """
        liste_nom= listNom.get(0,tk.END)
        liste_url = listUrl.get(0,tk.END)
        liste_prix = listPrix.get(0,tk.END)

        element = []
        for i in range(len(liste_nom)):
            element.append([liste_url[i],liste_nom[i],liste_prix[i]])
        wlo.Savewishlist(nom[0:-4],element)

        saveButton.config(text= 'Saved !!!')

    def modification(typemodif):
        """
            Objective : show a pop up windows that allow us to add an element 
            or many 
        """
        addwindow = tk.Toplevel()  
        addwindow.geometry("400x250+{}+{}".format(int(addwindow.winfo_screenwidth()/2 - 200), int(addwindow.winfo_screenheight()/2 - 112)))
        addwindow.focus_set()
        addwindow.resizable(False,False)
        if typemodif == "adding":

            addwindow.title("Adding Elements")
        
        

        addwindow.bind('<Escape>',lambda e: addwindow.destroy())
        addwindow.configure(bg=palette[2])

        urlEntree = tk.Entry(addwindow)
        urlEntree.place(relheight=0.14 , relwidth=0.25, relx=0.05 , rely=0.4)

        nomEntree = tk.Entry(addwindow,textvariable='Nom')
        nomEntree.place(relheight=0.14 , relwidth=0.25,relx=0.375, rely=0.4)

        prixEntree = tk.Entry(addwindow)
        prixEntree.place(relheight=0.14 , relwidth=0.25,relx=0.70, rely=0.4)

        
        urlLabel = tk.Label(addwindow,text="Url",bg=palette[1])
        urlLabel.place(relheight=0.1 , relwidth=0.25, relx=0.05 , rely=0.29)

        nomLabel = tk.Label(addwindow,text='Nom',bg=palette[1])
        nomLabel.place(relheight=0.1 , relwidth=0.25,relx=0.375, rely=0.29)

        prixLabel = tk.Label(addwindow,text="Prix",bg=palette[1])
        prixLabel.place(relheight=0.1 , relwidth=0.25,relx=0.70, rely=0.29)


        def sendadding():

            nom = nomEntree.get()
            prix = prixEntree.get()
            url = urlEntree.get()

            if prix and nom and url :
                    
                listNom.insert(tk.END,nom)
                listPrix.insert(tk.END,url)
                listUrl.insert(tk.END,url)

                urlEntree.delete(0,tk.END)
                prixEntree.delete(0,tk.END)
                nomEntree.delete(0,tk.END)
                saving()

            else:
                return 0
            
        
        validerButton = tk.Button(addwindow,text='Ajouter',command=sendadding)
        validerButton.place(relheight=0.1 , relwidth=0.25 , relx=0.2 , rely=0.7)

        closeButton = tk.Button(addwindow,text='Quitter',command= addwindow.destroy)
        closeButton.place(relheight=0.1 , relwidth=0.25, relx=0.55, rely=0.7)

        if typemodif=='modify':
            addwindow.title("Modify Elements")
            validerButton.config(text='Modifier')
            
            urlLabel = tk.Label(addwindow,text=,bg=palette[1])
            urlLabel.place(relheight=0.1 , relwidth=0.25, relx=0.05 , rely=0.29)

            nomLabel = tk.Label(addwindow,text='Nom',bg=palette[1])
            nomLabel.place(relheight=0.1 , relwidth=0.25,relx=0.375, rely=0.29)

            prixLabel = tk.Label(addwindow,text="Prix",bg=palette[1])
            prixLabel.place(relheight=0.1 , relwidth=0.25,relx=0.70, rely=0.29)
        


    def deleting():
        #Essai 1:
        #   Faire un get anchor de chacun et detruirece l'element avec de l'id
        #Essai 2
        #   Faire un pop up demandant de doublecliquer sur un element pour le supr
        print("")
        
    #Adding the 3 listbox
    listUrl=  tk.Listbox(root, bg= palette[0],justify='center')
    listUrl.place(relheight=0.5 , relwidth=0.2 , relx=0.15 , rely= 0.22)

    listNom=  tk.Listbox(root, bg= palette[1],justify='center')
    listNom.place(relheight=0.5 , relwidth=0.2 , relx=0.4 , rely= 0.22)

    listPrix=  tk.Listbox(root, bg= palette[0],justify='center')
    listPrix.place(relheight=0.5 , relwidth=0.2 , relx=0.65 , rely= 0.22)


    #Adding the 3 bottom Button
    addButton = tk.Button(root,bg=palette[1],activebackground=palette[0], text='Add', command=adding)
    addButton.place(relheight=0.06, relwidth=0.12, relx=0.2, rely=0.8)

    deleteButton = tk.Button(root,bg=palette[0],activebackground=palette[1])
    deleteButton.place(relheight=0.06, relwidth=0.12, relx=0.45, rely=0.8)

    saveButton = tk.Button(root,bg=palette[1],activebackground=palette[0], command = saving, text='Save')
    saveButton.place(relheight=0.06, relwidth=0.12, relx=0.7, rely=0.8)
    
    #The expose binding allow us the show the wishlist when we call updateWishlist()
    root.bind("<Expose>", afficherliste(nom))

#The call of the function
if __name__ == "__main__":
    main()