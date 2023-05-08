# Python program to explain cv2.line() method  
   
# importing cv2  
import cv2  
   
# path  
path = r'C:\Users\Rajnish\Desktop\geeksforgeeks\geeks.png'
   
# Reading an image in default mode 
image = cv2.imread(path) 
   
# Window name in which image is displayed 
window_name = 'Image'
  
# Start coordinate, here (0, 0) 
# represents the top left corner of image 
start_point = (0, 0) 
  
# End coordinate, here (250, 250) 
# represents the bottom right corner of image 
end_point = (250, 250) 
  
# Green color in BGR 
color = (0, 255, 0) 
  
# Line thickness of 9 px 
thickness = 9
  
# Using cv2.line() method 
# Draw a diagonal green line with thickness of 9 px 
image = cv2.line(image, start_point, end_point, color, thickness) 
  
# Displaying the image  
cv2.imshow(window_name, image)
————————————————
版权声明：本文为CSDN博主「Mr.小蔡」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/weixin_42228294/article/details/124109458
