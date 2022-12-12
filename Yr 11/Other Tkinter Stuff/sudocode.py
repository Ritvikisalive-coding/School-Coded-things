#begin
#declare an array to store 6 computer brands
#get array location
#display array location value
#end
#

computerBrand = ["IBM","Dell","Microsoft","Asus","Apple"]

x=int(input("Enter An array location: "))
x =computerBrand[x]


print("The selected location contains " + x)