def unlu_sayan(cumle, output= 0):
    unluler = "aeiıoöuüAEIİOÖUÜ"
    for char in cumle:
        if char in unluler:
            output +=1
    return output
    
cumle = input("Bir cümle yaz: ")
print("Cümlede yer alan ünlü sayısı: {}".format(unlu_sayan(cumle)))