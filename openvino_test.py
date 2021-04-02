import numpy as np
import cv2
import math

img = cv2.imread('/Users/krishnasagarreddy/images/clearqrcodes/d3.png')


def func_code(th2, max_Radius, j1):
        circles = cv2.HoughCircles(th2 ,cv2.HOUGH_GRADIENT,2,max_Radius,
                                    param1=50,param2=j1,minRadius=int(max_Radius/2),maxRadius=int(max_Radius))
                                    #circles = np.uint16()

        k=0
        #cv2.waitKey(1000)
        font = cv2.FONT_HERSHEY_SIMPLEX
        if(circles is not None):
            pass
        else:
            #if( j1 == 35):
            print (" nocircles found for l =", l, "j1=", j1)
                #red_flag = 1

            return -3
        #print "    circles    =    ", circles
        circles = np.uint16(np.around(circles))
        #if(!circles.any())
        if 'circles' in globals() and circles.any():
        #if circles or circles.any() :
            #circles = np.uint16(np.around(circles))
            for i in circles[0,:]:
                # draw the outer circle
                #cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),1)
                # draw the center of the circle
                #cv2.circle(img,(i[0],i[1]),2,(0,0,255),1)
                arr_circle[k]=(i[0],i[1],i[2])
                #print i, k, arr_circle[k]
                #cv2.putText(img,str(k),(i[0],i[1]), font, 1,(255,255,255),1,cv2.LINE_AA)
                
                if (k==0):
                    avg_rad = i[2]
                    print( "k=",k,"avg_rad= ", avg_rad)
                else:
                    print( "k=",k,"avg_rad= ", avg_rad)
                    avg_rad = (avg_rad+i[2])/2
                    # reduce parameter to increase circles
                if(k > 27):
                    del circles
                    return -3
                k=k+1
        del circles
        print ("k=",k,"j1 =", j1,"l=",l, "max_Radius=", max_Radius)
#cv2.waitKey(5000)
        dist= dist1= dist2= greater= circle1= circle2 = np.uint32((0))
            #if( (k>27) ):
