using System.IO.Compression;

namespace helloApp
{

    public class Employee{
        int Id;
        string Name;
        string Department;
        float Salary;
        char Gender;

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
        }

        public void DisplayDetails(){

            Console.WriteLine("-------------- Employee Deatils ------------");
            Console.WriteLine($"Employee Id: {Id}");
            Console.WriteLine($"Employee Name: {Name}");
            Console.WriteLine($"Employee Department: {Department}");
            Console.WriteLine($"Employee Salary: {Salary}");
            Console.WriteLine($"Employee Gender: {Gender}");

        }


    }

}
