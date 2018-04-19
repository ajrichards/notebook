import shutil,os,re,sys

## get the home directory
home_dir = os.path.expanduser('~')
data_dir = os.path.join(home_dir,'data')
print("my data directory is: {}".format(data_dir))

## demonstrate how to check if a directory exists
data_dir_1 = os.path.join(home_dir,'sandbox')
data_dir_2 = os.path.join(home_dir,'foo')

if os.path.isdir(data_dir_1):
    data_dir = data_dir_1
else:
    data_dir = data_dir_2

print("my data directory is: {}".format(data_dir))

sys.exit()

## to check if a file exists use os.path.exists
print(os.path.exists(os.path.join(home_dir,"foo.txt")))

for file_name in os.listdir(data_dir):
    file_path = os.path.join(data_dir,file_name)
    if re.search("zip",file_name):
        print(file_name)
        print(file_path)

## create a directory
some_dir = os.path.join(home_dir,'figures')
if not os.path.isdir(some_dir):
    os.mkdir(some_dir)

## copy a directory
#shutil.copy(src_path, dest_path)
