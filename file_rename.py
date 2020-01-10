# Pythono3 code to rename multiple
# files in a directory or folder
# importing os module
import os

# Function to rename multiple files
def main():
    i = 0
    parent_dir = os.getcwd()
    j = 1
    dir_name = 'C:/Users/kumar_vaibhav/PycharmProjects/Object_Detection/Images/'
    for filename in os.listdir(dir_name):
        # print(filename)
        src = "NoObject" + str(i) + ".jpg"
        dst = "test" + str(j) + ".jpg"

        # dst = 'xyz' + dst

        # rename() function will
        # rename all the files
        os.rename(os.path.join(dir_name,filename),os.path.join(dir_name,dst))
        # os.rename(os.path.join(dir_name, src), os.path.join(dir_name, dst))
        i += 2
        j += 1
    print("File rename done.")


# Driver Code
if __name__ == '__main__':
    # Calling main() function
    main()