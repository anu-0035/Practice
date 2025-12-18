using System;

namespace helloApp {

    public class Calulator{

        int num1;
        int num2;
        int res;

        public void add(){
            Console.WriteLine("Program for addition of 2 numbers.");
            Console.WriteLine("Enter num1 : ");
            num1 = int.Parse(Console.ReadLine());

            Console.WriteLine("Enter num2 : ");
            num2 = int.Parse(Console.ReadLine());

            res = num1 + num2;

            Console.WriteLine($"The addition of {num1} and {num2} is : {res}");

        }

        public void subtract(){
            Console.WriteLine("Program for substraction of 2 numbers.");
            Console.WriteLine("Enter num1 : ");
            num1 = int.Parse(Console.ReadLine());

            Console.WriteLine("Enter num2 : ");
            num2 = int.Parse(Console.ReadLine());

            res = num1 - num2;

            Console.WriteLine($"The subtraction of {num1} from {num2} is : {res}");

        }

        public void mul(){
            Console.WriteLine("Program for multiplication of 2 numbers.");
            Console.WriteLine("Enter num1 : ");
            num1 = int.Parse(Console.ReadLine());

            Console.WriteLine("Enter num2 : ");
            num2 = int.Parse(Console.ReadLine());

            res = num1 * num2;

            Console.WriteLine($"The multiplication of {num1} and {num2} is : {res}");

        }
        
        public void div(){
            Console.WriteLine("Program for division of 2 numbers.");
            Console.WriteLine("Enter num1 : ");
            num1 = int.Parse(Console.ReadLine());

            Console.WriteLine("Enter num2 : ");
            num2 = int.Parse(Console.ReadLine());
            if(num2 == 0){
                Console.WriteLine("Divisor cannot be ZERO.");
            }
            else{
                res = num1 / num2;

                Console.WriteLine($"The division of {num1} by {num2} is : {res}");
            }


        }

        public void rem(){
            Console.WriteLine("Program for reminder of 2 numbers.");
            Console.WriteLine("Enter num1 : ");
            num1 = int.Parse(Console.ReadLine());

            Console.WriteLine("Enter num2 : ");
            num2 = int.Parse(Console.ReadLine());

            res = num1 % num2;

            Console.WriteLine($"The reminder  of {num1} by {num2} is : {res}");

        }

        public void ar_circle(){
            Console.WriteLine("Program for area of circle.");
            float radius;
            float area;
            
            Console.WriteLine("Enter the radius of circle : ");
            radius = float.Parse(Console.ReadLine());

            area = 3.14f * radius * radius;
            Console.WriteLine($"Area of the circle of radius {radius} unit is {area} sq unit.");
        }

        public void sign_of_number(){
            Console.WriteLine("Program to check if a number is positive or negative.");
            Console.WriteLine("Enter num1 : ");
            num1 = int.Parse(Console.ReadLine());

            if (num1 > 0){
                Console.WriteLine($"{num1} is positive number.");
            }
            else if(num1 < 0){
                Console.WriteLine($"{num1} is negative number.");   
            }
            else{
                Console.WriteLine($"{num1} is zero.");
            }
        }

        public void big_number(){
            Console.WriteLine("Program to find bigger of 2 numbers.");
            Console.WriteLine("Enter num1 : ");
            num1 = int.Parse(Console.ReadLine());

            Console.WriteLine("Enter num2 : ");
            num2 = int.Parse(Console.ReadLine());

            if (num1 > num2){
                Console.WriteLine($"{num1} is bigger than {num2}.");
            }
            else if(num1 == num2){
                Console.WriteLine($"{num1} is equal to {num2}.");
            }
            else{
                Console.WriteLine($"{num2} is bigger than {num1}.");
            }

        }

        public void greatest(){
            Console.WriteLine("Program to find the greatest of 2 numbers.");
            Console.WriteLine("Enter num1 : ");
            num1 = int.Parse(Console.ReadLine());

            Console.WriteLine("Enter num2 : ");
            num2 = int.Parse(Console.ReadLine());

            int num3;

            Console.WriteLine("Enter num3 : ");
            num3 = int.Parse(Console.ReadLine());

            if (num1 == num2 && num2 == num3){
                Console.WriteLine($"All are the equal.");
            }

            if (num1 > num2 && num1 > num3){
                Console.WriteLine($"{num1} is the greatest.");
            }
            else{
                if(num2 > num3){
                    Console.WriteLine($"{num2} is the greatest.");
                }
                else{
                    Console.WriteLine($"{num3} is the greatest.");
                }
            }


        }

        public void type_of_number(){
            Console.WriteLine("Program to find if a number is even or odd.");
            Console.WriteLine("Enter num1 : ");
            num1 = int.Parse(Console.ReadLine());

            
            if(num1 % 2 == 0){
                Console.WriteLine($"{num1} is Even number.");
            }
            else{
                Console.WriteLine($"{num1} is Even number.");
            }


        }

    }
}