#continue
        if(k<3):
            return -3
 
        # find outer diagonal two outer circles
        for i in range(0,k-1):
            for j in range(i+1,k):
                if(arr_circle[i][0]>arr_circle[j][0]):
                    dist1 = arr_circle[i][0]-arr_circle[j][0]
                else:
                    dist1 = arr_circle[j][0]-arr_circle[i][0]

                if(arr_circle[i][1]>arr_circle[j][1]):
                    dist2 = arr_circle[i][1]-arr_circle[j][1]
                else:
                    dist2 = arr_circle[j][1]-arr_circle[i][1]

                dist = math.pow( (math.pow(dist1 , 2) + math.pow(dist2 , 2)),0.5)
             
                if(dist > greater):
                    greater = dist
                    circle1 = i
                    circle2 = j
                #print dist,greater, circle1,circle2,'next',

        print ("Largest distance between two circles in whole image", arr_circle[circle1][0],arr_circle[circle1][1],circle1,arr_circle[circle2][0],arr_circle[circle2][1],circle2)

        greater = average= dist1= dist2=  dist_c1= dist_c2 = great_dist1 = great_dist2 = great_dist3 =circle3 = x3 = y3 = 0

        # find 3rd outer circle and distance
        for i in range(0,k):
            if((i == circle1) or (i == circle2)):
                continue
            else:
                if(arr_circle[i][0]>arr_circle[circle1][0]):
                    dist1 = arr_circle[i][0]-arr_circle[circle1][0]
                else:
                    dist1 = arr_circle[circle1][0]-arr_circle[i][0]

                if(arr_circle[i][1]>arr_circle[circle1][1]):
                    dist2 = arr_circle[i][1]-arr_circle[circle1][1]
                else:
                    dist2 = arr_circle[circle1][1]-arr_circle[i][1]

                dist_c1 = math.pow( (math.pow(dist1 , 2) + math.pow(dist2 , 2)),0.5)
            

                if(arr_circle[i][0]>arr_circle[circle2][0]):
                    dist1 = arr_circle[i][0]-arr_circle[circle2][0]
                else:
                    dist1 = arr_circle[circle2][0]-arr_circle[i][0]

                if(arr_circle[i][1]>arr_circle[circle2][1]):
                    dist2 = arr_circle[i][1]-arr_circle[circle2][1]
                else:
                    dist2 = arr_circle[circle2][1]-arr_circle[i][1]

                dist_c2 = math.pow( (math.pow(dist1 , 2) + math.pow(dist2 , 2)),0.5)

            average = (dist_c1+dist_c2)/2
            if(average >greater):
                greater = average
                circle3 = i
                great_dist1 = dist_c1
                great_dist2 = dist_c2
            
        #    print " dist between circles ", dist_c1,dist_c2
        # To find 3rd circle is in right angle to other two

        print ("distance from main circle to 1st circle great_dist1 ", great_dist1, " 2nd circle great_dist2",great_dist2, "great_dist2*1.1", great_dist2*1.1, "great_dist2 * 0.9",  great_dist2*0.9)

        if( (great_dist1 < great_dist2*1.1)and (great_dist1 > great_dist2*0.9)) :
            print ("inside first loop +ve if great_dist1", great_dist1, "great_dist2", great_dist2)
            #cv2.waitKey(2000)
            pass
        else:
            print( " in  first  loop -ve")
            return -3

        # center of bigger outer two circles
        x3 = (arr_circle[circle1][0] + arr_circle[circle2][0])/2
        y3 = (arr_circle[circle1][1] + arr_circle[circle2][1])/2
        print ("x3", x3, "y3",y3)

        # Distance between center and 3rd circle
        if(arr_circle[circle3][0]>x3):
            dist1 = arr_circle[circle3][0]-x3
        else:
            dist1 = x3-arr_circle[circle3][0]
                
        if(arr_circle[circle3][1]>y3):
            dist2 = arr_circle[circle3][1]-y3
        else:
            dist2 = y3-arr_circle[circle3][1]
        
        great_dist3 = math.pow( (math.pow(dist1 , 2) + math.pow(dist2 , 2)),0.5)

        print ("Distance between main circle to center of two largest circles great_dist3=",great_dist3,"great_dist3*1.414=",great_dist3*1.414,"great_dist3*1.1*1.41",great_dist3*1.1*1.41, "great_dist3*0.9*1.41",great_dist3*0.9*1.41)

        if( (great_dist1 < great_dist3*1.05*1.414) and (great_dist1 > great_dist3*0.95*1.414)) :
            print (" in  secound loop +ve")
            pass
        else:
            print (" in  secound loop -ve")
            return -3
        #cv2.imshow('image',img)
        #cv2.waitKey(3000)
        greater = np.uint32((greater))
        print ("circle 3 =",circle3,arr_circle[circle3][0],arr_circle[circle3][1],"greater =",greater)

        # find points to rotate

        temp= v1=v2=v3=v4 = np.uint16((0))

        if(arr_circle[circle1][0]>arr_circle[circle3][0]):
            #dist1 = arr_circle[circle1][0]-arr_circle[circle3][0]
            v1 = 1
        else:
            #dist1 = arr_circle[circle3][0]-arr_circle[circle1][0]
            v1 = 0

        if(arr_circle[circle1][1]>arr_circle[circle3][1]):
            dist1 = arr_circle[circle1][1]-arr_circle[circle3][1]
            v2 = 1
        else:
            dist1 = arr_circle[circle3][1]-arr_circle[circle1][1]
            v2 = 0

        if(arr_circle[circle2][0]>arr_circle[circle3][0]):
            #dist1 = arr_circle[circle2][0]-arr_circle[circle3][0]
            v3 = 1
        else:
            #dist1 = arr_circle[circle3][0]-arr_circle[circle2][0]
            v3 = 0

        if(arr_circle[circle2][1]>arr_circle[circle3][1]):
            dist2 = arr_circle[circle2][1]-arr_circle[circle3][1]
            v4 = 1
        else:
            dist2 = arr_circle[circle3][1]-arr_circle[circle2][1]
            v4 = 0

        if(v1==0 and v2==0):
            if(v3==0 and v4==1):
                pass
            if(v3==1 and v4==0):
                temp = circle1
                circle1=circle2
                circle2 = temp
            if(v3==0 and v4==0):
                pass
            if(dist1>dist2):
                pass
            else:
                temp = circle1
                circle1=circle2
                circle2 = temp


        if(v1==0 and v2==1):
            if(v3==1 and v4==1):
                pass
            if(v3==0 and v4==0):
                temp = circle1
                circle1=circle2
                circle2 = temp
            if(v3==0 and v4==1):
                if(dist1<dist2):
                    pass
                else:
                    temp = circle1
                    circle1=circle2
                    circle2 = temp


        if(v1==1 and v2==0):
            if(v3==0 and v4==0):
                pass
            if(v3==1 and v4==1):
                temp = circle1
                circle1=circle2
                circle2 = temp
            if(v3==1 and v4==0):
                if(dist1<dist2):
                    pass
                else:
                    temp = circle1
                    circle1=circle2
                    circle2 = temp


        if(v1==1 and v2==1):
            if(v3==1 and v4==0):
                pass
            if(v3==0 and v4==1):
                temp = circle1
                circle1=circle2
                circle2 = temp
            if(v3==1 and v4==1):
                if(dist1>dist2):
                    pass
                else:
                    temp = circle1
                    circle1=circle2
                    circle2 = temp


        #do rotation transform

        rows,cols,ch = img.shape
        print ("rows=",rows,"cols", cols)

        pts1 = np.float32([[arr_circle[circle1][0],arr_circle[circle1][1]],[arr_circle[circle3][0],arr_circle[circle3][1]],[arr_circle[circle2][0],arr_circle[circle2][1]]])
        pts2 = np.float32([[0,greater],[0,0],[greater,0]])

        M = cv2.getAffineTransform(pts1,pts2)

        dst = cv2.warpAffine(img,M,(cols,rows))
        
        print( " avg_rad= ",avg_rad, "greater = " , greater)
        pts1 = np.float32([[avg_rad,(greater)],[avg_rad,avg_rad],[greater,avg_rad]])
        pts2 = np.float32([[0,(greater-avg_rad)],[0,0],[(greater-avg_rad),0]])
        #pts2 = np.float32([[0,(avg_rad*)],[0,0],[(greater-avg_rad),0]])

        M = cv2.getAffineTransform(pts1,pts2)

        dst = cv2.warpAffine(dst,M,(int(greater-avg_rad*2),int(greater-avg_rad*2)))
        #dst = cv2.warpAffine(dst,M,(rows,cols))


        return dst


