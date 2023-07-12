import tkinter as tk
import Wishlistopener as wlo

palette = ["#16697A","#489FB5","#82C0CC","#EDE7E3","#FFA62B"]

def main():
    global palette

    root = tk.Tk()  
    root.geometry("800x450+{}+{}".format(int(root.winfo_screenwidth()/2 - 400), int(root.winfo_screenheight()/2 - 225)))

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
        leftframe =tk.Frame(root, bg=palette[1])
        leftframe.place(relheight=0.5 , relwidth=0.35 ,relx=0.1 , rely=0.4)

        topline  = tk.Frame(leftframe, bg=palette[0])
        topline.place(relheight=0.03 , relwidth=1 , relx=0, rely=0)

        botline  = tk.Frame(leftframe, bg=palette[0])
        botline.place(relheight=0.03 , relwidth=1 , relx=0, rely=0.97)

        titleLabel = tk.Label(leftframe, bg= palette[4], text= "Your Wishlist")
        titleLabel.place(relheight=0.2 , relwidth=0.9 , relx=0.05 , rely=0.09)
        
        listeWishlist = tk.Listbox(leftframe, bg= palette[3])
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
        rightframe =tk.Frame(root, bg=palette[1])
        rightframe.place(relheight=0.5 , relwidth=0.35 ,relx=0.55, rely=0.4)

        topline  = tk.Frame(rightframe, bg=palette[0])
        topline.place(relheight=0.03 , relwidth=1 , relx=0, rely=0)

        botline  = tk.Frame(rightframe, bg=palette[0])
        botline.place(relheight=0.03 , relwidth=1 , relx=0, rely=0.97)

        titleLabel = tk.Label(rightframe, bg= palette[4], text= "New Wishlist")
        titleLabel.place(relheight=0.2 , relwidth=0.9 , relx=0.05 , rely=0.09)
    

    TopFrame()
    LeftFrame()
    RightFrame()
    root.mainloop()

def UpdateWishlist(nom):
    global palette

    root = tk.Toplevel()  
    root.geometry("800x450+{}+{}".format(int(root.winfo_screenwidth()/2 - 400), int(root.winfo_screenheight()/2 - 225)))

    root.resizable(False,False)
    root.title("Updatewishlist")
    root.bind('<Escape>',lambda e: root.destroy())
    root.configure(bg=palette[2])

    def afficherliste(nom):
        print(nom)
        t = wlo.openWishlist(nom)
        try:
            for i in range (len(t)):
                listUrl.insert(tk.END, t[i][0])
                listNom.insert(tk.END, t[i][1])
                listPrix.insert(tk.END, t[i][2])
        except:
            return 0

    listUrl=  tk.Listbox(root, bg= palette[3])
    listUrl.place(relheight=0.6 , relwidth=0.2 , relx=0.1 , rely= 0.2)

    listNom=  tk.Listbox(root, bg= palette[3])
    listNom.place(relheight=0.6 , relwidth=0.2 , relx=0.4 , rely= 0.2)

    listPrix=  tk.Listbox(root, bg= palette[3])
    listPrix.place(relheight=0.6 , relwidth=0.2 , relx=0.7 , rely= 0.2)

    root.bind("<Expose>", afficherliste(nom))


if __name__ == "__main__":
    main()