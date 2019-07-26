# General documentation
For the project, I used tensorflow object detection API on Rpi, with the help of openCV for visualisation. 
For other resources like images, train and test record, model files etc, please visit the GDrive link
https://drive.google.com/drive/folders/1mzldgopL2Ulk414s0cHEtUbpGnOLbjDJ?usp=sharing

# Step 1:
Setting up - environment and hardware

Download tensorflow and openCV onto Rpi. 
Afterthought: Was actually harder than I thought because need to compile protocol buffer, protobuf.

Download tensorflow and openCV onto my laptop

Decided on using Single-Shot Multi-box Detector algo. 
I chose a pre-trained model provided by the tensorflow model zoo. This is because my hardware is limited, 
thus I believe this approach would be more efficient. The particular model I chose is SSDlite MobileNet v2 coco.
The accuracy of the model is not the highest. I actually tested out FasterR CNN as well. However this would result in slower FPS when running real time on the pi. Hence upon consideration, I decided on a balance of accurracy and speed by choosing SSDlite MobileNet V2. 

Set up Pi hardware, some of the components are:
  Rpi
  Pi hat
  USB camera
  jumpers
  Motors
  Battery
  CAD custom outershell and trailer, which we 3D printed

# Step 2:
Preparation of training Data. 

Even with a pre-trained model, I still need to unfreeze end neurons to be trainable. 
I took over hundreds of images for training. I then labelled them manually. 
I split them into training set and test set in a 80% to 20% respectively
I passed the images and xml files into the neural network for training. 
After that, I saved a model ckpt file, which I will then use to load onto my Rpi.

# Step 3:
Linking up with Rpi

I then transferred my model files and labelmap onto Rpi.
A few scripts needs to be written/modified:
  1. Pi movement script. This is to interface the GPIOs, which i will put in the Utils directory
  2. Pi main script to load model into memory and use openCV to visualise results
  3. Need to go into Utils directory to modify the visualization_utils.py file to insert movement logic code.
     This way, the movement code will directly be tied to visualisation. If code was executed with display, 
     can see the openCV boxes. However, we are executing in headless situation, thus we will only print to console. 
 
 General logic : 
 If obstacle/bottle is detected, pivot away
 if robot(master) detected, move towards it. 

