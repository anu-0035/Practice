
using System.IO.Compression;

namespace helloApp
{

    public class Employee{
        private int _id = 0;
        private string _name = string.Empty;
        private string _department = string.Empty;
        private float _salary = 0.0f;
        private char _gender = 'M';

        private bool _status = true;


        public int Id
        {
            get
            {
                return _id;
            }
            set
            {
                _id = value;
            }
        }
        public string Name
        {
            get
            {
                return _name;
            }
            set
            {
                _name = value;
            }
        }

        public string Department
        {
            get
            {
                return _department;
            }
            set
            {
                _department = value;
            }
        }

        public float Salary
        {
            get
            {
                return _salary;
            }
            set
            {
                _salary = value;
            }
        }
        public char Gender
        {
            get
            {
                return _gender;
            }
            set
            {
                _gender = value;
            }
        }

        public bool Status
        {
            get
            {
                return _status;
            }
            set
            {
                _status = value;
            }
        }
        public void AcceptDetails(){
            Console.WriteLine("Enter Employee details : ");

            Console.WriteLine("Enter the Id : ");
            Id = int.Parse(Console.ReadLine());

            Console.WriteLine("Enter the Name : ");
            Name = Console.ReadLine();

            Console.WriteLine("Enter the Department : ");
            Department = Console.ReadLine();
            
            Console.WriteLine("Enter the Salary : ");
            Salary = float.Parse(Console.ReadLine()); // Conver.ToSingle()


            Console.WriteLine("Enter the Gender : ");
            Gender = char.Parse(Console.ReadLine());

            Console.WriteLine("Enter the Status : ");
            Status = bool.Parse(Console.ReadLine());
        }

        public void DisplayDetails(){

            Console.WriteLine("-------------- Employee Deatils ------------");
            Console.WriteLine($"Employee Id: {Id}");
            Console.WriteLine($"Employee Name: {Name}");
            Console.WriteLine($"Employee Department: {Department}");
            Console.WriteLine($"Employee Salary: {Salary}");
            Console.WriteLine($"Employee Gender: {Gender}");
            Console.WriteLine($"Employee status: {Status}");

        }


    }

    public class Student
    {
        private int _id = 0;
        private string _name = string.Empty;
        private int _m1 = 0;
        private int _m2 = 0;
        private int _m3 = 0;
        private int _m4 = 0;
        private int _m5 = 0;
        private int _m6 = 0;

        public int Total = 0;
        public float Avg = 0.0f;
        public string Result = "Pass";
    

        public int Id
        {
            get
            {
                return _id;
            }
            set
            {
                _id = value;
            }
        }

        public string Name
        {
            get
            {
                return _name;
            }
            set
            {
                _name = value;
            }
        }

        public int M1
        {
            get
            {
                return _m1;
            }
            set
            {
                _m1 = value;
            }
        }

        public int M2
        {
            get
            {
                return _m2;
            }
            set
            {
                _m2 = value;
            }
        }

        public int M3
        {
            get
            {
                return _m3;
            }
            set
            {
                _m3 = value;
            }
        }

        public int M4
        {
            get
            {
                return _m4;
            }
            set
            {
                _m4 = value;
            }
        }

        public int M5
        {
            get
            {
                return _m5;
            }
            set
            {
                _m5 = value;
            }
        }

        public int M6
        {
            get
            {
                return _m6;
            }
            set
            {
                _m6 = value;
            }
        }

        public void set_total()
        {
            Total = M1 + M2 + M3 + M4 + M5 + M6;

        }

        public void set_Avg()
        {
            Avg = Total / 6;

        }

        public void set_Result()
        {
            if (Avg >= 75){
                Result = "Pass";
            }
            else
            {
                Result = "Fail";
            }

        }




        public void AcceptDetails(){
            Console.WriteLine("Enter Student details : ");

            Console.WriteLine("Enter the Id : ");
            Id = int.Parse(Console.ReadLine());

            Console.WriteLine("Enter the Name : ");
            Name = Console.ReadLine();

            Console.WriteLine("Enter marks in subject 1 : ");
            M1 = int.Parse(Console.ReadLine());

            Console.WriteLine("Enter marks in subject 2 : ");
            M2 = int.Parse(Console.ReadLine());

            Console.WriteLine("Enter marks in subject 3 : ");
            M3 = int.Parse(Console.ReadLine());

            Console.WriteLine("Enter marks in subject 4 : ");
            M4 = int.Parse(Console.ReadLine());

            Console.WriteLine("Enter marks in subject 5 : ");
            M5 = int.Parse(Console.ReadLine());

            Console.WriteLine("Enter marks in subject 6 : ");
            M6 = int.Parse(Console.ReadLine());
            
            
        }

