
maktaba_books=["kitab al taweheed","bulugh al maram","the sealed nector"]

initial_count= len(maktaba_books)
print("current library scale:","initial_count,classical volumes")

maktaba_books.append("stories of prophet")
updated_count=len(maktaba_books)

if updated_count>=4:
    print("maktaba expansion milestone achived! shelf capacity increasing up.")
    
else:
    print ("keep gathering classical volumes")

