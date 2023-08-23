from os import listdir
import cv2

# C:\Users\HP\Desktop\fingerprint\SOCOFing\Altered\Altered-Easy\1__M_Left_index_finger_CR
#opening the finger print to test


#None == NULL
filename = None
image = None
kp1, kp2, mp = None, None, None
fingerPrintS = []
sift = cv2.SIFT_create()


#only crating an aray of files names not opening them
for pic in [pic for pic in listdir("C:/Users/TROY/Desktop/finger/SOCOFing/Real")]:
#        print(i , s, best_score)
    #just printing
    #reading the pic to comare to
    fingerprint_Image = cv2.imread("C:/Users/TROY/Desktop/finger/SOCOFing/Real/" + pic)
    #getting the keyPoints
    keyPoints_2, descriptors_2 = sift.detectAndCompute(fingerprint_Image, None)
    fingerPrintS.append({"keyPoints": keyPoints_2, "descriptors" :  descriptors_2, "name" : pic})



    #C:/Users/TROY/Desktop/finger/SOCOFing/Real/1__M_Left_index_finger

s = 0
while s != "exit":
    i = 0
    s = input("file Path: ")
    # ref = open("C:/Users/TROY/Desktop/finger/SearchFingerPrint.txt","a") 
    try:
        test =  cv2.imread(s +".BMP")
        Resoult = open("C:/Users/TROY/Desktop/finger/Resoult.txt","w")

        keyPoints_1, descriptors_1 = sift.detectAndCompute(test, None)


        best_score = 0

        for fingerPrint in fingerPrintS:
                #getting matches if any
                matches = cv2.FlannBasedMatcher({'algorithm': 1, 'trees': 5}, {}).knnMatch(descriptors_1, fingerPrint["descriptors"], k=2)

                match_points = []

                #adding the matches
                for first, second in matches:
                    if first.distance < 0.1 * second.distance:
                        match_points.append(first)
                    keyPoints = 0

                #asigning the number of key points to the number of keyoints in the oicter with lest keyPoints
                if len(keyPoints_1) < len(fingerPrint["keyPoints"]):
                    keyPoints = len(keyPoints_1)
                else:
                    keyPoints = len(fingerPrint["keyPoints"])


                #if fund a new best match save it
                if len(match_points) / keyPoints * 100 > best_score:
                    best_score = len(match_points) / keyPoints * 100
                    filename = fingerPrint["name"]
                    # image = fingerprint_Image
                    kp1, kp2, mp = keyPoints_1, fingerPrint["keyPoints"], match_points
                
                if best_score > 50 :
                    print(best_score , fingerPrint["name"])
                    break
    except :
        pass


#printing the last reasults
    if filename == None:
        Resoult.write("No Matche found")
    else:
        Resoult.write("Best Match: " + filename)
        Resoult.write("  Score: " + str(best_score))
    Resoult.close()
    # ref.close()