def circle_count(dst,th3, max_Radius, j1):

        count_1 = count_0 = 0
        rows1,cols1,ch = dst.shape
        #cv2.imshow('test',th3)
        #cv2.waitKey(5000)
        circles = cv2.HoughCircles(th3 ,cv2.HOUGH_GRADIENT,2,max_Radius,
                                    param1=50,param2=j1,minRadius=int(max_Radius/2),maxRadius=int(max_Radius))
        if(circles is not None):
            pass
        else:
            
            print ("bottom half no circles found for l =", l, "j1=", j1)
            return -3
        circles = np.uint16(np.around(circles))
        k=1
        count_1 = count_0 = 0
        font = cv2.FONT_HERSHEY_SIMPLEX
        avg_radius = 0
        #circles = np.uint16()
        #if circles is not None:
        if 'circles' in globals() and circles.any():
        #if circles or circles.any() :
        #circles = np.round(circles[0, :]).astype("int")
            for i in circles[0,:]:
                # draw the outer circle
                cv2.circle(dst,(i[0],i[1]),i[2],(0,255,0),1)
                # draw the center of the circle
                #cv2.circle(dst,(i[0],i[1]),2,(0,0,255),1)
                arr_circle[k]=(i[0],i[1],i[2])
                if(k>28):
                    print ("here k should not be greater than 28 ")
                    
                    return -3
                if(k==1):
                    avg_radius = i[2]
                else :
                    avg_radius= (avg_radius+i[2])/2
                print (i, k, arr_circle[k])
                #cv2.putText(dst,str(k),(i[0],i[1]), font, 1,(255,255,255),1,cv2.LINE_AA)
                k=k+1
        # find offset to find blocks where circles are there
        print (" in secound half k = ", k)
        del circles
        if( k>25 ):
            return -3
        offset1 = rows1/6
        offset= rows1/6
        offset1 = (rows1-12*avg_radius)/7 + avg_radius*1.85
        offset = 44
        print ("offset1=",offset1, "k=",k)
        #cv2.waitKey(4000)
        x_offset= y_offset = flag= 0
        for j in range(1,7):
            for i in range(1,7):
                for m in range(1,k):
                    if(i==1 or j==1):
                        offset = offset1 #- (rows1-12*avg_radius)/7
                    else :
                        offset =offset1
                    x_offset= y_offset = 0
                    if( arr_circle[m][0] < (max_Radius/2)):
                        pass
                    if(arr_circle[m][1] <(max_Radius/2)):
                        pass
                    if((i*offset)>arr_circle[m][0]):
                        x_offset=(i*offset)-arr_circle[m][0]
                    else:
                        x_offset=arr_circle[m][0]-(i*offset)
                    if((j*offset)>arr_circle[m][1]):
                        y_offset=(j*offset)-arr_circle[m][1]
                    else:
                        y_offset=arr_circle[m][1]-(j*offset)

                    #print i, j, k,m, x_offset, y_offset,i*offset, arr_circle[m][0],j*offset, arr_circle[m][1]
                    if(((x_offset+y_offset)/2) < (max_Radius/2)):
                        cv2.putText(dst,str(1),(arr_circle[m][0],arr_circle[m][1]), font, 1,(255,255,255),1,cv2.LINE_AA)
                        print( 1,)
                        flag = m
                        count_1=count_1+1
                if(flag==0):
                    cv2.putText(dst,str(0),(int(float(i*offset)), int(float(j*offset))), font, 1,(255,255,255),1,cv2.LINE_AA)
                    print( 0,)
                    count_0 = count_0 + 1
                flag =0
            print (' ')
        
        #if((count_0 + count_1) == 25):