        public void DisplayDetails(){

            Console.WriteLine("-------------- Student Deatils ------------");
            Console.WriteLine($"Student Id: {Id}");
            Console.WriteLine($"Student Name: {Name}");
            Console.WriteLine($"Student marks in subjet 1 : {M1}");
            Console.WriteLine($"Student marks in subjet 2 : {M2}");
            Console.WriteLine($"Student marks in subjet 3 : {M3}");
            Console.WriteLine($"Student marks in subjet 4 : {M4}");
            Console.WriteLine($"Student marks in subjet 5 : {M5}");
            Console.WriteLine($"Student marks in subjet 6 : {M6}");
            Console.WriteLine($"Student total marks in 6 subjets : {Total}");
            Console.WriteLine($"Student Average marks  : {Avg}");
            Console.WriteLine($"Student Result : {Result}");

            

        }
    }

}




namespace helloApp
{
    public class Code1
    {
        public void f1()
        {
            Console.WriteLine($"Progrm to check ita leap year or not");
            
            int year = 0;
            Console.WriteLine($"Enter the year : ");
            year = int.Parse(Console.ReadLine());

            if (year % 4 == 0 && year % 100 != 0 ||  year % 400 == 0)
            {
                Console.WriteLine($"{year} is a leap year.");
            }
            else
            {
                Console.WriteLine($"{year} is not a leap year.");
            }

        }

        public void f2()
        {
            Console.WriteLine($"Progrm to convert celcius to fahrenheit.");
            
            int celcius = 0;
            Console.WriteLine($"Enter the year : ");
            celcius = int.Parse(Console.ReadLine());

            float fahrenheit = 1.8f * celcius + 32 ;

            Console.WriteLine($"Temperature in Celcius : {celcius}");
            Console.WriteLine($"Temperature in Fahrenheit : {fahrenheit}");


        }

        public void f3()
        {
            Console.WriteLine($"Progrm to check the gradeof a student");
            
            int score = 0;
            Console.WriteLine($"Enter the score : ");
            score = int.Parse(Console.ReadLine());

            if (score >= 90)
            {
                Console.WriteLine($"Grade : A");
            }
            else if (score < 90 && score >= 80)
            {
                Console.WriteLine($"Grade : B");
            }
            else if (score < 80 && score >= 70)
            {
                Console.WriteLine($"Grade : C");
            }
            else if (score < 70 && score >= 60)
            {
                Console.WriteLine($"Grade : D");
            }
            else
            {
                Console.WriteLine($"Grade : F");
            }

        }

        public static int Fact(int x)
        {
            int res = 1;
            while (x > 1)
            {
                res *= x;
                x --;
            }

            return res;
        }

        public void f4()
        {
            Console.WriteLine($"Progrm to find the factorail");
            string n = string.Empty;
            do
            {
                
                Console.WriteLine($"Enter the score : ");
                n = Console.ReadLine();

                if (int.Parse(n) < 0)
                {
                    Console.WriteLine($"There is no factorial of negative numbers. ");
                    continue;
                }

                Console.WriteLine($"There is  factorial of {n} is : {Fact(int.Parse(n))} ");


            }while (n != "q");
                
            
            
        }

        public void f5(){
            Console.WriteLine("To print sum first natural n numbers.");
            int n = 0;
            Console.WriteLine("Enter n: ");
            n = int.Parse(Console.ReadLine());
            int res = 0;
            for(int i=1;i<=n;i++){
                res += i;
            }
            Console.WriteLine($"the sum of first {n} natural number is: {res} ");

        }
        public void f6(){
            Console.WriteLine("To find first n even numbers .");
            int n = 0;
            Console.WriteLine("Enter n: ");
            n = int.Parse(Console.ReadLine());

            

            for(int i=1;i<=n;i++){
                Console.WriteLine(2 * i);
            }

        }



        
    }
}
