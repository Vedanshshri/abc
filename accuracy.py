import os

f=open('/model_files/accuracy.txt')
content=f.read()
accuracy=int(content[-47:-45])
print("Accuracy is ",accuracy)
if accuracy < 80:
	print("Accuracy is less than 80 Running Hyper Parameter File")
	os.system("python3 /model_files/code_changer.py")
        os.system("python3 /model_files/model.py")
else:
	print("Just got the Accuracy Greater Than 80 [Accuracy :- {}]".format(accuracy))