#   pass
#       else:
#           continue

#       if(count_0 == 25):
#           continue
        if(count_1 == 9):
            print ("count_1=",count_1," is equal to 9 for 8.jpg 16 for 20.jpg !!!!!")
            
            
            cv2.imshow('Output',dst)
            cv2.waitKey(5000)
            cv2.destroyWindow('Output')

           
        else:
            print ("count_1=",count_1," ERROR is not equal to 9 for 8.jpg 16 for 20.jpg !!!!!")
            cv2.imshow('Output',dst)
            #cv2.waitKey(3000)
            cv2.destroyWindow('Output')
            return -3


#first find outer circles and do rotation affine transformation
w,h = 30,3

arr_circle=np.uint32(np.zeros((w,h)))


#img = cv2.imread('/Users/krishnasagarreddy/images/clearqrcodes/8.jpg')
img1=img.copy()
rows,cols,ch = img1.shape

if(rows<cols):
    max_Radius=rows/17
else:
    max_Radius=cols/17


radius_range = max_Radius - 3

print ("rows, cols, max_Radius", rows, cols, max_Radius, "radius_range",radius_range)

#img = cv2.medianBlur(img1, 3)
gray  = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#th2 = gray.copy()

th2 = cv2.Canny(gray,50,200)
arr=[0 for i in range(100)]
#arr=[]
#circles = np.uint16()
red_flag = 0
font = cv2.FONT_HERSHEY_SIMPLEX

circles =0



for l in range(1,int(radius_range)):
    max_Radius = max_Radius - 1
    
    #max_Radius=35
    #if(red_flag == 1):
    #   print "in red_flag max_radius=", max_Radius, "l", l
    #  red_flag = 0
    # continue
    for j1 in range(20,80):
        print ("j1=",j1)
        ret_dst = func_code(th2,max_Radius,j1)
        if(ret_dst is not -3 ):
            cv2.imshow('Output2',ret_dst)
            #cv2.waitKey(5000)
            rows1,cols1,ch = ret_dst.shape
            
            if(rows1<cols1):
                max_Radius1=rows1/12
            else:
                max_Radius1=cols1/12

            gray  = cv2.cvtColor(ret_dst,cv2.COLOR_BGR2GRAY)
            th3 = cv2.Canny(gray,50,200)
            circle_count(ret_dst,th3,max_Radius1,j1)
        else:
            continue
#cv2.imshow('gray',gray)
#cv2.imshow('th2_thresh', th2)

#cv2.imshow('Input',img)
print (" see output2")
#cv2.imshow('Output2',ret_dst)
#cv2.waitKey(7000)

cv2.destroyAllWindows()
#cv2.waitKey(3000)

