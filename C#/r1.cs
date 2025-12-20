
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
