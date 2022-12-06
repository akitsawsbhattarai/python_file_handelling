import json

class User():
    def __init__(self):
        self.id = ""
        self.fname=""
        self.lname=""
        self.DOB=""
        self.address=""
        self.phoneNumber=""
    
    # encapsulation=> binding data to method for securing
    def set_id(self, id):
        self.id = id
    
    def get_id(self):
        return self.id 
    
    def set_fname(self, fname):
        self.fname = fname
    
    def get_fname(self):
        return self.fname 
    
    def set_lname(self, lname):
        self.lname = lname
    
    def get_lname(self):
        return self.lname 
    
    def set_DOB(self, DOB):
        self.DOB = DOB
    
    def get_DOB(self):
        return self.DOB 
    
    def set_address(self, address):
        self.address = address
    
    def get_address(self):
        return self.address 
    
    def set_phoneNumber(self, phoneNumber):
        self.phoneNumber = phoneNumber
    
    def get_phoneNumber(self):
        return self.phoneNumber 
    
    def __str__(self) -> str:
        name = self.fname + " " + self.lname
        return name
    
    
        

def menu():
    menu = ['1 : View all students', '2 : Search students by ID', '3 : Insert students', '4 : Delete students', '5 : Export to csv', '6 : RETURN']
    for m in menu :
        print(m)
        
class Student(User):
    def __init__(self):
        super().__init__()
        
    def __str__(self) -> str:
        return super().__str__()
        
    
while True:
    students_detail = Student()
    no_id = True
    menu()
    number = int(input('Please select any to proceed...\n'))
    
    if number == 1:
        
        with open('students.json', 'r+') as studentfile:
            data = studentfile.readlines()
            for d in data:
                print(d)
            
      
    
    elif number == 2:
        id = (input("Provide Id of student \n"))
        
        with open('students.json', 'r+') as studentfile:
            datas = studentfile.read()
            data = list(json.loads(datas))
            for d in data:
                # print(d['id'])
                if id == d['id']:
                    no_id = False
                    print(d)
        if no_id:
            print('not found..')
        
        
            
    elif number == 3:
        while True:
            if not students_detail.get_id():
                id = students_detail.set_id(input('id = '))
                continue
            
            if not students_detail.get_fname():
                students_detail.set_fname(input('fname :  '))
                continue
        
            if not students_detail.get_lname():
                students_detail.set_lname(input('lname :  '))
                continue
        
            if not students_detail.get_DOB():
                students_detail.set_DOB(input('DOB :  '))
                continue
        
            if not students_detail.get_address():
                students_detail.set_address(input('address :  '))
                continue
        
            if not students_detail.get_phoneNumber():
                students_detail.set_phoneNumber(input('phoneNumber :  '))
                continue
            
            break
          
        # print(students_detail.__dict__)
        data = students_detail.__dict__    
        
        with open("students.json", "r+") as file:
            filedata = file.read()
            datafromdb =list( json.loads(filedata))
            # print(datafromdb)
            
            
        datafromdb.append(data)
        # print(datafromdb)
        json_object = json.dumps(datafromdb)
        
        with open("students.json", "w+") as file:
            file.write(json_object)
       
        
        print('Sucessfully registered !!')
        print('-------------------------------')
        
        
    elif number == 4:
        id = (input("Provide Id of student you want to delete \n"))
        
        with open('students.json', 'r+') as studentfile:
            students_file = studentfile.read()
            students_list = list(json.loads(students_file))
            for index,s in enumerate(students_list):
                if id == s['id']:
                    print(s)
                    no_id = False
                    
                    confirm = input('Are you sure you want to delete it? y/n \n')
                    if confirm == "y":
                        students_list.pop(index)
                        print('deleted...')
                        
                        json_object = json.dumps(students_list)
                        with open('students.json', 'w+') as studentfile:
                            studentfile.write(json_object)
                        
                    elif confirm == "n":
                        break
            if no_id:
                print('not found..')    
    
    elif number == 5:
      
        with open ('students.json', 'r+') as file:
            datafile = file.read()
            dataforcsv = (json.loads(datafile))
  
        with open('students.csv', 'w+') as csvfile: 
              
            for dat in dataforcsv:
                tmp = "" 
                tmp += ",".join(dat.values())+'\n'
                print(tmp)
                csvfile.write(tmp)

        with open('students.csv', 'r+') as csvfile:
            csv_data = csvfile.readlines() 
            print(csv_data)
              
        
    elif number == 6:
        break
        
             
    else:
            print('please provide valid response')   
           