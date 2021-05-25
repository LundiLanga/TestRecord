class RecordMarks:

    def accept_studNo(self):
        self.StudentNmbr = input("Faka amanani omfundi wakho")
        return self.StudentNmbr


    def accept_test1(self):
         self.Test1 = float(input("Faka amanqaku wakho ovavanyo lokuqala"))
         return self.Test1


    def accept_test2(self):
        self.Test2 = float(input("Faka amanqaku wakho ovavanyo lwesibini"))
        return self.Test2


    def accept_test3(self):
        self.Test3 = float(input("Faka amanqaku wakho ovavanyo lwesithathu"))
        return self.Test3


    def accept_exam(self):
        self.exam = float(input("Faka amanqaku wakho wemviwo zokuphela konyaka"))
        return self.exam


R = RecordMarks()

dp = (R.accept_test1() + R.accept_test2() + R.accept_test3()) / 3
FinalMark = (0.6 * R.accept_exam() + (0.4 * dp))
print(" amanqaku owafumene phakathi konyaka ewonke", dp)
print("Amanqaku owafumene ekupheleni konyaka", FinalMark)
